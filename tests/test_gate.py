from fastapi.testclient import TestClient
from cnml.main import app

client = TestClient(app)


def test_pass_and_fail():
    good = client.post("/check", json={'spot': True, 'scale_to_zero': True}).json()
    assert good["passed"] is True
    assert good["applied"] is False
    bad = client.post("/check", json={'spot': True}).json()
    assert bad["passed"] is False
    assert "need_scale_to_zero" in bad["failed"]
