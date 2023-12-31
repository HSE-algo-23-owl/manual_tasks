### Вариант 2: 
- Стратегия: уровневая
- Количество задач: 13
- Количество исполнителей: 2 
- Количество деревьев: 1

#### 1. Постановка задачи
#### Составить расписание выполнения в кратчайшие сроки 13 заданий двумя идентичными исполнителями. Все задания имеют единичную длительность, а зависимость между ними задана таблицей (задания обозначены буквами A, B, C, …, M):
#### Таблица зависимостей:
| A | C | D | E | F | G | H | J | K | L | M | N |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B | D | F | M | J | D | A | B | M | H | H | M |

#### 2. Решение задачи:
Для решения этой задачи необходимо построить граф, который будет отображать зависимости задач друг от друга, основываясь на виде графа необходимо выбрать стратегию для решения поставленной задачи
```mermaid
graph TB
A((A)) --> B((B))
C((C)) --> D((D))
D((D)) --> F((F))
E((E)) --> M((M))
F((F)) --> J((J))
G((G)) --> D((D))
H((H)) --> A((A))
J((J)) --> B((B))
K((K)) --> M((M))
L((L)) --> H((H))
M((M)) --> H((H))
N((N)) --> M((M))
```
Т.к. граф, который мы построили является деревом, ориентированным к корню, работники универесальны и задания одинаковой длительности, мы можем использовать уровневую стратегию, которая является эффективной

Для начала необходимо задать приоритеты для задач, основываясь на приоритете их потомков, т.е. приоритет получит раньше та задача, чей потомок обладает наименьшим приоритетом, задача B в нашем случае получит приоритет 1, т.к. является стоком (не имеет потмоков)

Дерево с расставленными приоритетами приведено ниже:
```mermaid
graph TB
A-2((A-2)) --> B-1((B-1))
C-12((C-12)) --> D-8((D-8))
D-8((D-8)) --> F((F-5))
E-10((E-10)) --> M-7((M-7))
F((F-5)) --> J-3((J-3))
G-13((G-13)) --> D-8((D-8))
H-4((H-4)) --> A-2((A-2))
J-3((J-3)) --> B-1((B-1))
K-9((K-9)) --> M-7((M-7))
L-6((L-6)) --> H-4((H-4))
M-7((M-7)) --> H-4((H-4))
N-11((N-11)) --> M-7((M-7))
```
#### 3. Ответ:
1. Диаграмма Ганта
```mermaid
gantt
    title Диаграмма Ганта - Ленточная стратегия для 4 исполнителей
    dateFormat  HH:mm    
    axisFormat %H:%M
    Начало выполнения работ : milestone, m1, 00:00, 0h
    section Исполнитель 1
    Задача G            :a1, 00:00, 1h
    Задача N            :a1, 01:00, 1h
    Задача K            :a1, 02:00, 1h
    Задача M            :a1, 03:00, 1h
    Задача F            :a1, 04:00, 1h
    Задача J            :a1, 05:00, 1h
    Задача B            :a1, 06:00, 1h
    section Исполнитель 2
    Задача C            :b1, 00:00, 1h
    Задача E            :b1, 01:00, 1h
    Задача D            :b1, 02:00, 1h
    Задача L            :b1, 03:00, 1h
    Задача H            :b1, 04:00, 1h
    Задача A            :b1, 05:00, 1h
    
    Окончание выполнения работ : milestone, m2, 07:00, 0h
```
2. Длительность расписания 7 часов. 
