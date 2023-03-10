input = """
1 2 0 0
1 3 0 0
1 4 0 0
1 5 0 0
1 6 0 0
1 7 0 0
1 8 0 0
1 9 0 0
1 10 0 0
1 11 0 0
1 12 0 0
1 13 0 0
1 14 0 0
1 15 0 0
1 16 0 0
1 17 0 0
1 18 0 0
1 19 0 0
1 20 0 0
1 21 0 0
1 22 0 0
1 23 0 0
1 24 0 0
1 25 0 0
1 26 0 0
1 27 1 1 28
1 29 1 1 30
1 31 1 0 27
1 32 1 0 29
1 33 2 1 34 31
1 35 2 1 36 32
1 37 2 0 31 33
1 38 2 0 32 35
1 28 1 1 27
1 30 1 1 29
1 34 2 1 33 31
1 36 2 1 35 32
2 39 2 0 1 28 30
1 40 1 1 39
1 41 1 0 40
2 42 2 0 1 34 36
1 43 1 1 42
1 44 1 0 43
1 45 1 0 41
1 46 1 0 41
1 47 2 0 44 31
1 48 2 0 44 32
1 49 1 0 41
1 50 1 0 41
1 51 2 0 44 31
1 52 2 0 44 32
1 53 1 0 49
1 54 1 0 50
1 55 1 0 51
1 56 1 0 52
1 57 2 0 41 28
1 58 2 0 41 30
1 59 2 0 44 34
1 60 2 0 44 36
1 61 1 0 45
1 62 1 0 46
1 63 1 0 47
1 64 1 0 48
1 65 1 0 53
1 66 1 0 54
1 67 1 0 55
1 68 1 0 56
1 59 1 0 57
1 60 1 0 58
1 47 1 0 57
1 48 1 0 58
1 69 1 0 61
1 70 1 0 62
1 71 1 0 63
1 72 1 0 64
1 41 2 0 30 65
1 41 2 0 28 66
1 44 2 0 36 67
1 44 2 0 34 68
1 73 3 1 41 30 69
1 73 3 1 41 28 70
1 74 3 1 44 36 71
1 74 3 1 44 34 72
1 45 1 0 73
1 46 1 0 73
1 47 2 0 74 31
1 48 2 0 74 32
1 49 1 0 73
1 50 1 0 73
1 51 2 0 74 31
1 52 2 0 74 32
1 75 2 0 73 28
1 76 2 0 73 30
1 77 2 0 74 34
1 78 2 0 74 36
1 77 1 0 75
1 78 1 0 76
1 51 1 0 75
1 52 1 0 76
2 79 2 0 2 28 30
1 80 1 0 79
1 1 1 0 80
2 81 2 0 2 34 36
1 82 1 0 81
1 1 1 0 82
1 83 1 0 41
1 84 1 0 44
1 83 1 0 73
1 84 1 0 74
1 1 1 1 83
1 1 1 1 84
1 85 1 0 59
1 86 1 0 60
1 87 1 0 77
1 88 1 0 78
8 2 45 49 0 0
8 2 46 50 0 0
8 2 47 51 1 0 31
8 2 48 52 1 0 32
6 0 2 2 87 88 1 1
6 0 2 2 85 86 1 1
0
2 ac(7,neg(8))
3 ac(8,neg(7))
4 statement(8)
5 statement(7)
6 subformula2(8,neg(7))
7 subformula2(7,neg(8))
8 subformula2(8,7)
9 subformula2(7,8)
14 subformula(neg(7))
15 subformula(neg(8))
16 subformula(7)
17 subformula(8)
18 noatom(neg(7))
19 noatom(neg(8))
20 atom(7)
21 atom(8)
45 in(8,1)
46 in(7,1)
47 in(8,0)
48 in(7,0)
61 ismodel(8,1)
62 ismodel(7,1)
63 ismodel(8,0)
64 ismodel(7,0)
65 ismodel(neg(8),1)
66 ismodel(neg(7),1)
67 ismodel(neg(8),0)
68 ismodel(neg(7),0)
25 iteration(1)
26 iteration(0)
53 nomodel(8,1)
54 nomodel(7,1)
55 nomodel(8,0)
56 nomodel(7,0)
69 nomodel(neg(8),1)
70 nomodel(neg(7),1)
71 nomodel(neg(8),0)
72 nomodel(neg(7),0)
49 out(8,1)
50 out(7,1)
51 out(8,0)
52 out(7,0)
22 snum(2)
23 undec(8,2)
24 undec(7,2)
31 undec(8,1)
32 undec(7,1)
37 undec(8,0)
38 undec(7,0)
57 inA(8,1)
58 inA(7,1)
59 inA(8,0)
60 inA(7,0)
75 inR(8,1)
76 inR(7,1)
77 inR(8,0)
78 inR(7,0)
27 deselect(8,1)
29 deselect(7,1)
33 deselect(8,0)
35 deselect(7,0)
28 select(8,1)
30 select(7,1)
34 select(8,0)
36 select(7,0)
41 okA(1)
44 okA(0)
73 okR(1)
74 okR(0)
83 ok(1)
84 ok(0)
85 accept(8)
86 accept(7)
87 reject(8)
88 reject(7)
0
B+
0
B-
1
0
1
"""
output = """
COST 2@2 2@1
"""
