from datetime import datetime

import jsonpickle

import isodatetimehandler


class A:
    def __init__(self):
        self.created_at = datetime.utcnow()


def test_basic():
    a = A()
    assert type(a.created_at) is datetime
    encoded = jsonpickle.encode(a)
    expected = a.created_at.isoformat()
    assert expected in encoded
    decoded = jsonpickle.decode(encoded)
    assert type(decoded.created_at) is datetime
    assert decoded.created_at == a.created_at
