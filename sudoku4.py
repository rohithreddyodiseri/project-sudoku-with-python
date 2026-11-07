import sys

from clingo.application import clingo_main

from sudoku1 import ClingoApp as SudokuSolver
from sudoku_board import Sudoku


class ClingoApp(SudokuSolver):
    def print_model(self, model, printer):
        print(Sudoku.from_model(model))
        sys.stdout.flush()


if __name__ == "__main__":
    clingo_main(ClingoApp())
