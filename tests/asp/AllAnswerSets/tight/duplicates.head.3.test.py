input = """
1 2 1 0 3
1 4 1 0 5
1 2 1 0 4
1 1 2 0 2 3
1 1 2 0 4 5
1 6 1 0 4
1 7 1 0 6
1 7 1 0 2
1 8 2 1 4 6
1 9 2 1 2 7
8 2 3 7 0 0
8 2 5 6 0 0
8 2 7 7 0 0
8 2 6 6 0 0
0
2 a
3 la0
7 ka
4 b
5 lb0
6 kb
8 gapkb
9 gapka
0
B+
0
B-
1
0
1
"""
output = """
{kb, ka, gapkb, gapka}
"""
