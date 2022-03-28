# Usage

**Simple usage**

```python

tabler = Tabler(
    data=[
        [1, 2, 3],
        [4, 5, 6],
    ],
    columns=["col1", "col2", "col3"],
)
tabler.format()

""" Output
+------+------+------+
| col1 | col2 | col3 |
+------+------+------+
| 1    | 2    | 3    |
| 4    | 5    | 6    |
+------+------+------+
"""
```

**Alignment**

```python

tabler = Tabler(
    data=[
        [1, 2, 3],
        [4, 5, 6],
    ],
    columns=["col1", "col2", "col3"],
    alignment=Tabler.ALIGN_RIGHT,
)
tabler.format()

"""Output
+------+------+------+
| col1 | col2 | col3 |
+------+------+------+
|    1 |    2 |    3 |
|    4 |    5 |    6 |
+------+------+------+
"""
```

**Column width**

```python
tabler = Tabler(
    data=[
        [1, 2, 3],
        [4, 5, 6],
    ],
    columns=["col1", "col2", "col3"],
    columns_width=[(0, 10), (2, 20)]
)
tabler.format()

""" Output
+------------+------+----------------------+
| col1       | col2 | col3                 |
+------------+------+----------------------+
| 1          | 2    | 3                    |
| 4          | 5    | 6                    |
+------------+------+----------------------+
"""
```

**Dividers**

```python
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
tabler.format()

""" Output
#======#======#======#
/ col1 / col2 / col3 /
#======#======#======#
/ 1    / 2    / 3    /
/ 4    / 5    / 6    /
#======#======#======#
"""
```

**Data operations**

```python
tabler = Tabler(
    data=[
        [4, 5, 6],
    ],
    columns=["col1", "col2", "col3"],
)

tabler.insert(0, [1, 2, 3])
tabler.append([7, 8, 9])
tabler.format()

""" Output
+------+------+------+
| col1 | col2 | col3 |
+------+------+------+
| 1    | 2    | 3    |
| 4    | 5    | 6    |
| 7    | 8    | 9    |
+------+------+------+
"""
```
