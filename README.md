# Fourier Visualizer / Synthesis

**Author:** André Luiz Caillot de Oliveira Filho

**Base Code Attribution:** Giovanni Alfredo Guarneri (Communication Systems Professor)

---
## Problem's description
During my classes of Linear Systems back in the 4th semester (Sinais e Sistemas), we learnt how to approximate any (or at least some kinds of) signals using Fourier Series Expansion (FSE), which breaks a periodical function into an infinite sum of sines and cossines. You can see below the formula:

$f(x) = \frac{a_0}{2} + \displaystyle \sum_{n=1}^{\infty} \left[ a_n \cos\left(\frac{n \pi x}{L}\right) + b_n \sin\left(\frac{n \pi x}{L}\right) \right]$

I won't give exactly all the context to calculate the expansion (in this moment), but as the answers become too big, it becomes really hard to verify if your result is correct in an exam question or something. Thinking of this problem has led me, a semester later, to develop a tool that can help other students to visualize if their results match with the base function.

Right now, I am in the 5th semester, and I have a discipline called Communication Systems (Sistemas de Comunicação), and my teacher proposed the students to implement some functions from a base code that he has developed. 

I know that there are already many tools to visualize signals, but as I'm not as skilled in Python as I want, I've challenged myself to create this tool using the base code, Python's documentation and some AI help. I also hope that this project can help someone in their studies.

---

## Objectives and Project Especifications
The main objective of this project is to develop a Python tool to synthesize, approximate, evaluate, and plot periodic signals.
 * **Language:** Python 3.14
* **Dependencies:** NumPy, Matplotlib
* **Core Capabilities:**
  * Fundamental angular frequency calculation ($\omega_0$).
  * Ideal square wave generation based on time-domain conditions.
  * Wave approximation via Fourier Series Expansion up to $N$ harmonics.
  * Signal quality evaluation via Mean Square Error (MSE).
  * Power analysis using Parseval's Theorem.
  * Overlaid visualization of ideal vs. approximated signals.

---

##  Program Logic (How it Works?)
The execution flow follows these steps: 
1. **Initialization:** Defines period $T_0 = 2.0$, time vector $t \in [0, 2.001]$ with step $0.001$, and maximum harmonic order $N = 19$.
2. **Fundamental Frequency ($\omega_0$):** Computes $\omega_0 = \frac{2\pi}{T_0}$ via `calcular_frequencia_fundamental()`.
3. **Ideal Signal Generation:** Constructs a square wave $g(t) \in \{-1, 1\}$ using Boolean mask conditions in `gerar_sinal_ideal()`.
4. **Fourier Synthesis:** 
   * Iterates through odd harmonics ($n = 1, 3, 5, \dots, N$).
   * Calculates Fourier coefficients $a_n = \frac{4 \sin(n\pi/2)}{n\pi}$.
   * Accumulates harmonic components: $g_{approx}(t) = \sum a_n \cos(n \omega_0 t)$.
   * Computes power contribution of the $N$-th harmonic: $P_N = \frac{a_n^2}{2}$.
5. **Error Calculation:** Evaluates approximation fidelity using Mean Square Error:
   $$\text{MSE} = \frac{1}{M} \sum_{i=1}^{M} (g_{approx}(t_i) - g_{ideal}(t_i))^2$$
6. **Visualization:** Displays a dual-plot overlay using Matplotlib.

---

## Mathematical Formulas

### Fourier Series Coefficients (Even Square Wave)
$$a_n = \frac{4 \sin\left(\frac{n\pi}{2}\right)}{n\pi}, \quad b_n = 0$$

### Signal Approximation
$$g_{approx}(t) = \sum_{n=1, 3, 5, \dots}^{N} a_n \cos(n \omega_0 t)$$

### Mean Square Error (MSE)
$$\text{MSE} = \frac{1}{M} \sum_{i=1}^{M} \left( g_{approx}[i] - g_{ideal}[i] \right)^2$$

### Harmonic Power Component (Parseval's Relation)
$$P_N = \frac{a_n^2}{2}$$

---

## How to run the project

### Prerequisites
Make sure you have Python installed along with the required libraries:

```bash
pip install numpy matplotlib
```
After installing Python and the libraries, clone the repository and run the main script:
```bash
git clone [https://github.com/alcdof/Fourier-Synthesis.git](https://github.com/alcdof/Fourier-Synthesis.git)
cd Fourier-Synthesis
python main.py
```
---
## Disclaimer
This project is for educational purposes. The initial skeleton code was created by Prof. Giovanni Alfredo Guarneri for the Communication Systems course. Functions for signal generation, Fourier expansion, error metrics, and plotting were expanded and refined by André Luiz Caillot de Oliveira Filho.

---

## Contact
**André Luiz Caillot de Oliveira Filho** - Computer Engineering Student @ UTFPR

* **LinkedIn:** [linkedin.com/in/alcdof](https://linkedin.com/in/alcdof)
* **GitHub:** [github.com/alcdof](https://github.com/alcdof)
* **Email:** [andreluizfilho@alunos.utfpr.edu.br](mailto:andreluizfilho@alunos.utfpr.edu.br)

---

*Feel free to reach out if you have any questions, suggestions, or just want to discuss Signal Processing and Python!*