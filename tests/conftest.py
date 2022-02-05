import pytest


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    """
    Prevent “requests” from remote operations by removing
    "requests.sessions.Session.request" for all tests.

    cf. https://docs.pytest.org/en/6.2.x/monkeypatch.html#global-patch-example-preventing-requests-from-remote-operations
    """
    monkeypatch.delattr("requests.sessions.Session.request")
