# AGENTS.md

Magento 2 REST API SDK — distribution `entirius-py-magento2-sdk`, import `magento2_sdk`.

## Commands

| Command | Meaning |
|---|---|
| `make install` | sync dependencies (uv, incl. extras) |
| `make check` | lint + format-check (ruff) |
| `make fix` | auto-fix lint + format |
| `make test` | test suite (pytest) |

## Conventions

- English only: code, docs, commits, branches, PRs.
- MPL-2.0: every non-trivial source file carries the license header (pre-commit inserts it).
- Toolchain: uv + ruff + hatchling + pytest; all config in `pyproject.toml`; `uv.lock` committed.
- Git flow: `master` (production) + `develop` (integration); changes land via PR; semver tag on `master`.
- Never rename the import package `magento2_sdk` — it is a public API contract.
- Default: do not commit — git is the user's call.
- No AI attribution in commits or PR descriptions.

## Architecture

`src/magento2_sdk/`: `client.py` holds `Client(base_url, access_token)` (Bearer token, REST over `requests`);
`services/` holds `OrderService` (orders, delivery point, invoice, shipment) and `InvoiceService`; DTOs live in `dto/`.
`InvoiceService.create_for_order()` posts to `V1/ecomhouse/assigne-invoice-to-order`, the endpoint of a custom Magento module, not core Magento.
Runtime dependency: `requests`. The integration test hits a live Magento and is skipped without `MAGENTO_URL` /
`MAGENTO_TOKEN` env vars.
