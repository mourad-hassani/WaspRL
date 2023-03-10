input = """
a v n_a.
b v n_b.
c v n_c.
d v n_d.

e :- a.
f :- b.
g :- c.
h :- d.
i :- a.
j :- b.
k :- a.
l :- b.
m :- c.
n :- d.
k :- o, not i.
l :- k, not j.
p :- not i. 
n :- c.
q :- not i.
r :- m. 
:- s, t.
:- not i, u.
:- e, g.
:- h, f.
:- not n.
:- not l.
"""

output = """
{a, d, e, h, i, k, l, n, n_b, n_c}
{b, c, f, g, j, l, m, n, n_a, n_d, p, q, r}
"""
