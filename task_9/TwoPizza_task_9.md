### Вариант 4: 
- Стратегия: уровневая
- Количество задач: 14 
- Количество исполнителей: 3
- Количество деревьев: 2

#### 1. Постановка задачи
#### Составить расписание выполнения в кратчайшие сроки 14 заданий тремя идентичными исполнителями. Все задания имеют единичную длительность, а зависимость между ними задана таблицей (задания обозначены буквами A, B, C, …, N):
#### Таблица зависимостей:
|Предшествующее задание| K | L | G | H | M | N | I | J | E | F | B | D |
|----------------------|---|---|---|---|---|---|---|---|---|---|---|---|
|Последующее задание   | G | G | C | C | I | I | D | D | B | B | A | A |

#### 2. Решение задачи:
Для решения этой задачи необходимо построить граф, который будет отображать зависимости задач друг от друга, основываясь на виде графа необходимо выбрать стратегию для решения поставленной задачи
```mermaid
graph TB
K((K)) --> G((G))
L((L)) --> G((G))
G((G)) --> C((C))
H((H)) --> C((C))
M((M)) --> I((I))
N((N)) --> I((I))
I((I)) --> D((D))
J((J)) --> D((D))
E((E)) --> B((B))
F((F)) --> B((B))
B((B)) --> A((A))
D((D)) --> A((A))
```
Т.к. граф, который мы построили, представляет собой два дерева, ориентированным к корню, работники универесальны и задания одинаковой длительности, то мы можем использовать уровневую стратегию, которая является эффективной.

Для начала необходимо задать приоритеты для задач, основываясь на приоритете их потомков, т.е. приоритет получит раньше та задача, чей потомок обладает наименьшим приоритетом, задача B в нашем случае получит приоритет 1, т.к. является стоком (не имеет потомков)

Дерево с расставленными приоритетами приведено ниже:
```mermaid
graph TB
K-11((K-11)) --> G-5((G-5))
L-12((L-12)) --> G-5((G-5))
G-5((G-5)) --> C-2((C-2))
H-6((H-6)) --> C-2((C-2))
M-13((M-13)) --> I-7((I-7))
N-14((N-14)) --> I-7((I-7))
I-7((I-7)) --> D-3((D-3))
J-8((J-8)) --> D-3((D-3))
E-9((E-9)) --> B-4((B-4))
F-10((F-10)) --> B-4((B-4))
B-4((B-4)) --> A-1((A-1))
D-3((D-3)) --> A-1((A-1))

```
#### 3. Ответ:
1. Диаграмма Ганта
```mermaid
gantt
    title Диаграмма Ганта - Ленточная стратегия для 3 исполнителей
    dateFormat  HH:mm    
    axisFormat %H:%M
    Начало выполнения работ : milestone, m1, 00:00, 0h
    section Исполнитель 1
    Задача N            :a1, 00:00, 1h
    Задача K            :a1, 01:00, 1h
    Задача J            :a1, 02:00, 1h
    Задача G            :a1, 03:00, 1h
    Задача C            :a1, 04:00, 1h
    section Исполнитель 2
    Задача M            :b1, 00:00, 1h
    Задача F            :b1, 01:00, 1h
    Задача I            :b1, 02:00, 1h
    Задача B            :b1, 03:00, 1h
    Задача A            :b1, 04:00, 1h
    section Исполнитель 3
    Задача L            :c1, 00:00, 1h
    Задача E            :c1, 01:00, 1h
    Задача H            :c1, 02:00, 1h
    Задача D            :c1, 03:00, 1h
    
    Окончание выполнения работ : milestone, m2, 05:00, 0h
```
2. Длительность расписания 5 часов.