#const n = 30.
d(1..n).

1 { q(X,Y) : d(Y) } 1 :- d(X).

:- q(X,Y1),q(X,Y2),Y1 < Y2.
:- q(X1,Y),q(X2,Y),X1 < X2.
:- q(X1,Y1),q(X2,Y2),X1 < X2,Y1 < Y2,d(Z1),d(Z2),Z1 = X2 - X1,Z2 = Y2 - Y1,Z1 = Z2.
:- q(X1,Y1),q(X2,Y2),X1 < X2,Y2 < Y1,d(Z1),d(Z2),Z1 = X2 - X1,Z2 = Y1 - Y2,Z1 = Z2.

#show q/2.
q(25,9). q(18,4). q(22,18). q(3,11). q(2,14). q(15,26). q(14,6). q(4,23). q(23,22). q(11,2). q(5,30). q(16,17). q(27,25).
