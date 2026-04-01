% Sudoku Solver
%
% Hints:
% For subgrid of size n, subgrids can be identified by labels 1..n*n
% A cell (x,y) can be mapped to the subgrid labeled 1+(((x-1)/n)*n+(y-1)/n)
#const n = 9.

sudoku(X,Y,N) :- initial(X,Y,N).
%achieved translates initial filled squared to sudoku
{sudoku(X,Y,N): N=1..n } = 1 :- X=1..n,Y=1..n.
%achieved: fills all squares with numbers
:-sudoku(X1,Y,N1),sudoku(X2,Y,N2),N1=N2,X1!=X2.
%achieved: remove solutions with duplicate numbers in the same column
:-sudoku(X,Y1,N1),sudoku(X,Y2,N2),N1=N2,Y1!=Y2.
%achieved: remove solutions with duplicate numbers in the same row
subgrid(X,Y,G) :- sudoku(X,Y,_),G=1+(((X-1)/S)*S+(Y-1)/S),S=3.
%achieved: obtained subgrid for each coordinate
:- subgrid(X1,Y1,G), subgrid(X2,Y2,G), sudoku(X1,Y1,N), sudoku(X2,Y2,N),
sudoku(X1,Y1,N)!=sudoku(X2,Y2,N).
%achieved: removed instances where there are duplicate numbers in the
%same subgrid
#show sudoku/3.
%retest