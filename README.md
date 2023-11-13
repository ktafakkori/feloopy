

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
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

```mermaid
graph TD;
   A[Linear Programming (LP)];
   B[Unconstrained Linear Programming (ULP, or LP)];
   C[Constrained Linear Programming (CLP, or LP)];
   D[Non-Linear Programming (NLP)];
   E[Integer Programming (IP)];
   F[Pure Integer Linear Programming (PILP)];
   G[Unconstrained Pure Integer Linear Programming (UPILP, or PILP)];
   H[Constrained Pure Integer Linear Programming (CPILP, or PILP)];
   I[Pure Integer Non-Linear Programming (PINLP)];
   J[General Pure Integer Non-Linear Programming (GPINLP)];
   K[Mixed Integer Programming (MIP)];
   L[Mixed Integer Linear Programming (MILP)];
   M[Unconstrained Mixed Integer Linear Programming (UMILP, or MILP)];
   N[Constrained Mixed Integer Linear Programming (CMILP, or MILP)];
   O[Mixed Integer Non-Linear Programming (MINLP)];
   A --> B;
   A --> C;
   D --> E;
   E --> F;
   F --> G;
   E --> H;
   E --> I;
   I --> J;
   K --> L;
   L --> M;
   M --> N;
   N --> O;
```