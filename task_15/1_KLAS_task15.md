﻿# 1.KLA$ Team
# Задание №15
# Задача о максимальном потоке минимальной стоимости.


## Постановка задачи
1. Дана сеть (взвешенный ориентированный граф) с источником s и стоком t.
2. Для каждой дуги определена пропускная способность и стоимость транспортировки.
3. Необходимо найти для указанной сети максимальный поток минимальной стоимости. 

## Решение

Пропускная способность дуг сети и стоимость транспортировки указана в таблице.

### Вариант 7:

| Дуги                      | sa | sc | ab | ad | ac | cd | bd | dt |
|:--------------------------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Пропускная способность    | 10 | 10 | 6  | 6  | 6  | 12 | 6  | 12 |
| Стоимость транспортировки | 1  | 1  | 1  | 3  | 1  | 5  | 1  | 1  |

### 1. Построим сеть с источником **s**, стоком **t** и указанными пропускными способностями дуг для поиска максимального потока.

```mermaid
graph LR
    s-->|10|a
    s-->|10|c
    a-->|6|b
    a-->|6|d
    a-->|6|c
    c-->|12|d
    b-->|6|d
    d-->|12|t
```
Укажем начальный поток величиной 6 **s -> a -> c -> d -> t**. Построим соответствующую остаточную сеть.

```mermaid
graph LR
	s-->|6|a-->|6|c-->|6|d-->|6|t
    t-.->|6|d-.->|6|a-.->|4|s
    d-.->|6|c-.->|10|s
    d-.->|6|b-.->|6|a
	
    
```

### 2. Проведем поиск увеличивающего пути в остаточной сети
В остаточной сети найден увеличивающий путь t -> d -> c -> s. Минимальный вес дуг на этом пути равен 6.

Уменьшим вес дуг на найденном пути, дуги для которых вес стал нулевым удалим из остаточной сети.

```mermaid
graph RL
	d-.->|6|a-.->|4|s
    d-.->|6|b-.->|6|a
    s-->|6|c
	c-.->|4|s
	s-->|6|a-->|6|c-->|12|d-->|12|t
```


### 3. Продолжим поиск увеличивающего пути в остаточной сети

В остаточной сети не найдено увеличивающих путей, следовательно, алгоритм завершил работу и найденный поток величиной 12 является максимальным для данной сети.

```mermaid
graph LR
    s-->|6,10|a
    s-->|6,10|c
    a-->|0,6|b
    a-->|0,6|d
    a-->|6,6|c
    c-->|12,12|d
    b-->|0,6|d
    d-->|12,12|t
```

### 4. Рассчитаем стоимость полученного максимального потока.

| Дуги                                          | sa | sc | ab | ad | ac | cd | bd | dt | Итого |
|:----------------------------------------------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:-----:|
| Пропускная способность p(e)                   | 10 | 10 | 6  | 6  | 6  | 12 | 6  | 12 |       |
| Локальный поток f(e)                          | 6  | 6  | 0  | 0  | 6  | 12 | 0  | 12 |       |
| Стоимость транспортировки единицы потока c(e) | 1  | 1  | 1  | 3  | 1  | 5  | 1  | 1  |       |
| Суммарная стоимость f(e)*c(e)                 | 6  | 6  | 0  | 0  | 6  | 60 | 0  | 12 | **90**|

Стоимость полученного потока составляет 90. 

### 5. Попробуем уменьшить стоимость потока для чего построим остаточную сеть.
Для каждого ребра остаточной сети укажем стоимость транспортировки единицы потока.

```mermaid
graph LR
	d-.->|3|a-.->|1|s
    d-.->|1|b-.->|1|a
    s-->|-1|c
	c-.->|1|s
	s-->|-1|a-->|-1|c-->|-5|d-->|-1|t
```

В остаточной сети найден ориентированный цикл отрицательной стоимости d -> b -> a -> c ->  d ( 1 + 1 - 1 - 5  = -4). 

Найдем минимальный вес ребра в указанном цикле, изображенном **в остаточной сети с указанием величины потока**.  

```mermaid
graph LR
	d-.->|6|a-.->|4|s
    d-.->|6|b-.->|6|a
    s-->|6|c
	c-.->|4|s
	s-->|6|a-->|6|c-->|12|d-->|12|t
```

Минимальный вес ребра в цикле 6 - это неиспользованный резерв ребра d -> b и b -> a.

Удалим найденный цикл - уменьшим на 6 вес всех ребер, входящих в цикл.

```mermaid
graph LR
	s-->|6|a
	a-.->|4|s
	s-->|6|c
	c-.->|4|s
	d-.->|6|a
	a-->|6|b
    c-.->|6|a
    b-->|6|d
	c-->|6|d
	d-->|12|t
	d-.->|6|c
```

### 6. Проведем повторный поиск цикла отрицательной стоимости в остаточной сети.
Скорректируем остаточную сеть с указанием стоимости транспортировки единицы потока.

```mermaid
graph LR
	s-->|-1|a
	a-.->|1|s
	s-->|-1|c
	c-.->|1|s
	d-.->|3|a
	a-->|-1|b
    c-.->|1|a
    b-->|-1|d
	c-->|-5|d
	d-->|-1|t
	d-.->|5|c
```

В остаточной сети найден ориентированный цикл отрицательной стоимости s -> c -> d -> a -> s (- 1 - 5 + 3 - 1 = -4). 

Найдем минимальный вес ребра в указанном цикле, изображенном **в остаточной сети с указанием величины потока**.  

```mermaid
graph LR
	s-->|6|a
	a-.->|4|s
	s-->|6|c
	c-.->|4|s
	d-.->|6|a
	a-->|6|b
    c-.->|6|a
    b-->|6|d
	c-->|6|d
	d-->|12|t
	d-.->|6|c
```

Минимальный вес ребра в цикле 4 - это неиспользованный резерв ребер a -> s.

Удалим найденный цикл - уменьшим на 4 вес всех ребер, входящих в цикл.

```mermaid
graph LR 
	s-->|10|a
	s-->|2|c
	c-.->|8|s
	d-.->|2|a
	a-->|4|d
	a-->|6|b
    c-.->|6|a
    b-->|6|d
	c-->|2|d
	d-->|12|t
	d-.->|10|c
```

### 7. Проведем повторный поиск цикла отрицательной стоимости в остаточной сети.
Скорректируем остаточную сеть с указанием стоимости транспортировки единицы потока.

```mermaid
graph LR
	s-->|-1|a
	s-->|-1|c
	c-.->|1|s
	d-.->|3|a
	a-->|-3|d
	a-->|-1|b
    c-.->|1|a
    b-->|-1|d
	c-->|-5|d
	d-->|-1|t
	d-.->|5|c
```
В остаточной сети отсутствуют циклы отрицательной стоимости, следовательно, стоимость потока минимальна.

### 8. Рассчитаем стоимость полученного максимального потока.

Получившаяся сеть:

```mermaid
graph LR
    s-->|10,10|a
    s-->|2,10|c
    a-->|6,6|b
    a-->|4,6|d
    a-->|0,6|c
    c-->|2,12|d
    b-->|6,6|d
    d-->|12,12|t
```
Расчет стоимости:

| Дуги                                          | sa | sc | ab | ad | ac | cd | bd | dt | Итого |
|:----------------------------------------------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:-----:|
| Пропускная способность p(e)                   | 10 | 10 | 6  | 6  | 6  | 12 | 6  | 12 |       |
| Локальный поток f(e)                          | 10 | 2  | 6  | 4  | 0  | 2  | 6  | 12 |       |
| Стоимость транспортировки единицы потока c(e) | 1  | 1  | 1  | 3  | 1  | 5  | 1  | 1  |       |
| Суммарная стоимость f(e)*c(e)                 | 10 | 2  | 6  | 12 | 0  | 10 | 6  | 12 | **58**|

Стоимость полученного потока составляет 58. 

### Ответ:
Максимальный поток в сети равен 12, минимальная стоимость потока 58, она реализуется следующим локальными потоками:

```mermaid
graph LR
    s-->|10,10|a
    s-->|2,10|c
    a-->|6,6|b
    a-->|4,6|d
    a-->|0,6|c
    c-->|2,12|d
    b-->|6,6|d
    d-->|12,12|t
```
