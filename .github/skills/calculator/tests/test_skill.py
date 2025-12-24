import json
from skill import calculate

def test_calculate_success():
    result = json.loads(calculate("2+2"))
    assert result["status"] == "success"
    assert result["result"] == 4