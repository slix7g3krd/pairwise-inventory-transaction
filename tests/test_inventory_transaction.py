import pytest
import math
from gameplay import inventory_transaction as mod

CASES = [
    ("key", 'm.tx_key("A", "B") == "A:B"'),
    ("apply", 'm.apply(3, -1) == 2'),
    ("rollback", 'm.rollback(3) == 3'),
    ("lock", 'm.lock_order(["b", "a"]) == ("a", "b")'),
    ("split", 'm.split_stack(5, 2) == (2, 3)'),
    ("cansplit", 'm.can_split(5, 2) is True'),
    ("snap", 'm.snapshot(3, 7) == (3, 7)'),
    ("seen", 'm.is_seen("k", {"k"}) is True'),
    ("audit", 'm.audit(True, "move") == "move:ok"'),
    ("mail", 'm.merge_mail(1, 2) == 3'),
    ("fee", 'm.fee(100, 0.05) == approx(5.0)'),
    ("conflict", 'm.conflict(1, 1) is True'),
    ("net", 'm.net(-2) == -2'),
    ("qty", 'm.apply_qty(3, 2) == 5'),
    ("id", 'm.tx_id(3, 2) == "3:2"')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
