Про выполнение команд

  

- Shift + Enter - выполнить код в ячейке и перейти на следующую

- Ctrl + Enter - выполнить и остаться

  

Про создание/улание ячеек

- b - создать ячейку снизу

- a - создать ячейку сверху

- двойное нажатие d - удалить ячейку

  
  

```python

# длинные переменные и названия функций в питоне записывают через snake_case

  

snake_case_integer = 5

```

  

## Коллекции

  

### Работа с листами

  
  

```python

just_numbers = [4, 1, 13, 0, 6]

```

  
  

```python

sum(just_numbers)

```

  
  
  
  

24

  
  
  
  

```python

sorted(just_numbers)

```

  
  
  
  

[0, 1, 4, 6, 13]

  
  
  
  

```python

just_numbers + [1, 2, 3]

```

  
  
  
  

[4, 1, 13, 0, 6, 1, 2, 3]

  
  
  
  

```python

min(just_numbers)

```

  
  
  
  

0

  
  
  
  

```python

max(just_numbers)

```

  
  
  
  

13

  
  
  
  

```python

for idx,x in enumerate(just_numbers):

print(idx, x)

```

  

0 4

1 1

2 13

3 0

4 6

  
  
  

```python

list(zip([1, 2, 3], [4, 5, 6]))

```

  
  
  
  

[(1, 4), (2, 5), (3, 6)]

  
  
  

### Пару слов про модель памяти

  
  

```python

just_numbers

```

  
  
  
  

[4, 1, 13, 0, 6]

  
  
  
  

```python

new_arr = just_numbers

new_arr

```

  
  
  
  

[4, 1, 13, 0, 6]

  
  
  
  

```python

new_arr.append(42)

print(new_arr)

print(just_numbers)

```

  
  
  
  

[4, 1, 13, 0, 6, 42, 42]

  
  
  
  

```python

from copy import copy

  

just_numbers = [4, 1, 13, 0, 6]

new_arr = copy(just_numbers)

new_arr.append(42)

print(new_arr)

print(just_numbers)

```

  

[4, 1, 13, 0, 6, 42]

[4, 1, 13, 0, 6]

  
  
  

```python

from copy import copy

  

matrix = [[4, 1], [13, 0]]

new_matrix = copy(matrix)

new_matrix[0].append(42)

print(new_matrix)

print(matrix)

```

  

[[4, 1, 42], [13, 0]]

[[4, 1, 42], [13, 0]]

  
  
  

```python

from copy import deepcopy

  

matrix = [[4, 1], [13, 0]]

new_matrix = deepcopy(matrix)

new_matrix[0].append(42)

print(new_matrix)

print(matrix)

```

  

[[4, 1, 42], [13, 0]]

[[4, 1], [13, 0]]

  
  

### Срезы

  
  

```python

just_numbers

```

  
  
  
  

[4, 1, 13, 0, 6]

  
  
  
  

```python

just_numbers[1:3]

```

  
  
  
  

[1, 13]

  
  
  
  

```python

just_numbers[-1]

```

  
  
  
  

6

  
  
  
  

```python

# Третий с конца

just_numbers[-3]

```

  
  
  
  

13

  
  
  
  

```python

# Все эоементы наченая со второго

just_numbers[1:]

```

  
  
  
  

[1, 13, 0, 6]

  
  
  
  

```python

# Тривиальный срез

just_numbers[:]

```

  
  
  
  

[4, 1, 13, 0, 6]

  
  
  
  

```python

# Каждый второй

just_numbers[::2]

```

  
  
  
  

[4, 13, 6]

  
  
  
  

```python

# задом наперед

just_numbers[::-1]

```

  
  
  
  

[6, 0, 13, 1, 4]

  
  
  

### List comprehension

  
  

```python

just_numbers = [4, 1, 13, 0, 6]

[x + 1 for x in just_numbers]

```

  
  
  
  

[5, 2, 14, 1, 7]

  
  
  
  

```python

[x for x in just_numbers if x < 10]

```

  
  
  
  

[4, 1, 0, 6]

  
  
  

### Кортежи

  
  

```python

tup = (1, 2, 3)

tup

```

  
  
  
  

(1, 2, 3)

  
  
  
  

```python

def get_min_max(arr):

return min(arr), max(arr)

  

min_, max_ = get_min_max(just_numbers)

print(min_)

print(max_)

```

  

0

13

  
  
  

```python

#Поменять переменные местами

a = -5

b = 100

  

a, b = b, a

  

print(f"a={a} b={b}")

```

  

a=100 b=-5

  
  

### Множества

  
  

```python

arr = [1, 1, 2, 3, 4]

```

  
  

```python

s = set(arr)

s

```

  
  
  
  

{1, 2, 3, 4}

  
  
  
  

```python

# Грязный способ выкинуть все повторки из массива

list(set(arr))

```

  
  
  
  

[1, 2, 3, 4]

  
  
  
  

```python

if 3 in s:

print("yes")

else:

print("no")

```

  

yes

  
  
  

```python

{x + 1 for x in arr}

```

  
  
  
  

{2, 3, 4, 5}

  
  
  
  

```python

s1 = {1, 2, 3}

s2 = {1, 3, 6}

```

  
  

```python

s1.intersection(s2)

```

  
  
  
  

{1, 3}

  
  
  
  

```python

s1.union(s2)

```

  
  
  
  

{1, 2, 3, 6}

  
  
  

### Словарь

  
  

```python

person = {

"first_name": "Иван",

"last_name": "Иванов",

"age": 23,

"profession":"Data Scientist",

}

```

  
  

```python

days = {

'2023-08-20': 'Sunday',

'2023-08-21': 'Monday',

'2023-08-22': 'Tuesday',

}

```

  
  

```python

days['2023-08-20']

```

  
  
  
  

'Sunday'

  
  
  
  

```python

days['no_such_day']

```

  
  

---------------------------------------------------------------------------

  

KeyError Traceback (most recent call last)

  

Cell In[36], line 1

----> 1 days['no_such_day']

  
  

KeyError: 'no_such_day'

  
  
  

```python

print(days.get('no_such_day'))

```

  

None

  
  
  

```python

print(days.get('no_such_day', 'unknown'))

```

  

unknown

  
  
  

```python

for v in days.keys():

print(v)

```

  

2023-08-20

2023-08-21

2023-08-22

  
  
  

```python

for v in days.values():

print(v)

```

  

Sunday

Monday

Tuesday

  
  
  

```python

for k,v in days.items():

print(k, v)

```

  

2023-08-20 Sunday

2023-08-21 Monday

2023-08-22 Tuesday

  
  
  

```python

person_employed = {

"first_name": "Иван",

"last_name": "Иванов",

"age": 23,

"profession":"Data Scientist",

"company": {

"name": "ООО ДатаСаенс",

"address": "ул. Пушкина, дом Колотушкина"

}

}

```

  
  

```python

person_employed["company"]["name"]

```

  
  
  
  

'ООО ДатаСаенс'

  
  
  
  

```python

person["company"]["name"]

```

  
  

---------------------------------------------------------------------------

  

KeyError Traceback (most recent call last)

  

Cell In[51], line 1

----> 1 person["company"]["name"]

  
  

KeyError: 'company'

  
  
  

```python

print(person.get("company", {}).get("name"))

```

  

None

  
  
  

```python

{str(i)x: i for i in range(5)}

```

  
  
  
  

{'0': 0, '1': 1, '2': 2, '3': 3, '4': 4}

  
  
  

## Функции

  
  

```python

# Возвращает квадрат числа num

def square(num):

return num**2

```

  
  

```python

square(3)

```

  
  
  
  

9

  
  
  
  

```python

square(num=3)

```

  
  
  
  

9

  
  
  
  

```python

def sub(a, b):

return a - b

```

  
  

```python

sub(10, 5)

```

  
  
  
  

5

  
  
  
  

```python

sub(b=5, a=10)

```

  
  
  
  

5

  
  
  
  

```python

def split_words(s, sep=" "):

return s.split(sep)

  

print(split_words("one two three"))

print(split_words("one_two_three", sep="_"))

```

  

['one', 'two', 'three']

['one', 'two', 'three']

  
  
  

```python

def many_args(*args):

print(args)

many_args(1, 2, "zuzuka", list())

```

  

(1, 2, 'zuzuka', [])

1

2

zuzuka

[]

  
  
  

```python

def many_named_args(**kwargs):

print(kwargs)

many_named_args(a=1, b=2, name="zuzuka", arr=list())

```

  

{'a': 1, 'b': 2, 'name': 'zuzuka', 'arr': []}

  
  

### lambda-функции + map, filter

  
  

```python

just_numbers = [4, 1, 13, 0, 6]

```

  
  

```python

def is_above_zero(x):

return x > 0

  

list(filter(is_above_zero, just_numbers))

```

  
  
  
  

[4, 1, 13, 6]

  
  
  
  

```python

list(filter(lambda x: x > 0, just_numbers))

```

  
  
  
  

[4, 1, 13, 6]

  
  
  
  

```python

list(map(lambda x: x - 1, just_numbers))

```

  
  
  
  

[3, 0, 12, -1, 5]

  
  
  
  

```python

"yes" if 1 > 2 else "no"

```

  
  
  
  

'no'

  
  
  
  

```python

list(map(lambda x: "yes" if x < 10 else "no", just_numbers))

```

  
  
  
  

['yes', 'yes', 'no', 'yes', 'yes']

  
  
  

## Регулярные выражения

  
  

```python

import re

  

pattern = re.compile('[0-9]{4}')

```

  
  

```python

pattern.fullmatch("1245")

```

  
  
  
  

<re.Match object; span=(0, 4), match='1245'>

  
  
  
  

```python

pattern.fullmatch("1245")

```

  
  

```python

arr = ["1245", "3456", "aabb", "1ab4", ""]

list(filter(pattern.fullmatch, arr))

```

  
  
  
  

['1245', '3456']

  
  
  
  

```python

pattern.findall("1245 6789 aabb")

```

  
  
  
  

['1245', '6789']

  
  
  

## Работа с датами

  
  

```python

from datetime import datetime, timedelta

  

startDate = '2017-05-01'

some_date = datetime.strptime(startDate, '%Y-%m-%d')

some_date

```

  
  
  
  

datetime.datetime(2017, 5, 1, 0, 0)

  
  
  
  

```python

some_date.day

```

  
  
  
  

1

  
  
  
  

```python

some_date.strftime('%Y.%m.%d %H:%M')

```

  
  
  
  

'2017.05.01 00:00'

  
  
  
  

```python

some_date + timedelta(days = 1)

```

  
  
  
  

datetime.datetime(2017, 5, 2, 0, 0)

  
  
  

## Try-except

  
  

```python

1 / 0

```

  
  

---------------------------------------------------------------------------

  

ZeroDivisionError Traceback (most recent call last)

  

Cell In[104], line 1

----> 1 1 / 0

  
  

ZeroDivisionError: division by zero

  
  
  

```python

try:

1 / 0

except ZeroDivisionError:

print("cannot devide by zero")

```

  

cannot devide by zero

  
  
  

```python

open("no_such_file.txt")

```

  
  

---------------------------------------------------------------------------

  

FileNotFoundError Traceback (most recent call last)

  

Cell In[106], line 1

----> 1 open("no_such_file.txt")

  
  

File /opt/homebrew/lib/python3.11/site-packages/IPython/core/interactiveshell.py:282, in _modified_open(file, *args, **kwargs)

275 if file in {0, 1, 2}:

276 raise ValueError(

277 f"IPython won't let you open fd={file} by default "

278 "as it is likely to crash IPython. If you know what you are doing, "

279 "you can use builtins' open."

280 )

--> 282 return io_open(file, *args, **kwargs)

  
  

FileNotFoundError: [Errno 2] No such file or directory: 'no_such_file.txt'

  
  
  

```python

try:

open("no_such_file.txt")

except BaseException as e:

print("error:", e)

```

  

error: [Errno 2] No such file or directory: 'no_such_file.txt'

  
  

## ООП

  
  

```python

class MyModel:

def __init__(self, threshold):

self.threshold = threshold

def apply(self, value):

return value > self.threshold

model = MyModel(0.5)

print(model.apply(0.1))

print(model.apply(0.9))

```

  

False

True