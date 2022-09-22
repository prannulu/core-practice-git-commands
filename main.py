import pytest


def always_returns_true():
    return "Pavi"


def test_always_returns_true():
    assert always_returns_true()
