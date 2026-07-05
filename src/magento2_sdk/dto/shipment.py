# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from dataclasses import dataclass


@dataclass
class ShipmentItem:
    order_item_id: int
    qty: int


@dataclass
class ShipmentTrack:
    track_number: str
    title: str
    carrier_code: str


@dataclass
class Shipment:
    notify: bool
    items: list[ShipmentItem]
    tracks: list[ShipmentTrack]
