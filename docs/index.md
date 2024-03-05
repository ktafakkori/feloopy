#

<img src="assets/banner.png" alt="logo">

<h2 align='center'>Efficient & Feature-Rich Integrated Optimization Environment</h2>

<center>

[![GitHub stars](https://img.shields.io/github/stars/ktafakkori/feloopy?label=stars&style=flat-rounded&color=success&logo=github)](https://github.com/ktafakkori/feloopy/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/ktafakkori/feloopy?label=forks&style=flat-rounded&color=blue)](https://github.com/ktafakkori/feloopy/network/members)
[![GitHub tag](https://img.shields.io/github/v/tag/ktafakkori/feloopy?sort=semver&label=version&style=flat-rounded&color=orange)](https://github.com/ktafakkori/feloopy/releases)
[![Downloads](https://pepy.tech/badge/feloopy?style=flat-rounded&color=green)](https://pepy.tech/project/feloopy)
[![GitHub](https://img.shields.io/github/license/ktafakkori/feloopy?style=flat-rounded&color=red)](https://github.com/ktafakkori/feloopy/blob/main/LICENSE)

</center>

FelooPy (pronounced /fɛlupaɪ/) is a comprehensive and versatile Decision Science and Operations Research library. It allows for coding, modeling, and solving decision problems and aligns with low or no-code requirements, letting you focus more on analytics. The library covers various categories of mathematical and statistical methods for decision-making and utilizes numerous interfaces and solvers without requiring prompting large language models or learning complex coding syntaxes. It is primarily developed in Python, which makes it accessible and callable from multiple programming languages.

## Key features

- Efficient: Optimized for speed, designed with Python in mind.
- Integrated: Seamlessly integrates with any interface and solver for optimziation, easy switch.
- Versatile: Covers linear, non-linear, integer, mixed-integer, mixed integer nonlinear programming.
- Intuitive: Code as it is mathematically modeled, no advanced programming knowledge needed.
- Automated: Configure your solution method, let FelooPy handle the rest.

## Motivation

- To increase the applicability of operations research in solving real-world problems.
- To focus more on analyzing impact and importance than solving, modeling, or coding.
- To reduce the need for prompting large language models and seeking coding suggestions.
- To focus more on stability and scalability than feasibility, logicality, or optimality.
- To have an all-in-one integrated optimization environment for decision analytics.
- To enable benchmarking of various policies, models, solvers, methods, and algorithms.

## Example

```py
import feloopy as flp

m = flp.model("exact", "model_name", "pymprog")

x = m.bvar(name="x", dim=0)
y = m.pvar(name="y", dim=0, bound=[0, 10])
m.con(x + y <= 1, label="c1")
m.con(x - y >= 1, label="c2")
m.obj(x + y)

m.sol(["max"], "glpk")

m.report()
```

## License

FelooPy is licensed based on the [MIT license](https://github.com/ktafakkori/feloopy/blob/main/LICENSE).