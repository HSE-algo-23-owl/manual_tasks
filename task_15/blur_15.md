### Вариант 1:

| Дуги                      | sa | sb | sc | ac | ad | ab | bd | ct | dt |
|:--------------------------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Пропускная способность    | 10 | 10 | 5  | 7  | 8  | 5  | 8  | 10 | 10 |
| Стоимость транспортировки | 1  | 1  | 1  | 2  | 3  | 1  | 1  | 2  | 1  |
### 1. Построим сеть с источником S, стоком t и указанными пропускными способностями дуг. Найдём максимальный поток.
```mermaid
graph LR
    s-->|10|a
    s-->|10|b
    s-->|5|c
    a-->|7|c
    a-->|8|d
    a-->|5|b
    b-->|8|d
    c-->|10|t
    d-->|10|t
```
Построим остаточную сеть, так как изначальный поток равен нулю все дуги являются пустыми, соответственно в остаточную сеть необходимо внести обратные дуги с весом, который равен пропускной способности изначальной сети
```mermaid
graph RL
    a-.->|10|s
    b-.->|10|s
    c-.->|5|s
    c-.->|7|a
    d-.->|8|a
    b-.->|5|a
    d-.->|8|b
    t-.->|10|c
    t-.->|10|d
```    
### 2. Найдём увеличивающий путь в остаточной сети.
Возьмём увеличивающий путь t -> d -> b -> a -> s. Минимальная длина дуг на этом пути равна 5. Уменьшим вес дуг на полученном пути. Дуги, который стали нулевыми из остаточной сети удаляем.
```mermaid
graph RL
    a-.->|5|s
    b-.->|10|s
    c-.->|5|s
    c-.->|7|a
    d-.->|8|a
    d-.->|3|b
    t-.->|10|c
    t-.->|5|d
```    
Скорректируем локальные потоки в исходной сети, первое число - локальный поток, второе - пропускная способность.
```mermaid
graph LR
    s-->|5, 10|a
    s-->|0,10|b
    s-->|0,5|c
    a-->|0,7|c
    a-->|0,8|d
    a-->|5,5|b
    b-->|5, 8|d
    c-->|0, 10|t
    d-->|5, 10|t
```
### 3. Продолжим поиск увеличивающего пути в остаточной сети.

Возьмём увеличивающий путь t -> c -> a -> s. Минимальная длина дуг на этом пути равна 5. Уменьшим вес дуг на полученном пути. Дуги, который стали нулевыми из остаточной сети удаляем.
```mermaid
graph RL
    b-.->|10|s
    c-.->|5|s
    c-.->|2|a
    d-.->|8|a
    d-.->|3|b
    t-.->|5|c
    t-.->|5|d
```    
Скорректируем локальные потоки в исходной сети, первое число - локальный поток, второе - пропускная способность.
```mermaid
graph LR
    s-->|10, 10|a
    s-->|0,10|b
    s-->|0, 5|c
    a-->|5, 7|c
    a-->|0,8|d
    a-->|5,5|b
    b-->|5, 8|d
    c-->|5, 10|t
    d-->|5, 10|t
```
### 4. Продолжим поиск увеличивающего пути в остаточной сети.

Возьмём увеличивающий путь t -> c -> s. Минимальная длина дуг на этом пути равна 5. Уменьшим вес дуг на полученном пути. Дуги, который стали нулевыми из остаточной сети удаляем.
```mermaid
graph RL
    b-.->|10|s
    c-.->|2|a
    d-.->|8|a
    d-.->|3|b
    t-.->|5|d
```    
Скорректируем локальные потоки в исходной сети, первое число - локальный поток, второе - пропускная способность.
```mermaid
graph LR
    s-->|10, 10|a
    s-->|0, 10|b
    s-->|5, 5|c
    a-->|5, 7|c
    a-->|0, 8|d
    a-->|5,5|b
    b-->|5, 8|d
    c-->|10, 10|t
    d-->|5, 10|t
```
### 5. Продолжим поиск увеличивающего пути в остаточной сети.

Возьмём увеличивающий путь t -> d -> b -> s. Минимальная длина дуг на этом пути равна 3. Уменьшим вес дуг на полученном пути. Дуги, который стали нулевыми из остаточной сети удаляем.
```mermaid
graph RL
    b-.->|7|s
    c-.->|2|a
    d-.->|8|a
    t-.->|2|d
```    
Скорректируем локальные потоки в исходной сети, первое число - локальный поток, второе - пропускная способность.
```mermaid
graph LR
    s-->|10, 10|a
    s-->|3, 10|b
    s-->|5, 5|c
    a-->|5, 7|c
    a-->|0,8|d
    a-->|5,5|b
    b-->|8, 8|d
    c-->|10, 10|t
    d-->|8, 10|t
```
### 6. Продолжим поиск увеличивающего пути в остаточной сети.
В остаточной сети не найдено увеличивающих путей, следовательно алгоритм завершает работу, найденный поток величиной 18 является максимальным

### 7. Рассчитаем стоимость полученного максимального потока.

| Дуги                                          | sa | sb | sc | ac | ad | ab | bd | ct | dt | Итого  |
|:----------------------------------------------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:------:|
| Пропускная способность p(e)                   | 10 | 10 | 5  | 7  | 8  | 5  | 8  | 10 | 10 |        |
| Локальный поток f(e)                          | 10 | 3  | 5  | 5  | 0  | 5  | 8  | 10 | 8  |        |
| Стоимость транспортировки единицы потока c(e) | 1  | 1  | 1  | 2  | 3  | 1  | 1  | 2  | 1  |        |
| Суммарная стоимость f(e)*c(e)                 | 10 | 3  | 5  | 10 | 0  | 5  | 8  | 20 | 8  | **69** |

### 8. Попробуем уменьшить стоимость потока. Для этого используем остаточную сеть.

Указываем стоимость транспортировки одной единицы потока для каждого ребра остаточной сети.

```mermaid
graph LR
    s-->|-1|a
    s-->|-1|b
    b-.->|1|s
    s-->|-1|c
    a-->|-2|c
    c-.->|2|a
    a-->|-3|d
    d-.->|3|a
    a-->|-1|b
    b-->|-1|d
    c-->|-2|t
    d-->|-1|t
    t-.->|1|d
```
В остаточной сети найдём ориентированный цикл отрицательной стоимости. Таким циклом будет b -> s -> a ->b (-1 + 1 - 1 = -1).
Найдём минимальный вес ребра в данном цикле, изображённом в остаточной сети с указанием величины потока.

```mermaid
graph LR
    s-->|10|a
    s-->|3|b
    b-.->|7|s
    s-->|5|c
    a-->|5|c
    c-.->|2|a
    a-->|0|d
    d-.->|8|a
    a-->|5|b
    b-->|8|d
    c-->|10|t
    d-->|8|t
    t-.->|2|d
```

Минимальный вес ребра в цикле равен 5 - это неиспользованный резерв ребра a -> b.
Удалим найденный цикл - уменьшим на 5 вес всех рёбер, входящих в цикл.

```mermaid
graph LR
    s-->|5|a
    s-->|3|b
    b-.->|2|s
    s-->|5|c
    a-->|5|c
    c-.->|2|a
    a-->|0|d
    d-.->|8|a
    b-->|8|d
    c-->|10|t
    d-->|8|t
    t-.->|2|d
```
Отобразим полученную остаточную сеть с указанием стоимости перевозки единицы потока.
```mermaid
graph LR
    s-->|-1|a
    s-->|-1|b
    b-.->|1|s
    s-->|-1|c
    a-->|-2|c
    c-.->|2|a
    a-->|-3|d
    d-.->|3|a
    b-->|-1|d
    c-->|-2|t
    d-->|-1|t
    t-.->|1|d
```
### 9. Проведём повторный поиск цикла отрицательной стоимости в остаточной сети.

В остаточной сети отсутствуют циклы отрицательной стоимости, следовательно стоимость потока минимальна.

```mermaid
graph LR
    s-->|-1|a
    s-->|-1|b
    b-.->|1|s
    s-->|-1|c
    a-->|-2|c
    c-.->|2|a
    a-->|-3|d
    d-.->|3|a
    b-->|-1|d
    c-->|-2|t
    d-->|-1|t
    t-.->|1|d
```

### 10. Расчитаем стоимость полученного потока


| Дуги                                          | sa | sb | sc | ac | ad | ab | bd | ct | dt | Итого  |
|:----------------------------------------------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:------:|
| Пропускная способность p(e)                   | 10 | 10 | 5  | 7  | 8  | 5  | 8  | 10 | 10 |        |
| Локальный поток f(e)                          | 10 | 3  | 5  | 5  | 0  | 5  | 8  | 10 | 8  |        |
| Стоимость транспортировки единицы потока c(e) | 1  | 1  | 1  | 2  | 3  | 1  | 1  | 2  | 1  |        |
| Суммарная стоимость f(e)*c(e)                 | 10 | 3  | 5  | 10 | 0  | 5  | 8  | 20 | 8  | **69** |

#### Ответ:
Максимальный поток в сети равен 18, минимальная стоимость потока 69, она реализуется следующими локальными потоками:

```mermaid
graph LR
    s-->|5, 10|a
    s-->|8, 10|b
    s-->|5, 5|c
    a-->|5, 7|c
    a-->|8, 8|d
    a-->|0,5|b
    b-->|8, 8|d
    c-->|10, 10|t
    d-->|8, 10|t
```