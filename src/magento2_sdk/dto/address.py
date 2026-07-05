# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from dataclasses import dataclass

from magento2_sdk.dto import DTO


@dataclass
class Address(DTO):
    city: str
    country_id: str
    email: str
    firstname: str
    lastname: str
    postcode: str
    street: list[str]
    telephone: str
    address_type: str
    company: str = ""
    vat_id: str | None = None


@dataclass
class BillingAddress(Address):
    address_type: str = "billing"


@dataclass
class ShippingAddress(Address):
    address_type: str = "shipping"
