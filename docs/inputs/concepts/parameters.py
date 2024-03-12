# --8<-- [start:parameterenvironment]
import feloopy as flp

dt = flp.data_toolkit(key=0)
# --8<-- [end:parameterenvironment]


print()


print("# --8<-- [start:generatingparameters]")
# --8<-- [start:generatingparameters]
I = dt.set(name="I", bound=[0, 9])

a = dt.zeros(name="a", dim=[I])
a = dt.ones(name="a", dim=[I])
a = dt.bernoulli(name="a", dim=[I], p=0.5)
a = dt.binomial(name="a", dim=[I], n=15, p=0.4)
a = dt.poisson(name="a", dim=[I], lam=4)
a = dt.geometric(name="a", dim=[I], p=0.4)
a = dt.negative_binomial(name="a", dim=[I], r=1, p=0.4)
a = dt.hypergeometric(name="a", dim=[I], N=10, m=5, n=6)
a = dt.uniformint(name="a", dim=[I], bound=[0, 1])
a = dt.uniform(name="a", dim=[I], bound=[0, 1])
a = dt.uniform(name="a", dim=[I], bound=[0, 1])
a = dt.normal(name="a", dim=[I], mu=0, sigma=1)
a = dt.gaussian(name="a", dim=[I], mu=0, sigma=1)
a = dt.standard_normal(name="a", dim=[I])
a = dt.exponential(name="a", dim=[I], lam=0.5)
a = dt.gamma(name="a", dim=[I], alpha=0.9, lam=1)
a = dt.erlang(name="a", dim=[I], alpha=1, lam=1)
a = dt.beta(name="a", dim=[I], a=1, b=1)
a = dt.dirichlet(name="a", dim=[I])
a = dt.weight(name="a", dim=[I])
a = dt.weibull(name="a", dim=[I], beta=1, alpha=1)
a = dt.cauchy(name="a", dim=[I])

print(a)
print(type(a))
# --8<-- [end:generatingparameters]
print("# --8<-- [end:generatingparameters]")


print()


print("# --8<-- [start:samplingaset]")
# --8<-- [start:samplingaset]
a = dt.sample(name="a", init={11, 4, 21, 30}, size=2, replace=False)

print(a)
print(type(a))
# --8<-- [end:samplingaset]
print("# --8<-- [end:samplingaset]")


print()


print("# --8<-- [start:samplingalist]")
# --8<-- [start:samplingalist]
a = dt.sample(name="a", init=[11, 4, 21, 30], size=2, replace=False)

print(a)
print(type(a))
# --8<-- [end:samplingalist]
print("# --8<-- [end:samplingalist]")


print()


print("# --8<-- [start:samplinganarray]")
# --8<-- [start:samplinganarray]
import numpy as np

a = dt.sample(name="a", init=np.array([11, 4, 21, 30]), size=2, replace=False)

print(a)
print(type(a))
# --8<-- [end:samplinganarray]
print("# --8<-- [end:samplinganarray]")


print()


print("# --8<-- [start:samplingpandas]")
# --8<-- [start:samplingpandas]
import pandas as pd


data = {
    "Name": ["E", "F", "G", "H"],
    "Age": [25, 30, 22, 35],
    "City": ["A", "B", "C", "D"],
    "Salary": [60000, 80000, 55000, 70000],
}

df = pd.DataFrame(data)

a = dt.sample(name="a", init=df, size=2, replace=False)

print(a)
print(type(a))
# --8<-- [end:samplingpandas]
print("# --8<-- [end:samplingpandas]")


print()


print("# --8<-- [start:storingaparameter]")
# --8<-- [start:storingaparameter]

a = dt.store(name="a", value=1)

print(a)
print(type(a))
# --8<-- [end:storingaparameter]
print("# --8<-- [end:storingaparameter]")


print()


print("# --8<-- [start:loadingaparameter1]")
# --8<-- [start:loadingaparameter1]

a = dt.load_from_excel(
    name="a", 
    dim=0, 
    labels=["i"], 
    appearance=[1, 0], 
    file_name="data.xlsx"
)

print(a)
print(type(a))
# --8<-- [end:loadingaparameter1]
print("# --8<-- [end:loadingaparameter1]")


print()


print("# --8<-- [start:loadingaparameter2]")
# --8<-- [start:loadingaparameter2]

b = dt.load_from_excel(
    name="b", 
    dim=[4], 
    labels=["i"], 
    appearance=[1, 0], 
    file_name="data.xlsx"
)

print(b)
print(type(b))
# --8<-- [end:loadingaparameter2]
print("# --8<-- [end:loadingaparameter2]")


print()


print("# --8<-- [start:loadingaparameter3]")
# --8<-- [start:loadingaparameter3]

c = dt.load_from_excel(
    name="c", 
    dim=[4, 3], 
    labels=["i", "j"], 
    appearance=[1, 1], 
    file_name="data.xlsx"
)

print(c)
print(type(c))
# --8<-- [end:loadingaparameter3]
print("# --8<-- [end:loadingaparameter3]")


print()


print("# --8<-- [start:loadingaparameter4]")
# --8<-- [start:loadingaparameter4]

d = dt.load_from_excel(
    name="d",
    dim=[4, 2, 2],
    labels=["i", "j", "k"],
    appearance=[1, 2],
    file_name="data.xlsx",
)

print(d)
print(type(d))
# --8<-- [end:loadingaparameter4]
print("# --8<-- [end:loadingaparameter4]")


print()


print("# --8<-- [start:loadingaparameter5]")
# --8<-- [start:loadingaparameter5]

e = dt.load_from_excel(
    name="e",
    dim=[4, 2, 2],
    labels=["i", "j", "k"],
    appearance=[2, 1],
    file_name="data.xlsx",
)

print(e)
print(type(e))
# --8<-- [end:loadingaparameter5]
print("# --8<-- [end:loadingaparameter5]")
