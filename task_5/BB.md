## Условие задачи для нашей команды (BB Team) 😊😱😴🥰:
| $   | A  | B  | С  | D  | 
|-----|----|----|----|----|  
| 30  | 6  | 8  | 1  | 9  | 
| 60  | 8  | 9  | 3  | 10 | 
| 90  | 10 | 11 | 5  | 14 | 
| 120 | 12 | 13 | 7  | 15 | 
| 150 | 14 | 15 | 10 | 18 | 
>### Задача о распределении инвестиций между проектами
>Условия задачи представлены в виде прямоугольной матрицы, где столбцы соответствуют проектам, а строки части инвестиций, направляемых в проекты, объем инвестиций указыван в первом столбце. В ячейках таблицы представлены суммы прибыли от вложения некоторой части средств в определенный проект.
>
> Для решения задачи требуется рассчитать максимально возможную сумму прибыли от вложения всех средств в проекты и распределение этой суммы между проектами.

**Решение содержит подробное пошаговое описание работы алгоритма.**

 - *Для начала зафиксируем 2 проекта A и B и ищем оптимальный вариант распределения инвестиций между двумя этими проектами, распишем это ввиде таблицы. А так же в виде таблиц обоснуем все варианты наших рассуждений:*
### A и B
| $   | A  | B  | AB              |
|-----|----|----|-----------------|
| 30  | 6  | 8  | 8 (30B)         |
| 60  | 8  | 9  | 14 (30А + 30В)  |
| 90  | 10 | 11 | 16 (60А + 30В)  |
| 120 | 12 | 13 | 18 (90А + 30В)  |
| 150 | 14 | 15 | 20 (120А + 30В) |

##### Варианты распределения 30 между проектами А и В:
| A  | B  | Выгода |
|----|----|--------|
| 0  | 30 | 8      |   
| 30 | 0  | 6      |
##### Варианты распределения 60 между проектами А и В:
| A  | B  | Выгода |
|----|----|--------|
| 60 | 0  | 8      | 
| 30 | 30 | 14     |
| 0  | 60 | 9      |
##### Варианты распределения 90 между проектами А и В:
| A  | B  | Выгода |
|----|----|--------|
| 90 | 0  | 10     | 
| 60 | 30 | 16     |
| 30 | 60 | 15     |
| 0  | 90 | 11     |
##### Варианты распределения 120 между проектами А и В:
| A   | B   | Выгода |
|-----|-----|--------|
| 120 | 0   | 12     | 
| 90  | 30  | 18     |
| 60  | 60  | 17     |
| 30  | 90  | 17     |
| 0   | 120 | 13     |
##### Варианты распределения 150 между проектами А и В:
| A   | B   | Выгода |
|-----|-----|--------|
| 150 | 0   | 14     | 
| 120 | 30  | 20     |
| 90  | 60  | 19     |
| 60  | 90  | 19     |
| 30  | 120 | 19     |
| 0   | 150 | 15     |   

 - *Теперь фиксируем 2 проекта AB и С и ищем оптимальный вариант распределения инвестиций между двумя этими проектами, распишем это ввиде таблицы. А так же в виде таблиц обоснуем все варианты наших рассуждений:*

### AB и C                                         
| $   | AB | C  | ABC        |               
|-----|----|----|------------|               
| 30  | 8  | 1  | 8 (30AB)   |               
| 60  | 14 | 3  | 14 (60АB)  |               
| 90  | 16 | 5  | 16 (90АВ)  |               
| 120 | 18 | 7  | 18 (120АВ) |               
| 150 | 20 | 10 | 20 (150АВ) |     

##### Варианты распределения 30 между проектами АB и C:          
| AB | C  | Выгода |                                            
|----|----|--------|                                            
| 0  | 30 | 1      |                                            
| 30 | 0  | 8      |                                            
##### Варианты распределения 60 между проектами АB и C:          
| AB | C  | Выгода |                                            
|----|----|--------|                                            
| 60 | 0  | 14     |                                            
| 30 | 30 | 9      |                                            
| 0  | 60 | 3      |                                            
##### Варианты распределения 90 между проектами АB и C:          
| AB | C  | Выгода |                                            
|----|----|--------|                                            
| 90 | 0  | 16     |                                            
| 60 | 30 | 15     |                                            
| 30 | 60 | 11     |                                            
| 0  | 90 | 5      |                                            
##### Варианты распределения 120 между проектами АB и C:         
| AB  | C   | Выгода |                                          
|-----|-----|--------|                                          
| 120 | 0   | 18     |                                          
| 90  | 30  | 17     |                                          
| 60  | 60  | 17     |                                          
| 30  | 90  | 13     |                                          
| 0   | 120 | 7      |                                          
##### Варианты распределения 150 между проектами АB и C:         
| AB  | C   | Выгода |                                          
|-----|-----|--------|                                          
| 150 | 0   | 20     |                                          
| 120 | 30  | 19     |                                          
| 90  | 60  | 19     |                                          
| 60  | 90  | 19     |                                          
| 30  | 120 | 15     |                                          
| 0   | 150 | 10     |   

- *Теперь фиксируем снова 2 проекта ABC и D и ищем оптимальный вариант распределения инвестиций между двумя этими проектами, распишем это ввиде таблицы. А так же в виде таблиц обоснуем все варианты наших рассуждений:*
### ABC и B                            
| $   | ABC | D  | ABCD           |       
|-----|-----|----|----------------|       
| 30  | 8   | 9  | 9 (30D)        |       
| 60  | 14  | 10 | 17 (30АBC+30D) |       
| 90  | 16  | 14 | 23 (60АВC+30D) |       
| 120 | 18  | 15 | 25 (90АВC+30D) |       
| 150 | 20  | 18 | 28 (60АВC+90D) |  

##### Варианты распределения 30 между проектами АBC и D:     
| ABC | D  | Выгода |                                        
|-----|----|--------|                                        
| 0   | 30 | 9      |                                        
| 30  | 0  | 8      |                                        
##### Варианты распределения 60 между проектами АBC и D:     
| ABC | D  | Выгода |                                        
|-----|----|--------|                                        
| 60  | 0  | 14     |                                        
| 30  | 30 | 17     |                                        
| 0   | 60 | 10     |                                        
##### Варианты распределения 90 между проектами АBC и D:     
| ABC | D  | Выгода |                                        
|-----|----|--------|                                        
| 90  | 0  | 16     |                                        
| 60  | 30 | 23     |                                        
| 30  | 60 | 18     |                                        
| 0   | 90 | 14     |                                        
##### Варианты распределения 120 между проектами АBC и D:    
| ABC | D   | Выгода |                                      
|-----|-----|--------|                                      
| 120 | 0   | 18     |                                      
| 90  | 30  | 25     |                                      
| 60  | 60  | 24     |                                      
| 30  | 90  | 22     |                                      
| 0   | 120 | 15     |                                      
##### Варианты распределения 150 между проектами АBC и D:    
| ABC | D   | Выгода |                                      
|-----|-----|--------|                                      
| 150 | 0   | 20     |                                      
| 120 | 30  | 27     |                                      
| 90  | 60  | 26     |                                      
| 60  | 90  | 28     |                                      
| 30  | 120 | 23     |                                      
| 0   | 150 | 18     |    

## В результате мы можем составить новую дополненную таблицу:

| $  | A  | B  | C  | D  | AB            | ABC        | ABCD               |
|----|----|----|----|----|---------------|------------|--------------------|
| 2  | 2  | 4  | 5  | 7  | 8 (30B)       | 8 (30AB)   | 9 (30D)            |
| 4  | 3  | 6  | 8  | 8  | 14 (30A+30B)  | 14 (60AB)  | 17 (30ABC+30D)     |
| 6  | 5  | 7  | 9  | 17 | 16 (60A+30B)  | 16 (90AB)  | 23 (60ABC+30D)     |
| 8  | 10 | 15 | 14 | 27 | 18 (90A+30B)  | 18 (120AB) | 25 (90ABC+30D)     |
| 10 | 20 | 30 | 18 | 29 | 20 (120A+30B) | 20 (150AB) | **28 (60ABC+90D)** |

<span style="color:#992667;">Ответ: вариант распределения, при котором прибыль от инвестиций будет максимальной, в нашем случае равна **28**, где 30A+30B+90D.
💕💞🅱️🅱️