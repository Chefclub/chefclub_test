from django.test import TestCase


def merge_steps(list_to_merge):
    """
    Merge a list of steps into max 6 steps
    Args:
        list_to_merge: List

    Returns:
        list
    """
    # TODO:
    return list_to_merge


class MergeStepsTest(TestCase):
    """
    python manage.py test test_1
    """
    def test_merge_steps(self):
        assert merge_steps([1, 2, 3, 4, 5, 6]) == [[1], [2], [3], [4], [5], [6]]
        assert merge_steps([1, 2, 3, 4, 5, 6, 7]) == [[1, 2], [3], [4], [5], [6], [7]]
        assert merge_steps([1, 2, 3, 4, 5, 6, 7, 8]) == [[1, 2], [3, 4], [5], [6], [7], [8]]
        assert merge_steps([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [
            [1, 2],
            [3, 4],
            [5, 6],
            [7],
            [8],
            [9],
        ]
        assert merge_steps([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8],
            [9],
            [10],
        ]
        assert merge_steps([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == [
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8],
            [9, 10],
            [11],
        ]
        assert merge_steps([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == [
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8],
            [9, 10],
            [11, 12],
        ]
        assert merge_steps(['a', 'b', 'c', 'd', 'e', 'f']) == [
            ['a'],
            ['b'],
            ['c'],
            ['d'],
            ['e'],
            ['f'],
        ]
        assert merge_steps(['a', 'b', 'c', 'd', 'e', 'f', 'g']) == [
            ['a', 'b'],
            ['c'],
            ['d'],
            ['e'],
            ['f'],
            ['g'],
        ]

