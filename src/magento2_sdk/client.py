# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from time import sleep

import requests

from .exceptions import RecoverableException


class Client:
    @classmethod
    def from_config(cls, config: dict):
        return cls(config["base_url"], config["access_token"])

    def __init__(self, base_url: str, access_token: str) -> None:
        self.base_url = base_url
        self.access_token = access_token

    def get(self, url: str, query: dict | bytes):
        # TODO move retry handlig higher so that every service can have its own behaviour
        retries = 0
        max_retires = 5

        while retries < max_retires:
            try:
                headers = {"Authorization": f"Bearer {self.access_token}", "Content-Type": "application/json"}
                full_url = f"{self.base_url}{url}"
                res = requests.get(full_url, params=query, headers=headers)
                res_data = res.json()
                return res_data
            except RecoverableException:
                retries += 1
                sleep(30)

    def post(self, url: str, payload: dict):
        headers = {"Authorization": f"Bearer {self.access_token}", "Content-Type": "application/json"}
        full_url = f"{self.base_url}{url}"
        payload = {"json": payload} if payload else {}
        res = requests.post(full_url, **payload, headers=headers)
        res_data = res.json()
        return res_data

    def put(self, url: str, payload: dict):
        headers = {"Authorization": f"Bearer {self.access_token}", "Content-Type": "application/json"}
        full_url = f"{self.base_url}{url}"
        res = requests.put(full_url, json=payload, headers=headers)
        res_data = res.json()
        return res_data
