input = """
2 2 2 0 1 3 4
1 1 2 0 5 2
2 6 2 0 2 3 4
1 1 2 0 7 6
3 2 3 4 0 0
3 2 5 7 0 0
0
3 a(1)
4 a(2)
5 value(1)
7 value(2)
0
B+
0
B-
1
0
1
"""
output = """
{}
{a(1)}
{a(2)}
{value(1)}
{a(1), a(2)}
{value(2), a(2)}
{value(2), a(1)}
{value(2)}
{value(2), value(1)}
"""
