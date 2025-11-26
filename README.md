<img width="100%" bottom=50px src ="https://capsule-render.vercel.app/api?type=waving&height=100&color=FF78CB&section=header&reversal=false&descAlign=22&descAlignY=42"/>

<div align = "center" id="english">
<img width="150" height="150" alt="Image" src="https://github.com/user-attachments/assets/a217336e-dd1f-4642-a127-15807e9133ef" />

<a href="https://github.com/albiecr"><img src="https://readme-typing-svg.herokuapp.com?font=Sour+Gummy&size=40&pause=100&color=EF82F7&width=400&height=60&lines=Photovoltaic+Simulator" alt="Typing SVG" /></a></div>



<p align="center">
  <strong>English</strong> | <a href="#português">Português</a>
</p>

<p align="center">
The Photovoltaic Simulator is a computational modeling tool developed in Python to simulate the electrical behavior of solar modulesunder varying environmental conditions.
</p>


<p align="center">
  <img src="https://img.shields.io/badge/status-in%20development-yellow" alt="Project Status">
</p>

## ☀️ About the project

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

## 🚧 Project under active development. Updates coming soon.

---

<div align = "center" id="português">
<img width="150" height="150" alt="Image" src="https://github.com/user-attachments/assets/a217336e-dd1f-4642-a127-15807e9133ef" />
  
<a href="https://github.com/albiecr"><img src="https://readme-typing-svg.herokuapp.com?font=Sour+Gummy&size=40&pause=100&color=EF82F7&width=400&height=60&lines=Simulador+Votoltaico" alt="Typing SVG" /></a></div>
<p align="center">
  <a href="#english">English</a> | <strong>Português</strong>
</p>

<p align="center"> O Simulador Fotovoltaico é uma ferramenta de modelagem computacional desenvolvida para simular as características elétricas de módulos fotovoltaicos sob condições ambientais variadas. 
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-em%20desenvolvimento-yellow" alt="Project Status">
</p>

## ☀️ Sobre o Projeto

Ao contrário de aproximações lineares simples, este projeto implementa o **Modelo de Diodo Único (Single Diode Model - SDM)**, um modelo físico que representa a célula solar como uma fonte de corrente em paralelo com um diodo e resistências parasitas ($R_s$ e $R_{sh}$). Como a equação característica $I-V$ deste modelo é transcendental (não-linear), o sistema utiliza o método numérico de **Newton-Raphson** para resolver a corrente de saída com alta precisão.

### Principais Funcionalidades

- **Modelagem Baseada na Física:** Representação precisa da deriva térmica de $V_{oc}$ (Tensão de Circuito Aberto) e $I_{sc}$ (Corrente de Curto-Circuito).
- **Arquitetura POO:** Design modular utilizando `dataclasses` para abstração do Datasheet e classes para componentes físicos, permitindo fácil escalabilidade para simular arranjos fotovoltaicos completos.
- **Visualização de Dados:** Geração automática de curvas I-V e P-V utilizando Matplotlib.

Este projeto serve tanto como uma ferramenta de engenharia para estimativa de desempenho quanto como um estudo sobre a aplicação de **Programação Orientada a Objetos** para resolver problemas físicos de engenharia.

## 🛠️ Tecnologias Utilizadas

O projeto foi construído utilizando Python 3, com foco em bibliotecas de computação científica e práticas de código limpo (clean code).

- **Linguagem Principal:** Implementação de lógica e POO.
- **Computação Numérica:** Utilizada para vetorização e manipulação de constantes matemáticas.
- **Plotagem:** Biblioteca usada para renderizar as curvas I-V e P-V.
- **Dataclasses:** Utilizadas para criar estruturas de dados imutáveis e tipadas para as especificações dos módulos.
- **Mermaid & LaTeX:** Utilizados para documentação, diagramas UML e renderização matemática dentro do repositório.

## 📐 Fundamentação Matemática

O núcleo desta simulação é o **Modelo de Diodo Único**, amplamente utilizado na engenharia fotovoltaica para representar o comportamento elétrico de uma célula solar. A equação fundamental que relaciona corrente ($I$) e tensão ($V$) é transcendental, o que significa que não pode ser resolvida analiticamente de forma direta.

A equação característica implementada é:

$$I = I_{ph} - I_0 \cdot \left( e^{\frac{V + I \cdot R_s}{n \cdot V_t}} - 1 \right)$$

Onde:

- $I$: Corrente de saída (A)
- $V$: Tensão de saída (V)
- $I_{ph}$: Fotocorrente (A), diretamente proporcional à irradiância ($G$).
- $I_0$: Corrente de saturação reversa do diodo (A).
- $n$: Fator de idealidade do diodo.
- $R_s$: Resistência série ($\Omega$).
- $V_t$: Tensão térmica (V).

### Tensão Térmica

A tensão térmica é uma função da temperatura da célula ($T_{cell}$), derivada de constantes físicas:

$$V_t = \frac{k \cdot T_{cell}}{q}$$

Onde $k$ é a constante de Boltzmann ($1.38 \times 10^{-23} J/K$) e $q$ é a carga elementar ($1.602 \times 10^{-19} C$).

### Solução Numérica

Como $I$ aparece em ambos os lados da equação, definimos uma função $f(I) = 0$ e encontramos sua raiz utilizando o **método de Newton-Raphson**:

$$I_{new} = I_{old} - \frac{f(I_{old})}{f'(I_{old})}$$

Este processo iterativo garante alta precisão na geração da curva I-V.

## 🚧 Projeto em desenvolvimento ativo. Atualizações em breve.

<img width="100%" bottom=50px src ="https://capsule-render.vercel.app/api?type=waving&height=100&color=FF78CB&section=footer&reversal=false&descAlign=22&descAlignY=42"/>
