# Задача о распределении инвестиций между проектами
Условия задачи представляются в виде прямоугольной матрицы, где столбцы соответствуют проектам, а строки части инвестиций, направляемых в проекты, объем инвестиций указывается в первом столбце. В ячейках таблицы представлены суммы прибыли от вложения некоторой части средств в определенный проект.

Для решения задачи требуется рассчитать максимально возможную сумму прибыли от вложения всех средств в проекты и распределение этой суммы между проектами.

**Решение должно содержать подробное пошаговое описание работы алгоритма.**
## Условия задачи для команд:

### TwoPizza:
| $  | A  | B  | C  | D  |
|----|----|----|----|----|
| 2  | 2  | 4  | 5  | 7  |
| 4  | 3  | 6  | 8  | 8  |
| 6  | 5  | 7  | 9  | 17 |
| 8  | 10 | 15 | 14 | 27 |
| 10 | 20 | 30 | 18 | 29 |


**1. Фиксируем два проекта А и В, и ищем оптимальный вариант распределения инвестиций между этими двумя проектами**
#### Таблица оптимального распределения А и В:
| $  | A  | B  | AB          |
|----|----|----|-------------|
| 2  | 2  | 4  | 4 (2В)      |
| 4  | 3  | 6  | 6 (4В)      |
| 6  | 5  | 7  | 8 (2А + 4В) |
| 8  | 10 | 15 | 15 (8В)     |
| 10 | 20 | 30 | 30 (10В)    |

##### Заполняем таблицу выше с помощью данных о наибольшей выгоде при распределении между проектами
##### Таблица вариантов распределения 2 единиц между проектами А и В:
| A   | B   | Выгода |
|-----|-----|--------|
| 0   | 2   | 4      |
| 2   | 0   | 2      |
##### Таблица вариантов распределения 4 единиц между проектами А и В:
| A   | B   | Выгода |
|-----|-----|--------|
| 0   | 4   | 6      |
| 2   | 2   | 6      |
| 4   | 0   | 3      |
##### Таблица вариантов распределения 6 единиц между проектами А и В:
| A   | B   | Выгода |
|-----|-----|--------|
| 0   | 6   | 7      |
| 2   | 4   | 8      |
| 4   | 2   | 7      |
| 6   | 0   | 5      |
##### Таблица вариантов распределения 8 единиц между проектами А и В:
| A   | B   | Выгода |
|-----|-----|--------|
| 0   | 8   | 15     |
| 2   | 6   | 9      |
| 4   | 4   | 9      |
| 6   | 2   | 9      |
| 8   | 0   | 10     |
##### Таблица вариантов распределения 10 единиц между проектами А и В:
| A   | B   | Выгода |
|-----|-----|--------|
| 0   | 10  | 30     |
| 2   | 8   | 17     |
| 4   | 6   | 10     |
| 6   | 4   | 11     |
| 8   | 2   | 14     |
| 10  | 0   | 20     |


**2. Фиксируем два проекта АВ и С, и ищем оптимальный вариант распределения инвестиций между этими двумя проектами, при этом за выгоду проекта АВ принимаем максимальную выгоду из прошлого пункта**
#### Таблица оптимального распределения АВ и С:
| $   | AB  | C   | ABC           |
|-----|-----|-----|---------------|
| 2   | 4   | 5   | 5 (2C)        |
| 4   | 6   | 8   | 9 (2AB + 2C)  |
| 6   | 8   | 9   | 12 (2AB + 4C) |
| 8   | 15  | 14  | 17 (4AB + 4C) |
| 10  | 30  | 18  | 30 (10AB)     |

##### Заполняем таблицу выше с помощью данных о наибольшей выгоде при распределении между проектами
##### Таблица вариантов распределения 2 единиц между проектами АB и C:
| AB  | C   | Выгода |
|-----|-----|--------|
| 0   | 2   | 5      |
| 2   | 0   | 4      |
##### Таблица вариантов распределения 4 единиц между проектами АB и C:
| AB  | C   | Выгода |
|-----|-----|--------|
| 0   | 4   | 8      |
| 2   | 2   | 9      |
| 4   | 0   | 6      |
##### Таблица вариантов распределения 6 единиц между проектами АB и C:
| AB  | C   | Выгода |
|-----|-----|--------|
| 0   | 6   | 9      |
| 2   | 4   | 12     |
| 4   | 2   | 11     |
| 6   | 0   | 8      |
##### Таблица вариантов распределения 8 единиц между проектами АB и C:
| AB  | C   | Выгода |
|-----|-----|--------|
| 0   | 8   | 14     |
| 2   | 6   | 13     |
| 4   | 4   | 17     |
| 6   | 2   | 13     |
| 8   | 0   | 15     |
##### Таблица вариантов распределения 10 единиц между проектами АB и C:
| AB  | C   | Выгода |
|-----|-----|--------|
| 0   | 10  | 18     |
| 2   | 8   | 18     |
| 4   | 6   | 17     |
| 6   | 4   | 16     |
| 8   | 2   | 20     |
| 10  | 0   | 30     |


**3. Фиксируем два проекта АВС и D, и ищем оптимальный вариант распределения инвестиций между этими двумя проектами, при этом за выгоду проекта АВС принимаем максимальную выгоду из прошлого пункта**
#### Таблица оптимального распределения АВС и D:
| $   | ABC | D   | ABCD           |
|-----|-----|-----|----------------|
| 2   | 5   | 7   | 7 (2D)         |
| 4   | 9   | 8   | 12 (2ABC + 2D) |
| 6   | 12  | 17  | 17 (6D)        |
| 8   | 17  | 27  | 27 (8D)        |
| 10  | 30  | 29  | 32 (2ABC + 8D) |

##### Заполняем таблицу выше с помощью данных о наибольшей выгоде при распределении между проектами
##### Таблица вариантов распределения 2 единиц между проектами АBC и D:
| ABC | D   | Выгода |
|-----|-----|--------|
| 0   | 2   | 7      |
| 2   | 0   | 5      |
##### Таблица вариантов распределения 4 единиц между проектами АBC и D:
| ABC | D   | Выгода |
|-----|-----|--------|
| 0   | 4   | 8      |
| 2   | 2   | 12     |
| 4   | 0   | 9      |
##### Таблица вариантов распределения 6 единиц между проектами АBC и D:
| ABC | D   | Выгода |
|-----|-----|--------|
| 0   | 6   | 17     |
| 2   | 4   | 13     |
| 4   | 2   | 16     |
| 6   | 0   | 12     |
##### Таблица вариантов распределения 8 единиц между проектами АBC и D:
| ABC | D   | Выгода |
|-----|-----|--------|
| 0   | 8   | 27     |
| 2   | 6   | 22     |
| 4   | 4   | 17     |
| 6   | 2   | 19     |
| 8   | 0   | 17     |
##### Таблица вариантов распределения 10 единиц между проектами АBC и D:
| ABC | D   | Выгода |
|-----|-----|--------|
| 0   | 10  | 29     |
| 2   | 8   | 32     |
| 4   | 6   | 26     |
| 6   | 4   | 20     |
| 8   | 2   | 24     |
| 10  | 0   | 30     |
 
**4. Расширяем изначальную таблицу с учетом группировки проектов**
| $  | A  | B  | C  | D  | AB          | ABC           | ABCD           |
|----|----|----|----|----|-------------|---------------|----------------|
| 2  | 2  | 4  | 5  | 7  | 4 (2B)      | 5 (2C)        | 7 (2D)         |
| 4  | 3  | 6  | 8  | 8  | 6 (4B)      | 9 (2AB + 2C)  | 12 (2ABC + 2D) |
| 6  | 5  | 7  | 9  | 17 | 8 (2A + 4B) | 12 (2AB + 4C) | 17 (6D)        |
| 8  | 10 | 15 | 14 | 27 | 15 (8B)     | 17 (4AB + 4C) | 27 (8D)        |
| 10 | 20 | 30 | 18 | 29 | 30 (10B)    | 30 (10AB)     | 32 (2ABC + 8D) |

***Ответ: Для максимальной выгоды при вложении 10 единиц необходимо выбрать следующую комбинацию проектов 2C + 8D, максимальная выгода составляет 32 единицы***