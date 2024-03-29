### Вариант 7:

|          Дуги          | sa | sc | at | ab | ad | cd | bd | bt | dt |
|:----------------------:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Пропускная способность | 10 | 10 | 3  | 9  | 6  | 12 | 6  | 6  | 12 |
#### 1. Построим сеть с источником S, стоком t и пропускными способностями дуг из таблицы выше
```mermaid
graph LR
    s-->|10|a
    s-->|10|c
    a-->|3|t
    a-->|9|b
    a-->|6|d
    c-->|12|d
    b-->|6|d
    b-->|6|t
    d-->|12|t
```
Построим остаточную сеть, так как изначальный поток равен нулю все дуги являются пустыми, соответственно в остаточную сеть необходимо внести обратные дуги с весом, который равен пропускной способности изначальной сети
```mermaid
graph RL
    a-.->|10|s
    c-.->|10|s
    t-.->|3|a
    b-.->|9|a
    d-.->|6|a
    d-.->|12|c
    d-.->|6|b
    t-.->|6|b
    t-.-|12|d
```
#### 2. Найдём увеличивающий путь в остаточной сети
Возьмём увеличивающий путь t -> b -> a -> S
Минимальная длина дуг на этом пути равна 6
Уменьшим вес дуг на полученном пути. Дуги которые стали нулевыми удаляем из остаточной сети.

```mermaid
graph RL
    a-.->|4|s
    c-.->|10|s
    t-.->|3|a
    b-.->|3|a
    d-.->|6|a
    d-.->|12|c
    d-.->|6|b
    t-.-|12|d
```
Скорректируем локальные потоки в исходной сети, первое число - локальный поток, второе - пропускная способность
```mermaid
graph LR
    s-->|6, 10|a
    s-->|0, 10|c
    a-->|0, 3|t
    a-->|6, 9|b
    a-->|0, 6|d
    c-->|0, 12|d
    b-->|0, 6|d
    b-->|6, 6|t
    d-->|0, 12|t
```
#### 3. Продолжим поиск увеличивающего пути в остаточной сети
Возьмём увеличивающий путь t -> a -> S Минимальная длина дуг на этом пути равна 3 Уменьшим вес дуг на полученном пути. Дуги которые стали нулевыми удаляем из остаточной сети.
```mermaid
graph RL
    a-.->|1|s
    c-.->|10|s
    b-.->|3|a
    d-.->|6|a
    d-.->|12|c
    d-.->|6|b
    t-.-|12|d
```
Скорректируем локальные потоки в исходной сети, первое число - локальный поток, второе - пропускная способность
```mermaid
graph LR
    s-->|9, 10|a
    s-->|0, 10|c
    a-->|3, 3|t
    a-->|6, 9|b
    a-->|0, 6|d
    c-->|0, 12|d
    b-->|0, 6|d
    b-->|6, 6|t
    d-->|0, 12|t
```
#### 4. Продолжим поиск увеличивающего пути в остаточной сети
Возьмём увеличивающий путь t -> d -> a -> S Минимальная длина дуг на этом пути равна 1 Уменьшим вес дуг на полученном пути. Дуги которые стали нулевыми удаляем из остаточной сети.
```mermaid
graph RL
    c-.->|10|s
    b-.->|3|a
    d-.->|5|a
    d-.->|12|c
    d-.->|6|b
    t-.-|11|d
```
Скорректируем локальные потоки в исходной сети, первое число - локальный поток, второе - пропускная способность
```mermaid
graph LR
    s-->|10, 10|a
    s-->|0, 10|c
    a-->|3, 3|t
    a-->|6, 9|b
    a-->|1, 6|d
    c-->|0, 12|d
    b-->|0, 6|d
    b-->|6, 6|t
    d-->|1, 12|t
```
#### 5. Продолжим поиск увеличивающего пути в остаточной сети
Возьмём увеличивающий путь t -> d -> c -> S Минимальная длина дуг на этом пути равна 10 Уменьшим вес дуг на полученном пути. Дуги которые стали нулевыми удаляем из остаточной сети.
```mermaid
graph RL
    b-.->|3|a
    d-.->|5|a
    d-.->|2|c
    d-.->|6|b
    t-.-|1|d
```
Скорректируем локальные потоки в исходной сети, первое число - локальный поток, второе - пропускная способность
```mermaid
graph LR
    s-->|10, 10|a
    s-->|10, 10|c
    a-->|3, 3|t
    a-->|6, 9|b
    a-->|1, 6|d
    c-->|10, 12|d
    b-->|0, 6|d
    b-->|6, 6|t
    d-->|11, 12|t
```
#### 6. Продолжим поиск увеличивающего пути в остаточной сети
Так как в остаточной сети больше нет увеличивающих путей, работу алгоритма можно считать завершённой. Найденный поток имеет величину 20 и является максимальным для данной сети.
#### 7. Проверим значение максимального потока перебором всех срезов сети
| №  | I         |      II      | Пропускная способность разреза |
|----|-----------|:------------:|--------------------------------|
| 1  | S         | t, a, b, c d | 10+10 = 20                     | 
| 2  | S,a       |   t,b,c,d    | 3 + 9 + 6 + 10 = 28            |
| 3  | S,b       |   t,a,c,d    | 10 + 6 + 6 = 22                |
| 4  | S,c       |   t,a,b,d    | 10 + 12 = 22                   |
| 5  | S,d       |   t,a,b,c    | 10 + 10 + 12 = 32              |
| 6  | S,a,b     |    t,c,d     | 3 + 6 + 10 + 6 + 6 = 31        |
| 7  | S,a,c     |    t,b,d     | 9 + 3 + 6 + 12 = 30            |
| 8  | S,a,d     |    t,b,c     | 10 + 3 + 9 + 12 = 34           |
| 9  | S,b,c     |    t,a,d     | 10 + 12 + 6 + 6 = 34           |
| 10 | S,b,d     |    t,a,c     | 10 + 10 + 6 + 12 = 38          |
| 11 | S,c,d     |    t,a,b     | 10 + 12 = 22                   |
| 12 | S,a,b,c   |     t,d      | 3 + 6 + 6 + 12 = 27            |
| 13 | S,a,b,d   |     t,c      | 10 + 3 + 6 + 12 = 31           |
| 14 | S,a,c,d   |     t,b      | 3 + 12 + 9 = 24                |
| 15 | S,b,c,d   |     t,a      | 3 + 6 + 12 + 10 = 31           |
| 16 | S,a,b,c,d |      t       | 3 + 6 + 12 = 21                |
Минимальная пропускная способность разрезов равна 20 (S)/(t,a,b,c,d), что совпадает с найденной величиной максимального потока в сети.
#### Ответ
Максимальный поток в сети равен 20, он реализуется следующими локальными потоками:
```mermaid
graph LR
    s-->|10, 10|a
    s-->|10, 10|c
    a-->|3, 3|t
    a-->|6, 9|b
    a-->|1, 6|d
    c-->|10, 12|d
    b-->|0, 6|d
    b-->|6, 6|t
    d-->|11, 12|t
```

