print("# --8<-- [start:prodbb]")
# --8<-- [start:prodbb]
import feloopy as flp

def test(m):
    x = m.bvar(name="x", bound=[0,10])
    y = m.bvar(name="y", bound=[0,10])
    #obj: x*y
    m.obj(m.lin_prod_bb(x,y))
    return m

flp.search(test, key_vars=["x","y"]).report()
# --8<-- [end:prodbb]
print("# --8<-- [end:prodbb]")




print("# --8<-- [start:prodii]")
# --8<-- [start:prodii]
import feloopy as flp

def test(m):
    x = m.ivar(name="x", bound=[0,10])
    y = m.ivar(name="y", bound=[0,10])
    #obj: x*y
    m.obj(m.lin_prod_ii(x,y,ub_integer1=10,ub_integer2=10))
    return m

flp.search(test, key_vars=["x","y"]).report()
# --8<-- [end:prodii]
print("# --8<-- [end:prodii]")




print("# --8<-- [start:prodpp]")
# --8<-- [start:prodpp]
import feloopy as flp

def test(m):
    x = m.pvar(name="x", bound=[0,10])
    y = m.pvar(name="y", bound=[0,10])
    #obj: x*y
    m.obj(m.lin_prod_pp(x,y,ub_positive1=10,ub_positive2=10,num_breakpoints=10))
    return m

flp.search(test, key_vars=["x","y"]).report()
# --8<-- [end:prodpp]
print("# --8<-- [end:prodpp]")




print("# --8<-- [start:prodff]")
# --8<-- [start:prodff]
import feloopy as flp

def test(m):
    x = m.fvar(name="x", bound=[-10,10])
    y = m.fvar(name="y", bound=[-10,10])
    #obj: x*y
    m.obj(m.lin_prod_ff(x,y,bound1=[-10,10],bound2=[-10,10],num_breakpoints=10))
    return m

flp.search(test, key_vars=["x","y"]).report()
# --8<-- [end:prodff]
print("# --8<-- [end:prodff]")




print("# --8<-- [start:prodbp]")
# --8<-- [start:prodbp]
import feloopy as flp

def test(m):
    x = m.pvar(name="x", bound=[0,10])
    y = m.bvar(name="y")
    #obj: x*y
    m.obj(m.lin_prod_bp(y,x,ub_positive=10))
    return m

flp.search(test, key_vars=["y","x"]).report()
# --8<-- [end:prodbp]
print("# --8<-- [end:prodbp]")




print("# --8<-- [start:prodbi]")
# --8<-- [start:prodbi]
import feloopy as flp

def test(m):
    y = m.bvar(name="y")
    x = m.ivar(name="x")
    #y*x
    m.obj(m.lin_prod_bi(y,x,ub_integer=10))
    return m

flp.search(test, key_vars=["y","x"]).report()
# --8<-- [end:prodbi]
print("# --8<-- [end:prodbi]")




print("# --8<-- [start:prodip]")
# --8<-- [start:prodip]
import feloopy as flp

def test(m):
    y = m.ivar("y", bound=[0,10])
    x = m.pvar("x", bound=[0,10])
    #y*x
    m.obj(m.lin_prod_ip(y,x,ub_integer=10, ub_positive=10))
    return m

flp.search(test, key_vars=["y","x"]).report()
# --8<-- [end:prodip]
print("# --8<-- [end:prodip]")




print("# --8<-- [start:piecewise]")
# --8<-- [start:piecewise]
import feloopy as flp

def test(m):
    x = m.fvar(name="x", bound=[-10,10])
    m.obj(-m.lin_approx(name="x", f=lambda x:x**2, var=x, bound=[-10,10], num_breakpoints=10))
    return m

flp.search(test,key_vars=["y","x"]).report()
# --8<-- [end:piecewise]
print("# --8<-- [end:piecewise]")



print("# --8<-- [start:linabs1]")
# --8<-- [start:linabs1]
import feloopy as flp

def test(m):
    x = m.fvar(name="x", bound=[-20,10])
    m.obj(m.lin_abs_in_obj(x, method=2, dir_obj="min"))
    return m

flp.search(test,directions=["min"],key_vars=["x"]).report()
# --8<-- [end:linabs1]
print("# --8<-- [end:linabs1]")


print("# --8<-- [start:linabs2]")
# --8<-- [start:linabs2]
import feloopy as flp

def test(m):
    x = m.fvar(name="x", bound=[-20,10])
    m.obj(m.lin_abs_in_obj(x, method=1, dir_obj="max"))
    return m

flp.search(test,directions=["max"],key_vars=["x"]).report()
# --8<-- [end:linabs2]
print("# --8<-- [end:linabs2]")



print("# --8<-- [start:linmin]")
# --8<-- [start:linmin]
import feloopy as flp

def test(m):
    x = m.fvar(name="x", bound=[-20,10])
    y = m.fvar(name="y", bound=[-30,15])
    m.obj(m.lin_min([x,y], type_min="fvar"))
    return m

flp.search(test,directions=["max"],key_vars=["x","y"]).report()
# --8<-- [end:linmin]
print("# --8<-- [end:linmin]")




print("# --8<-- [start:linmax]")
# --8<-- [start:linmax]
import feloopy as flp

def test(m):
    x = m.fvar(name="x", bound=[-20,10])
    y = m.fvar(name="y", bound=[-30,15])
    m.obj(m.lin_max([x,y], type_max="fvar"))
    return m

flp.search(test,directions=["min"],key_vars=["x","y"]).report()
# --8<-- [end:linmax]
print("# --8<-- [end:linmax]")

