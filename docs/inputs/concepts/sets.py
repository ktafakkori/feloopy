# --8<-- [start:setenvironment]
import feloopy as flp
dt = flp.data_toolkit(key=0)
# --8<-- [end:setenvironment]



print()



print("# --8<-- [start:simpleset]")
# --8<-- [start:simpleset]
I = dt.set(name="I", bound=[0, 9], named_indices=True)

print(I)
print(type(I))
# --8<-- [end:simpleset]
print("# --8<-- [end:simpleset]")



print()



print("# --8<-- [start:recommendedset]")
# --8<-- [start:recommendedset]
I = dt.set(name='I', bound=[0, 9])

print(I)
print(type(I))
# --8<-- [end:recommendedset]
print("# --8<-- [end:recommendedset]")


print()


print("# --8<-- [start:conditionalset]")
# --8<-- [start:conditionalset]
I = dt.set(name="I", bound=[0, 9], callback=lambda x: x % 2 == 0)

print(I)
print(type(I))
# --8<-- [end:conditionalset]
print("# --8<-- [end:conditionalset]")


print()


print("# --8<-- [start:setaslist]")
# --8<-- [start:setaslist]
I = dt.set(name="I", bound=[0, 9], to_list=True)

print(I)
print(type(I))
# --8<-- [end:setaslist]
print("# --8<-- [end:setaslist]")


print()


print("# --8<-- [start:setasrange]")
# --8<-- [start:setasrange]
I = dt.set(name="I", bound=[0, 9], to_range=True)

print(I)
print(type(I))
# --8<-- [end:setasrange]
print("# --8<-- [end:setasrange]")

print()


print("# --8<-- [start:directset1]")
# --8<-- [start:directset1]
I = dt.set(name="I", init=range(10))

print(I)
print(type(I))
# --8<-- [end:directset1]
print("# --8<-- [end:directset1]")


print()


print("# --8<-- [start:directset2]")
# --8<-- [start:directset2]
I = dt.set(name="I", init=10)

print(I)
print(type(I))
# --8<-- [end:directset2]
print("# --8<-- [end:directset2]")


print()


print("# --8<-- [start:directset3]")
# --8<-- [start:directset3]
import numpy as np
a = np.array([[1,2,3,2,3,53,55,21,1,23]])

I = dt.set(name="I", init=a, axis=1)

print(I)
print(type(I))
# --8<-- [end:directset3]
print("# --8<-- [end:directset3]")


print()


print("# --8<-- [start:directset4]")
# --8<-- [start:directset4]
I = dt.set(name="I", size=10)

print(I)
print(type(I))
# --8<-- [end:directset4]
print("# --8<-- [end:directset4]")



print("# --8<-- [start:aliasset1]")
# --8<-- [start:aliasset1]
I = dt.set(name="I", size=10)
J = dt.alias(name="J", init=I)

print(J)
print(type(J))
# --8<-- [end:aliasset1]
print("# --8<-- [end:aliasset1]")


print("# --8<-- [start:aliasset2]")
# --8<-- [start:aliasset2]
J = I

print(J)
print(type(J))
# --8<-- [end:aliasset2]
print("# --8<-- [end:aliasset2]")