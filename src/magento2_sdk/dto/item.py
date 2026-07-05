# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from dataclasses import dataclass
from decimal import Decimal

from magento2_sdk.dto import DTO


@dataclass
class Item(DTO):
    sku: str
    name: str

    # Quantity
    qty_ordered: Decimal

    # Price of one quantity
    price: Decimal

    # Price of one quantity not including discounts
    original_price: Decimal

    # Tax of all quantity
    tax_amount: Decimal

    # Price + Tax of one quantity
    price_incl_tax: Decimal

    # Discount
    discount_amount: Decimal = Decimal(0)
    discount_percent: Decimal = Decimal(0)

    # Tax percent for information, example: 23% is Decimal(23.00)
    tax_percent: Decimal = Decimal(0)

    # Price times quantity
    row_total: Decimal | None = None

    # Price + tax times quantity
    row_total_incl_tax: Decimal | None = None

    # Base
    base_price: Decimal | None = None
    base_original_price: Decimal | None = None
    base_tax_amount: Decimal | None = None
    base_price_incl_tax: Decimal | None = None
    base_row_total: Decimal | None = None
    base_row_total_incl_tax: Decimal | None = None
    base_discount_amount: Decimal | None = None
    additional_data: dict | None = None

    # This values will be assined to base_ if its None
    values = [
        "price",
        "original_price",
        "tax_amount",
        "price_incl_tax",
        "row_total",
        "row_total_incl_tax",
        "discount_amount",
    ]

    def __post_init__(self):
        if self.row_total is None:
            self.row_total = self.price * self.qty_ordered
        if self.row_total_incl_tax is None:
            self.row_total_incl_tax = self.price_incl_tax * self.qty_ordered
        super().__post_init__()

    # Not Used
    # base_row_invoiced: Decimal
    # base_tax_invoiced: Decimal
    # free_shipping: Decimal
    # is_virtual: int
    # product_id: int
    # product_type: str
    # store_id: int
