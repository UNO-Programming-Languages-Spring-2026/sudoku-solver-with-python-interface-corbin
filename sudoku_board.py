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
                int(row)=atom[8]
                int(cols)=atom[10]
                int(value)=atom[12]
            else:    
                int(row)=atom[7]
                int(cols)=atom[9]
                int(value)=atom[11]
            sudoku[(row,cols)]=value
        return cls(sudoku)
