# magento2-sdk

Magento 2 REST API SDK — orders, invoices, and related resources over the Magento 2 REST API.

## Installation

```shell
pip install entirius-py-magento2-sdk
```

## Usage

```python
from magento2_sdk.client import Client
from magento2_sdk.services import OrderService

client = Client(base_url="https://your-magento/rest/", access_token="...")
orders = OrderService(client=client)
```

## Development

```shell
make install     # sync dependencies (uv)
make check       # lint + format check (ruff)
make test        # test suite (pytest) — integration test skipped without MAGENTO_URL / MAGENTO_TOKEN
```

Development and agent instructions: [AGENTS.md](AGENTS.md).

## License

Mozilla Public License 2.0 — see [LICENSE](LICENSE).
