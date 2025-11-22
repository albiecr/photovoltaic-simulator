<img width="100%" bottom=50px src ="https://capsule-render.vercel.app/api?type=waving&height=100&color=FF78CB&section=header&reversal=false&descAlign=22&descAlignY=42"/>

<div align = "center" id="english">
<a href="https://github.com/albiecr"><img src="https://readme-typing-svg.herokuapp.com?font=Sour+Gummy&size=40&pause=100&color=EF82F7&width=400&height=60&lines=Photovoltaic+Simulator" alt="Typing SVG" /></a></div>



<p align="center">
  <strong>English</strong> | <a href="#português">Português</a>
</p>

<p align="center">
The Photovoltaic Simulator is a computational modeling tool developed in Python to simulate the electrical behavior of solar modules.
</p>


<p align="center">
  <img src="https://img.shields.io/badge/status-in%20development-yellow" alt="Project Status">
</p>

## ☀️ About the project

The Photovoltaic Simulator is a computational modeling tool developed to simulate the electrical characteristics of photovoltaic modules under varying environmental conditions.

Unlike simple linear approximations, this project implements the Single Diode Model (SDM), a physical model that represents the solar cell as a current source in parallel with a diode and parasitic resistances ($R_s$ and $R_{sh}$). Since the characteristic $I-V$ equation of this model is transcendental (non-linear), the system utilizes the Newton-Raphson numerical method to solve for the output current with high precision.

### Key Features

- Physics-based Modeling: accurate representation of $V_{oc}$ and $I_{sc}$ thermal drift.
- OOP Architecture: modular design using dataclasses for Datasheet abstraction and classes for physical components, allowing easy scalability to simulate full PV arrays.

- Data Visualization: automated generation of I-V and P-V curves using Matplotlib.

This project serves as both an engineering tool for performance estimation and a study on applying Object-Oriented Programming to solve physical engineering problems.

## 🛠️ Technologies Used

The project was built using Python 3, focusing on scientific computing libraries and clean code practices.

- **Core Language:** Logic and OOP implementation.

- **Numerical Computing:** Used for vectorization and handling mathematical constants.

- **Plotting:** Library used to render the I-V and P-V curves.

- **Dataclasses:** Used to create immutable and type-safe data structures for module specifications.

- **Mermaid & LaTeX:** Used for documentation, UML diagrams, and mathematical rendering within the repository.

## 📐 Mathematical Background

The core of this simulation is the **Single Diode Model**, widely used in photovoltaic engineering to represent the electrical behavior of a solar cell. The fundamental equation relating current ($I$) and voltage ($V$) is transcendental, meaning it cannot be solved analytically directly.

The characteristic equation implemented is:

$$I = I_{ph} - I_0 \cdot \left( e^{\frac{V + I \cdot R_s}{n \cdot V_t}} - 1 \right)$$

Where:

- $I$: Output current (A)
- $V$: Output voltage (V)
- $I_{ph}$: Photocurrent (A), directly proportional to irradiance ($G$).
- $I_0$: Diode reverse saturation current (A).
- $n$: Diode ideality factor.
- $R_s$: Series resistance ($\Omega$).
- $V_t$: Thermal voltage (V).

### Thermal Voltage

The thermal voltage is a function of the cell temperature ($T_{cell}$), derived from physical constants:

$$V_t = \frac{k \cdot T_{cell}}{q}$$

Where $k$ is the Boltzmann constant ($1.38 \times 10^{-23} J/K$) and $q$ is the elementary charge ($1.602 \times 10^{-19} C$).

### Numerical Solution

Since $I$ appears on both sides of the equation, we define a function $f(I) = 0$ and find its root using the **Newton-Raphson method**:

$$I_{new} = I_{old} - \frac{f(I_{old})}{f'(I_{old})}$$

This iterative process ensures high precision for the $I-V$ curve generation.

## New informations soon

