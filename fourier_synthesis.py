# Disclaimer: This code isn't my intellectual property. The base code (this file) was made 
# by my Communication Systems' teacher: Giovanni Alfredo Guarneri. 
# I've just added/improved some of the functions that are below.

import numpy as np
import matplotlib.pyplot as plt

T0 = 2.0
t = np.arange(0, 2.001, 0.001)
N = 19

def calcular_frequencia_fundamental(T0):
    w0 = 2 * np.pi / T0

    return w0

def gerar_sinal_ideal(t):
    condicao = ((t >= 0.0) & (t < 0.5) | (t >= 1.5) & (t <= 2.0))
        
    return np.where(condicao, 1.0, -1.0)

def aproximar_fourier(t, w0, N):
    g_approx = np.zeros_like(t)

    for n in range(1, N+1, 2):
        a_n = (4 * np.sin(n * np.pi / 2) / (n * np.pi))
        g_approx += a_n * np.cos(n * w0 * t)
        PN = a_n**2/2
    
    return g_approx, PN

def calcular_mse(g_ideal, g_approx):
    mse = np.mean((g_approx-g_ideal) ** 2)
    
    return mse

def plot(t, g1, g2):
    plt.figure(figsize=(8, 4))
    plt.plot(t, g1, label='g(t) ideal', color='blue', linewidth=2)
    plt.plot(t, g2, label='g(t) aproximado', color='red', linewidth=2)
    plt.title(f'Sinal Quadrado Ideal x Sinal Quadrado Aproximado por Fourier (N = {N})')
    plt.xlabel('Tempo (t)')
    plt.ylabel('Amplitude')
    plt.ylim(-1.5, 1.5)
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    w0 = calcular_frequencia_fundamental(T0)
    g_ideal = gerar_sinal_ideal(t)
    g_approx, PN = aproximar_fourier(t, w0, N)
    mse = calcular_mse(g_ideal, g_approx)
    t_vetor = np.linspace(0, 2, 2001)

    print("================ RESULTADOS EM CONSOLE ================")
    print(f"w0 calculado: {w0:.6f} rad/s")
    print(f"Potência acumulada (Parseval PN): {PN:.6f} W")
    print(f"Erro Quadrático Médio (MSE): {mse:.6f}")
    print("=======================================================")

    plot(t, g_ideal, g_approx)
