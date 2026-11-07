
"""Solve Sudoku instances with clingo's standard command-line interface."""

import sys
from pathlib import Path

from clingo.application import Application, clingo_main


class ClingoApp(Application):
    def main(self, ctl, files):
        ctl.load(str(Path(__file__).with_name("sudoku.lp")))
        for filename in files:
            ctl.load(filename)
        if not files:
            ctl.load("-")
        ctl.ground([("base", [])])
        ctl.solve()

    def print_model(self, model, printer):
        print(" ".join(sorted(str(symbol) for symbol in model.symbols(shown=True))))
        sys.stdout.flush()


if __name__ == "__main__":
    clingo_main(ClingoApp())
