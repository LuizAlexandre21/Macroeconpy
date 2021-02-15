import numpy as np

alpha = [2,1] # Estado de Contigencia das utilidades
beta=0.9 # Fator de disconto
p1=0.9  # Probabilidade do estado 1
p2=0.1  # Probabilidade do estado 2

P=np.matrix([[p1,1-p1],[1-p2,p2]]) # Matriz de Transição
xt_minus_one = np.matrix([[0],[0]]) # Estado inicial do x_{t-1}
xt = np.matrix([[0],[0]]) # Estado inicial de x_{t}

for i in range(1,10000): # Numero de interações
    xk = alpha+beta*P*xk_minus_one # Algoritmos da interação do ponto fixo
    if np.linalg.norm(xk - xk_minus_one) < 1e-50: # Checando a convergência -> 1e-5
        break
    xk_minus_one = xk # Preparando a proxima interação


