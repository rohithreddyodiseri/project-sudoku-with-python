% Assign exactly one digit to each cell and preserve the given clues.
1 { sudoku(R,C,V) : V = 1..9 } 1 :- R = 1..9, C = 1..9.
:- initial(R,C,V), not sudoku(R,C,V).

% A digit cannot repeat in a row, column, or 3-by-3 block.
:- sudoku(R,C1,V), sudoku(R,C2,V), C1 < C2.
:- sudoku(R1,C,V), sudoku(R2,C,V), R1 < R2.
:- sudoku(R1,C1,V), sudoku(R2,C2,V),
   (R1-1)/3 = (R2-1)/3, (C1-1)/3 = (C2-1)/3,
   (R1,C1) < (R2,C2).

#show sudoku/3.