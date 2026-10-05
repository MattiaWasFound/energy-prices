from pathlib import Path

import pytest

from energyprices import config, http

HERE = Path(__file__).parent
FIXTURES = HERE / "fixtures"


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    """No test may reach a live source; the one HTTP entry point raises."""
    def refuse(*args, **kwargs):
        raise AssertionError("a test tried to reach the network")
    monkeypatch.setattr(http, "get", refuse)


@pytest.fixture
def cfg():
    return config.load(HERE / "config")


@pytest.fixture
def fixture_bytes():
    return lambda name: (FIXTURES / name).read_bytes()
