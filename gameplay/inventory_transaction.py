import math

def tx_key(a, b):
    """事务键。"""
    raise NotImplementedError("TODO: tx_key")

def apply(before, delta):
    """原子增减。"""
    raise NotImplementedError("TODO: apply")

def rollback(before):
    """回滚。"""
    raise NotImplementedError("TODO: rollback")

def lock_order(ids):
    """锁顺序。"""
    raise NotImplementedError("TODO: lock_order")

def split_stack(count, amount):
    """拆堆。"""
    raise NotImplementedError("TODO: split_stack")

def can_split(count, amount):
    """拆分合法性。"""
    raise NotImplementedError("TODO: can_split")

def snapshot(value, generation):
    """结算快照。"""
    raise NotImplementedError("TODO: snapshot")

def is_seen(key, seen):
    """幂等命中。"""
    raise NotImplementedError("TODO: is_seen")

def audit(ok, op):
    """审计记录。"""
    raise NotImplementedError("TODO: audit")

def merge_mail(inventory, mail):
    """邮件合并。"""
    raise NotImplementedError("TODO: merge_mail")

def fee(total, rate):
    """手续费。"""
    raise NotImplementedError("TODO: fee")

def conflict(a, b):
    """锁冲突。"""
    raise NotImplementedError("TODO: conflict")

def net(delta):
    """净变化。"""
    raise NotImplementedError("TODO: net")

def apply_qty(base, qty):
    """数量结算。"""
    raise NotImplementedError("TODO: apply_qty")

def tx_id(seed, index):
    """事务 id。"""
    raise NotImplementedError("TODO: tx_id")
