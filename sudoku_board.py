from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku
        self.board = sudoku

    def __str__(self) -> str:
        rows = []
        for row in range(1, 10):
            blocks = []
            for start in (1, 4, 7):
                blocks.append(" ".join(
                    str(self.sudoku.get((row, col), "-"))
                    for col in range(start, start + 3)
                ))
            rows.append("  ".join(blocks))
            if row in (3, 6):
                rows.append("")
        return "\n".join(rows)

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}
        for symbol in model.symbols(shown=True):
            if symbol.match("sudoku", 3):
                row, col, value = symbol.arguments
                sudoku[(row.number, col.number)] = value.number
        return cls(sudoku)
