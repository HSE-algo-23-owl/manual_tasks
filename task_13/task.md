# Задача о назначениях. Венгерский алгоритм.
1. В условиях задачи для каждой команды указан полный двудольный граф, в котором каждое ребро имеет определенную стоимость. Вершины первой доли представляют задачи, вершины второй доли исполнителей. Стоимость ребра определяет затраты при выполнении соответствующей задачи соответствующим исполнителем.
2. Затраты неотрицательны и представлены в виде матрицы затрат, в которой на пересечении i-й строки и j-го столбца указаны затраты j-го исполнителя на выполнение i-го задания.
3. Необходимо назначить исполнителей на задачи таким образом, чтобы общая стоимость затрат была минимальной.
4. Для решения задачи требуется найти совершенное паросочетание с минимальной суммарной стоимостью в двудольном графе.

## Условия задачи для команд:
### Kotyatki Team:

|       | **1** | **2** | **3** | **4** | **5** |
|-------|:-----:|:-----:|:-----:|:-----:|:-----:|
| **A** |   7   |  12   |   3   |  14   |  10   |
| **B** |  11   |   5   |   8   |  12   |   7   |
| **C** |   6   |   9   |  13   |   7   |  12   |
| **D** |  10   |   4   |  15   |   7   |   9   |
| **E** |   8   |   6   |  11   |   5   |  13   |

### Blur Team:


|       | **1** | **2** | **3** | **4** | **5** |
|-------|:-----:|:-----:|:-----:|:-----:|:-----:|
| **A** |  15   |  20   |  18   |  16   |  17   |
| **B** |  19   |  14   |  13   |  12   |  15   |
| **C** |  16   |  17   |  18   |  19   |  20   |
| **D** |  15   |  14   |  13   |  12   |  11   |
| **E** |  10   |   9   |   8   |   7   |   6   |

### sluggish_pythons Team: 

|       | **1** | **2** | **3** | **4** | **5** |
|-------|:-----:|:-----:|:-----:|:-----:|:-----:|
| **A** |   5   |   6   |   7   |   8   |   9   |
| **B** |  10   |  11   |  12   |  13   |  14   |
| **C** |  15   |  16   |  17   |  18   |  19   |
| **D** |  20   |   5   |   6   |   7   |   8   |
| **E** |   9   |  10   |  11   |  12   |  13   |

### All ca$h Team: 

|       | **1** | **2** | **3** | **4** | **5** |
|-------|:-----:|:-----:|:-----:|:-----:|:-----:|
| **A** |  14   |  15   |  16   |  17   |  18   |
| **B** |  19   |  20   |   5   |   6   |   7   |
| **C** |   8   |   9   |  10   |  11   |  12   |
| **D** |  13   |  14   |  15   |  16   |  17   |
| **E** |  18   |  19   |  20   |   5   |   6   |

### TwoPizza Team:

|       | **1** | **2** | **3** | **4** | **5** |
|-------|:-----:|:-----:|:-----:|:-----:|:-----:|
| **A** |  17   |  20   |  10   |   5   |   8   |
| **B** |  16   |   8   |  12   |  14   |   8   |
| **C** |  10   |   7   |   9   |  12   |  11   |
| **D** |  13   |  13   |  17   |  15   |   6   |
| **E** |  11   |  12   |  12   |  19   |  13   |

### AlgoWizards Team:

|        | **1** | **2** | **3** | **4** | **5** |
|--------|:-----:|:-----:|:-----:|:-----:|:-----:|
| **A**  |   5   |   6   |  14   |  14   |  20   |
| **B**  |   5   |  20   |  15   |   9   |  12   |
| **C**  |   8   |  19   |  16   |   7   |  12   |
| **D**  |  17   |   7   |  10   |   5   |   9   |
| **E**  |  10   |  10   |  11   |  13   |   9   |

### 1.KLA$ Team:

|       | **1** | **2** | **3** | **4** | **5** |
|-------|:-----:|:-----:|:-----:|:-----:|:-----:|
| **A** |   6   |  20   |   9   |  14   |  15   |
| **B** |  15   |  20   |  13   |   6   |   6   |
| **C** |  12   |  14   |  14   |   8   |  11   |
| **D** |  12   |  16   |  19   |   7   |  16   |
| **E** |   5   |  19   |   8   |  10   |  17   |

### Cupcakes Team:

|       | **1** | **2** | **3** | **4** | **5** |
|-------|:-----:|:-----:|:-----:|:-----:|:-----:|
| **A** |  14   |  15   |   9   |  16   |   9   |
| **B** |  11   |   9   |  20   |  20   |   9   |
| **C** |   8   |  17   |   9   |   9   |  13   |
| **D** |  19   |  20   |   9   |   8   |  15   |
| **E** |  12   |  20   |  18   |  10   |  12   |

### BB Team:

|       | **1** | **2** | **3** | **4** | **5** |
|-------|:-----:|:-----:|:-----:|:-----:|:-----:|
| **A** |   5   |  15   |   7   |  16   |  15   |
| **B** |  20   |  12   |  16   |   7   |  14   |
| **C** |   7   |  19   |   8   |  19   |  16   |
| **D** |   8   |   7   |  19   |   8   |   9   |
| **E** |   6   |   7   |  16   |  19   |  14   |

### zavod_dao Team:

|       | **1** | **2** | **3** | **4** | **5** |
|-------|:-----:|:-----:|:-----:|:-----:|:-----:|
| **A** |  16   |  12   |  13   |  15   |  10   |
| **B** |  12   |  14   |   7   |   9   |   9   |
| **C** |  12   |  10   |   9   |  11   |   6   |
| **D** |  13   |  13   |   5   |  13   |  11   |
| **E** |  14   |  13   |  11   |  10   |  15   |

