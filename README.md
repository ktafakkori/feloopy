<div align="center">
  <p>
    <a align="center" href="" target="https://ktafakkori.github.io">
      <img
        width="100%"
        src="docs/assets/banner.png"
      >
    </a>
  </p>
</div>

<h2 align='center'>Efficient & Feature-Rich Integrated Decision Environment</h2>


<div align="center" style="margin-bottom: 2px;">

![Version](https://img.shields.io/static/v1?label=Version&message=v0.2.9&color=darkgreen)
![Release Date](https://img.shields.io/github/release-date/ktafakkori/feloopy?label=release&color=darkgreen)
[![Documentation](https://readthedocs.org/projects/feloopy/badge/?label=docs&version=latest&color=darkgreen)](https://feloopy.readthedocs.io/en/latest/?badge=latest&color=darkgreen&label=docs)
[![Discord](https://img.shields.io/discord/1196153377969676399)](https://discord.gg/VpZDeG8wbv)
![License](https://img.shields.io/static/v1?label=license&message=MIT&color=darkred)

[![Total Users](https://static.pepy.tech/personalized-badge/feloopy?period=total&units=international_system&left_color=grey&right_color=blue&left_text=total%20users)](https://pepy.tech/project/feloopy?&left_text=totalusers)
[![Monthly Users](https://img.shields.io/pypi/dm/feloopy?label=monthly%20users&color=blue)](https://pypistats.org/packages/feloopy)
![Source Users](https://img.shields.io/github/downloads/ktafakkori/feloopy/total?label=source%20users&color=blue)
</div>

FelooPy (pronounced /fɛlupaɪ/) is a comprehensive and versatile Decision Science and Operations Research library. It allows for coding, modeling, and solving decision problems and aligns with low or no-code requirements, letting you focus more on analytics. The library covers various categories of mathematical and statistical methods for decision-making and utilizes numerous interfaces and solvers without requiring prompting large language models or learning complex coding syntaxes. It is primarily developed in Python, which makes it accessible and callable from multiple programming languages.

[This](https://github.com/ktafakkori/feloopy) is FelooPy project's repository hosted by GitHub.  For more information, please refer to FelooPy's [documentation](https://feloopy.readthedocs.io/en/latest/).

## Quick installation

You can install `feloopy` inside a Python>=3.10.x environment.

```py
pip install -U "feloopy[stock]==0.2.9"
```

## Quick test

Here is an example to test FelooPy's functionality:

```py
import feloopy as flp

m = flp.model(name="model_name", method="exact", interface="pymprog")

x = m.bvar(name="x")
y = m.pvar(name="y", bound=[0, 1])
m.con(x + y <= 1, name="c1")
m.con(x - y >= 1, name="c2")
m.obj(x + y)

m.sol(directions=["max"], solver="glpk")

m.clean_report()
```

## Citation

To cite or give credit to FelooPy in publications, projects, presentations, web pages, blog posts, etc. please use one of the following entries, based on the used version:

### Version<=0.2.8

- LaTeX:

   ```console
   @software{ktafakkori2022Sep,
   author       = {Keivan Tafakkori},
   title        = { {FelooPy: An integrated optimization environment for AutoOR in Python} },
   year         = {2022},
   month        = sep,
   publisher    = {GitHub},
   url          = {https://github.com/ktafakkori/feloopy/}
   }
   ```

- APA:

   Tafakkori, K. (2022). FelooPy: An integrated optimization environment for AutoOR in Python [Python Library]. Retrieved from https://github.com/ktafakkori/feloopy (Original work published September 2022).

### Version>=0.2.9


- LaTeX:

   ```console
   @software{ktafakkori2024Apr,
   author       = {Keivan Tafakkori},
   title        = { {FelooPy: Efficient and feature-rich integrated decision environment} },
   year         = {2024},
   month        = apr,
   publisher    = {GitHub},
   url          = {https://github.com/ktafakkori/feloopy/}
   }
   ```

- APA:

   Tafakkori, K. (2024). Efficient and feature-rich integrated decision environment [Python Library]. Retrieved from https://github.com/ktafakkori/feloopy (Original work published April 2024).

- In-text:

   * _Note_ 1: Please write the version you used, the latest is v0.2.9.
   * _Note_ 2: Using secondary interfaces or solvers might also require a citation to their projects.

   Example: FelooPy (v0.2.9) was used in conjunction with [interface x] (v0.0.0) (except `feloopy` itself) as the interface and [solver y] (v0.0.0) as the solver.
