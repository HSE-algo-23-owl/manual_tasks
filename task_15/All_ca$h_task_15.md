# Задание №15
# Задача о максимальном потоке минимальной стоимости.
## Постановка задачи
1. Дана сеть (взвешенный ориентированный граф) с источником s и стоком t.
2. Для каждой дуги определена пропускная способность и стоимость транспортировки.
3. Необходимо найти для указанной сети максимальный поток минимальной стоимости. 

### Вариант 3: 

| Дуги                      | sa | sb | ac | ba | bc | bd | cd | dt |
|:--------------------------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Пропускная способность    | 3  | 10 | 4  | 1  | 3  | 10 | 8  | 12 |
| Стоимость транспортировки | 1  | 1  | 1  | 2  | 3  | 5  | 1  | 1  |

### 1. Построим сеть с источником **s**, стоком **t** и указанными пропускными способностями дуг для поиска максимального потока.

```mermaid
graph LR
    s-->|3|a
    s-->|10|b
    a-->|4|c
    b-->|1|a
    b-->|3|c
    b-->|10|d
    c-->|8|d
    d-->|12|t
```
Построим остаточную сеть
```mermaid
graph LR
    a-.->|3|s
    b-.->|10|s
    c-.->|4|a
    a-.->|1|b
    c-.->|3|b
    d-.->|10|b
    d-.->|8|c
    t-.->|12|d
```
Возьмем увеличивающий путь t->d->b->s. Минимальный вес по пути составляет 10. Вычтем его из пути и составим остаточную сеть
```mermaid
graph LR
    a-.->|3|s
    s-->|10|b
    c-.->|4|a
    a-.->|1|b
    c-.->|3|b
    b-->|10|d
    d-.->|8|c
    t-.->|2|d
    d-->|10|t
```
Возьмем увеличивающий путь t->d->c->a->s. Минимальный вес составляет по пути 2. Вычтем его из пути и составим остаточную сеть
```mermaid
graph LR
    a-.->|1|s
    s-->|2|a
    s-->|10|b
    a-->|2|c
    c-.->|2|a
    a-.->|1|b
    c-.->|3|b
    b-->|10|d
    d-.->|6|c
    c-->|2|d
    d-->|12|t
```
### 2. Продолжим поиск увеличивающего пути в остаточной сети

В остаточной сети не найдено увеличивающих путей, следовательно, алгоритм завершил работу и найденный поток величиной 10 является максимальным для данной сети.

```mermaid
graph LR
    s-->|2,3|a
    s-->|10,10|b
    a-->|2,4|c
    b-->|0,1|a
    b-->|0,3|c
    b-->|10,10|d
    c-->|2,8|d
    d-->|12,12|t
```

### 3. Рассчитаем стоимость полученного максимального потока.

| Дуги                                          | sa | sb | ac | ba | bc | bd | cd | dt | Итого  |
|:----------------------------------------------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:------:|
| Пропускная способность p(e)                   | 3  | 10 | 4  | 1  | 3  | 10 | 8  | 12 |        |
| Локальный поток f(e)                          | 2  | 10 | 2  | 0  | 0  | 10 | 2  | 12 |        |
| Стоимость транспортировки единицы потока c(e) | 1  | 1  | 1  | 2  | 3  | 5  | 1  | 1  |        |
| Суммарная стоимость f(e)*c(e)                 | 2  | 10 | 2  | 0  | 0  | 50 | 2  | 12 | **78** |

### 4. Попробуем уменьшить стоимость потока для чего построим остаточную сеть.
Для каждого ребра остаточной сети укажем стоимость транспортировки единицы потока.

```mermaid
graph LR
    a-.->|+1|s
    s-->|-1|a
    s-->|-1|b
    a-->|-1|c
    c-.->|+1|a
    a-.->|+2|b
    c-.->|+3|b
    b-->|-5|d
    d-.->|+1|c
    c-->|-1|d
    d-->|-1|t
```
В остаточной сети найден ориентированный цикл отрицательной стоимости s -> b -> d -> c -> a -> s (-1 -5 +1 +1 +1 = -3). 

Найдем минимальный вес ребра в указанном цикле, изображенном **в остаточной сети с указанием величины потока**.
Минимальный вес ребра в цикле 1 - это неиспользованный резерв ребра s -> a.

Удалим найденный цикл - уменьшим на 1 вес всех ребер, входящих в цикл.

```mermaid
graph LR
    s-->|3|a
    s-->|9|b
    b-.->|1|s
    a-->|3|c
    c-.->|1|a
    a-.->|1|b
    c-.->|3|b
    b-->|9|d
    d-.->|1|b
    d-.->|5|c
    c-->|3|d
    d-->|12|t
```
### 5. Проведем повторный поиск цикла отрицательной стоимости в остаточной сети.
Скорректируем остаточную сеть с указанием стоимости транспортировки единицы потока.
```mermaid
graph LR
    s-->|-1|a
    s-->|-1|b
    b-.->|+1|s
    a-->|-1|c
    c-.->|+1|a
    a-.->|+2|b
    c-.->|+3|b
    b-->|-5|d
    d-.->|+5|b
    d-.->|+1|c
    c-->|-1|d
    d-->|-1|t
```

В остаточной сети найден ориентированный цикл отрицательной стоимости b -> d -> c -> b (-5 +1 +3 = -1). 

Найдем минимальный вес ребра в указанном цикле, изображенном **в остаточной сети с указанием величины потока**.  
Минимальный вес ребра в цикле 3 - это неиспользованный резерв ребра b -> c.

Удалим найденный цикл - уменьшим на 3 вес всех ребер, входящих в цикл.
```mermaid
graph LR
    s-->|3|a
    s-->|9|b
    b-.->|1|s
    a-->|3|c
    c-.->|1|a
    a-.->|1|b
    b-->|3|c
    b-->|6|d
    d-.->|4|b
    d-.->|2|c
    c-->|6|d
    d-->|12|t
```
### 6. Проведем повторный поиск цикла отрицательной стоимости в остаточной сети.
Скорректируем остаточную сеть с указанием стоимости транспортировки единицы потока.
```mermaid
graph LR
    s-->|-1|a
    s-->|-1|b
    b-.->|+1|s
    a-->|-1|c
    c-.->|+1|a
    a-.->|+2|b
    b-->|-3|c
    b-->|-5|d
    d-.->|+5|b
    d-.->|+1|c
    c-->|-1|d
    d-->|-1|t
```
В остаточной сети найден ориентированный цикл отрицательной стоимости d -> c -> a -> b -> d (+1 +1 + 2 - 5 = -1). 

Найдем минимальный вес ребра в указанном цикле, изображенном **в остаточной сети с указанием величины потока**.  
Минимальный вес ребра в цикле 1 - это неиспользованный резерв ребра b -> a.

Удалим найденный цикл - уменьшим на 1 вес всех ребер, входящих в цикл.
```mermaid
graph LR
    s-->|3|a
    s-->|9|b
    b-.->|1|s
    a-->|4|c
    b -->|1|a
    b-->|3|c
    b-->|5|d
    d-.->|5|b
    d-.->|1|c
    c-->|7|d
    d-->|12|t
```
В остаточной сети отсутствуют циклы отрицательной стоимости, следовательно, стоимость потока минимальна.
```mermaid
graph LR
    s-->|3,3|a
    s-->|9,10|b
    a-->|4,4|c
    b-->|1,1|a
    b-->|3,3|c
    b-->|5,10|d
    c-->|7,8|d
    d-->|12,12|t
```

| Дуги                                          | sa | sb | ac | ba | bc | bd | cd | dt | Итого  |
|:----------------------------------------------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:------:|
| Пропускная способность p(e)                   | 3  | 10 | 4  | 1  | 3  | 10 | 8  | 12 |        |
| Локальный поток f(e)                          | 3  | 9  | 4  | 1  | 3  | 5  | 7  | 12 |        |
| Стоимость транспортировки единицы потока c(e) | 1  | 1  | 1  | 2  | 3  | 5  | 1  | 1  |        |
| Суммарная стоимость f(e)*c(e)                 | 1  | 9  | 4  | 2  | 9  | 25 | 7  | 12 | **71** |

### Ответ:
Максимальный поток в сети равен   12, минимальная стоимость потока 71, она реализуется следующим локальными потоками:
```mermaid
graph LR
    s-->|3,3|a
    s-->|9,10|b
    a-->|4,4|c
    b-->|1,1|a
    b-->|3,3|c
    b-->|5,10|d
    c-->|7,8|d
    d-->|12,12|t
```