# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from dataclasses import dataclass
from decimal import Decimal
from typing import TYPE_CHECKING

from magento2_sdk.dto import DTO

if TYPE_CHECKING:
    from magento2_sdk.dto.extension_attributes import ShippingTotal
    from magento2_sdk.dto.item import Item


@dataclass
class Payment(DTO):
    method: str

    # Sum of items prices + taxes times quantity
    # with shipping price + tax
    amount_ordered: Decimal
    base_amount_ordered: Decimal | None = None
    additional_information: dict | None = None
    # This values will be assined to base_ if its None
    values = ["amount_ordered"]

    @staticmethod
    def calc_amount_ordered(items: list["Item"], shipping_total: "ShippingTotal", base=False) -> Decimal:
        result = Decimal(0)

        for item in items:
            result += item.base_row_total_incl_tax if base else item.row_total_incl_tax

        result += shipping_total.base_shipping_incl_tax if base else shipping_total.shipping_incl_tax

        return result
