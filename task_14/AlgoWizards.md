### Вариант 5: 

|          Дуги          | sa | sb | sc | ba | bc | cd | dt | ac | at |
|:----------------------:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Пропускная способность | 6  | 4  | 6  | 5  | 5  | 10 | 8  | 5  | 8  |

## 1. Построим сеть с источником s и стоком t на основе информации из таблицы:

```mermaid
graph LR
    s-->|6|a
    s-->|4|b
    s-->|6|c
    b-->|5|a
    b-->|5|c
    c-->|10|d
    d-->|8|t
    a-->|5|c
    a-->|8|t
```
Т.к. локальный поток равен нулю, строим остаточную сеть, состоящую из обратных дуг

### 1.1 Остаточная сеть:

```mermaid
graph LR
    a-.->|6|s
    b-.->|4|s
    c-.->|6|s
    a-.->|5|b
    c-.->|5|b
    d-.->|10|c
    t-.->|8|d
    c-.->|5|a
    t-.->|8|a
```

## 2. Найдем увеличивающий путь (из стока в источник) в остаточной сети:
Путь найден: t -> a -> s. Минимальный вес дуги: min(8,6) = 6

### 2.1 Уменьшим вес дуг:

```mermaid
graph LR
    s--->|6|a
    b-.->|4|s
    c-.->|6|s
    a-.->|5|b
    c-.->|5|b
    d-.->|10|c
    t-.->|8|d
    c-.->|5|a
    a--->|6|t
    t-.->|2|a
```

### 2.2 Скорректируем локальные потоки в исходной сети: 
Первое число - локальный поток, второе - пропускная способность

```mermaid
graph LR
    s-->|"(6, 6)"|a
    s-->|"(0, 4)"|b
    s-->|"(0, 6)"|c
    b-->|"(0, 5)"|a
    b-->|"(0, 5)"|c
    c-->|"(0, 10)"|d
    d-->|"(0, 8)"|t
    a-->|"(0, 5)"|c
    a-->|"(6, 8)"|t
```

## 3. Найдем увеличивающий путь в остаточной сети:
```mermaid
graph LR
    s--->|6|a
    b-.->|4|s
    c-.->|6|s
    a-.->|5|b
    c-.->|5|b
    d-.->|10|c
    t-.->|8|d
    c-.->|5|a
    a--->|6|t
    t-.->|2|a
```
Путь найден: t -> d -> c -> s. Минимальный вес дуги: min(8,10,6) = 6

### 3.1 Уменьшим вес дуг:

```mermaid
graph LR
    s--->|6|a
    b-.->|4|s
    s--->|6|c
    a-.->|5|b
    c-.->|5|b
    c--->|6|d
    d-.->|4|c
    d--->|6|t
    t-.->|2|d
    c-.->|5|a
    a--->|6|t
    t-.->|2|a
```

### 3.2 Скорректируем локальные потоки в исходной сети: 

```mermaid
graph LR
    s-->|"(6, 6)"|a
    s-->|"(0, 4)"|b
    s-->|"(6, 6)"|c
    b-->|"(0, 5)"|a
    b-->|"(0, 5)"|c
    c-->|"(6, 10)"|d
    d-->|"(6, 8)"|t
    a-->|"(0, 5)"|c
    a-->|"(6, 8)"|t
```

## 4. Найдем увеличивающий путь:

```mermaid
graph LR
    s--->|6|a
    b-.->|4|s
    s--->|6|c
    a-.->|5|b
    c-.->|5|b
    c--->|6|d
    d-.->|4|c
    d--->|6|t
    t-.->|2|d
    c-.->|5|a
    a--->|6|t
    t-.->|2|a
```
Путь найден: t -> d -> c -> b -> s. Минимальный вес дуги: min(2,4,5,4) = 2

### 4.1 Уменьшим вес дуг:

```mermaid
graph LR
    s--->|6|a

    s--->|2|b
    b-.->|2|s

    s--->|6|c

    a-.->|5|b

    b--->|2|c
    c-.->|3|b

    c--->|8|d
    d-.->|2|c

    d--->|8|t

    c-.->|5|a

    a--->|6|t
    t-.->|2|a
```

### 4.2 Скорректируем локальные потоки в исходной сети: 

```mermaid
graph LR
    s-->|"(6, 6)"|a
    s-->|"(2, 4)"|b
    s-->|"(6, 6)"|c
    b-->|"(0, 5)"|a
    b-->|"(2, 5)"|c
    c-->|"(8, 10)"|d
    d-->|"(8, 8)"|t
    a-->|"(0, 5)"|c
    a-->|"(6, 8)"|t
```

## 5. Найдем увеличивающий путь:

```mermaid
graph LR
    s--->|6|a
    s--->|2|b
    b-.->|2|s
    s--->|6|c
    a-.->|5|b
    b--->|2|c
    c-.->|3|b
    c--->|8|d
    d-.->|2|c
    d--->|8|t
    c-.->|5|a
    a--->|6|t
    t-.->|2|a
```
Путь найден: t -> a -> b -> s. Минимальный вес дуги: min(2,5,2) = 2

### 5.1 Уменьшим вес дуг:

```mermaid
graph LR
    s--->|6|a

    s--->|4|b 

    s--->|6|c

    b--->|2|a
    a-.->|3|b

    b--->|2|c
    c-.->|3|b

    c--->|8|d
    d-.->|2|c

    d--->|8|t

    c-.->|5|a

    a--->|8|t
```

### 5.2 Скорректируем локальные потоки в исходной сети: 

```mermaid
graph LR
    s-->|"(6, 6)"|a
    s-->|"(4, 4)"|b
    s-->|"(6, 6)"|c
    b-->|"(2, 5)"|a
    b-->|"(2, 5)"|c
    c-->|"(8, 10)"|d
    d-->|"(8, 8)"|t
    a-->|"(0, 5)"|c
    a-->|"(8, 8)"|t
```
В остаточной цепи отсутствуют увеличивающие пути, значит алгоритм завершает работу. Величина максимального потока: 16.

### 6. Проведем проверка методом перебором всех разрезов сети:
Построим разрез сети, то есть разобъем множества на подмножества V<sub>1</sub> и V<sub>2</sub>. 
Источник входит во множество V<sub>1</sub>
Сток входит во множество V<sub>2</sub>

По формуле для сети из _n_ вершин существует 2<sup>n - 2</sup> разрезов.

Для данной сети из 6 вершин существует 2<sup>6 - 2</sup> = 2<sup>4</sup> = 16 вариантов 

| №  | V<sub>1</sub>                   | V<sub>2</sub> | Пропускная способность разреза |
|----|:--------------------------------|:--------------|:------------------------------:|
| 1  | s                               | a, b, c, d, t |         6 + 6 + 4 = 16         |
|    | **s + {a, b, c, d} x1**         |               |                                |
| 2  | s, a                            | b, c, d, t    |         4 + 6 + 5 + 8 = 23     |
| 3  | s, b                            | a, c, d, t    |         6 + 5 + 6 + 5 = 22     |
| 4  | s, c                            | a, b, d, t    |         4 + 6 + 10 = 20        |
| 5  | s, d                            | a, b, c, t    |         4 + 6 + 6 + 8 = 24     |
|    | **s + {a, b, c, d} x2**         |               |                                |
| 6  | s, a, b                         | c, d, t       |         6 + 5 + 5 + 8 = 24     |
| 7  | s, a, c                         | b, d, t       |         4 + 8 + 10 = 22        |
| 8  | s, a, d                         | b, c, t       |         4 + 5 + 6 + 8 + 8 = 31 |
| 9  | s, b, c                         | a, d, t       |         6 + 5 + 10 = 21        |
| 10 | s, b, d                         | a, c, t       |         6 + 5 + 6 + 5 + 8 = 30 |
| 11 | s, c, d                         | a, b, t       |         4 + 6 + 8 = 18         |
|    | **s + {a, b, c, d} x3**         |               |                                |
| 12 | s, a, b, c                      | d, t          |         10 + 8 = 18            |
| 13 | s, a, c, d                      | b, t          |         4 + 8 + 8 = 20         |
| 14 | s, b, c, d                      | a, t          |         6 + 5 + 8 = 19         |
| 15 | s, a, b, d                      | c, t          |         5 + 5 + 6 + 8 + 8 = 32 |
|    | **s + {a, b, c, d} x4**         |               |                                |
| 16 | s, a, b, c, d                   | t             |         8 + 8 = 16             |


Минимальная пропускная способность, исходя из таблицы, равна 16. Это соответствует величине максимального потока.


### Ответ: максимальный поток равен 16, сеть с конфигурациями представлена ниже

```mermaid
graph LR
    s-->|"(6, 6)"|a
    s-->|"(4, 4)"|b
    s-->|"(6, 6)"|c
    b-->|"(2, 5)"|a
    b-->|"(2, 5)"|c
    c-->|"(8, 10)"|d
    d-->|"(8, 8)"|t
    a-->|"(0, 5)"|c
    a-->|"(8, 8)"|t
```
