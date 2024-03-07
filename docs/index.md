---
title: FelooPy user guide
---

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

<table align="center">
  <tr>
    <td style="text-align: center;">
      <canvas id="gameCanvas" width="400" height="400" style="border: 3px solid white;"></canvas>
    </td>
  </tr>
</table>

<script>
  var canvas = document.getElementById('gameCanvas');
  var context = canvas.getContext('2d');

  var snake, prey, direction, updateInterval, drawInterval, gameOver;

  function startGame() {
      snake = [{ top: canvas.height / 2, left: canvas.width / 2, direction: 'right' }];
      prey = generatePrey();
      direction = 'right';
      gameOver = false;

      if (updateInterval) clearInterval(updateInterval);
      if (drawInterval) clearInterval(drawInterval);

      updateInterval = setInterval(update, 100);
      drawInterval = setInterval(draw, 100);
  }

  function generatePrey() {
      return {
          top: Math.floor(Math.random() * (canvas.height / 20)) * 20,
          left: Math.floor(Math.random() * (canvas.width / 20)) * 20
      };
  }

  function draw() {
      if (gameOver) {
          startGame();
          return;
      }

      context.clearRect(0, 0, canvas.width, canvas.height);

      context.fillStyle = 'lightblue';
      for (var i = 0; i < snake.length; i++) {
          var segment = snake[i];
          context.save();
          context.translate(segment.left + 20, segment.top + 20);
          context.rotate((segment.direction === 'right' ? 45 : segment.direction === 'down' ? 135 : segment.direction === 'left' ? 225 : 315) * Math.PI / 180);

          context.fillRect(-20, -20, 40, 40);

          if (i === 0) {
              context.fillStyle = 'white';
              context.beginPath();
              context.arc(0, -10, 6, 0, Math.PI * 2);
              context.closePath();
              context.fill();
          }

          context.restore();
      }

      if (prey !== null) {
          context.fillStyle = 'orange';
          context.save();
          context.translate(prey.left + 20, prey.top + 20);
          context.rotate(45 * Math.PI / 180);
          context.fillRect(-20, -20, 40, 40);

          context.fillStyle = 'white';
          context.beginPath();
          context.arc(0, -10, 6, 0, Math.PI * 2);
          context.closePath();
          context.fill();

          context.restore();
      }
  }

  function update() {
      if (gameOver || prey === null) return;

      var head = Object.assign({}, snake[0]);
      var preyDirection;

      if (prey.top < head.top) {
          direction = 'up';
          preyDirection = 'down';
      } else if (prey.top > head.top) {
          direction = 'down';
          preyDirection = 'up';
      } else if (prey.left < head.left) {
          direction = 'left';
          preyDirection = 'right';
      } else if (prey.left > head.left) {
          direction = 'right';
          preyDirection = 'left';
      }

      head.direction = direction;

      if (direction === 'left') {
          head.left -= 20;
      } else if (direction === 'right') {
          head.left += 20;
      } else if (direction === 'up') {
          head.top -= 20;
      } else if (direction === 'down') {
          head.top += 20;
      }

      snake.unshift(head);

      if (head.left === prey.left && head.top === prey.top) {
          snake.push({});
          prey = generatePrey();
      } else {
          snake.pop();
      }
  }

  startGame();
</script>

## Key features

- Efficient: Optimized for speed, designed with Python in mind.
- Integrated: Seamlessly integrates with any interface and solver for optimization, making switching easy.
- Versatile: Covers linear, nonlinear, integer, mixed-integer linear, mixed-integer nonlinear programming.
- Intuitive: Code as mathematically modeled; no advanced programming knowledge is needed.
- Automated: Configure your solution method and let FelooPy handle the rest.

## Supported decision problems

FelooPy supports the following _mathematical structure-based_ classification of decision problems:

- Numerical optimization
   - Linear Programming (LP)
      - [Unconstrained] Linear Programming (ULP, or LP)
      - [Constrained] Linear Programming (CLP, or LP)
      - General Linear Programming (GLP, or LP)
   - Nonlinear Programming (NLP)
      - with nonlinear objectives
         - [Unconstrained] Quadratic Programming (UQP, or QP)
         - [Constrained] Quadratic Programming (CQP, or QP)
      - with nonlinear constraints
         - Second Order Cone Programming (SOCP)
      - with nonlinear objectives and constraints
         - General Nonlinear Programming (GNLP)
- Combinatorial optimization
   - Integer Programming (IP)
      - Pure Integer Linear Programming (PILP)
         - [Unconstrained] Pure Integer Linear Programming (UPILP, or PILP)
         - [Constrained] Pure Integer Linear Programming (CPILP, or PILP)
      - Pure Integer Nonlinear Programming (PINLP)
         - with nonlinear objectives
            - [Unconstrained] Integer Quadratic Programming (UIQP, IQP, or QUIO)
            - [Unconstrained] Binary Quadratic Programming (UBQP, BQP, or QUBO)
            - [Constrained] Integer Quadratic Programming (CIQP, IQP, or QUIO)
            - [Constrained] Binary Quadratic Programming (CBQP, BQP, or QUBO)
         - with nonlinear constraints
         - with nonlinear objectives and constraints
            - General Pure Integer Nonlinear Programming (GPINLP)
   - Mixed Integer Programming (MIP)
      - Mixed Integer Linear Programming (MILP)
         - [Unconstrained] Mixed Integer Linear Programming (UMILP, or MILP)
         - [Constrained] Mixed Integer Linear Programming (CMILP, or MILP)
      - Mixed Integer Nonlinear Programming (MINLP)
         - with nonlinear objectives
            - [Unconstrained] Mixed Integer Quadratic Programming (UMIQP, or MIQP)
            - [Constrained] Mixed Integer Quadratic Programming (CMIQP, or MIQP)
         - with nonlinear constraints
         - with nonlinear objectives and constraints
            - General Mixed Integer Nonlinear Programming (GMINLP, or GMIP)


```mermaid
graph LR 
 CLASS["FelooPy"] --> SUBCLASS1["Numerical Optimization"]
 CLASS["FelooPy"] --> SUBCLASS2["Combinatorial Optimization"]
 SUBCLASS1["Numerical Optimization"] --> A["LP"]
 SUBCLASS1["Numerical Optimization"] --> B["NLP"]
 SUBCLASS2["Combinatorial Optimization"] --> C["IP"]
 SUBCLASS2["Combinatorial Optimization"] --> D["MIP"]
 A["LP"] --> A1["ULP, or LP"]
 A["LP"] --> A2["CLP, or LP"]
 A["LP"] --> A3["GLP, or LP"]
 B["NLP"] --> B1["NLO"]
 B1["NLO"] --> B11["UQP, or QP"]
 B1["NLO"] --> B12["CQP, or QP"]
 B["NLP"] --> B2["NLC"]
 B2["NLC"] --> B21["SOCP"]
 B["NLP"] --> B3["NLOC"]
 B3["NLOC"] --> B31["GNLP"]
 C["IP"] --> C1["PILP"]
 C1["PILP"] --> C11["UPILP, or PILP"]
 C1["PILP"] --> C12["CPILP, or PILP"]
 C["IP"] --> C2["PINLP"]
 C2["PINLP"] --> C21["NLO"]
 C21["NLO"] --> C211["UIQP, IQP, or UQIO"]
 C21["NLO"] --> C212["UBQP, BQP, or UBIO"]
 C21["NLO"] --> C213["CIQP, IQP, or CQIO"]
 C21["NLO"] --> C214["CBQP, BQP, or CBIO"]
 C2["PINLP"] --> C22["NLC"]
 C2["PINLP"] --> C23["NLOC"]
 C23["NLOC"] --> C231["GPINLP"]
 D["MIP"] --> D1["MILP"]  
 D1["MILP"] --> D11["UMILP, or MILP"]
 D1["MILP"] --> D12["CMILP, or MILP"]
 D["MIP"] --> D2["MINLP"]  
 D2["MINLP"] --> D21["NLO"]
 D21["NLO"] --> D211["UMIQP"]
 D21["NLO"] --> D212["CMIQP"]
 D2["MINLP"] --> D22["NLC"]
 D2["MINLP"] --> D23["NLOC"]
 D23["NLOC"] --> D231["GMINLP, or GMIP"]
```

FelooPy supports the following _expert-based_ classification of decision problems:

- Multi-Attribute Decision-Making (MADM)
   - Weighting methods
      - without a decision-making matrix
      - with a decision-making matrix
   - Ranking methods
      - Compensatory methods
         - Scoring methods
         - Compromising methods
      - Non-compensatory methods
         - Conjunctive satisfying methods
         - Lexicographic methods
         - Outranking methods

- Group Decision-Making (GDM)

```mermaid
graph LR 
 CLASS["FelooPy"] --> SUBCLASS1["MADM"]
 CLASS["FelooPy"] --> SUBCLASS2["GDM"]
 SUBCLASS1["MADM"] --> A["Weighting"]
 SUBCLASS1["MADM"] --> B["Ranking"]
 A["Weighting"] --> A1["without decision matrix"]
 A["Weighting"] --> A2["with decision matrix"]
 B["Ranking"] --> B1["Compensatory"]
 B["Ranking"] --> B2["Non-compensatory"]
 B1["Compensatory"] --> B11["Scoring"]
 B1["Compensatory"] --> B12["Compromising"]
 B2["Non-compensatory"] --> B21["Conjunctive satisfying"]
 B2["Non-compensatory"] --> B22["Lexicographic"]
 B2["Non-compensatory"] --> B23["Outranking"]
```

## Motivation

- To increase the applicability of operations research in solving real-world problems.
- To focus more on analyzing impact and importance than solving, modeling, or coding.
- To reduce the need to prompt large language models and seek coding suggestions.
- To focus more on stability and scalability than feasibility, logicality, or optimality.
- To have an all-in-one integrated optimization environment for decision analytics.
- To enable benchmarking of various policies, models, solvers, methods, and algorithms.


## Example

```py
import feloopy as flp

m = flp.model("exact", "model_name", "pymprog")

x = m.bvar(name="x")
y = m.pvar(name="y", bound=[0, 1])
m.con(x + y <= 1, name="c1")
m.con(x - y >= 1, name="c2")
m.obj(x + y)

m.sol(["max"], "glpk")

m.report()
```

## License

FelooPy is licensed based on the [MIT license](https://github.com/ktafakkori/feloopy/blob/main/LICENSE).
