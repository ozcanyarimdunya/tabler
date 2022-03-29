__version__ = "0.1.0"


class Tabler(list):
    ALIGN_RIGHT = 0
    ALIGN_LEFT = 1
    ALIGN_CENTER = 2

    def __init__(
        self,
        data,
        columns,
        padding=1,
        alignment=ALIGN_LEFT,
        columns_width=None,
        column_divider="|",
        row_divider="-",
        break_divider="+",
    ):
        """
        Tabler
        ~~~~~~
        A very simple tabular data formatter for console application

        :param data: a list of list data
        :param columns: a list of columns data
        :param padding: inner space when printing table, default: 2
        :param alignment: text alignment, options: ALIGN_RIGHT, ALIGN_LEFT, ALIGN_CENTER
        :param columns_width: column width for specific columns: [(index, width)] ex: [(1, 10)]
        :param column_divider: column divider, default: |
        :param row_divider: row divider, default: -
        :param break_divider: break divider, default: +

        >>> import sys
        >>> tabler = Tabler(data=[[1, "A test"]], columns=["No", "Name"])
        >>> tabler.append([2, "Another test"])
        >>> tabler.insert(0, [0, "First test"])
        >>> print(tabler.format())
        +----+--------------+
        | No | Name         |
        +----+--------------+
        | 0  | First test   |
        | 1  | A test       |
        | 2  | Another test |
        +----+--------------+
        """
        super(Tabler, self).__init__(data)
        self._columns = columns
        self._padding = padding
        self._alignment = alignment
        self._columns_width = columns_width
        self._col_divider = column_divider
        self._row_divider = row_divider
        self._break_divider = break_divider
        self._maxes = None

    @staticmethod
    def _length(item):
        return len(str(item))

    def _set_maxes(self):
        maxes = {}
        for idx, col in enumerate(self._columns):
            maxes[idx] = len(str(col))

        for rows in self:
            for idx, row in enumerate(rows):
                maxes[idx] = max(maxes[idx], len(str(row)))

        if self._columns_width:
            for idx, width in self._columns_width:
                maxes[idx] = width

        return maxes

    def _format(self, text, justify):
        if self._alignment == Tabler.ALIGN_LEFT:
            _text = str(text).ljust(justify)
        elif self._alignment == Tabler.ALIGN_RIGHT:
            _text = str(text).rjust(justify)
        elif self._alignment == Tabler.ALIGN_CENTER:
            _text = str(text).center(justify)
        else:
            raise Exception("No such alignment: {}".format(self._alignment))

        pad = " " * self._padding
        return pad + _text + pad

    @property
    def divider(self):
        divs = []
        for v in self._maxes.values():
            t = self._row_divider * (v + self._padding * 2)

            divs.append(t)

        divs.insert(0, "")
        divs.append("")
        return self._break_divider.join(divs)

    @property
    def headers(self):
        text = []
        for idx, col in enumerate(self._columns):
            mx = self._maxes[idx]
            text.append(self._format(col, mx))

        text.insert(0, "")
        text.append("")
        return self._col_divider.join(text)

    @property
    def rows(self):
        text = []
        for rows in self:
            for idx, row in enumerate(rows):
                mx = self._maxes[idx]
                text.append(self._format(row, mx))
            text.append("\n")

        text.insert(0, "")
        text[-1] = ""
        return self._col_divider.join(text)

    def format(self):
        self._maxes = self._set_maxes()

        return "\n".join(
            [
                self.divider,
                self.headers,
                self.divider,
                self.rows,
                self.divider
            ]
        )

    def __str__(self):
        return self.format()

    def __repr__(self):
        return self.format()

    def __unicode__(self):
        return self.format()
