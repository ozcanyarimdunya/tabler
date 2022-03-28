import textwrap
import unittest

from tabler import Tabler


class TestTabler(unittest.TestCase):
    """
    Test class for Tabler
    """

    @staticmethod
    def dedent(text):
        return textwrap.dedent(text).strip()

    def test_format(self):
        """test for format"""
        tabler = Tabler(
            data=[
                [1, 2, 3],
                [4, 5, 6],
            ],
            columns=["col1", "col2", "col3"],
        )

        expected = """
            +------+------+------+
            | col1 | col2 | col3 |
            +------+------+------+
            | 1    | 2    | 3    |
            | 4    | 5    | 6    |
            +------+------+------+
        """
        self.assertEqual(tabler.format(), self.dedent(expected))

    def test_list_operations(self):
        tabler = Tabler(
            data=[
                [4, 5, 6],
            ],
            columns=["col1", "col2", "col3"],
        )

        tabler.insert(0, [1, 2, 3])
        tabler.append([7, 8, 9])
        expected = """
            +------+------+------+
            | col1 | col2 | col3 |
            +------+------+------+
            | 1    | 2    | 3    |
            | 4    | 5    | 6    |
            | 7    | 8    | 9    |
            +------+------+------+
        """
        self.assertEqual(tabler.format(), self.dedent(expected))

    def test_alignment(self):
        tabler = Tabler(
            data=[
                [1, 2, 3],
                [4, 5, 6],
            ],
            columns=["col1", "col2", "col3"],
            alignment=Tabler.ALIGN_RIGHT,
        )
        expected = """
            +------+------+------+
            | col1 | col2 | col3 |
            +------+------+------+
            |    1 |    2 |    3 |
            |    4 |    5 |    6 |
            +------+------+------+
        """
        self.assertEqual(tabler.format(), self.dedent(expected))

    def test_column_width(self):
        tabler = Tabler(
            data=[
                [1, 2, 3],
                [4, 5, 6],
            ],
            columns=["col1", "col2", "col3"],
            columns_width=[(0, 10), (2, 20)]
        )
        expected = """
            +------------+------+----------------------+
            | col1       | col2 | col3                 |
            +------------+------+----------------------+
            | 1          | 2    | 3                    |
            | 4          | 5    | 6                    |
            +------------+------+----------------------+
        """
        self.assertEqual(tabler.format(), self.dedent(expected))

    def test_dividers(self):
        tabler = Tabler(
            data=[
                [1, 2, 3],
                [4, 5, 6],
            ],
            columns=["col1", "col2", "col3"],
            column_divider="/",
            row_divider="=",
            break_divider="#"
        )
        expected = """
            #======#======#======#
            / col1 / col2 / col3 /
            #======#======#======#
            / 1    / 2    / 3    /
            / 4    / 5    / 6    /
            #======#======#======#
        """
        self.assertEqual(tabler.format(), self.dedent(expected))


if __name__ == '__main__':
    unittest.main()
