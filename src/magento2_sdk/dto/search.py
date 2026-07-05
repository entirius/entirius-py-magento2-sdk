# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from collections.abc import Sequence
from dataclasses import dataclass, field, replace


@dataclass
class Filter:
    field: str
    value: str
    condition_type: str

    def to_query_parameters(self) -> Sequence[str]:
        return [
            f"[field]={self.field}",
            f"[value]={self.value}",
            f"[condition_type]={self.condition_type}",
        ]


@dataclass
class FilterGroup:
    filters: Sequence[Filter]

    def to_query_parameters(self) -> Sequence[str]:
        return [
            f"[filters][{idx}]{param}" for idx, flt in enumerate(self.filters) for param in flt.to_query_parameters()
        ]


@dataclass
class SortOrder:
    field: str
    direction: str  # "ASC" or "DESC"

    def to_query_parameters(self) -> Sequence[str]:
        return [
            f"[field]={self.field}",
            f"[direction]={self.direction}",
        ]


@dataclass
class SearchCriteria:
    page_size: int = field(default=10)
    current_page: int = field(default=1)
    filter_groups: Sequence[FilterGroup] = field(default_factory=list)
    sort_orders: Sequence[SortOrder] = field(default_factory=list)

    def update(self, other: "SearchCriteria") -> "SearchCriteria":
        return replace(
            self,
            page_size=other.page_size,
            current_page=other.current_page,
            filter_groups=[*self.filter_groups, *other.filter_groups],
            sort_orders=[*self.sort_orders, *other.sort_orders],
        )

    def get_criteria_for_next_page(self) -> "SearchCriteria":
        return replace(self, current_page=self.current_page + 1)

    def to_query_parameters(self) -> bytes:
        page_size = f"searchCriteria[page_size]={self.page_size}"
        current_page = f"searchCriteria[current_page]={self.current_page}"
        filter_groups = [
            f"searchCriteria[filter_groups][{idx}]{param}"
            for idx, flt_group in enumerate(self.filter_groups)
            for param in flt_group.to_query_parameters()
        ]
        sort_orders = [
            f"searchCriteria[sort_orders][{idx}]{param}"
            for idx, srt_order in enumerate(self.sort_orders)
            for param in srt_order.to_query_parameters()
        ]
        result = "&".join([page_size, current_page, *filter_groups, *sort_orders]).encode()
        return result
