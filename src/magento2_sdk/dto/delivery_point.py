# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from dataclasses import dataclass

from magento2_sdk.dto import DTO


@dataclass
class DeliveryPoint(DTO):
    """
    Only for Magento 2 ECOM DPM Module
    """

    entity_id: str  # ID adresu wysyłki
    parent_id: str  # ID zamówienia Magento
    delivery_point_code: str
    delivery_point_name: str
    delivery_point_address: str
    delivery_point_city: str
    delivery_point_postcode: str
