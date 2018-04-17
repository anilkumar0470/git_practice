import pytest
import unittest


@pytest.mark.windows
def test_windows1():
    print("windows1")


@pytest.mark.windows
def test_windows2():
    print("windows2")


@pytest.mark.mac
def test_mac1():
    print("mac1")


@pytest.mark.mac
def test_mac2():
    print("mac2")
