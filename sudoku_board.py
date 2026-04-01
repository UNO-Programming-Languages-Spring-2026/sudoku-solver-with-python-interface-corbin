from typing import Tuple
import clingo

class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        for row in range(1,10):
            for cols in range(1,10):
                if cols == 3 or cols == 6:
                    value_to_add=f'{self.sudoku[(row,cols)]}  '
                elif cols == 1 and (row != 1 and row !=4 and row != 7):
                    value_to_add=f'\n{self.sudoku[(row,cols)]} '
                elif cols == 1 and (row != 1 and (row == 4 or row == 7)):
                    value_to_add=f'\n\n{self.sudoku[(row,cols)]} '
                elif cols == 9:
                    value_to_add=f'{self.sudoku[(row,cols)]}'
                else:
                    value_to_add=f'{self.sudoku[(row,cols)]} '
                s += value_to_add
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
