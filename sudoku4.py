import sys, clingo
import sudoku_board
class ClingoApp(clingo.application.Application):
    def main(self, ctl, files):
        ctl.load("sudoku.lp")
        for f in files:
            ctl.load(f)
        if not files:
            ctl.load("-")
        ctl.ground()
        ctl.solve()
    def print_model(self, model, printer) -> None:
        symbols = sorted(model.symbols(shown=True))
        sudoku_dict={}
        sudoku = sudoku_board.Sudoku(sudoku=sudoku_dict)
        print(sudoku.from_model(model=model))
        sys.stdout.flush()
clingo.application.clingo_main(ClingoApp())