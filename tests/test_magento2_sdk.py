# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import os
from decimal import Decimal

import pytest

from magento2_sdk.client import Client
from magento2_sdk.dto.address import BillingAddress, ShippingAddress
from magento2_sdk.dto.extension_attributes import (
    ExtensionAttributes,
    Shipping,
    ShippingAssignment,
    ShippingTotal,
    StatusHistories,
)
from magento2_sdk.dto.item import Item
from magento2_sdk.dto.order import Order, OrderState, OrderStatus
from magento2_sdk.dto.payment import Payment
from magento2_sdk.services import OrderService

MAGENTO_URL = os.environ.get("MAGENTO_URL")
MAGENTO_TOKEN = os.environ.get("MAGENTO_TOKEN")

pytestmark = pytest.mark.skipif(
    not (MAGENTO_URL and MAGENTO_TOKEN),
    reason="Magento credentials not set (MAGENTO_URL, MAGENTO_TOKEN env vars)",
)


def test_get():
    client: Client = Client(base_url=MAGENTO_URL, access_token=MAGENTO_TOKEN)
    order_service: OrderService = OrderService(client=client)

    entity_id = 1

    response = order_service.get_order_by_id(id=entity_id)
    assert response["entity_id"] == entity_id


def test_create():

    items = []
    item = Item(
        sku="sku-1",
        name="sku-1",
        qty_ordered=Decimal("2"),
        price=Decimal("10.00"),
        original_price=Decimal("10.00"),
        tax_amount=Decimal("2.30"),
        price_incl_tax=Decimal("12.30"),
    )
    items.append(item)

    billing_address = BillingAddress(
        city="Testowo",
        country_id="PL",
        email="test@example.com",
        firstname="Jan",
        lastname="Kowalski",
        postcode="12-123",
        street=["Testowa", "123"],
        telephone="123123123",
    )

    shipping_address = ShippingAddress(
        city="Testowo",
        country_id="PL",
        email="test@example.com",
        firstname="Jan",
        lastname="Kowalski",
        postcode="12-123",
        street=["Testowa", "123"],
        telephone="123123123",
    )

    ext_attr = ExtensionAttributes(
        shipping_assignments=[
            ShippingAssignment(
                shipping=Shipping(address=shipping_address, method="flatrate_flatrate"),
            )
        ],
    )
    increment_id = 100100001
    status_histories = StatusHistories(
        comment="Test comment",
        is_customer_notified=1,
        is_visible_on_front=1,
        parent_id=increment_id,
    )

    shipping_total = ShippingTotal(
        shipping_amount=Decimal("10.00"),
        shipping_incl_tax=Decimal("12.30"),
        shipping_tax_amount=Decimal("2.30"),
    )

    payment = Payment(
        method="banktransfer",
        amount_ordered=Payment.calc_amount_ordered(items, shipping_total),
    )

    subtotal, tax_amount, subtotal_incl_tax, discount_amount = Order.calc_totals(items, shipping_total)

    order = Order(
        increment_id="100100001",
        state=OrderState.PENDING,
        status=OrderStatus.PENDING,
        order_currency_code="PLN",
        items=items,
        billing_address=billing_address,
        extension_attributes=ext_attr,
        payment=payment,
        subtotal=subtotal,
        tax_amount=tax_amount,
        subtotal_incl_tax=subtotal_incl_tax,
        total_due=payment.amount_ordered,
        grand_total=payment.amount_ordered,
        discount_amount=discount_amount,
        customer_email="test@example.com",
        customer_firstname="Jan",
        customer_lastname="Kowalski",
        customer_group_id=0,
        customer_is_guest=1,
        shipping_description="Flat Rate",
        shipping_amount=shipping_total.shipping_amount,
        shipping_incl_tax=shipping_total.shipping_incl_tax,
        shipping_tax_amount=shipping_total.shipping_tax_amount,
    )

    entity = order.asdict()
    # print(json.dumps(entity, cls=DecimalEncoder))

    client: Client = Client(base_url=MAGENTO_URL, access_token=MAGENTO_TOKEN)
    order_service: OrderService = OrderService(client=client)

    response = order_service.create_order(entity)
    assert int(response["entity_id"]) > 0
