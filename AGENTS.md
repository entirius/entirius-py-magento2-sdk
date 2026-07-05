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

## Architecture

`magento2_sdk/`: `Client` (REST over `requests`), `services/` (e.g. `OrderService`, invoice),
DTOs in `dto/`. Runtime dependency: `requests`. `invoice.py` calls a custom `V1/ecomhouse/…`
Magento module endpoint (allowlisted in the secret scanner). The integration test hits a live
Magento and is skipped without `MAGENTO_URL` / `MAGENTO_TOKEN` env vars.
