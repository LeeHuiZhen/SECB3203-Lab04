import pytest

from lookup import kmer_counts, safe_expression
from panel import Variant, sort_variants, sorted_copy


def test_sorted_copy_leaves_original_unchanged():
    original = ["TP53", "BRCA1", "CFTR"]
    result = sorted_copy(original)
    assert result == ["BRCA1", "CFTR", "TP53"]
    assert original == ["TP53", "BRCA1", "CFTR"]
    assert result is not original


def test_chromosome_order_including_x_and_m():
    variants = [
        Variant("chrM", 100, "A", "T"),
        Variant("10", 50, "C", "G"),
        Variant("chr2", 30, "G", "A"),
        Variant("X", 20, "T", "C"),
        Variant("chr1", 10, "A", "C"),
    ]
    assert [v.chrom for v in sort_variants(variants)] == [
        "chr1",
        "chr2",
        "10",
        "X",
        "chrM",
    ]


def test_kmer_counts_k_larger_and_empty():
    assert kmer_counts("ACGT", 5) == {}
    assert kmer_counts("", 2) == {}
    with pytest.raises(ValueError):
        kmer_counts("ACGT", 0)


def test_safe_expression_missing_and_zero():
    expression = {"BRCA1": 8.2, "TP53": 0.0}
    assert safe_expression(expression, "MYC") is None
    assert safe_expression(expression, "TP53") == 0.0
    assert "MYC" not in expression