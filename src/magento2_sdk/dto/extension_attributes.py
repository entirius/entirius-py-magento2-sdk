# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from dataclasses import dataclass
from decimal import Decimal

from magento2_sdk.dto import DTO
from magento2_sdk.dto.address import ShippingAddress


@dataclass
class ShippingTotal(DTO):
    shipping_amount: Decimal
    shipping_incl_tax: Decimal
    shipping_tax_amount: Decimal

    base_shipping_amount: Decimal | None = None
    base_shipping_incl_tax: Decimal | None = None
    base_shipping_tax_amount: Decimal | None = None

    # This values will be assined to base_ if its None
    values = ["shipping_amount", "shipping_incl_tax", "shipping_tax_amount"]


@dataclass
class Shipping(DTO):
    address: ShippingAddress
    method: str
    total: ShippingTotal | None = None


@dataclass
class ShippingAssignment(DTO):
    shipping: Shipping


@dataclass
class ExtensionAttributes(DTO):
    shipping_assignments: list[ShippingAssignment]
    requested_invoice: bool = False

    # Only for Magento 2 ECOM DPM Module
    delivery_point_code: str | None = None
    delivery_point_name: str | None = None
    delivery_point_address: str | None = None
    delivery_point_city: str | None = None
    delivery_point_postcode: str | None = None

    is_over_vat_threshold: bool | None = None


@dataclass
class StatusHistories(DTO):
    comment: str
    entity_name: str
    is_customer_notified: int
    is_visible_on_front: int
