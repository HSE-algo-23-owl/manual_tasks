# Задача о максимальном потоке минимальной стоимости.
Для каждого варианта представлены условия задачи, в соответствии с которыми необходимо: 
1. Построить сеть с указанием пропускной способности дуг.
2. Построить остаточную сеть.
3. Определить максимальный поток методом поиска увеличивающих путей в остаточной сети.
4. Минимизировать стоимость максимального потока посредством поиска циклов отрицательной стоимости.
5. Оформить решение задачи по шагам с подробными комментариями, таблицами и диаграммами.
6. В ответе указать максимальную величину потока, минимальную стоимость и сеть с указанием соответствующих локальных потоков.

## Варианты условий задачи:
### Вариант 1:

| Дуги                      | sa | sb | sc | ac | ad | ab | bd | ct | dt |
|:--------------------------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Пропускная способность    | 10 | 10 | 5  | 7  | 8  | 5  | 8  | 10 | 10 |
| Стоимость транспортировки | 1  | 1  | 1  | 2  | 3  | 1  | 1  | 2  | 1  |

### Вариант 2:

| Дуги                      | sa | sb | ad | ab | ac | bc | bd | cd | dt |
|:--------------------------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Пропускная способность    | 10 | 10 | 6  | 6  | 5  | 8  | 5  | 10 | 18 |
| Стоимость транспортировки | 1  | 1  | 7  | 1  | 1  | 1  | 5  | 1  | 1  |

### Вариант 3: 

| Дуги                      | sa | sb | ac | ba | bc | bd | cd | dt |
|:--------------------------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Пропускная способность    | 3  | 10 | 4  | 1  | 3  | 10 | 8  | 12 |
| Стоимость транспортировки | 1  | 1  | 1  | 2  | 3  | 5  | 1  | 1  |

### Вариант 4: 

| Дуги                      | se | ea | ec | ed | ab | cb | dc | bt | ct | dt |
|:--------------------------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Пропускная способность    | 18 | 5  | 6  | 10 | 5  | 4  | 3  | 8  | 4  | 8  |
| Стоимость транспортировки | 1  | 2  | 3  | 2  | 1  | 1  | 1  | 2  | 3  | 5  |

### Вариант 5: 

| Дуги                      | sa | sb | sc | ba | bc | cd | ac | ad | dt |
|:--------------------------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Пропускная способность    | 6  | 6  | 6  | 6  | 5  | 10 | 5  | 8  | 12 |
| Стоимость транспортировки | 1  | 1  | 3  | 1  | 1  | 1  | 3  | 4  | 1  |

### Вариант 6:

| Дуги                      | sa | sc | ab | bd | ad | cb | ct | bt | dt |
|:--------------------------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Пропускная способность    | 8  | 8  | 2  | 3  | 6  | 4  | 4  | 6  | 8  |
| Стоимость транспортировки | 1  | 1  | 1  | 1  | 2  | 2  | 5  | 3  | 1  |

### Вариант 7:

| Дуги                      | sa | sc | ab | ad | ac | cd | bd | dt |
|:--------------------------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Пропускная способность    | 10 | 10 | 6  | 6  | 6  | 12 | 6  | 12 |
| Стоимость транспортировки | 1  | 1  | 1  | 3  | 1  | 5  | 1  | 1  |

### Вариант 8:

| Дуги                      | sa | sс | sd | ac | ad | ab | db | cb | at | bt |
|:--------------------------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Пропускная способность    | 7  | 5  | 5  | 5  | 5  | 5  | 5  | 6  | 3  | 9  |
| Стоимость транспортировки | 1  | 1  | 1  | 1  | 1  | 3  | 1  | 3  | 7  | 1  |

### Вариант 9:

| Дуги                      | sa | sс | ab | ac | cb | bd | de | be | ce | et |
|:--------------------------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Пропускная способность    | 8  | 8  | 7  | 3  | 6  | 6  | 5  | 5  | 12 | 12 |
| Стоимость транспортировки | 1  | 1  | 2  | 1  | 1  | 2  | 2  | 5  | 7  | 1  |

### Вариант 10:

| Дуги                      | sa | ab | ae | ad | bc | cd | ct | dt | bt | et |
|:--------------------------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Пропускная способность    | 7  | 4  | 8  | 6  | 6  | 4  | 5  | 5  | 5  | 5  |
| Стоимость транспортировки | 1  | 1  | 3  | 3  | 1  | 2  | 1  | 1  | 3  | 3  |