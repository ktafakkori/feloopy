### **Introduction**

| FelooPy                                            | [![version code](https://img.shields.io/badge/version-0.2.4-darkgreen.svg)](https://github.com/ktafakkori/feloopy/releases) [![number of users](https://static.pepy.tech/personalized-badge/feloopy?period=total&units=international_system&left_color=grey&right_color=darkgreen&left_text=users)](https://pepy.tech/project/feloopy) ![release date](https://img.shields.io/github/release-date/ktafakkori/feloopy?color=blue) [![monthly Downloads](https://static.pepy.tech/personalized-badge/feloopy?period=month&units=international_system&left_color=grey&right_color=blue&left_text=monthly%20downloads%20)](https://pepy.tech/project/feloopy) [![license type](https://img.shields.io/badge/license-MIT-darkred.svg)](https://opensource.org/licenses/MIT) |
| :------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![Image description](miscellaneous/logo/logo1.png) | FelooPy (pronounced /fɛlupaɪ/) is a free and open-source Python library for automated operations research. It serves as both a hyper-optimization interface and an integrated optimization environment. The name comes from the idea of suggesting practical and applicable solutions for systems, industries, and supply chains. It also references the importance of loops in programming and algorithm development, and draws similarities to the name "Floppy" to highlight memory efficiency. FelooPy helps operations research scientists achieve their goals using various target, representor, and learner models, shifting their focus from coding to modeling and analytics. _Quick install_: `pip install --upgrade feloopy`                                |

### **Installation**

<div align="center">

<table>
<tr>
<td> Method </td> <td> Description </td>
</tr>

<tr>
<td> Pypi </td>
<td>
    
`pip install feloopy==0.2.4`
</td>
</tr>

<tr>
<td> Command </td>
<td>
    
`!pip install feloopy==0.2.4`
</td>
</tr>


<tr>
<td> Script </td>
<td>
    
```python
import pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install','-U', package])
    else:
        pip._internal.main(['install','-U', package])

install('feloopy')
```
</td>
</tr>

<tr>
<td> Local </td>
<td>
    
1. Download the [feloopy-0.2.4.zip][c] file.
2. Extract it into a specific directory.
3. Open a terminal in that directory.
4. Type: `pip install .`

</td>
</tr>

<tr>
<td> Git </td>
<td>
    
`pip install -U git+https://github.com/ktafakkori/feloopy`
</td>
</tr>

</table>

[c]: https://github.com/ktafakkori/feloopy/releases