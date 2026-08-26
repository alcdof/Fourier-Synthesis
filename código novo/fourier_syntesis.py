# fourier_synthesis.py
import numpy as np
import matplotlib.pyplot as plt

# Parâmetros estruturais (Não alterar)
T0 = 2.0
t = np.arange(0, 2.001, 0.001)
N = 19

def calcular_frequencia_fundamental(T0):
    """
    Retorna a frequência fundamental w0 em rad/s.
    """
    # TODO: Calcule e retorne w0 = 2 * pi / T0
    w0 = 2 * np.pi / T0
    return w0

def gerar_sinal_ideal(t):
    """
    Gera o sinal quadrado ideal g(t) baseado no vetor de tempo t.
    Deve ser 1.0 nos intervalos [0.0, 0.5[ e [1.5, 2.0], e -1.0 no intervalo [0.5, 1.5[.
    """
    # TODO: Implemente os intervalos do sinal ideal quadrado
    condicao = ((t >= 0.0) & (t < 0.5) | (t >= 1.5) & (t <= 2.0))
        
    return np.where(condicao, 1.0, -1.0)

def aproximar_fourier(t, w0, N):
    """
    Retorna o vetor de aproximação g_approx com N harmônicos
    e a potência acumulada PN usando o Teorema de Parseval.
    O loop deve varrer apenas os harmônicos ímpares de 1 até N.
    """
    # TODO: Inicialize os vetores e acumule as componentes cossenoidais
    # e a potência média PN pelo Teorema de Parseval.
    g_approx = None
    PN = None
    return g_approx, PN

def calcular_mse(g_ideal, g_approx):
    """
    Retorna o Erro Quadrático Médio (MSE) entre g_ideal e g_approx.
    """
    # TODO: Calcule o Erro Quadrático Médio discreto
    mse = None
    return mse

def plot_g_ideal(t):
    g = gerar_sinal_ideal(t)

    plt.figure(figsize=(8, 4))
    plt.plot(t, g, label='g(t) ideal', color='blue', linewidth=2)
    plt.title('Sinal Quadrado Ideal')
    plt.xlabel('Tempo (t)')
    plt.ylabel('Amplitude')
    plt.ylim(-1.5, 1.5)
    plt.grid(True)
    plt.legend()
    plt.show()

# Se o script for executado diretamente, mostra os resultados no console
if __name__ == "__main__":
    w0 = calcular_frequencia_fundamental(T0)
    g_ideal = gerar_sinal_ideal(t)

    t_vetor = np.linspace(0, 2, 2001)
    plot_g_ideal(t)

    if w0 is not None and g_ideal is not None:
        g_approx, PN = aproximar_fourier(t, w0, N)
        if g_approx is not None and PN is not None:
            mse = calcular_mse(g_ideal, g_approx)
            print("================ RESULTADOS EM CONSOLE ================")
            print(f"w0 calculado: {w0:.6f} rad/s")
            print(f"Potência acumulada (Parseval PN): {PN:.6f} W")
            print(f"Erro Quadrático Médio (MSE): {mse:.6f}")
            print("=======================================================")
        else:
            print("Implemente as funções de aproximação de Fourier.")
    else:
        print("Implemente as funções de frequência fundamental e sinal ideal.")