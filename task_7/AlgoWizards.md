### Вариант 2:

```mermaid
graph LR

A((A)) --> C((C))
A --> A
B((B)) --> A
B --> C
B --> B
C --> C
C --> A
```
Допустимые маршруты:
- A --> C
- A --> A
- B --> A
- B --> C
- B --> B
- C --> C
- C --> A

Найти формулу расчета количества маршрутов, начинающихся в вершине B и заканчивающихся в вершине A. 

#### I. Составим систему уравнений и выведем рекуррентную формулу вершины A через вершину B

$$\begin{cases}
a_{n} = a_{n-1} + b_{n-1} + c_{n-1} \\ 
b_{n} = b_{n-1} \\
c_{n} = b_{n-1} + c_{n-1} + a_{n-1}  
\end{cases} $$

$a_{n} - c_{n} = a_{n-1} + b_{n-1} + c_{n-1} - (b_{n-1} + c_{n-1} + a_{n-1}) $

$a_{n} = c_{n}  $

$a_{n-1} = c_{n-1}  $

$$\begin{cases}
a_{n} = a_{n-1} + b_{n-1} + a_{n-1}  \\ 
b_{n} = b_{n-1} \\
b_{n-1} = a_{n} - a_{n-1} + a_{n-1}
\end{cases} $$

$b_{n-1} = a_{n} $

$a_{n-1} = b_{n-2} $

$a_{n} = 2 * a_{n-1} + b_{n-1}$

##### Искомая рекуррентная формула вершины B:
$a_{n} = 2 * b_{n-2} + b_{n-1}$

#### II. Составим и решим характеристическое уравнение на основе рекуррентной формулы

$2 * \lambda^2 + \lambda - 1 = 0$

Корни уравнения: $\lambda_{1} = -1 \\ \lambda_{2} = \frac{1}{2}$

##### Составим уравнение с получившимися корнями характеристического уравнения для вычисления коэффициентов
$a_{n} = k_{1} * \lambda_{1}^n +  k_{2} * \lambda_{2}^n$ => $a_{n} = k_{1} * -1^n +  k_{2} * (\frac{1}{2})^n$ 

Из вершины B в вершину A есть один маршрут за 1 ход => $a_{1} = 1$

Из вершины A в вершину A есть три маршрута за 2 хода => $a_{2} = 3$

##### Подставляем все параметры в систему и вычисляем коэффициенты $k_{1}$, $k_{2}$
при n=1:
при n=2:

$$\begin{cases}
1 = -k_{1} + \frac{1}{2} * k_{2} \\ 
3 = -k_{1} + \frac{1}{8} * k_{2} 
\end{cases} $$

$2 = -\frac{3}{8} * k_{2} $

$k_{2} = \frac{16}{3} $

$1 = -k_{1} - \frac{16}{6}$ => $k_{1} = -\frac{22}{6} = -\frac{11}{3} $

#### Ответ: $a_{n} = -\frac{11}{3} * -1^n + \frac{16}{3} * (\frac{1}{2})^n$ 