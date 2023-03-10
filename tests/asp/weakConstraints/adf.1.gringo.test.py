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
1 19 1 1 20
1 21 1 1 22
1 23 1 0 19
1 24 1 0 21
1 25 2 1 26 23
1 27 2 1 28 24
1 29 2 0 23 25
1 30 2 0 24 27
1 20 1 1 19
1 22 1 1 21
1 26 2 1 25 23
1 28 2 1 27 24
1 31 0 0
1 32 0 0
2 33 2 0 1 20 22
1 34 1 1 33
1 35 1 0 34
2 36 2 0 1 26 28
1 37 1 1 36
1 38 1 0 37
1 39 1 0 35
1 40 1 0 35
1 41 2 0 38 23
1 42 2 0 38 24
1 43 1 0 35
1 44 1 0 35
1 45 2 0 38 23
1 46 2 0 38 24
1 47 1 0 43
1 48 1 0 45
1 35 1 0 20
1 38 1 0 26
1 49 2 0 35 20
1 50 2 0 35 22
1 51 2 0 38 26
1 52 2 0 38 28
1 53 1 0 39
1 54 1 0 41
1 55 3 1 35 22 47
1 56 3 1 38 28 48
1 51 1 0 49
1 52 1 0 50
1 41 1 0 49
1 42 1 0 50
1 35 2 0 22 53
1 38 2 0 28 54
1 39 1 0 55
1 40 1 0 55
1 41 2 0 56 23
1 42 2 0 56 24
1 43 1 0 55
1 44 1 0 55
1 45 2 0 56 23
1 46 2 0 56 24
1 57 2 0 55 20
1 58 2 0 55 22
1 59 2 0 56 26
1 60 2 0 56 28
1 59 1 0 57
1 60 1 0 58
1 45 1 0 57
1 46 1 0 58
2 61 2 0 2 20 22
1 62 1 0 61
1 1 1 0 62
2 63 2 0 2 26 28
1 64 1 0 63
1 1 1 0 64
1 65 1 0 35
1 66 1 0 38
1 65 1 0 55
1 66 1 0 56
1 1 1 1 65
1 1 1 1 66
1 67 1 0 51
1 68 1 0 52
1 69 1 0 59
1 70 1 0 60
8 2 39 43 0 0
8 2 40 44 0 0
8 2 41 45 1 0 23
8 2 42 46 1 0 24
6 0 2 2 69 70 1 1
6 0 2 2 67 68 1 1
0
4 ac(1,c(v))
5 ac(2,1)
2 statement(1)
3 statement(2)
6 subformula2(1,c(v))
7 subformula2(2,1)
10 subformula(c(v))
11 subformula(1)
12 atom(c(v))
13 atom(1)
39 in(1,1)
40 in(2,1)
41 in(1,0)
42 in(2,0)
31 ismodel(c(v),1)
32 ismodel(c(v),0)
53 ismodel(1,1)
54 ismodel(1,0)
17 iteration(1)
18 iteration(0)
47 nomodel(1,1)
48 nomodel(1,0)
43 out(1,1)
44 out(2,1)
45 out(1,0)
46 out(2,0)
14 snum(2)
15 undec(1,2)
16 undec(2,2)
23 undec(1,1)
24 undec(2,1)
29 undec(1,0)
30 undec(2,0)
49 inA(1,1)
50 inA(2,1)
51 inA(1,0)
52 inA(2,0)
57 inR(1,1)
58 inR(2,1)
59 inR(1,0)
60 inR(2,0)
19 deselect(1,1)
21 deselect(2,1)
25 deselect(1,0)
27 deselect(2,0)
20 select(1,1)
22 select(2,1)
26 select(1,0)
28 select(2,0)
35 okA(1)
38 okA(0)
55 okR(1)
56 okR(0)
65 ok(1)
66 ok(0)
67 accept(1)
68 accept(2)
69 reject(1)
70 reject(2)
0
B+
0
B-
1
0
1
"""
output = """
COST 0@2 2@1
"""
