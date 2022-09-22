import pytest


def always_returns_true():

    it_works = True
    if it_works:
        return "Misha and Pavi are working together on this"


def test_always_returns_true():
    assert always_returns_true()
