from utils import arrs

import pytest


@pytest.mark.parametrize('array, index, default, expected', [
    ([1, 2, 3], 1, None, 2),
    ([], 0, "test", "test"),
    ([1, 2], 1, None, 2),
])
def test_get(array, index, default, expected):
    assert arrs.get(array, index, default) == expected


@pytest.mark.parametrize('coll, start, end, expected', [
    ([1, 2, 3, 4], 1, 3, [2, 3]),
    ([1, 2, 3], 1, None, [2, 3]),
    ([], None, None, []),
    ([1, 2, 3, 4], 3, None, [4]),
    ([1, 2, 3], None, None, [1, 2, 3])
])
def test_slice(coll, start, end, expected):
    assert arrs.my_slice(coll, start, end) == expected
