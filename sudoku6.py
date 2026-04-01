import sys, clingo
import sudoku_board

class Context:
    def __init__(self, board: sudoku_board.Sudoku):
        self.board = board
        
    def initial(self) -> list[clingo.symbol.Symbol]:
        symbols=[]
        for (row, col), value in self.board.sudoku.items():
            symbol = clingo.Function("", [
                clingo.Number(row),
                clingo.Number(col),
                clingo.Number(value)
            ])
            symbols.append(symbol)
        return symbols

class ClingoApp(clingo.application.Application):
    def main(self, ctl, files):
        ctl.load("sudoku.lp")
        ctl.load("sudoku_py.lp")
        file_path = sys.argv[1]
        with open(file_path, "r") as f:
            txt = f.read()
        context=Context(board=sudoku_board.Sudoku.from_str(txt))
        ctl.ground(context=context)
        ctl.solve()
    def print_model(self, model, printer) -> None:
        symbols = sorted(model.symbols(shown=True))
        sudoku_dict={}
        sudoku = sudoku_board.Sudoku(sudoku=sudoku_dict)
        print(sudoku.from_model(model=model))
        sys.stdout.flush()
clingo.application.clingo_main(ClingoApp())


