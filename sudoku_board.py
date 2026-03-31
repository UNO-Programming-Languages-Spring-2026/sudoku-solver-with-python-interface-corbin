from typing import Tuple
import clingo

class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        # YOUR CODE HERE
        return s

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}
        clingo_output=str(model.symbols(shown=True))
        clingo_output=clingo_output.split(" ")
        for atom in clingo_output:
            if atom[0] == "[":
                row=int(atom[8])
                cols=int(atom[10])
                value=int(atom[12])
            else:    
                row=int(atom[7])
                cols=int(atom[9])
                value=int(atom[11])
            sudoku[(row,cols)]=value
        return cls(sudoku)
