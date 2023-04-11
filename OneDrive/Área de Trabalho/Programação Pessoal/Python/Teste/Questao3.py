# a) 1, 3, 5, 7, ___
def sequencia_a():
    sequencia_a = [1, 3, 5, 7]
    proximo_elemento = sequencia_a[-1] + 2
    return proximo_elemento

# b) 2, 4, 8, 16, 32, 64, ____
def sequencia_b():
    sequencia_b = [2, 4, 8, 16, 32, 64]
    proximo_elemento = sequencia_b[-1] * 2
    return proximo_elemento

# c) 0, 1, 4, 9, 16, 25, 36, ____
def sequencia_c():
    sequencia_c = [0, 1, 4, 9, 16, 25, 36]
    proximo_elemento = (len(sequencia_c) ** 2)
    return proximo_elemento

# d) 4, 16, 36, 64, ____
def sequencia_d():
    sequencia_d = [4, 16, 36, 64]
    proximo_elemento = (len(sequencia_d) * 2 + 2) ** 2
    return proximo_elemento

# e) 1, 1, 2, 3, 5, 8, ____
def sequencia_e():
    sequencia_e = [1, 1, 2, 3, 5, 8]
    proximo_elemento = sequencia_e[-1] + sequencia_e[-2]
    return proximo_elemento

# f) 2,10, 12, 16, 17, 18, 19, ____
def sequencia_f():
    sequencia_f = [2, 10, 12, 16, 17, 18, 19]
    proximo_elemento = sequencia_f[-1] + 1
    return proximo_elemento

# Chamada das funções e exibição dos resultados
print("Próximo elemento da sequência a):", sequencia_a())
print("Próximo elemento da sequência b):", sequencia_b())
print("Próximo elemento da sequência c):", sequencia_c())
print("Próximo elemento da sequência d):", sequencia_d())
print("Próximo elemento da sequência e):", sequencia_e())
print("Próximo elemento da sequência f):", sequencia_f())
