from pkg.mod import Number

nr = Number()
nr.add(2)
nr.mul(3)
s = str(nr)
assert(s=='Number(6)')