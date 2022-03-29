# Tabler

A very simple tabular data formatter for console application.

## Installation

```shell
pip install py-tabler
```

## Example

```python
from tabler import Tabler

table = Tabler(
    data=[
        [1, 2, 3],
        [4, 5, 6],
    ],
    columns=["col1", "col2", "col3"],
)

print(table.format())
```

**Output**

```text
+------+------+------+
| col1 | col2 | col3 |
+------+------+------+
| 1    | 2    | 3    |
| 4    | 5    | 6    |
+------+------+------+
```
