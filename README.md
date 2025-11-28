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

## ⚙️ Physics Implementation Details

The `SolarPanel` class encapsulates the physical behavior of the photovoltaic module. The methods are grounded in semiconductor physics and the Single Diode Model equations.

### 1. Fundamental Constants & Model Parameters
Defined in the `__init__` method, these constants are essential for the diode equation:

* **Boltzmann Constant ($k$):** $1.38 \times 10^{-23} J/K$. Relates temperature to energy.
* **Elementary Charge ($q$):** $1.60 \times 10^{-19} C$. The electric charge carried by a single proton/electron.
* **Ideality Factor ($n$):** Represents how closely the diode follows the ideal diode equation. For silicon cells, this typically ranges between $1.0$ and $1.5$.
* **Series Resistance ($R_s$):** Accounts for internal losses due to contact resistance and wire connections.

### 2. Environmental Adjustments (`calculate_thermal_parameters`)
Since solar panels rarely operate under Standard Test Conditions (STC: $1000W/m^2$, $25^{\circ}C$), the model calculates real-time parameters using the following physical corrections:

**A. Thermal Voltage ($V_t$)**
The driving force for the diode diffusion current, strictly dependent on cell temperature ($T$ in Kelvin):
$$V_t = \frac{N_{cells} \cdot k \cdot T}{q}$$

**B. Photocurrent correction ($I_{sc}'$)**
The generated current increases linearly with Irradiance ($G$) and slightly with temperature (due to bandgap narrowing):
$$I_{sc}(G, T) = \frac{G}{G_{ref}} \cdot I_{sc_{ref}} \cdot [1 + \alpha \cdot (T - T_{ref})]$$

**C. Open Circuit Voltage correction ($V_{oc}'$)**
Voltage drops significantly as temperature rises due to increased intrinsic carrier concentration. This is modeled using the temperature coefficient $\beta$:
$$V_{oc}(T) = V_{oc_{ref}} \cdot [1 + \beta \cdot (T - T_{ref})]$$

**D. Reverse Saturation Current ($I_0$)**
A critical parameter that defines the "leakage" of the diode. Since it is not provided in datasheets, it is numerically extracted by solving the diode equation at the Open Circuit point ($I=0, V=V_{oc}$):
$$I_0 = \frac{I_{sc}'}{e^{\left(\frac{V_{oc}'}{n \cdot V_t}\right)} - 1}$$

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

## ⚙️ Detalhes da Implementação Física

A classe `SolarPanel` encapsula o comportamento físico do módulo fotovoltaico. Os métodos são fundamentados na física de semicondutores e nas equações do Modelo de Diodo Único.

### 1. Constantes Fundamentais e Parâmetros do Modelo
Definidas no método `__init__`, estas constantes são essenciais para a equação do diodo:

* **Constante de Boltzmann ($k$):** $1.38 \times 10^{-23} J/K$. Relaciona a temperatura com a energia.
* **Carga Elementar ($q$):** $1.60 \times 10^{-19} C$. A carga elétrica transportada por um único próton/elétron.
* **Fator de Idealidade ($n$):** Representa o quão próximo o diodo segue a equação ideal. Para células de silício, este valor tipicamente varia entre $1.0$ e $1.5$.
* **Resistência Série ($R_s$):** Contabiliza as perdas internas devido à resistência de contato e conexões dos fios.

### 2. Ajustes Ambientais (`calculate_thermal_parameters`)
Como os painéis solares raramente operam sob Condições Padrão de Teste (STC: $1000W/m^2$, $25^{\circ}C$), o modelo calcula os parâmetros em tempo real usando as seguintes correções físicas:

**A. Tensão Térmica ($V_t$)**
A força motriz para a corrente de difusão do diodo, estritamente dependente da temperatura da célula ($T$ em Kelvin):
$$V_t = \frac{N_{cells} \cdot k \cdot T}{q}$$

**B. Correção da Fotocorrente ($I_{sc}'$)**
A corrente gerada aumenta linearmente com a Irradiância ($G$) e levemente com a temperatura (devido ao estreitamento do *bandgap*):
$$I_{sc}(G, T) = \frac{G}{G_{ref}} \cdot I_{sc_{ref}} \cdot [1 + \alpha \cdot (T - T_{ref})]$$

**C. Correção da Tensão de Circuito Aberto ($V_{oc}'$)**
A tensão cai significativamente conforme a temperatura sobe devido ao aumento da concentração intrínseca de portadores. Isso é modelado usando o coeficiente de temperatura $\beta$:
$$V_{oc}(T) = V_{oc_{ref}} \cdot [1 + \beta \cdot (T - T_{ref})]$$

**D. Corrente de Saturação Reversa ($I_0$)**
Um parâmetro crítico que define a "fuga" do diodo. Como não é fornecido nos datasheets, é extraído numericamente resolvendo a equação do diodo no ponto de Circuito Aberto ($I=0, V=V_{oc}$):
$$I_0 = \frac{I_{sc}'}{e^{\left(\frac{V_{oc}'}{n \cdot V_t}\right)} - 1}$$

## 🚧 Projeto em desenvolvimento ativo. Atualizações em breve.

<img width="100%" bottom=50px src ="https://capsule-render.vercel.app/api?type=waving&height=100&color=FF78CB&section=footer&reversal=false&descAlign=22&descAlignY=42"/>
