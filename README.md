

<p align="center">
   <img src="miscellaneous/logo/logo1.png" width="20%">
</p>


## Introduction

**FelooPy** (pronounced /fɛlupaɪ/) is an **integrated optimization environment** (IOE) designed for **decision optimization**. It involves the use of **automated operations research** (AutoOR) methods and techniques to identify **feasible solutions** that lead to **logical decisions** with the **optimal (best possible)** outcomes based on **given** or **learnable** policies. This Python library **simplifies** and **enhances** the use of **_existing_** and **_originally developed_** modeling, algorithm development, and analytical tools for decision-making within simulated **systems**, **industries**, and **supply chains**. FelooPy is an acronym alluding to an operations research scientist in pursuit of **fe**asible solutions, **lo**gical decisions, and **op**timal outcomes by optimization in **Py**thon. Additionally, it alludes to the concept of **loops** in computer programming and the **floppy disk**, symbolizing computing and memory efficiency. The development of FelooPy, which started in **September 2022**, continues under the **MIT license**.

Overview:

![Version](https://img.shields.io/static/v1?label=version&message=0.2.7&color=darkgreen)
![Score](https://img.shields.io/github/stars/ktafakkori/feloopy?label=score&color=darkgreen)
![Release Date](https://img.shields.io/github/release-date/ktafakkori/feloopy?label=release%20date&color=darkgreen)
[![Total Users](https://static.pepy.tech/personalized-badge/feloopy?period=total&units=international_system&left_color=grey&right_color=blue&left_text=total%20users)](https://pepy.tech/project/feloopy?&left_text=totalusers)
![Monthly Users](https://img.shields.io/pypi/dm/feloopy?label=monthly%20users&color=blue)
![Source Users](https://img.shields.io/github/downloads/ktafakkori/feloopy/total?label=source%20users&color=blue)
![License](https://img.shields.io/static/v1?label=license&message=MIT&color=darkred) 


Learn more:

[![LinkedIn](https://img.shields.io/badge/LinkedIn%20Group%20-blue?&color=darkblue&label=join)](https://www.linkedin.com/groups/12881077/) [![Telegram](https://img.shields.io/badge/Telegram%20Group%20-blue?&color=darkblue&label=join)](https://t.me/feloop_group)
[![Telegram](https://img.shields.io/badge/Instagram%20Page%20-blue?&color=darkblue&label=follow)](https://instagram.com/feloop_page)

## Features

FelooPy supports the following _mathematical structure-based_ classification of optimization problems:

 - Linear Programming (LP)
   - [Unconstrained] Linear Programming (ULP, or LP)
   - [Constrained] Linear Programming (CLP, or LP)
 - Non-Linear Programming (NLP)
   - with non-linear objectives
      - [Unconstrained] Quadratic Programming (UQP, or QP)
      - [Constrained] Quadratic Programming (CQP, or QP)
   - with non-linear constraints
      - Second Order Cone Programming (SOCP)
   - with non-linear objectives and constraints
      - General Non-Linear Programming (GNLP)
- Integer Programming (IP)
   - Pure Integer Linear Programming (PILP)
      - [Unconstrained] Pure Integer Linear Programming (UPILP, or PILP)
      - [Constrained] Pure Integer Linear Programming (CPILP, or PILP)
   - Pure Integer Non-Linear Programming (PINLP)
      - with non-linear objectives
         - [Unconstrained] Integer Quadratic Programming (UIQP, IQP, or QUIO)
         - [Unconstrained] Binary Quadratic Programming (UBQP, BQP, or QUBO)
         - [Constrained] Integer Quadratic Programming (CIQP, CIQP, or QUIO)
         - [Constrained] Binary Quadratic Programming (CBQP, CBQP, or QUBO)
      - with non-linear constraints
      - with non-linear objectives and constraints
         - General Pure Integer Non-Linear Programming (GPINLP)
 - Mixed Integer Programming (MIP)
   - Mixed Integer Linear Programming (MILP)
      - [Unconstrained] Mixed Integer Linear Programming (UMILP, or MILP)
      - [Constrained] Mixed Integer Linear Programming (CMILP, or MILP)
   - Mixed Integer Non-Linear Programming (MINLP)
      - with non-linear objectives
         - [Unconstrained] Mixed Integer Quadratic Programming (UMIQP, or MIQP)
         - [Constrained] Mixed Integer Quadratic Programming (CMIQP, or MIQP)
      - with non-linear constraints
      - with non-linear objectives and constraints
         - General Mixed Integer Non-Linear Programming (GMINLP)

```mermaid
graph TD
 A["LP"]
 B["ULP, or LP"]
 C["CLP, or LP"]
 D["NLP"]
 E["with non-linear objectives"]
 F["QP"]
 G["with non-linear constraints"]
 H["GNLP"]
 I["IP"]
 J["PILP"]
 K["UPILP, or PILP"]
 L["CPILP, or PILP"]
 M["PINLP"]
 N["with non-linear objectives"]
 O["UIQP, IQP, or QUIO"]
 P["with non-linear constraints"]
 Q["with non-linear objectives and constraints"]
 R["GPINLP"]
 S["MIP"]
 T["MILP"]
 U["UMILP, or MILP"]
 V["CMILP, or MILP"]
 W["MINLP"]
 X["with non-linear objectives"]
 Y["UMIQP, or MIQP"]
 Z["CMIQP, or MIQP"]
 AA["with non-linear constraints"]
 AB["with non-linear objectives and constraints"]
 AC["GMINLP"]
 A --> B
 A --> C
 A --> D
 D --> E
 D --> F
 F --> G
 D --> H
 D --> I
 I --> J
 J --> K
 J --> L
 I --> M
 M --> N
 M --> O
 O --> P
 O --> Q
 I --> R
 I --> S
 S --> T
 T --> U
 T --> V
 S --> W
 W --> X
 W --> Y
 Y --> Z
 Z --> AA
 Z --> AB
 S --> AC
```