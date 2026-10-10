# entirius-py-magento2-sdk

A Python client for the order side of the Magento 2 REST API, part of
Entirius, the open-source modular ecommerce platform. It wraps orders, invoices and shipments behind one `Client` and
two service classes.

[![PyPI](https://img.shields.io/pypi/v/entirius-py-magento2-sdk.svg)](https://pypi.org/project/entirius-py-magento2-sdk/)
[![Python](https://img.shields.io/pypi/pyversions/entirius-py-magento2-sdk.svg)](https://pypi.org/project/entirius-py-magento2-sdk/)
[![License: MPL-2.0](https://img.shields.io/badge/license-MPL--2.0-blue.svg)](https://github.com/entirius/entirius-py-magento2-sdk/blob/develop/LICENSE)

## What it does

- Lists orders with search criteria (filters, filter groups, sort orders) and reads one order by id.
- Creates and cancels orders; sets a delivery point on an order (needs a delivery-point module on the Magento side).
- Creates invoices and shipments for an order, and lists invoices.
- Authorizes every request with a Magento integration token (Bearer).

## Installation

```shell
uv add entirius-py-magento2-sdk
pip install entirius-py-magento2-sdk
```

The import name is `magento2_sdk`.

## Quick start

```python
from magento2_sdk.client import Client
from magento2_sdk.services import OrderService

client = Client(base_url="https://magento.example.com/rest/", access_token="...")
orders = OrderService(client=client)
found = orders.get_orders()
```

## Requirements

- Python 3.11 or newer.
- `requests` (installed as a dependency).
- A Magento 2 store with a REST API integration token.

## Documentation

- Entirius documentation: https://docs.entirius.com/
- Changelog: https://github.com/entirius/entirius-py-magento2-sdk/blob/develop/CHANGELOG.md

## Part of Entirius

This SDK is the order client of the bridges that connect the Entirius backend service (Volkanos) to an
existing Magento 2 store.

- Backend service: https://github.com/entirius/entirius-service-volkanos
- Docker harness: https://github.com/entirius/entirius-zeno
- Bridges that use it: https://github.com/entirius/entirius-django-checkout-export-to-magento-api,
  https://github.com/entirius/entirius-django-checkout-import-from-magento-api
- Sibling SDK (the catalog and customer side): https://github.com/entirius/entirius-py-magento2-sdk2

## Development

```shell
make install     # sync dependencies (uv)
make check       # lint + format check (ruff)
make test        # test suite (pytest); the integration tests are skipped without MAGENTO_URL / MAGENTO_TOKEN
```

Development and agent instructions: https://github.com/entirius/entirius-py-magento2-sdk/blob/develop/AGENTS.md

## License

Mozilla Public License 2.0 (MPL-2.0) — see https://github.com/entirius/entirius-py-magento2-sdk/blob/develop/LICENSE.
