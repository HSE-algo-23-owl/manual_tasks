# Задача о распределении инвестиций между проектами
Условия задачи представляются в виде прямоугольной матрицы, где столбцы соответствуют проектам, а строки части инвестиций, направляемых в проекты, объем инвестиций указывается в первом столбце. В ячейках таблицы представлены суммы прибыли от вложения некоторой части средств в определенный проект.

Для решения задачи требуется рассчитать максимально возможную сумму прибыли от вложения всех средств в проекты и распределение этой суммы между проектами.

**Решение должно содержать подробное пошаговое описание работы алгоритма.**
## Условия задачи для команд:
### Kotyatki Team:
| $   | A  | B  | C  | D  | E  |
|-----|----|----|----|----|----|
| 100 | 8  | 6  | 6  | 1  | 4  |
| 200 | 15 | 8  | 9  | 7  | 8  |
| 300 | 16 | 12 | 13 | 10 | 14 |
| 400 | 19 | 15 | 17 | 15 | 16 |
| 500 | 20 | 19 | 19 | 18 | 21 |
| 600 | 25 | 26 | 24 | 21 | 22 |
### Blur Team:
| $   | A   | B   | С   | D   | 
|-----|-----|-----|-----|-----|  
| 50  | 10  | 6   | 8   | 12  | 
| 100 | 13  | 9   | 11  | 14  | 
| 150 | 18  | 13  | 15  | 17  | 
| 200 | 20  | 14  | 17  | 18  | 
| 250 | 22  | 18  | 20  | 19  | 
### sluggish_pythons Team:
| $  | A   | B   | С   | D   | 
|----|-----|-----|-----|-----|  
| 10 | 4   | 7   | 5   | 6   | 
| 20 | 9   | 8   | 7   | 10  | 
| 30 | 12  | 13  | 10  | 11  | 
| 40 | 14  | 14  | 15  | 13  | 
| 50 | 19  | 18  | 20  | 19  | 
### All ca$h Team:
| $   | A  | B  | C  | D  | E  | F  |
|-----|----|----|----|----|----|----|
| 100 | 3  | 5  | 4  | 7  | 1  | 2  |
| 200 | 7  | 10 | 8  | 9  | 8  | 6  |
| 300 | 9  | 12 | 14 | 10 | 9  | 8  |
| 400 | 13 | 15 | 16 | 14 | 11 | 17 |
| 500 | 16 | 18 | 19 | 15 | 15 | 21 |
### TwoPizza Team:
| $  | A  | B  | C  | D  |
|----|----|----|----|----|
| 2  | 2  | 4  | 5  | 7  |
| 4  | 3  | 6  | 8  | 8  |
| 6  | 5  | 7  | 9  | 17 |
| 8  | 10 | 15 | 14 | 27 |
| 10 | 20 | 30 | 18 | 29 |
### AlgoWizards Team:
| $   | A  | B  | C  | D  |
|-----|----|----|----|----|
| 20  | 7  | 2  | 1  | 4  |
| 40  | 8  | 10 | 12 | 13 |
| 60  | 11 | 13 | 14 | 16 |
| 80  | 17 | 16 | 15 | 18 |
| 100 | 20 | 21 | 19 | 19 |
### 1.KLA$ Team:
| $   | A | B  | C  | D  |
|-----|---|----|----|----|
| 50  | 5 | 4  | 4  | 7  |
| 100 | 6 | 7  | 8  | 12 |
| 150 | 1 | 10 | 15 | 12 |
| 200 | 2 | 12 | 23 | 15 |
| 250 | 6 | 15 | 42 | 18 |
### Cupcakes Team:
| $   | A   | B   | C   | D   |
|-----|-----|-----|-----|-----|
| 100 | 11  | 14  | 16  | 12  |
| 200 | 29  | 27  | 23  | 29  |
| 300 | 30  | 35  | 33  | 32  |
| 400 | 41  | 43  | 40  | 45  |
### BB Team:
| $   | A  | B  | С  | D  | 
|-----|----|----|----|----|  
| 30  | 6  | 8  | 1  | 9  | 
| 60  | 8  | 9  | 3  | 10 | 
| 90  | 10 | 11 | 5  | 14 | 
| 120 | 12 | 13 | 7  | 15 | 
| 150 | 14 | 15 | 10 | 18 | 
### zavod_dao Team:
| $   | A  | B  | С  | D  | 
|-----|----|----|----|----|  
| 100 | 5  | 3  | 5  | 4  | 
| 200 | 8  | 7  | 10 | 8  | 
| 300 | 18 | 9  | 15 | 17 | 
| 400 | 21 | 10 | 20 | 19 | 
| 500 | 25 | 18 | 21 | 23 |