### All ca$h Team:
| $   | A  | B  | C  | D  | E  | F  |
|-----|----|----|----|----|----|----|
| 100 | 3  | 5  | 4  | 7  | 1  | 2  |
| 200 | 7  | 10 | 8  | 9  | 8  | 6  |
| 300 | 9  | 12 | 14 | 10 | 9  | 8  |
| 400 | 13 | 15 | 16 | 14 | 11 | 17 |
| 500 | 16 | 18 | 19 | 15 | 15 | 21 |

### Решение для A и B

| $   | A  | B  | AB              |                
|-----|----|----|-----------------|            
| 100 | 3  | 5  | 5(100 B)        | 
| 200 | 7  | 10 | 10(200 B)       | 
| 300 | 9  | 12 | 12(100A +200B)  | 
| 400 | 13 | 15 | 17(200A + 200B) |
| 500 | 16 | 18 | 19(200A+300B)   |      
### 100

| A   | B   | Выгода |
|-----|-----|--------|
| 0   | 100 | 5      |
| 100 | 0   | 3      |
### 200

| A   | B   | Выгода |
|-----|-----|--------|
| 0   | 200 | 10     |
| 100 | 100 | 8      |
| 200 | 0   | 7      |

### 300

| A   | B   | Выгода |
|-----|-----|--------|
| 0   | 300 | 12     |
| 100 | 200 | 13     |
| 200 | 100 | 12     |
| 300 | 0   | 9      |

### 400

| A   | B   | Выгода |
|-----|-----|--------|
| 0   | 400 | 15     |
| 100 | 300 | 15     |
| 200 | 200 | 17     |
| 300 | 100 | 14     |
| 400 | 0   | 13     |

### 500

| A   | B   | Выгода |
|-----|-----|--------|
| 0   | 500 | 18     |
| 100 | 400 | 18     |
| 200 | 300 | 19     |
| 300 | 200 | 19     |
| 400 | 100 | 18     |
| 500 | 0   | 16     |

### Решение для AB и С

| $   | AB | C  | ABC            |
|-----|----|----|----------------|
| 100 | 5  | 4  | 5(100AB)       |
| 200 | 10 | 8  | 10(200AB)      | 
| 300 | 12 | 14 | 14(300C)       |
| 400 | 17 | 16 | 19(300C+100AB) | 
| 500 | 19 | 19 | 24(200AB+300C) | 

### 100

| AB  | C   | Выгода |
|-----|-----|--------|
| 0   | 100 | 4      |
| 100 | 0   | 5      |

### 200

| AB  | C   | Выгода |
|-----|-----|--------|
| 0   | 200 | 8      |
| 100 | 100 | 9      |
| 200 | 0   | 10     |

### 300

| AB  | C   | Выгода |
|-----|-----|--------|
| 0   | 300 | 14     |
| 100 | 200 | 13     |
| 200 | 100 | 14     |
| 300 | 0   | 12     |

### 400

| AB  | C   | Выгода |
|-----|-----|--------|
| 0   | 400 | 16     |
| 100 | 300 | 19     |
| 200 | 200 | 18     |
| 300 | 100 | 16     |
| 400 | 0   | 17     |

### 500

| AB  | C   | Выгода |
|-----|-----|--------|
| 0   | 500 | 19     |
| 100 | 400 | 21     |
| 200 | 300 | 24     |
| 300 | 200 | 20     |
| 400 | 100 | 21     |
| 500 | 0   | 19     |

### Решение для ABC и D
| $   | ABC | D  | ABCD             |
|-----|-----|----|------------------|
| 100 | 5   | 7  | 7(100D)          |
| 200 | 10  | 9  | 11(100ABC+100D)  | 
| 300 | 14  | 10 | 17(200ABC+ 100D) | 
| 400 | 19  | 14 | 21(300ABC+100D)  | 
| 500 | 24  | 15 | 26(400ABC+100D)  |

### 100
| ABC | D   | Выгода |
|-----|-----|--------|
| 0   | 100 | 7      |
| 100 | 0   | 5      |

### 200

| ABC | D   | Выгода |
|-----|-----|--------|
| 0   | 200 | 9      |
| 100 | 100 | 11     |
| 200 | 0   | 10     |

### 300

| ABC | D   | Выгода |
|-----|-----|--------|
| 0   | 300 | 10     |
| 100 | 200 | 14     |
| 200 | 100 | 17     |
| 300 | 0   | 14     |

### 400

| ABC | D   | Выгода |
|-----|-----|--------|
| 0   | 400 | 14     |
| 100 | 300 | 15     |
| 200 | 200 | 19     |
| 300 | 100 | 21     |
| 400 | 0   | 17     |

### 500

| ABC | D   | Выгода |
|-----|-----|--------|
| 0   | 500 | 15     |
| 100 | 400 | 19     |
| 200 | 300 | 20     |
| 300 | 200 | 23     |
| 400 | 100 | 26     |
| 500 | 0   | 24     |


### Решение для ABCD и E
| $   | ABCD | E  | ABCDE       |
|-----|------|----|-------------|
| 100 | 7    | 1  | 7(100ABCD)  |
| 200 | 11   | 8  | 11(200ABCD) | 
| 300 | 17   | 9  | 17(300ABCD) | 
| 400 | 21   | 11 | 21(400ABCD) | 
| 500 | 26   | 15 | 26(500ABCD) |

### 100
| ABCD | E   | Выгода |
|------|-----|--------|
| 0    | 100 | 1      |
| 100  | 0   | 7      |

### 200

| ABCD | E   | Выгода |
|------|-----|--------|
| 0    | 200 | 8      |
| 100  | 100 | 8      |
| 200  | 0   | 11     |

### 300

| ABCD | E   | Выгода |
|------|-----|--------|
| 0    | 300 | 9      |
| 100  | 200 | 15     |
| 200  | 100 | 12     |
| 300  | 0   | 17     |

### 400

| ABCD | E   | Выгода |
|------|-----|--------|
| 0    | 400 | 11     |
| 100  | 300 | 16     |
| 200  | 200 | 19     |
| 300  | 100 | 18     |
| 400  | 0   | 21     |

### 500

| ABCD | E   | Выгода |
|------|-----|--------|
| 0    | 500 | 15     |
| 100  | 400 | 18     |
| 200  | 300 | 20     |
| 300  | 200 | 25     |
| 400  | 100 | 22     |
| 500  | 0   | 26     |

### Решение для ABCDE и F
| $   | ABCDE | F  | ABCDEF       |
|-----|-------|----|--------------|
| 100 | 7     | 2  | 7(100ABCDE)  |
| 200 | 11    | 6  | 11(200ABCDE) | 
| 300 | 17    | 8  | 17(300ABCDE) | 
| 400 | 21    | 17 | 21(400ABCDE) | 
| 500 | 26    | 21 | 26(500ABCDE) |

### 100
| ABCDE | F   | Выгода |
|-------|-----|--------|
| 0     | 100 | 2      |
| 100   | 0   | 7      |

### 200

| ABCDE | F   | Выгода |
|-------|-----|--------|
| 0     | 200 | 6      |
| 100   | 100 | 9      |
| 200   | 0   | 11     |

### 300

| ABCDE | F   | Выгода |
|-------|-----|--------|
| 0     | 300 | 8      |
| 100   | 200 | 13     |
| 200   | 100 | 13     |
| 300   | 0   | 17     |

### 400

| ABCDE | F   | Выгода |
|-------|-----|--------|
| 0     | 400 | 17     |
| 100   | 300 | 15     |
| 200   | 200 | 17     |
| 300   | 100 | 19     |
| 400   | 0   | 21     |

### 500

| ABCDE | F   | Выгода |
|-------|-----|--------|
| 0     | 500 | 21     |
| 100   | 400 | 24     |
| 200   | 300 | 19     |
| 300   | 200 | 23     |
| 400   | 100 | 23     |
| 500   | 0   | 26     |
### Ответ
Самая большая выгода получилась 26 - 500(ABCDEF) т.к. проекты E и F никак не повлияли на выгоду,
то можно считать, что наш ответ это 500(ABCD), а точнее 100D + 300C+ 100B