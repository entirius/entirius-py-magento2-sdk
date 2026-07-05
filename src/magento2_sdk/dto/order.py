# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from dataclasses import dataclass
from decimal import Decimal
from typing import TYPE_CHECKING

from magento2_sdk.dto import DTO
from magento2_sdk.dto.address import BillingAddress
from magento2_sdk.dto.extension_attributes import ExtensionAttributes, StatusHistories
from magento2_sdk.dto.item import Item
from magento2_sdk.dto.payment import Payment

if TYPE_CHECKING:
    from magento2_sdk.dto.extension_attributes import ShippingTotal


class OrderState:
    PENDING = "new"
    PROCESSING = "processing"
    ON_HOLD = "holded"
    CANCELED = "canceled"
    CLOSED = "closed"
    COMPLETE = "complete"
    SUSPECTED_FRAUD = "fraud"
    PAYMENT_REVIEW = "payment_review"
    PENDING_PAYMENT = "pending_payment"


class OrderStatus:
    PENDING = "pending"
    PROCESSING = "processing"
    ON_HOLD = "holded"
    CANCELED = "canceled"
    CLOSED = "closed"
    COMPLETE = "complete"
    SUSPECTED_FRAUD = "fraud"
    PAYMENT_REVIEW = "payment_review"
    PENDING_PAYMENT = "pending_payment"


@dataclass
class Order(DTO):
    state: str
    status: str
    order_currency_code: str

    items: list[Item]
    billing_address: BillingAddress
    extension_attributes: ExtensionAttributes

    payment: Payment

    # order id
    increment_id: str

    # Sum of items prices times quantity
    subtotal: Decimal

    # Sum of tax amount of items times quantity
    tax_amount: Decimal

    # Sum of items prices + taxes times quantity
    subtotal_incl_tax: Decimal

    # Total not paid
    total_due: Decimal

    # Total paid
    grand_total: Decimal

    # Total discount amount
    discount_amount: Decimal

    # Shipping
    shipping_amount: Decimal
    shipping_incl_tax: Decimal
    shipping_tax_amount: Decimal
    shipping_description: str

    # Customer data
    customer_email: str
    customer_firstname: str
    customer_lastname: str
    customer_group_id: int = 0
    customer_is_guest: int = 1

    # Store
    store_id: int = 1

    # Discount data
    coupon_code: str = ""
    discount_description: str = ""

    discount_tax_compensation_amount: Decimal | None = None

    # base_ : save price in base currency and non base_ save current currency price value
    base_currency_code: str | None = None
    base_subtotal: Decimal | None = None
    base_tax_amount: Decimal | None = None
    base_subtotal_incl_tax: Decimal | None = None
    base_total_due: Decimal | None = None
    base_grand_total: Decimal | None = None
    base_discount_amount: Decimal | None = None
    base_shipping_amount: Decimal | None = None
    base_shipping_incl_tax: Decimal | None = None
    base_shipping_tax_amount: Decimal | None = None
    base_discount_tax_compensation_amount: Decimal | None = None
    status_histories: list[StatusHistories] | None = None

    # This values will be assined to base_ if its None
    values = [
        "subtotal",
        "tax_amount",
        "subtotal_incl_tax",
        "total_due",
        "grand_total",
        "discount_amount",
        "shipping_amount",
        "shipping_incl_tax",
        "shipping_tax_amount",
        "discount_tax_compensation_amount",
    ]

    def __post_init__(self):
        super().__post_init__()
        self.base_currency_code = (
            self.order_currency_code if not isinstance(self.base_currency_code, str) else self.base_currency_code
        )

    @staticmethod
    def calc_totals(
        items: list["Item"], shipping_total: "ShippingTotal", base=False
    ) -> (Decimal, Decimal, Decimal, Decimal):
        subtotal = Decimal(0)
        tax_amount = Decimal(0)
        subtotal_incl_tax = Decimal(0)
        discount_amount = Decimal(0)

        for item in items:
            subtotal += item.base_row_total if base else item.row_total
            tax_amount += item.base_tax_amount if base else item.tax_amount
            subtotal_incl_tax += item.base_row_total_incl_tax if base else item.row_total_incl_tax
            discount_amount += item.base_discount_amount if base else item.discount_amount

        tax_amount += shipping_total.base_shipping_tax_amount if base else shipping_total.shipping_tax_amount

        return subtotal, tax_amount, subtotal_incl_tax, discount_amount

    # Not Used
    # customer_id: int
    # customer_note_notify: int
    # total_item_count: int
    # total_qty_ordered: int
    # email_sent: int
    # is_virtual: int
    # store_currency_code: str
    # store_name: str
    # weight: int
