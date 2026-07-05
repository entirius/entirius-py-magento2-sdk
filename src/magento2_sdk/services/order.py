# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from collections.abc import Sequence

from magento2_sdk.client import Client
from magento2_sdk.dto.delivery_point import DeliveryPoint
from magento2_sdk.dto.order import Order
from magento2_sdk.dto.search import SearchCriteria


class OrderService:
    def __init__(self, client: Client):
        self.client = client

    def get_orders(self, search_criteria: SearchCriteria = SearchCriteria()) -> Sequence[Order]:
        res = self.client.get("V1/orders", search_criteria.to_query_parameters())
        return res

    def get_order_by_id(self, id: int) -> dict:
        res = self.client.get(f"V1/orders/{id}", {})
        return res

    def create_order(self, data: dict) -> dict:
        res = self.client.put("V1/orders/create", data)
        return res

    def cancel_order(self, id: int) -> dict:
        res = self.client.post(f"V1/orders/{id}/cancel", {})
        return res

    def add_delivery_point(self, delivery_point: DeliveryPoint) -> dict:
        """Only for Magento 2 ECOM DPM Module"""
        # Nie wiem czy to jest POST, tak załozylem
        return self.client.post("V1/setdeliverypoint", delivery_point.asdict())

    def create_invoice(self, id: int, payload: dict = {}) -> int:
        final_payload = {"capture": True, "notify": True}.update(payload)
        res = self.client.post(f"V1/order/{id}/invoice", final_payload)
        return res

    def create_shipment(self, order_id: int, payload=None) -> int:
        if payload is None:
            payload = {}
        return self.client.post(f"V1/order/{order_id}/ship", payload)
