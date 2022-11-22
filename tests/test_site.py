"""Tests for the Site model."""


def test_create_site():
    from catchment.models import Site

    name = 'FP23'
    s = Site(name=name)

    assert s.name == name