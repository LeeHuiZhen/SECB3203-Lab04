"""Lab 4 - lists and tuples for a gene panel and variant records."""
from typing import NamedTuple


class Variant(NamedTuple):
    """One variant coordinate: an immutable record with named fields."""

    chrom: str
    pos: int
    ref: str
    alt: str


def filter_panel(genes: list[str], priority: set[str]) -> list[str]:
    """Keep the genes that are in priority, preserving the original order."""
    return [gene for gene in genes if gene in priority]


def sorted_copy(items: list) -> list:
    """Return a sorted copy; the original list is not changed."""
    return sorted(items)


def _chrom_key(chrom: str) -> tuple:
    name = chrom.upper().removeprefix("CHR")
    if name.isdigit():
        return (0, int(name), "")
    return (
        1,
        {"X": 0, "Y": 1, "M": 2, "MT": 2}.get(name, 3),
        name,
    )


def sort_variants(variants: list[Variant]) -> list[Variant]:
    """Sort by chromosome (1-22, X, Y, M) and then by position."""
    return sorted(
        variants, key=lambda v: (_chrom_key(v.chrom), v.pos)
    )
