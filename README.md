---
Title : Macrodotpy
author : Luiz Alexandre Moreira Barros
---

# Interação de Ponto Fixo 

Suponha que nos precisamos encontrar o vetor $x$ que resolve o ponto fixo:
* $x = \alpha + \beta \Pi x$ 
onde $x$ é um vetor $k × 1$, $\alpha$ é um vetor $k × 1$, $\beta \in (0, 1)$ é um escalar e $\Pi$ é uma Matriz de transição de Markov $k × k$ com elemento típico $\Pi _{i, j}^{i} = Pr (x'= x_j ∣x_i)$. O matriz $\Pi$ descreve a probabilidade de que o próximo período do estado será j quando for Eu hoje. As linhas de $\Pi$ somam um.

Suponha que 
* $k = 2$ 
* $\alpha_1 = 1$
*  $\alpha_2 =2$ 
* $\Pi_{1,1} = 0.9$
* $\Pi_{2.2} = 0.1$
* $\Pi = \left[\begin{array}{c|c}  0.9 & 0.1 \\ 0.9 & 0.1 \end{array} \right]$
---
## Modelo Computacional
Será desenvolvido codigo para encontrar o ponto fixo em x iterando em equação

Inicialmente vamos adicionar os pre-requisitos do códigos :

~~~Python 
import numpy

alpha = [2,1]
beta =0.9
p1 = 0.9 
p2 = 0.1 
P = ([[p1,1-p1],[1-p2,p2]])
~~~

Adicionando as condições iniciais do problema para $x_{t}$ e $x_{t-1}$ como: 
~~~ Python 
xt = [0,0] 
xt_minus_one = [0,0]
~~~

Na análise numérica, a iteração de ponto fixo é um método de computação pontos de funções iteradas. Como o nome sugere, um processo é repetido até que uma resposta seja encontrada. Para isso iremos criar a seguinte interação 

~~~Python 
for i in range(1,10000):  
	print(i)  
    xk = alpha+beta*P*xk_minus_one  
    print(xk)  
    if np.linalg.norm(xk - xk_minus_one) < 1e-50:  
        break  
	xk_minus_one = xk
~~~

