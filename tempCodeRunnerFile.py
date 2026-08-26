def aproximar_fourier(t, w0, N):
    """
    Retorna o vetor de aproximação g_approx com N harmônicos
    e a potência acumulada PN usando o Teorema de Parseval.
    O loop deve varrer apenas os harmônicos ímpares de 1 até N.
    """
    g_approx = np.zeros_like(t)

    idx_coef = 0

    for n in range(1, N+1, 2):
        a_n = (4 * np.sin(n * np.pi / 2) / (n * np.pi))

        g_approx += a_n * np.cos(n * w0 * t)

    # TODO: Inicialize os vetores e acumule as componentes cossenoidais
    # e a potência média PN pelo Teorema de Parseval.
    
    return g_approx