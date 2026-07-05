# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from collections.abc import Sequence

from magento2_sdk.client import Client
from magento2_sdk.dto.search import SearchCriteria


class InvoiceService:
    def __init__(self, client: Client):
        self.client = client

    def get_invoices(self, search_criteria: SearchCriteria = SearchCriteria()) -> Sequence["Invoice"]:
        res = self.client.get("V1/invoices", search_criteria.to_query_parameters())
        return res

    def get_invoice_by_id(self, id: int) -> "Invoice":
        res = self.client.get(f"V1/invoices/{id}", {})
        return res

    def create_invoice(self, order_id: int, capture: bool = False, notify: bool = False):
        payload = {
            "capture": capture,
            "notify": notify,
        }
        return self.client.post(f"V1/order/{order_id}/invoice", payload)

    def create_for_order(self, data: dict) -> dict:
        res = self.client.post("V1/ecomhouse/assigne-invoice-to-order", data)
        return res
