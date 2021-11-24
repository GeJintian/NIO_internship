import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--position", action="store", help="position of camera"
    )
    parser.addoption(
        "--tester", action="store", help="sample name"
    )
