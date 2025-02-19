# Lagrangian to Equations of Motion

A tiny package for symbolically deriving a system's equations of motion in the form
$$M(q)\ddot{q} + c(q,\dot{q}) - \tau_p(q) = \tau + \sum_j W_j(q) F_j$$
for a vector of generalized coordinates $q$ from the system's kinetic energy $T(q,\dot{q})$ and potential energy $V(q)$, that together form the Lagrangian $L = T-V$.

Additionally, given $r_j(q)$, i.e. vectors to points where external forces $F_j$ are applied to the system, wrench matrices can also be derived.

## Individual terms
$$
\begin{aligned}
M &= \frac{\partial^2 T}{\partial \dot{q}^2} \\
c &= \frac{\partial^2 T}{\partial \dot{q} \partial q} \dot{q} - \frac{\partial T}{\partial q} \\
\tau_p &= - \frac{\partial V}{\partial q} \\
W_j &= \left(\frac{\partial r_j}{\partial q}\right)^\top
\end{aligned}
$$

## Installation

lagrangian2eom can be installed using pip directly from github
```
pip install lagrangian2eom@git+https://github.com/lieskjur/lagrangian2eom
```
or by first cloning the repository and then providing the path
```
pip install <path to lagrangian2eom>
```

## Examples
- [Cart-Pole](https://github.com/JurajLieskovsky//CartPoleEoM)
- [Acrobot](https://github.com/JurajLieskovsky//AcrobotEoM)
- [Bi-Rotor](https://github.com/JurajLieskovsky//BiRotorEoM)
