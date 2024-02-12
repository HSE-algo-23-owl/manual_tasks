from collections import Counter


def initialize_cost_matrix(cost_matrix):
    # Вычитаем минимальное значение из каждой строки
    for i in range(len(cost_matrix)):
        min_in_row = min(cost_matrix[i])
        for j in range(len(cost_matrix[i])):
            cost_matrix[i][j] -= min_in_row

    # Вычитаем минимальное значение из каждого столбца
    for j in range(len(cost_matrix[0])):
        min_in_col = min(cost_matrix[i][j] for i in range(len(cost_matrix)))
        for i in range(len(cost_matrix)):
            cost_matrix[i][j] -= min_in_col

    return cost_matrix


def find_zero_coverage(matrix):
    rows_covered = set()
    cols_covered = set()

    # Поочередный проход по всем элементам матрицы
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0 and i not in rows_covered and j not in cols_covered:
                rows_covered.add(i)
                cols_covered.add(j)

    # Альтернативное покрытие
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0 and i in rows_covered and j not in cols_covered:
                cols_covered.add(j)
            elif matrix[i][j] == 0 and i not in rows_covered and j in cols_covered:
                rows_covered.add(i)

    return rows_covered, cols_covered


def build_chains(matrix, rows_covered, cols_covered):
    # Пока количество линий не равно общему количеству строк или столбцов
    while True:
        # Находим непокрытый нулевой элемент
        zero_element = None
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0 and i not in rows_covered and j not in cols_covered:
                    zero_element = (i, j)
                    break
            if zero_element:
                break

        # Если нет непокрытых нулей, выходим из цикла
        if not zero_element:
            break

        # Построение цепи
        chain = [zero_element]
        while True:
            i, j = chain[-1]
            # Ищем покрытые нулевые элементы в строке
            for col in range(len(matrix[0])):
                if matrix[i][col] == 0 and col in cols_covered and (i, col) not in chain:
                    chain.append((i, col))
                    break
            else:
                # Ищем покрытые нулевые элементы в столбце
                for row in range(len(matrix)):
                    if matrix[row][j] == 0 and row in rows_covered and (row, j) not in chain:
                        chain.append((row, j))
                        break
                else:
                    break

        # Ищем непокрытый нулевой элемент в конце цепи
        last_element = chain[-1]
        i, j = last_element
        for col in range(len(matrix[0])):
            if matrix[i][col] == 0 and col in cols_covered and (i, col) not in chain:
                chain.append((i, col))
                break
        else:
            for row in range(len(matrix)):
                if matrix[row][j] == 0 and row in rows_covered and (row, j) not in chain:
                    chain.append((row, j))
                    break

        # Меняем покрытие для всех элементов в цепи
        for i, j in chain:
            if i in rows_covered:
                rows_covered.remove(i)
            else:
                rows_covered.add(i)
            if j in cols_covered:
                cols_covered.remove(j)
            else:
                cols_covered.add(j)

    return rows_covered, cols_covered


def is_optimal_solution(rows_covered, cols_covered, matrix):
    return len(rows_covered) == len(matrix) or len(cols_covered) == len(matrix[0])


def print_optimal_solution(matrix, rows_covered, cols_covered):
    assignments = set()
    for row in rows_covered:
        for col in cols_covered:
            if matrix[row][col] == 0:
                assignments.add((row, col + 1))

    assignments = list(assignments)
    counter = Counter([item[0] for item in assignments])
    sorted_first_elements = sorted(counter.keys(), key=lambda x: (counter[x], x))
    assignments = [(first, second) for first in sorted_first_elements for second in
                   [item[1] for item in assignments if item[0] == first]]
    ans = {}
    used_performers = []
    used_tasks = []
    print("Оптимальное решение:")
    for assignment in assignments:
        task = chr(assignment[0] + ord('a'))
        performer = assignment[1]
        try:
            if ans[task] != performer:  # Если исполнитель уже присвоен
                if performer not in used_performers and task not in used_tasks:  # Если исполнитель еще не использован
                    ans[task] = performer
                    used_performers.append(performer)
                    used_tasks.append(task)

        except Exception as e:  # Если исполнитель не присвоен
            if performer not in used_performers:  # Если исполнитель еще не использован
                ans[task] = performer
                used_performers.append(performer)
                used_tasks.append(task)

    # Проверяем, есть ли нерешенные задачи
    for task in range(len(matrix)):
        if chr(task + ord('a')) not in ans:
            performer = 1
            while performer in used_performers:
                performer += 1
            ans[chr(task + ord('a'))] = performer
            used_performers.append(performer)

    for task, performer in ans.items():
        print(f"Задача {task} -> Исполнитель {performer}")
    return ans


def calculate_total_cost(cost_matrix, optimal_solution):
    total_cost = 0
    for task, performer in optimal_solution.items():
        task_index = ord(task) - ord('a')
        performer_index = performer - 1
        total_cost += cost_matrix[task_index][performer_index]
    return total_cost


# Пример матрицы стоимостей
"""
пример из задания
cost_matrix = [
    [1, 4, 4, 3],
    [2, 7, 6, 8],
    [4, 7, 5, 6],
    [2, 5, 1, 1]
]
a_cost_matrix = [
    [1, 4, 4, 3],
    [2, 7, 6, 8],
    [4, 7, 5, 6],
    [2, 5, 1, 1]
]
"""
cost_matrix = [
    [5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19],
    [20, 5, 6, 7, 8],
    [9, 10, 11, 12, 13]
]
a_cost_matrix = [
    [5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19],
    [20, 5, 6, 7, 8],
    [9, 10, 11, 12, 13]
]

# Инициализация матрицы стоимостей
reduced_matrix = initialize_cost_matrix(cost_matrix)
print("Редуцированная матрица:")
for row in reduced_matrix:
    print(row)

# Поиск нулевого покрытия
rows_covered, cols_covered = find_zero_coverage(reduced_matrix)
print("\nПокрытые строки:", rows_covered)
print("Покрытые столбцы:", cols_covered)

# Построение цепей
rows_covered, cols_covered = build_chains(reduced_matrix, rows_covered, cols_covered)
print("\nПокрытые строки после построения цепей:", rows_covered)
print("Покрытые столбцы после построения цепей:", cols_covered)


# Проверка достаточности линий
while not is_optimal_solution(rows_covered, cols_covered, reduced_matrix):
    print("\nПродолжаем итерацию алгоритма.")

    # Поиск нулевого покрытия
    rows_covered, cols_covered = find_zero_coverage(reduced_matrix)
    print("\nПокрытые строки:", rows_covered)
    print("Покрытые столбцы:", cols_covered)

    # Построение цепей
    rows_covered, cols_covered = build_chains(reduced_matrix, rows_covered, cols_covered)
    print("\nПокрытые строки после построения цепей:", rows_covered)
    print("Покрытые столбцы после построения цепей:", cols_covered)


if is_optimal_solution(rows_covered, cols_covered, reduced_matrix):
    print("\nДостигнуто оптимальное решение.")
    a = print_optimal_solution(cost_matrix, rows_covered, cols_covered)

total_cost = calculate_total_cost(a_cost_matrix, a)
print("Общая сумма затрат:", total_cost)