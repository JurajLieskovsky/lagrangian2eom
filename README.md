# Lagrangian to Equations of Motion

A tiny package for symbolically deriving a system's equations of motion in the form
$$\mathbf{M}(\mathbf{q})\mathbf{\ddot{q}} + \mathbf{c}(\mathbf{q},\mathbf{\dot{q}}) - \mathbf{\tau}_p(\mathbf{q}) = \mathbf{\tau} + \sum_j \mathbf{W}_j(\mathbf{r}_j,\mathbf{q}) \mathbf{F}_j$$
for a vector of generalized coordinates $\mathbf{q}$ from the system's kinetic energy $T(\mathbf{q},\mathbf{\dot{q}})$ and potential energy $V(\mathbf{q})$, that together form the Lagrangian $L = T-V$.

Additionally, given $\mathbf{r}_j(\mathbf{q})$, i.e. vectors to points where external forces $\mathbf{F}_j$ are applied to the system, wrench matrices can also be derived.

## Individual terms
$$
\begin{aligned}
\mathbf{M} &= \frac{\partial^2 T}{\partial \mathbf{\dot{q}}^2} \\
\mathbf{c} &= \frac{\partial^2 T}{\partial \mathbf{\dot{q}} \partial \mathbf{q}} \mathbf{\dot{q}} - \frac{\partial T}{\partial \mathbf{q}} \\
\mathbf{\tau}_p &= - \frac{\partial V}{\partial \mathbf{q}} \\
\mathbf{W}_j &= \frac{\partial \mathbf{r}_j}{\partial \mathbf{q}}
\end{aligned}
$$

## Installation

lagrangian2eom can be installed using pip directly from github
```
pip install lagrangian2eom@git+https://github.com/CVUT-FS-12110/lagrangian2eom
```
or by first cloning the repository and then providing the path
```
pip install <path to lagrangian2eom>
```

## Examples
[Cart-Pole](https://github.com/CVUT-FS-12110/CartPoleEoM)
[Acrobot](https://github.com/CVUT-FS-12110/AcrobotEoM)
