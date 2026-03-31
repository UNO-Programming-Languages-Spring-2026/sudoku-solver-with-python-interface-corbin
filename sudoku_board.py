from typing import Tuple
import clingo

class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        sudoku=self.from_model()
        for position,value in sudoku.items():
            value_format=''
            match position:
                #adds two spaces to the end of the value
                case position if position[0]==3 or position[0]==6:
                    value_format=f'{value}  '
                #adds a newline if cols is 9
                case position if position[0]==9:
                    value_format=f'{value}\n'
                #default adds one space after value
                case _:
                    value_format=f'{value} '
            s=+(f"{value_format}")
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
