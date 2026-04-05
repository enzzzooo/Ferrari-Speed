import sympy as sp

# time
t = sp.Symbol("t")

# position P(t)
P = t**2

# derivative of P(t) is velocity
v = sp.diff(P, t)

# derivative at t = 5
print(v.subs(t,5))