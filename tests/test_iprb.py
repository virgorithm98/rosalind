import pytest
from main.iprb import dominant_allele_offspring_probability, pairing_probability

def test_calculate_dominant_allele_offspring_probability():
    assert dominant_allele_offspring_probability("AA", "AA") == 1.0
    assert dominant_allele_offspring_probability("AA", "Aa") == 1.0
    assert dominant_allele_offspring_probability("AA", "aa") == 1.0
    assert dominant_allele_offspring_probability("Aa", "Aa") == 0.75
    assert dominant_allele_offspring_probability("Aa", "aa") == 0.5
    assert dominant_allele_offspring_probability("aa", "aa") == 0.0

def test_pairing_probability():
    assert pairing_probability({"k":2, "m":2,"n":2}, "k", "k") == 0.067
    assert pairing_probability({"k":2, "m":2,"n":2}, "k", "n") == 0.133