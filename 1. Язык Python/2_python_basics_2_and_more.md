# Jupyter Notebook vs JupyterLab?

Jupyter Notebook — это интерактивная веб-среда для создания документов блокнотов Jupyter. Он поддерживает несколько языков, таких как Python (IPython), Julia, R и т. д., и широко используется для анализа данных, визуализации данных и дальнейших интерактивных исследовательских вычислений.

JupyterLab — это пользовательский интерфейс нового поколения, включая блокноты. Он имеет модульную структуру, благодаря которой вы можете открывать несколько блокнотов или файлов (например, HTML, текст, уценки и т. д.) в виде вкладок в одном окне. Он предлагает больше возможностей, подобных IDE.

## Расширения Jupiter Notebook

A collection of various notebook extensions for Jupyter:
https://github.com/ipython-contrib/jupyter_contrib_nbextensions

Docs: https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/


```shell
pip install jupyter_contrib_nbextensions && jupyter contrib nbextension install
```

Как это должно выглядеть:

![[_resources/2_python_basics_2_and_more_internal/Screenshot 2023-11-03 at 15.48.38.png]]

## Расширения Jupiter Lab

Нужно посмотреть самим и выбрать то что понравится)

https://jupyterlab.readthedocs.io/en/stable/user/extensions.html
https://jupyterlab-contrib.github.io/extensions.html

https://github.com/mauhai/awesome-jupyterlab
https://neptune.ai/blog/jupyterlab-extensions-for-machine-learning


```python
!pip install jupyter_contrib_nbextensions && jupyter contrib nbextension install
```

# Collections

[Collections](https://docs.python.org/3.6/library/collections.html#module-collections) — это встроенная библиотека Python для эффективной работы со словарем Python. В этом разделе будут показаны некоторые полезные методы этого модуля.

## [`Counter`](https://docs.python.org/3.11/library/collections.html#collections.Counter "collections.Counter") objects

Counter — это разновидность словаря Python, созданная для подсчёта, что понятно из названия. Ключами в ней выступают подсчитываемые элементы, а значениями — их количества.


```python
char_list = ["a", "b", "c", "a", "d", "b", "b"]
```


```python
def custom_counter(list_: list):
    char_counter = {}
    for char in list_:
        if char not in char_counter:
            char_counter[char] = 1
        else:
            char_counter[char] += 1

    return char_counter


custom_counter(char_list)
```




    {'a': 2, 'b': 3, 'c': 1, 'd': 1}




```python
from collections import Counter
```


```python
Counter(char_list)
```




    Counter({'a': 2, 'b': 3, 'c': 1, 'd': 1})




```python
c = Counter('абвабббаввабббвавабг')
c
```




    Counter({'а': 6, 'б': 8, 'в': 5, 'г': 1})




```python
Counter('зима зима зима по полгода ни звоночка ни письма'.split())
```




    Counter({'зима': 3,
             'по': 1,
             'полгода': 1,
             'ни': 2,
             'звоночка': 1,
             'письма': 1})




```python
sum(c.values())
```




    20



Типовые примеры использования Counter():

```python
sum(c.values())                 # сумма всех количеств
c.clear()                       # сброс всех количеств
list(c)                         # список элементов
set(c)                          # преобразование во множество
dict(c)                         # преобразование в обычный словарь 
c.items()                       # преобразование в список кортежей (элемент, количество)
Counter(dict(list_of_pairs))    # обратное преобразование из списка кортежей вида (элемент, количество)
c.most_common()[:-n-1:-1]       # n самых редких элементов
c += Counter()                  # удаление элементов с отрицательными и нулевыми количествами
```

## [`namedtuple()`](https://docs.python.org/3.11/library/collections.html#collections.namedtuple "collections.namedtuple")

Кортеж (tuple, его часто называют «неизменяемым списком») в Python содержит некоторое количество элементов, к каждому из которых можно обратиться только по его индексу.

namedtuple это расширение над встроенными кортежами, которое даёт имя каждому элементу кортежа, а точнее — создаёт именованные поля, в которые мы, как в строку в таблице, складываем значения.

В итоге получаем что-то вроде неизменяемого (immutable) словаря, только гораздо легче читаемого.


```python
simple_tuple = (1, 'a', 123.4)
simple_tuple[1]
```




    'a'




```python
from collections import namedtuple
```


```python
fruit = namedtuple('fruit','number sort color')
apple = fruit(number=5, sort='Antonovka', color='red')
orange = fruit(number=7, sort='Navel Late', color='yellow')
```


```python
apple.sort, orange.color, apple[2]
```




    ('Antonovka', 'yellow', 'red')



## [`defaultdict`](https://docs.python.org/3.11/library/collections.html#collections.defaultdict "collections.defaultdict") objects

Безошибочный словарь


```python
my_dict = {'a':1, 'b':2, 'c':3}
my_dict['a']
```




    1




```python
my_dict['d']
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Cell In[43], line 1
    ----> 1 my_dict['d']


    KeyError: 'd'



```python
from collections import defaultdict
```


```python
my_new_dict = defaultdict(int, my_dict)
my_new_dict
```




    defaultdict(int, {'a': 1, 'b': 2, 'c': 3})




```python
my_new_dict['d']
```




    0




```python
my_new_dict
```




    defaultdict(int, {'a': 1, 'b': 2, 'c': 3, 'd': 0})



При создании словаря типа defaultdict можно писать любые стандартные типы данных: int, float, list, str — и даже другие словари dict


```python
my_new_dict_2 = defaultdict(dict, my_dict)
my_new_dict_2
```




    defaultdict(dict, {'a': 1, 'b': 2, 'c': 3})




```python
my_new_dict_2['f']
```




    {}




```python
my_new_dict_2
```




    defaultdict(dict, {'a': 1, 'b': 2, 'c': 3, 'f': {}})




```python
my_new_dict_2.items()
```




    dict_items([('a', 1), ('b', 2), ('c', 3), ('f', {})])




```python
my_new_dict_2.keys()
```




    dict_keys(['a', 'b', 'c', 'f'])



## [`OrderedDict`](https://docs.python.org/3.11/library/collections.html#collections.OrderedDict "collections.OrderedDict") objects


```python
unordered1 = {'a': 1, 'b': 2, 'c': 3}
unordered2 = {'b': 2, 'a': 1, 'c': 3}
unordered1 == unordered2
```




    True




```python
from collections import OrderedDict
```


```python
ordered1 = OrderedDict({'a': 1, 'b': 2, 'c': 3})
ordered2 = OrderedDict({'b': 2, 'a': 1, 'c': 3})
ordered1 == ordered2
```




    False




```python
d = OrderedDict.fromkeys('abcde')
d
```




    OrderedDict([('a', None), ('b', None), ('c', None), ('d', None), ('e', None)])



Так как OrderedDict это упорядоченная последовательность, объекты содержат соответствующие методы, реорганизующие структуру:

- popitem(last=True) – удаляет последний элемент если last=True, и первый, если last=False

- move_to_end(key, last=True) – переносит ключ key в конец, если last=True, и в начало, если last=False


```python
d.move_to_end('b')
''.join(d.keys())
```




    'acdeb'




```python
d.move_to_end('b', last=False)
''.join(d.keys())
```




    'bacde'



## [`ChainMap`](https://docs.python.org/3.11/library/collections.html#collections.ChainMap "collections.ChainMap") objects

ChainMap позволяет организовывать и получать ключи или значения из разных словарей.


```python
from collections import ChainMap
```


```python
fruits = {'apple': 2, 'tomato': 1}
veggies = {'carrot': 3, 'tomato': 1}
food = ChainMap(fruits, veggies) 
```


```python
food
```




    ChainMap({'apple': 2, 'tomato': 1}, {'carrot': 3, 'tomato': 1})




```python
food.keys()
```




    KeysView(ChainMap({'apple': 2, 'tomato': 1}, {'carrot': 3, 'tomato': 1}))




```python
food.items()
```




    ItemsView(ChainMap({'apple': 2, 'tomato': 1}, {'carrot': 3, 'tomato': 1}))




```python
food.get('apple'), food.get("tomato")
```




    (2, 1)



## [`deque`](https://docs.python.org/3.11/library/collections.html#collections.deque "collections.deque") objects

Объект типа deque (двусторонняя или двусвязная очередь) является усовершенствованным вариантом списка с оптимизированной вставкой/удалением элементов с обоих концов. 

Реализация deque оптимизирована так, что операции слева и справа имеют примерно одинаковую производительность O(1). 

Добавление новых элементов в конец происходит не сильно медленнее, чем во встроенных списках, но добавление в начало выполняется существенно быстрее.


```python
from collections import deque
```


```python
seq = list("bcd")
deq = deque(seq)
deq
```




    deque(['b', 'c', 'd'])




```python
deq.append('e')
```


```python
deq.appendleft('a')
```


```python
deq
```




    deque(['a', 'b', 'c', 'd', 'e'])




```python
deq.pop()
```




    'e'




```python
deq.popleft()
```




    'a'




```python
deq
```




    deque(['b', 'c', 'd'])



Если нужно посчитать число вхождений элемента в последовательность, применяем метод count():


```python
deq.count('b'), deq.count('a')
```




    (1, 0)



Кроме перечисленных, доступны следующие методы:

- remove(value) – удаление первого вхождения value
- reverse() – разворачивает очередь)
- rotate(n=1) – последовательно переносит n элементов из начала в конец (если n отрицательно, то с конца в начало). В этом поведение deque напоминает кольцевой связный список

Очередь deque имеет аргумент maxlen, позволяющий ограничить ее размер. При заполнении ограниченной очереди добавление n новых объектов «слева» вызовет удаление n элементов справа.

# Intermediate functions in Python

## Describe functions


```python
def multiply(*nums: int) -> int:
    print(f"nums: {nums}")
    res = 1
    for num in nums:
        res *= num
    return res
```


```python
multiply(1, 2, 3)
```

    nums: (1, 2, 3)





    6




```python
multiply()
```

    nums: ()





    1




```python
def foo(i : int = 0) -> int:
    print(i)
    return i

foo()
```

    0





    0



## Decorators

Если вы хотите применить одну и ту же часть функциональности к нескольким функциям, сохраняя при этом чистоту кода, используйте декоратор. Декоратор изменяет поведение ваших функций Python, не изменяя код напрямую.


```python
import time
```


```python
def time_func(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f'Elapsed time: {(end - start) * 1000:.3f}ms')
    return wrapper
```


```python
@time_func
def add(num1: int, num2: int):
    print(f"Add {num1} and {num2}")
    return num1 + num2

@time_func
def multiply(num1: int, num2: int):
    print(f"Multiply {num1} and {num2}")
    return num1 * num2
```


```python
add(1, 2)
multiply(1, 2)
```

    Add 1 and 2
    Elapsed time: 0.026ms
    Multiply 1 and 2
    Elapsed time: 0.008ms


# Itertools

![](https://khuyentran1401.github.io/Efficient_Python_tricks_and_tools_for_data_scientists/_images/itertools.png)

[itertools](https://docs.python.org/3/library/itertools.html) — это встроенная библиотека Python, которая создает итераторы для эффективного выполнения циклов. В этом разделе будут показаны некоторые полезные методы itertools.

## itertools.combinations


```python
num_list = [1, 2, 3]
```


```python
(1, 2)
(1, 3)
(2, 3)
```




    (2, 3)




```python
for i in num_list:
    for j in num_list:
        if i < j:
            print((i, j))
```

    (1, 2)
    (1, 3)
    (2, 3)



```python
from itertools import combinations

comb = combinations(num_list, 2)  # use this
for pair in list(comb):
    print(pair)
```

    (1, 2)
    (1, 3)
    (2, 3)


## itertools.product: Nested For-Loops in a Generator Expression 


```python
params = {
    "learning_rate": [1e-1, 1e-2, 1e-3],
    "batch_size": [16, 32, 64],
}
for learning_rate in params["learning_rate"]:
    for batch_size in params["batch_size"]:
        combination = (learning_rate, batch_size)
        print(combination)

```

    (0.1, 16)
    (0.1, 32)
    (0.1, 64)
    (0.01, 16)
    (0.01, 32)
    (0.01, 64)
    (0.001, 16)
    (0.001, 32)
    (0.001, 64)


`itertools.product` более эффективно, потому что `product(A, B)` == `((x,y) for x in A for y in B)`.


```python
from itertools import product

params = {
    "learning_rate": [1e-1, 1e-2, 1e-3],
    "batch_size": [16, 32, 64],
}

for combination in product(*params.values()):
    print(combination)
```

    (0.1, 16)
    (0.1, 32)
    (0.1, 64)
    (0.01, 16)
    (0.01, 32)
    (0.01, 64)
    (0.001, 16)
    (0.001, 32)
    (0.001, 64)


## itertools.starmap: Apply a Function With More Than 2 Arguments to Elements in a List

`map` это полезный метод, который позволяет вам применить функцию к элементам в списке. Однако он не может применить функцию с более чем одним аргументом к списку.


```python
def multiply(x: float, y: float):
    return x * y
```


```python
nums = [(1, 2), (4, 2), (2, 5)]
list(map(multiply, nums))
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[109], line 2
          1 nums = [(1, 2), (4, 2), (2, 5)]
    ----> 2 list(map(multiply, nums))


    TypeError: multiply() missing 1 required positional argument: 'y'


Чтобы применить функцию с более чем 2 аргументами к элементам списка, используйте `itertools.starmap`. С помощью `starmap` элементы в каждом кортеже списка `nums` используются в качестве аргументов для функции `multiply`.


```python
from itertools import starmap

list(starmap(multiply, nums))
```




    [2, 8, 10]



## itertools.compress: Filter a List Using Booleans


```python
fruits = ["apple", "orange", "banana", "grape", "lemon"]
chosen = [1, 0, 0, 1, 1]
fruits[chosen]
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[111], line 3
          1 fruits = ["apple", "orange", "banana", "grape", "lemon"]
          2 chosen = [1, 0, 0, 1, 1]
    ----> 3 fruits[chosen]


    TypeError: list indices must be integers or slices, not list



```python
from itertools import compress

list(compress(fruits, chosen))
```




    ['apple', 'grape', 'lemon']



## itertools.groupby: Group Elements in an Iterable by a Key

Если вы хотите сгруппировать элементы в списке по ключу, используйте `itertools.groupby`. В приведенном ниже примере я сгруппировал элементы в списке по первому элементу в каждом кортеже.


```python
from itertools import groupby

prices = [("apple", 3), ("orange", 2), ("apple", 4), ("orange", 1), ("grape", 3)]

key_func = lambda x: x[0]

# Sort the elements in the list by the key
prices.sort(key=key_func)

# Group elements in the list by the key
for key, group in groupby(prices, key_func):
    print(key, ":", list(group))
```

    apple : [('apple', 3), ('apple', 4)]
    grape : [('grape', 3)]
    orange : [('orange', 2), ('orange', 1)]


## itertools.zip_longest: Zip Iterables of Different Lengths

`zip` allows you to aggregate elements from each of the iterables. However, `zip` doesn't show all pairs of elements when iterables have different lengths. 


```python
fruits = ["apple", "orange", "grape"]
prices = [1, 2]
```


```python
list(zip(fruits, prices))
```




    [('apple', 1), ('orange', 2)]



Чтобы агрегировать повторяющиеся объекты разной длины, используйте `itertools.zip_longest`. Этот метод заполнит недостающие значения с помощью `fillvalue`.


```python
from itertools import zip_longest
```


```python
list(zip_longest(fruits, prices, fillvalue="-"))
```




    [('apple', 1), ('orange', 2), ('grape', '-')]



## itertools.dropwhile: Drop Elements in an Iterable Until a Condition Is False

Если вы хотите удалять элементы из iterable до тех пор, пока условие не станет ложным, используйте `itertools.dropwhile`.


```python
from itertools import dropwhile

nums = [1, 2, 5, 2, 4]

# Drop every number until a number >= 5
list(dropwhile(lambda n: n < 5, nums))
```




    [5, 2, 4]




```python
word = 'abcNice!'

# Drop every char until a char is in upper case
chars  = dropwhile(lambda char: char.islower(), word)
''.join(chars)
```




    'Nice!'



# Operator

[operator](https://docs.python.org/3/library/operator.html) - это встроенная библиотека Python, которая экспортирует набор эффективных функций, соответствующих встроенным операторам Python. В этом разделе мы покажем вам некоторые полезные методы этого модуля.

## operator.itemgetter: Get Multiple Items From a List or Dictionary


```python
fruits = ["apple", "orange", "banana", "grape"]

[fruit for fruit in fruits if fruits.index(fruit) in [1, 3]]
```




    ['orange', 'grape']




```python
from operator import itemgetter

itemgetter(1, 3)(fruits)
```




    ('orange', 'grape')



# Functools

[functools](https://docs.python.org/3/library/functools.html) это встроенная библиотека Python для эффективной работы с функциями.

## functools.partial: Generate a New Function with Fewer Arguments

Если вы хотите исправить некоторые аргументы функции и сгенерировать новую функцию с меньшим количеством аргументов, используйте `functools.partial`.

В приведенном ниже коде я использую `partial` для создания новой функции только с `x` в качестве аргумента.


```python
from functools import partial
```


```python
def linear_func(x, a, b):
    return a * x + b
```


```python
linear_func_partial = partial(linear_func, a=2, b=3)
print(linear_func_partial(2))
print(linear_func_partial(4))
```

    7
    11


# Pydash

[Pydash](https://pydash.readthedocs.io/en/latest/)


```python
!pip install pydash 
```

    Collecting pydash
      Obtaining dependency information for pydash from https://files.pythonhosted.org/packages/1b/8c/b0b1c3ed6eff8ef50e396084a0d0d8e82eeae44027c18cff9aef705f8eb0/pydash-7.0.6-py3-none-any.whl.metadata
      Downloading pydash-7.0.6-py3-none-any.whl.metadata (45 kB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m45.5/45.5 kB[0m [31m997.0 kB/s[0m eta [36m0:00:00[0m
    [?25hRequirement already satisfied: typing-extensions!=4.6.0,>=3.10 in /Users/dromakin/anaconda3/lib/python3.11/site-packages (from pydash) (4.7.1)
    Downloading pydash-7.0.6-py3-none-any.whl (110 kB)
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m110.1/110.1 kB[0m [31m2.3 MB/s[0m eta [36m0:00:00[0ma [36m0:00:01[0m
    [?25hInstalling collected packages: pydash
    Successfully installed pydash-7.0.6


## Work with List

### pydash.flatten: Flatten a Nested Python List

If you want to flatten a nested Python list, use the `flatten` method:


```python
from pydash import py_

a = [[1, 2], [3, 4, 5]]
py_.flatten(a)
```




    [1, 2, 3, 4, 5]



###  pydash.flatten_deep: Flatten a Deeply Nested Python List

If your list is deeply nested, use `flatten_deep` instead:


```python
b = [[1, 2, [4, 5]], [6, 7]]
py_.flatten_deep(b)
```




    [1, 2, 4, 5, 6, 7]



### pydash.chunk: Split Elements into Groups


```python
a = [1, 2, 3, 4, 5]
py_.chunk(a, 2)
```




    [[1, 2], [3, 4], [5]]



## Work with Dictionary

### Omit Dictionary’s Attribute

Чтобы исключить атрибут из словаря, мы можем использовать метод omit:


```python
fruits = {"name": "apple", "color": "red", "taste": "sweet"}
py_.omit(fruits, "name")
```




    {'color': 'red', 'taste': 'sweet'}



### Get Nested Dictionary’s Attribute

Как получить значение Walmart?


```python
apple = {
    "price": {
        "in_season": {"store": {"Walmart": [2, 4], "Aldi": 1}},
        "out_of_season": {"store": {"Walmart": [3, 5], "Aldi": 2}},
    }
}
```

Normally:


```python
apple["price"]["in_season"]["store"]["Walmart"]
```




    [2, 4]



True Data Scientist:


```python
py_.get(apple, "price.in_season.store.Walmart")
```




    [2, 4]



Senior =)


```python
py_.get(apple, "price.in_season.store.Walmart[0]")
```




    2



## Work with List of Dictionaries

### Find Item Index Using a Function

`list.index(element)` позволяет вам получить индекс указанного элемента в списке. Однако вы не можете получить индекс с помощью функции.


```python
fruits = [
    {"name": "apple", "price": 2},
    {"name": "orange", "price": 2},
    {"name": "grapes", "price": 4},
]
```


```python
fruits.index({"name": "apple", "price": 2})
```




    0




```python
filter_fruits = lambda fruit: fruit["name"] == "apple"

fruits.index(filter_fruits)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[135], line 3
          1 filter_fruits = lambda fruit: fruit["name"] == "apple"
    ----> 3 fruits.index(filter_fruits)


    ValueError: <function <lambda> at 0x11c1add00> is not in list


Чтобы получить индекс элемента в списке с помощью функции, используйте вместо этого метод `find_index`:


```python
py_.find_index(fruits, filter_fruits)
```




    0



### Find Objects With Matching Style

Метод `find_index` позволяет вам получить индекс объекта, который соответствует определенному шаблону. Но что, если вы хотите получить элементы в списке вместо индекса?
Это можно было бы сделать с помощью метода `filter`:


```python
from pydash import py_
```


```python
fruits = [
    {"name": "apple", "price": 2},
    {"name": "orange", "price": 2},
    {"name": "grapes", "price": 4},
]
```


```python
py_.filter_(fruits, {"name": "apple"})
```




    [{'name': 'apple', 'price': 2}]



### Get Nested Object Value

Иногда ваш список словарей может быть вложенным, как показано ниже. Как вы можете узнать вторую цену каждого `яблока`?


```python
l = [
    {"apple": {"price": [0, 1], "color": "red"}},
    {"apple": {"price": [2, 3], "color": "green"}},
]
```

Вот тогда-то и пригодится метод `map_`.


```python
py_.map_(l, "apple.price[1]")
```




    [1, 3]



## Work with Functions

### Execute a Function n Times

Вы можете выполнить функцию n раз, используя метод `times`. Этот метод является хорошей альтернативой циклу for.


```python
py_.times(3, lambda: "I have just bought some apple")
```




    ['I have just bought some apple',
     'I have just bought some apple',
     'I have just bought some apple']




```python
py_.times(4, lambda i: f"I have just bought {i} apple")
```




    ['I have just bought 0 apple',
     'I have just bought 1 apple',
     'I have just bought 2 apple',
     'I have just bought 3 apple']



## Chaining

### Pydash’s Methods

Иногда вам может потребоваться применить несколько методов к объекту. Вместо того чтобы писать несколько строк кода, можете ли вы применить все методы сразу?

Вот когда пригодится цепочка методов. Чтобы применить цепочку методов к объекту, используйте метод "chain":


```python
fruits = ["apple", "orange", "grapes"]
```


```python
(py_.chain(fruits).without("grapes").reject(lambda fruit: fruit.startswith("a")))
```




    <pydash.chaining.chaining.Chain at 0x10f9e1310>



Обратите внимание, что выполнение приведенного выше кода не даст нам значения.

Только когда мы добавляем .value() в конец цепочки, вычисляется конечное значение:


```python
(
    py_.chain(fruits)
    .without("grapes")
    .reject(lambda fruit: fruit.startswith("a"))
    .value()
)
```




    ['orange']



Это называется [lazy evaluation](https://www.tutorialspoint.com/functional_programming/functional_programming_lazy_evaluation.htm). Отложенное вычисление удерживает вычисление выражения до тех пор, пока не потребуется его значение, что позволяет избежать повторного вычисления.

### Customized Methods

Если вы хотите использовать свои собственные методы вместо методов pydash, используйте метод `map`:


```python
def get_price(fruit):
    prices = {"apple": 2, "orange": 2, "grapes": 4}
    return prices[fruit]
```


```python
total_price = py_.chain(fruits).map(get_price).sum()
total_price.value()
```




    8



### Planting a Value

Чтобы заменить начальное значение цепочки другим значением, используйте метод `plant`:


```python
total_price.plant(["apple", "orange"]).value()
```




    4



Круто! Мы заменяем `['яблоко', 'апельсин', 'виноград']` на `['яблоко', 'апельсин']`, используя ту же цепочку!

# pathlib

pathlib - это библиотека Python, которая упрощает обработку файлов на Python.

## Create a New Directory and File

Вы можете использовать либо os, либо pathlib для создания новых каталогов и файлов в Python. pathlib - мой выбор, потому что он проще в использовании и понятен.


```python
import os

# Create a new directory
if not os.path.exists("new"):
    os.makedirs("new")

# Create a new file inside new directory
file = os.path.join("new", "new_file.txt")

# Write text to the file
with open(file, "w") as f:
    f.write("Hello World!")

# Read the file
with open(file, "r") as f:
    print(f.read())

```

    Hello World!



```python
from pathlib import Path

# Create a new directory
folder = Path("new")
folder.mkdir(exist_ok=True)

# Create new file inside new directory
file = folder / "new_file.txt"

# Write text
file.write_text("Hello World!")

# Read text
file.read_text()

```




    'Hello World!'




```python
!cd new && ls
```

    new_file.txt


```bash
.
└── new/
    └── new_file.txt
```

## Get Access to Files from Home Directory

Если вы хотите получить путь к папкам/файлам из домашнего каталога, используйте `Path.home()`


```python
from pathlib import Path

path = Path.home()

docs = path / 'Documents'
pictures = path / 'Pictures'

print(docs)
print(pictures)
```

    /Users/dromakin/Documents
    /Users/dromakin/Pictures


Теперь вы можете использовать методы pathlabs для манипулирования папками /файлами в полученном пути.


```python
# Create a new file inside Documents
file = docs / 'new_file.txt'
file.touch()
```


```python
!tree /Users/dromakin/Documents | grep new_file.txt 
```

    ├── [00mnew_file.txt[0m


## Get the Parent of the Current Path with pathlib

Если вы хотите легко получить родительский путь или путь к прародителю, используйте pathlib `.parent`.


```python
from pathlib import Path

path = Path.cwd()

print(f'Current path: {path}')
print(f'Parent of the current path: {path.parent}')
print(f'Grandparent of the current path: {path.parent.parent}')
```

    Current path: /Users/dromakin/KIB/dsis-v2/lessons/Python для анализа данных/1. Язык Python
    Parent of the current path: /Users/dromakin/KIB/dsis-v2/lessons/Python для анализа данных
    Grandparent of the current path: /Users/dromakin/KIB/dsis-v2/lessons


## Get the Path Relative to Another Path

Если вы хотите получить путь относительно другого пути, используйте `path lib.Path.relative_to`.


```python
from pathlib import Path

nlp = Path('/Users/dromakin/Documents')
root = '/Users/dromakin/'
nlp.relative_to(root)
```




    PosixPath('Documents')



## Check if Two File Paths Are the Same

Если вы хотите проверить, совпадают ли пути к двум файлам, используйте `Path.samefile()`.


```python
from pathlib import Path 

home = Path.home()
absolute = home / "/KIB/dsis-v2/lessons/Python\ для\ анализа\ данных/1.\ Язык\ Python/2_python_basics_2_and_more.ipynb"
relative = Path("2_python_basics_2_and_more.ipynb")

absolute.samefile(relative)

```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    Cell In[116], line 7
          4 absolute = home / "/KIB/dsis-v2/lessons/Python\ для\ анализа\ данных/1.\ Язык\ Python/2_python_basics_2_and_more.ipynb"
          5 relative = Path("2_python_basics_2_and_more.ipynb")
    ----> 7 absolute.samefile(relative)


    File ~/anaconda3/lib/python3.11/pathlib.py:920, in Path.samefile(self, other_path)
        916 def samefile(self, other_path):
        917     """Return whether other_path is the same or not as this file
        918     (as returned by os.path.samefile()).
        919     """
    --> 920     st = self.stat()
        921     try:
        922         other_st = other_path.stat()


    File ~/anaconda3/lib/python3.11/pathlib.py:1013, in Path.stat(self, follow_symlinks)
       1008 def stat(self, *, follow_symlinks=True):
       1009     """
       1010     Return the result of the stat() system call on this path, like
       1011     os.stat() does.
       1012     """
    -> 1013     return os.stat(self, follow_symlinks=follow_symlinks)


    FileNotFoundError: [Errno 2] No such file or directory: '/KIB/dsis-v2/lessons/Python\\ для\\ анализа\\ данных/1.\\ Язык\\ Python/2_python_basics_2_and_more.ipynb'


# Profiling and Timing Code

В процессе разработки кода и создания конвейеров обработки данных часто приходится идти на компромиссы между различными реализациями.
На ранних этапах разработки вашего алгоритма беспокоиться о таких вещах может быть контрпродуктивно. Как знаменито заметил Дональд Кнут, "Мы должны забыть о малой эффективности, скажем, примерно в 97% случаев: преждевременная оптимизация - корень всех зол".

Но как только ваш код заработает, может оказаться полезным немного покопаться в его эффективности.
Иногда полезно проверить время выполнения данной команды или набора команд; в других случаях полезно изучить многострочный процесс и определить, где находится узкое место в какой-либо сложной серии операций.
IPython предоставляет доступ к широкому спектру функциональных возможностей для такого рода синхронизации и профилирования кода.
Здесь мы обсудим следующие магические команды IPython:

- `%time`: время выполнения одного оператора
- `%timeit`: время повторного выполнения одного оператора для большей точности
- `%prun`: Запуск кода с помощью профилировщика
- `%lprun`: Запуск кода с помощью построчного профилировщика
- `%memit`: Измеряет использование памяти одним оператором
- `%mprun`: Запуск кода с помощью построчного профилировщика памяти

Последние четыре команды не поставляются в комплекте с IPython; чтобы использовать их, вам нужно будет получить расширения `line_profiler` и `memory_profiler`, которые мы обсудим в следующих разделах.

## Timing Code Snippets: %timeit and %time


```python
%timeit sum(range(100))
```

    419 ns ± 2.46 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)


Обратите внимание, что поскольку эта операция выполняется очень быстро, `%timeit` автоматически выполняет большое количество повторений.
Для более медленных команд `%timeit` автоматически настроит и выполнит меньшее количество повторений:


```python
%%timeit
total = 0
for i in range(1000):
    for j in range(1000):
        total += i * (-1) ** j
```

    88.3 ms ± 1.05 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)


Иногда повторение операции - не самый лучший вариант.
Например, если у нас есть список, который мы хотели бы отсортировать, повторная операция может ввести нас в заблуждение; сортировка предварительно отсортированного списка намного быстрее, чем сортировка несортированного списка, поэтому повторение исказит результат:


```python
import random
L = [random.random() for i in range(100000)]
%timeit L.sort()
```

    196 µs ± 4.17 µs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)


Для этого магическая функция "%time" может быть лучшим выбором. Это также хороший выбор для длительно выполняемых команд, когда кратковременные задержки, связанные с системой, вряд ли повлияют на результат.
Давайте определим время сортировки несортированного и предварительно отсортированного списка:


```python
import random
L = [random.random() for i in range(100000)]
print("sorting an unsorted list:")
%time L.sort()
```

    sorting an unsorted list:
    CPU times: user 14.3 ms, sys: 945 µs, total: 15.2 ms
    Wall time: 14.7 ms



```python
print("sorting an already sorted list:")
%time L.sort()
```

    sorting an already sorted list:
    CPU times: user 4.56 ms, sys: 2.03 ms, total: 6.59 ms
    Wall time: 7.45 ms


Обратите внимание, насколько быстрее сортируется предварительно отсортированный список, но обратите также внимание, насколько больше времени занимает "%time" по сравнению с "% timeit", даже для предварительно отсортированного списка!
Это результат того факта, что "%timeit" делает некоторые хитрые вещи под капотом, чтобы предотвратить вмешательство системных вызовов в синхронизацию.
Например, это предотвращает очистку неиспользуемых объектов Python (известную как *сборка мусора*), которая в противном случае могла бы повлиять на время выполнения.
По этой причине результаты "%timeit" обычно заметно быстрее, чем результаты "%time".

Для `%time`, как и для `%timeit`, использование волшебного синтаксиса ячейки `%%` позволяет синхронизировать многострочные скрипты:


```python
%%time
total = 0
for i in range(1000):
    for j in range(1000):
        total += i * (-1) ** j
```

    CPU times: user 127 ms, sys: 1.79 ms, total: 128 ms
    Wall time: 127 ms


# Visualization with Matplotlib

## Importing Matplotlib


```python
import matplotlib as mpl
import matplotlib.pyplot as plt
```

## Setting Styles

Мы будем использовать директиву "plt.style", чтобы выбрать подходящие эстетические стили для наших фигур.
Здесь мы установим стиль "classic", который гарантирует, что графики, которые мы создаем, будут использовать классический стиль Matplotlib:


```python
plt.style.use('classic')
```

## Plotting from a Jupyter Notebook

Построение графиков в интерактивном режиме в Jupyter может быть выполнено с помощью команды "%matplotlib" и работает аналогично оболочке IPython.
У вас также есть возможность встраивать графику непосредственно в ноутбук с двумя возможными вариантами:

- `%matplotlib inline` приведет к появлению *статических* изображений вашего графика, встроенных в блокнот.
- `%matplotlib notebook` приведет к *интерактивным* графикам, встроенным в блокнот.

В этой книге мы, как правило, будем придерживаться настроек по умолчанию, с рисунками, отображаемыми в виде статических изображений (результат этого базового примера построения графиков показан на следующем рисунке).:


```python
%matplotlib inline
```


```python
import numpy as np
x = np.linspace(0, 10, 100)

fig = plt.figure()
plt.plot(x, np.sin(x), '-')
plt.plot(x, np.cos(x), '--');
```


    
![png](output_220_0.png)
    


### Saving Figures to File



```python
fig.savefig('my_figure.png')
```


```python
!ls -lh my_figure.png
```

    -rw-r--r--  1 dromakin  staff    38K Nov  3 20:47 my_figure.png



```python
from IPython.display import Image
Image('my_figure.png')
```




    
![png](output_224_0.png)
    




```python
fig.canvas.get_supported_filetypes()
```




    {'eps': 'Encapsulated Postscript',
     'jpg': 'Joint Photographic Experts Group',
     'jpeg': 'Joint Photographic Experts Group',
     'pdf': 'Portable Document Format',
     'pgf': 'PGF code for LaTeX',
     'png': 'Portable Network Graphics',
     'ps': 'Postscript',
     'raw': 'Raw RGBA bitmap',
     'rgba': 'Raw RGBA bitmap',
     'svg': 'Scalable Vector Graphics',
     'svgz': 'Scalable Vector Graphics',
     'tif': 'Tagged Image File Format',
     'tiff': 'Tagged Image File Format',
     'webp': 'WebP Image Format'}



### Two Interfaces for the Price of One

Потенциально сбивающей с толку особенностью Matplotlib является его двойной интерфейс: удобный интерфейс, основанный на состоянии в стиле MATLAB, и более мощный объектно-ориентированный интерфейс. Здесь я кратко остановлюсь на различиях между ними.


```python
plt.figure()  # create a plot figure

# create the first of two panels and set current axis
plt.subplot(2, 1, 1) # (rows, columns, panel number)
plt.plot(x, np.sin(x))

# create the second panel and set current axis
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x));
```


    
![png](output_227_0.png)
    


# Interactive plot with widgets


```python
import ipywidgets as widgets

# For explicitly displaying widgets
from IPython.display import display

# Just need these for the demo purposes here
from datetime import datetime
import matplotlib.pyplot as plt
```


```python
demo_IntSlider_1 = widgets.IntSlider(
    min=1,                      # The minimum value
    max=100,                    # The maximum value
    description='Int Slider 1', # Label
    value=53,                   # Default value
)

# Display the widget
display(demo_IntSlider_1)
```


    IntSlider(value=53, description='Int Slider 1', min=1)



```python
for i, el in enumerate(dir(widgets)):
    print(str(i + 1) + '.', el)
```

    1. Accordion
    2. AppLayout
    3. Audio
    4. BoundedFloatText
    5. BoundedIntText
    6. Box
    7. Button
    8. ButtonStyle
    9. CallbackDispatcher
    10. Checkbox
    11. Color
    12. ColorPicker
    13. ColorsInput
    14. Combobox
    15. Controller
    16. CoreWidget
    17. DOMWidget
    18. DatePicker
    19. Datetime
    20. DatetimePicker
    21. Dropdown
    22. FileUpload
    23. FloatLogSlider
    24. FloatProgress
    25. FloatRangeSlider
    26. FloatSlider
    27. FloatText
    28. FloatsInput
    29. GridBox
    30. GridspecLayout
    31. HBox
    32. HTML
    33. HTMLMath
    34. Image
    35. IntProgress
    36. IntRangeSlider
    37. IntSlider
    38. IntText
    39. IntsInput
    40. Label
    41. Layout
    42. NaiveDatetimePicker
    43. NumberFormat
    44. Output
    45. Password
    46. Play
    47. RadioButtons
    48. Select
    49. SelectMultiple
    50. SelectionRangeSlider
    51. SelectionSlider
    52. SliderStyle
    53. Stack
    54. Style
    55. Tab
    56. TagsInput
    57. Text
    58. Textarea
    59. TimePicker
    60. ToggleButton
    61. ToggleButtons
    62. ToggleButtonsStyle
    63. TwoByTwoLayout
    64. TypedTuple
    65. VBox
    66. Valid
    67. ValueWidget
    68. Video
    69. Widget
    70. __builtins__
    71. __cached__
    72. __doc__
    73. __file__
    74. __jupyter_widgets_base_version__
    75. __jupyter_widgets_controls_version__
    76. __loader__
    77. __name__
    78. __package__
    79. __path__
    80. __protocol_version__
    81. __spec__
    82. __version__
    83. _handle_ipython
    84. _version
    85. dlink
    86. docutils
    87. domwidget
    88. fixed
    89. get_ipython
    90. interact
    91. interact_manual
    92. interaction
    93. interactive
    94. interactive_output
    95. jsdlink
    96. jslink
    97. link
    98. load_ipython_extension
    99. os
    100. register
    101. register_comm_target
    102. trait_types
    103. utils
    104. valuewidget
    105. widget
    106. widget_bool
    107. widget_box
    108. widget_button
    109. widget_color
    110. widget_controller
    111. widget_core
    112. widget_date
    113. widget_datetime
    114. widget_description
    115. widget_float
    116. widget_int
    117. widget_layout
    118. widget_link
    119. widget_media
    120. widget_output
    121. widget_selection
    122. widget_selectioncontainer
    123. widget_serialization
    124. widget_string
    125. widget_style
    126. widget_tagsinput
    127. widget_templates
    128. widget_time
    129. widget_upload
    130. widgets



```python
import ipywidgets as widgets
from ipywidgets import HBox, VBox
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display
%matplotlib inline
```


```python
@widgets.interact_manual(
    color=['blue', 'red', 'green'], lw=(1., 10.))
def plot(freq=1., color='blue', lw=2, grid=True):
    t = np.linspace(-1., +1., 1000)
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    ax.plot(t, np.sin(2 * np.pi * freq * t),
            lw=lw, color=color)
    ax.grid(grid)
```


    interactive(children=(FloatSlider(value=1.0, description='freq', max=3.0, min=-1.0), Dropdown(description='col…



```python
%matplotlib notebook
from ipywidgets import *
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
line, = ax.plot(x, np.sin(x))

def update(w = 1.0):
    line.set_ydata(np.sin(w * x))
    fig.canvas.draw_idle()

interact(update);
```


    <IPython.core.display.Javascript object>



<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABQAAAAPACAYAAABq3NR5AAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAFAKADAAQAAAABAAADwAAAAADIn4SfAABAAElEQVR4AezdCZxdVZ3g8X/2fV/JnkACAsGAGhGQERRcGltxgVbGj2i3OM64jU4P4949jkJrj6PSLt1OK62NCNogCq22rQjDIgEhEAOBQHbInpAKIXtl3v8d/nm3KvWq3nKXc8793c8nVa/eu/ec//mel6r3/u8s/W6//fYjwoEAAggggAACCCCAAAIIIIAAAggggAACUQr0j7JVNAoBBBBAAAEEEEAAAQQQQAABBBBAAAEEqgIkAHkiIIAAAggggAACCCCAAAIIIIAAAgggELEACcCIO5emIYAAAggggAACCCCAAAIIIIAAAgggQAKQ5wACCCCAAAIIIIAAAggggAACCCCAAAIRC5AAjLhzaRoCCCCAAAIIIIAAAggggAACCCCAAAIkAHkOIIAAAggggAACCCCAAAIIIIAAAgggELEACcCIO5emIYAAAggggAACCCCAAAIIIIAAAgggQAKQ5wACCCCAAAIIIIAAAggggAACCCCAAAIRC5AAjLhzaRoCCCCAAAIIIIAAAggggAACCCCAAAIkAHkOIIAAAggggAACCCCAAAIIIIAAAgggELEACcCIO5emIYAAAggggAACCCCAAAIIIIAAAgggQAKQ5wACCCCAAAIIIIAAAggggAACCCCAAAIRC5AAjLhzaRoCCCCAAAIIIIAAAggggAACCCCAAAIkAHkOIIAAAggggAACCCCAAAIIIIAAAgggELEACcCIO5emIYAAAggggAACCCCAAAIIIIAAAgggQAKQ5wACCCCAAAIIIIAAAggggAACCCCAAAIRC5AAjLhzaRoCCCCAAAIIIIAAAggggAACCCCAAAIkAHkOIIAAAggggAACCCCAAAIIIIAAAgggELEACcCIO5emIYAAAggggAACCCCAAAIIIIAAAgggQAKQ5wACCCCAAAIIIIAAAggggAACCCCAAAIRC5AAjLhzaRoCCCCAAAIIIIAAAggggAACCCCAAAIkAHkOIIAAAggggAACCCCAAAIIIIAAAgggELEACcCIO5emIYAAAggggAACCCCAAAIIIIAAAgggQAKQ5wACCCCAAAIIIIAAAggggAACCCCAAAIRC5AAjLhzaRoCCCCAAAIIIIAAAggggAACCCCAAAIkAHkOIIAAAggggAACCCCAAAIIIIAAAgggELEACcCIO5emIYAAAggggAACCCCAAAIIIIAAAgggQAKQ5wACCCCAAAIIIIAAAggggAACCCCAAAIRC5AAjLhzaRoCCCCAAAIIIIAAAggggAACCCCAAAIkAHkOIIAAAggggAACCCCAAAIIIIAAAgggELEACcCIO5emIYAAAggggAACCCCAAAIIIIAAAgggQAKQ5wACCCCAAAIIIIAAAggggAACCCCAAAIRC5AAjLhzaRoCCCCAAAIIIIAAAggggAACCCCAAAIkAHkOIIAAAggggAACCCCAAAIIIIAAAgggELEACcCIO5emIYAAAggggAACCCCAAAIIIIAAAgggQAKQ5wACCCCAAAIIIIAAAggggAACCCCAAAIRC5AAjLhzaRoCCCCAAAIIIIAAAggggAACCCCAAAIkAHkOIIAAAggggAACCCCAAAIIIIAAAgggELEACcCIO5emIYAAAggggAACCCCAAAIIIIAAAgggQAKQ5wACCCCAAAIIIIAAAggggAACCCCAAAIRC5AAjLhzaRoCCCCAAAIIIIAAAggggAACCCCAAAIkAHkOIIAAAggggAACCCCAAAIIIIAAAgggELEACcCIO5emIYAAAggggAACCCCAAAIIIIAAAgggQAKQ5wACCCCAAAIIIIAAAggggAACCCCAAAIRC5AAjLhzaRoCCCCAAAIIIIAAAggggAACCCCAAAIkAHkOIIAAAggggAACCCCAAAIIIIAAAgggELEACcCIO5emIYAAAggggAACCCCAAAIIIIAAAgggQAKQ5wACCCCAAAIIIIAAAggggAACCCCAAAIRC5AAjLhzaRoCCCCAAAIIIIAAAggggAACCCCAAAIkAHkOIIAAAggggAACCCCAAAIIIIAAAgggELEACcCIO5emIYAAAggggAACCCCAAAIIIIAAAgggQAKQ5wACCCCAAAIIIIAAAggggAACCCCAAAIRC5AAjLhzaRoCCCCAAAIIIIAAAggggAACCCCAAAIkAHkOIIAAAggggAACCCCAAAIIIIAAAgggELEACcCIO5emIYAAAggggAACCCCAAAIIIIAAAgggQAKQ5wACCCCAAAIIIIAAAggggAACCCCAAAIRC5AAjLhzaRoCCCCAAAIIIIAAAggggAACCCCAAAIkAHkOIIAAAggggAACCCCAAAIIIIAAAgggELEACcCIO5emIYAAAggggAACCCCAAAIIIIAAAgggQAKQ5wACCCCAAAIIIIAAAggggAACCCCAAAIRC5AAjLhzaRoCCCCAAAIIIIAAAggggAACCCCAAAIkAHkOIIAAAggggAACCCCAAAIIIIAAAgggELEACcCIO5emIYAAAggggAACCCCAAAIIIIAAAgggQAKQ5wACCCCAAAIIIIAAAggggAACCCCAAAIRC5AAjLhzaRoCCCCAAAIIIIAAAggggAACCCCAAAIkAHkOIIAAAggggAACCCCAAAIIIIAAAgggELEACcCIO5emIYAAAggggAACCCCAAAIIIIAAAgggQAKQ5wACCCCAAAIIIIAAAggggAACCCCAAAIRC5AAjLhzaRoCCCCAAAIIIIAAAggggAACCCCAAAIkAHkOIIAAAggggAACCCCAAAIIIIAAAgggELEACcCIO5emIYAAAggggAACCCCAAAIIIIAAAgggQAKQ5wACCCCAAAIIIIAAAggggAACCCCAAAIRC5AAjLhzaRoCCCCAAAIIIIAAAggggAACCCCAAAIkAHkOIIAAAggggAACCCCAAAIIIIAAAgggELEACcCIO5emIYAAAggggAACCCCAAAIIIIAAAgggQAKQ5wACCCCAAAIIIIAAAggggAACCCCAAAIRC5AAjLhzaRoCCCCAAAIIIIAAAggggAACCCCAAAIkAHkOIIAAAggggAACCCCAAAIIIIAAAgggELEACcCIO5emIYAAAggggAACCCCAAAIIIIAAAgggQAKQ5wACCCCAAAIIIIAAAggggAACCCCAAAIRC5AAjLhzaRoCCCCAAAIIIIAAAggggAACCCCAAAIkAHkOIIAAAggggAACCCCAAAIIIIAAAgggELHAwIjbFn3Tjhw5IuvWrZPHHntMVqxYUf23atUqOXjwYLXt119/vUydOjUVh927d8uPf/xjueuuu2TTpk3Sv39/mT59upx33nly8cUXy5AhQ1Kph0IQQAABBBBAAAEEEEAAAQQQQAABBNIVIAGYrmeupW3evFkuv/zyzOvUpOKVV14p27Zt61LXE088Ifrv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AAIIIIAAAggggAACCCCAAAIIFBdgEZDiNuxBAAEEEEAAAQQQQAABBBBAAAEEEEDAewECgN53IQ1AAAEEEEAAAQQQQAABBBBAAAEEEECguAABwOI27EEAAQQQQAABBBBAAAEEEEAAAQQQQMB7AQKA3nchDUAAAQQQQAABBBBAAAEEEEAAAQQQQKC4AAHA4jbsQQABBBBAAAEEEEAAAQQQQAABBBBAwHsBAoDedyENQAABBBBAAAEEEEAAAQQQQAABBBBAoLgAAcDiNuxBAAEEEEAAAQQQQAABBBBAAAEEEEDAewECgN53IQ1AAAEEEEAAAQQQQAABBBBAAAEEEECguAABwOI27EEAAQQQQAABBBBAAAEEEEAAAQQQQMB7AQKA3nchDUAAAQQQQAABBBBAAAEEEEAAAQQQQKC4AAHA4jbsQQABBBBAAAEEEEAAAQQQQAABBBBAwHsBAoDedyENQAABBBBAAAEEEEAAAQQQQAABBBBAoLgAAcDiNuxBAAEEEEAAAQQQQAABBBBAAAEEEEDAewECgN53IQ1AAAEEEEAAAQQQQAABBBBAAAEEEECguAABwOI27EEAAQQQQAABBBBAAAEEEEAAAQQQQMB7AQKA3nchDUAAAQQQQAABBBBAAAEEEEAAAQQQQKC4AAHA4jbsQQABBBBAAAEEEEAAAQQQQAABBBBAwHsBAoDedyENQAABBBBAAAEEEEAAAQQQQAABBBBAoLgAAcDiNuxBAAEEEEAAAQQQQAABBBBAAAEEEEDAewECgN53IQ1AAAEEEEAAAQQQQAABBBBAAAEEEECguAABwOI27EEAAQQQQAABBBBAAAEEEEAAAQQQQMB7AQKA3nchDUAAAQQQQAABBBBAAAEEEEAAAQQQQKC4AAHA4jbsQQABBBBAAAEEEEAAAQQQQAABBBBAwHsBAoDedyENQAABBBBAAAEEEEAAAQQQQAABBBBAoLgAAcDiNuxBAAEEEEAAAQQQQAABBBBAAAEEEEDAewECgN53IQ1AAAEEEEAAAQQQQAABBBBAAAEEEECguAABwOI27EEAAQQQQAABBBBAAAEEEEAAAQQQQMB7AQKA3nchDUAAAQQQQAABBBBAAAEEEEAAAQQQQKC4AAHA4jbsQQABBBBAAAEEEEAAAQQQQAABBBBAwHsBAoDedyENQAABBBBAAAEEEEAAAQQQQAABBBBAoLgAAcDiNuxBAAEEEEAAAQQQQAABBBBAAAEEEEDAewECgN53IQ1AAAEEEEAAAQQQQAABBBBAAAEEEECguAABwOI27EEAAQQQQAABBBBAAAEEEEAAAQQQQMB7AQKA3nchDUAAAQQQQAABBBBAAAEEEEAAAQQQQKC4AAHA4jbsQQABBBBAAAEEEEAAAQQQQAABBBBAwHsBAoDedyENQAABBBBAAAEEEEAAAQQQQAABBBBAoLgAAcDiNuxBAAEEEEAAAQQQQAABBBBAAAEEEEDAewECgN53IQ1AAAEEEEAAAQQQQAABBBBAAAEEEECguAABwOI27EEAAQQQQAABBBBAAAEEEEAAAQQQQMB7AQKA3nchDUAAAQQQQAABBBBAAAEEEEAAAQQQQKC4AAHA4jbsQQABBBBAAAEEEEAAAQQQQAABBBBAwHsBAoDedyENQAABBBBAAAEEEEAAAQQQQAABBBBAoLgAAcDiNuxBAAEEEEAAAQQQQAABBBBAAAEEEEDAewECgN53IQ1AAAEEEEAAAQQQQAABBBBAAAEEEECguAABwOI27EEAAQQQQAABBBBAAAEEEEAAAQQQQMB7AQKA3nchDUAAAQQQQAABBBBAAAEEEEAAAQQQQKC4AAHA4jbsQQABBBBAAAEEEEAAAQQQQAABBBBAwHsBAoDedyENQAABBBBAAAEEEEAAAQQQQAABBBBAoLgAAcDiNuxBAAEEEEAAAQQQQAABBBBAAAEEEEDAewECgN53IQ1AAAEEEEAAAQQQQAABBBBAAAEEEECguAABwOI27EEAAQQQQAABBBBAAAEEEEAAAQQQQMB7AQKA3nchDUAAAQQQQAABBBBAAAEEEEAAAQQQQKC4AAHA4jbsQQABBBBAAAEEEEAAAQQQQAABBBBAwHsBAoDedyENQAABBBBAAAEEEEAAAQQQQAABBBBAoLgAAcDiNuxBAAEEEEAAAQQQQAABBBBAAAEEEEDAewECgN53IQ1AAAEEEEAAAQQQQAABBBBAAAEEEECguAABwOI27EEAAQQQQAABBBBAAAEEEEAAAQQQQMB7AQKA3nchDUAAAQQQQAABBBBAAAEEEEAAAQQQQKC4AAHA4jbsQQABBBBAAAEEEEAAAQQQQAABBBBAwHsBAoDedyENQAABBBBAAAEEEEAAAQQQQAABBBBAoLgAAcDiNuxBAAEEEEAAAQQQQAABBBBAAAEEEEDAewECgN53IQ1AAAEEEEAAAQQQQAABBBBAAAEEEECguAABwOI27EEAAQQQQAABBBBAAAEEEEAAAQQQQMB7AQKA3nchDUAAAQQQQAABBBBAAAEEEEAAAQQQQKC4AAHA4jbsQQABBBBAAAEEEEAAAQQQQAABBBBAwHsBAoDedyENQAABBBBAAAEEEEAAAQQQQAABBBBAoLjA/wcPi5GjMVu1wAAAAABJRU5ErkJggg==" width="640">



    interactive(children=(FloatSlider(value=1.0, description='w', max=3.0, min=-1.0), Output()), _dom_classes=('wi…



```python
%matplotlib notebook
from ipywidgets import *
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10,100)

def f(x, A, B, C):
    return A*x**2 + B*x + C

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
line, = ax.plot(x, f(x, A=1, B=1, C=1))

def update(A = 1, B = 0, C = 0):
    line.set_ydata(f(x,A,B,C))
    fig.canvas.draw_idle()
    
interact(update, A = (-4,4,0.1), B = (-4,4,0.1), C = (-4,4,0.1));
```


    <IPython.core.display.Javascript object>



<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABQAAAAPACAYAAABq3NR5AAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAFAKADAAQAAAABAAADwAAAAADIn4SfAABAAElEQVR4AezdB7xcVbk/7m8glNCLdFBRuiLi9QKCgoKKVxEV/YGo9CZVBBS9Yi9gQxQkSC8iCP4pIgo2bMAVEUTvRZqI9N5DCST5z5rtJCHkhJQzc/bsefbnk5M5M3uv9b7PmsCZ96y91qhLLrlkUhwECBAgQIAAAQIECBAgQIAAAQIECDRSYK5GZiUpAgQIECBAgAABAgQIECBAgAABAgTaAgqA3ggECBAgQIAAAQIECBAgQIAAAQIEGiygANjgwZUaAQIECBAgQIAAAQIECBAgQIAAAQVA7wECBAgQIECAAAECBAgQIECAAAECDRZQAGzw4EqNAAECBAgQIECAAAECBAgQIECAgAKg9wABAgQIECBAgAABAgQIECBAgACBBgsoADZ4cKVGgAABAgQIECBAgAABAgQIECBAQAHQe4AAAQIECBAgQIAAAQIECBAgQIBAgwUUABs8uFIjQIAAAQIECBAgQIAAAQIECBAgoADoPUCAAAECBAgQIECAAAECBAgQIECgwQIKgA0eXKkRIECAAAECBAgQIECAAAECBAgQUAD0HiBAgAABAgQIECBAgAABAgQIECDQYAEFwAYPrtQIECBAgAABAgQIECBAgAABAgQIKAB6DxAgQIAAAQIECBAgQIAAAQIECBBosIACYIMHV2oECBAgQIAAAQIECBAgQIAAAQIEFAC9BwgQIECAAAECBAgQIECAAAECBAg0WEABsMGDKzUCBAgQIECAAAECBAgQIECAAAECCoDeAwQIECBAgAABAgQIECBAgAABAgQaLKAA2ODBlRoBAgQIECBAgAABAgQIECBAgAABBUDvAQIECBAgQIAAAQIECBAgQIAAAQINFlAAbPDgSo0AAQIECBAgQIAAAQIECBAgQICAAqD3AAECBAgQIECAAAECBAgQIECAAIEGCygANnhwpUaAAAECBAgQIECAAAECBAgQIEBAAdB7gAABAgQIECBAgAABAgQIECBAgECDBRQAGzy4UiNAgAABAgQIECBAgAABAgQIECCgAOg9QIAAAQIECBAgQIAAAQIECBAgQKDBAgqADR5cqREgQIAAAQIECBAgQIAAAQIECBBQAPQeIECAAAECBAgQIECAAAECBAgQINBgAQXABg+u1AgQIECAAAECBAgQIECAAAECBAgoAHoPECBAgAABAgQIECBAgAABAgQIEGiwgAJggwdXagQIECBAgAABAgQIECBAgAABAgQUAL0HCBAgQIAAAQIECBAgQIAAAQIECDRYQAGwwYMrNQIECBAgQIAAAQIECBAgQIAAAQIKgN4DBAgQIECAAAECBAgQIECAAAECBBosoADY4MGVGgECBAgQIECAAAECBAgQIECAAAEFQO8BAgQIECBAgAABAgQIECBAgAABAg0WUABs8OBKjQABAgQIECBAgAABAgQIECBAgIACoPcAAQIECBAgQIAAAQIECBAgQIAAgQYLKAA2eHClRoAAAQIECBAgQIAAAQIECBAgQEAB0HuAAAECBAgQIECAAAECBAgQIECAQIMFFAAbPLhSI0CAAAECBAgQIECAAAECBAgQIKAA6D1AgAABAgQIECBAgAABAgQIECBAoMECCoANHlypESBAgAABAgQIECBAgAABAgQIEFAA9B4gQIAAAQIECBAgQIAAAQIECBAg0GABBcAGD67UCBAgQIAAAQIECBAgQIAAAQIECCgAeg8QIECAAAECBAgQIECAAAECBAgQaLCAAmCDB1dqBAgQIECAAAECBAgQIECAAAECBBQAvQcIECBAgAABAgQIECBAgAABAgQINFhAAbDBgys1AgQIECBAgAABAgQIECBAgAABAgqA3gMECBAgQIAAAQIECBAgQIAAAQIEGiygANjgwZUaAQIECBAgQIAAAQIECBAgQIAAAQVA7wECBAgQIECAAAECBAgQIECAAAECDRZQAGzw4EqNAAECBAgQIECAAAECBAgQIECAgAKg9wABAgQIECBAgAABAgQIECBAgACBBgsoADZ4cKVGgAABAgQIECBAgAABAgQIECBAQAHQe4AAAQIECBAgQIAAAQIECBAgQIBAgwUUABs8uFIjQIAAAQIECBAgQIAAAQIECBAgoADoPUCAAAECBAgQIECAAAECBAgQIECgwQIKgA0eXKkRIECAAAECBAgQIECAAAECBAgQUAD0HiBAgAABAgQIECBAgAABAgQIECDQYAEFwAYPrtQIECBAgAABAgQIECBAgAABAgQIKAB6DxAgQIAAAQIECBAgQIAAAQIECBBosIACYIMHV2oECBAgQIAAAQIECBAgQIAAAQIEFAC9BwgQIECAAAECBAgQIECAAAECBAg0WEABsMGDKzUCBAgQIECAAAECBAgQIECAAAECCoDeAwQIECBAgAABAgQIECBAgAABAgQaLKAA2ODBlRoBAgQIECBAgAABAgQIECBAgAABBUDvAQIECBAgQIAAAQIECBAgQIAAAQINFlAAbPDgSo0AAQIECBAgQIAAAQIECBAgQICAAqD3AAECBAgQIECAAAECBAgQIECAAIEGCygANnhwpUaAAAECBAgQIECAAAECBAgQIEBAAdB7gAABAgQIECBAgAABAgQIECBAgECDBRQAGzy4UiNAgAABAgQIECBAgAABAgQIECCgAOg9QIAAAQIECBAgQIAAAQIECBAgQKDBAgqADR5cqREgQIAAAQIECBAgQIAAAQIECBBQAPQeIECAAAECBAgQIECAAAECBAgQINBgAQXABg+u1AgQIECAAAECBAgQIECAAAECBAgoAHoPECBAgAABAgQIECBAgAABAgQIEGiwgAJggwdXagQIECBAgAABAgQIECBAgAABAgQUAL0HCBAgQIAAAQIECBAgQIAAAQIECDRYQAGwwYMrNQIECBAgQIAAAQIECBAgQIAAAQIKgN4DBAgQIECAAAECBAgQIECAAAECBBosoADY4MGVGgECBAgQIECAAAECBAgQIECAAAEFQO8BAgQIECBAgAABAgQIECBAgAABAg0WUABs8OBKjQABAgQIECBAgAABAgQIECBAgIACoPcAAQIECBAgQIAAAQIECBAgQIAAgQYLKAA2eHClRoAAAQIECBAgQIAAAQIECBAgQEAB0HuAAAECBAgQIECAAAECBAgQIECAQIMFFAAbPLhSI0CAAAECBAgQIECAAAECBAgQIKAA6D1AgAABAgQIECBAgAABAgQIECBAoMECCoANHlypESBAgAABAgQIECBAgAABAgQIEFAA9B4gQIAAAQIECBAgQIAAAQIECBAg0GABBcAGD67UCBAgQIAAAQIECBAgQIAAAQIECIxGQGAkBMaPH5+bb7653fViiy2WueeeeyTC0CcBAgQIECBAgAABAgQIEGi0wIQJE/Lwww+3c3zZy16Weeedt9H5Sm76AgqA03fxbJcFSvFvzz337HIvmidAgAABAgQIECBAgAABAgQ6AmPHjs0aa6zR+dbfAyTgFuABGmypEiBAgAABAgQIECBAgAABAgQIDJ6AGYCDN+a1yLjc9ts5rrjiiiy33HKdb+f478ceeyxrrbVWrr322iy88MJz3J4GRkbg2GOTL34xWWKJ5Mork3nmGZk49FovAf++6zUeoiEwnAL+fQ+nprYI1EvAv+96jccgRXP11cmWW1YZ//rXyaqrDlL2U3K96667st5667WfmPqz+JQzPBoEAQXAQRjlGuY49Zp/pfi34oorDluUjz76aLutFVZYIYssssiwtauh3grsvXfyla8kDz6Y/O1vU/7H3dso9FY3Af++6zYi4iEwfAL+fQ+fpZYI1E3Av++6jcjgxFM+T5TjP/8zedObqseD/nXqz+KDbjFo+bsFeNBGXL4E+kRgmWWSt7+9Cvbkk/skaGESIECAAAECBAgQIFALgaeeSs48swplhx1qEZIgCIyogALgiPLrnACBGQnsuGP16gUXJPfdN6MzvUaAAAECBAgQIECAAIEpAuUzxEMPpbXjbfL+90953iMCgyqgADioIy9vAn0gsMUWyZJLJs8+m5xxRh8ELEQCBAgQIECAAAECBGohcMopVRjvfGf1maIWQQmCwAgKKACOIL6uCRCYsUD5bd0HPlCd4zbgGVt5lQABAgQIECBAgACBSuDuu5OLLqoeu/3Xu4JAJaAA6J1AgECtBTq3AZcdvK65ptahCo4AAQIECBAgQIAAgRoIfP/7yYQJyVJLJW97Ww0CEgKBGggoANZgEIRAgMDQAuuum6y9dvV6Zxr/0Gd7hQABAgQIECBAgACBQRaYNCk58cRKYPvtk3nmGWQNuROYIjB6ykOPmizwwAMP5Pzzz88VV1yR22+/PU+1tkRaYIEFstJKK2W99dbLu971riy22GIzJCjXljauv/76PProo1l88cVbhZm1s9VWW2Wttdaa4bW9fHG++ebLZz/72ZS/Hf0vMGpUUmYBHnhgUn6T99Wv+p94/4/q7Gfg3/fs27mSQN0F/Puu+wiJj8DsC/j3Pft2rpx1gdbH1vz979V1O+0069e7gkBTBUZdcsklrfq4o8kCpXD3hS98IePGjRsyzUUWWaR9zjrrrDPdc4488sicc845031trrnmyu67755tttlmuq9P78n7Wlu6br311u2Xbrvttqy44orTO81zBNoC99yTrLBCNY2/VYPOlluCIUCAAAECBAgQIECAwPMF9tgjOfbYtCa6JH/84/NfH8RnyiSgMvmnHGeddVbr1ujWvdGOgRNwC3DDh/yeVuWkzIYrxb8xY8Zkl112aU2HPjHnnXde6z+Kx+Z973tf5p577vaMvk9/+tN5+OGHnydS/gPRKf5tsMEGGTt2bPv6b33rW+2ZfxMnTswxxxyT3/3ud8+71hMEhkNgmWWSt7+9aslmIMMhqg0CBAgQIECAAAECzRN44onkjDOqvHbeuXn5yYjAnAgoAM6JXh9c+5Of/KR9u28J9eMf/3g+9KEPZeWVV86iiy6aVVddNXvvvXe7KFhef+yxx/LLX/6yPJx8PPLIIznl3wuvrdtajO3LX/5y1lhjjfb1r371q3P44YdP/k1CKQw+88wzk6/1gMBwCnQ2A7nggqQ1gdRBgAABAgQIECBAgACB5wiUm9ZaH2sz//zJ+9//nJd8Q2DgBRQAG/4WuOmmm9oZlnU33vCGN0w327e85S2Tny+34059XHzxxXmi/BqldZTbfMvtvlMfpd2d/r2wwt2tvdb/aI711DweD6PAFlskSy6ZPPvslN/qDWPzmiJAgAABAgQIECBAoM8FOpt/vPe9aU1a6fNkhE9gmAWeW80Z5sY1N/IC8/x7y6NRrZ0Uyp/pHVMX9abdCOSyyy5rX7Lccsu1Z/5N7/qNNtoo8847b/ulSy+9dHqneI7AHAuUt9gHPlA14zbgOebUAAECBAgQIECAAIFGCdx8c3LJJVVKbv9t1NBKZpgEFACHCbKuzay22mrt0Mquv0PNzvvNb34zOfz1119/8uPy4MYbb2x/P6Ndfkvxr9xOXI4bbrih/bcvBLoh0LkN+Oqrk2uu6UYP2iRAgAABAgQIECBAoB8F/r1yVV760uSNb+zHDMRMoLsCCoDd9R3x1t/97ndn8cUXb8dx6KGH5txzz03ZGGT8+PG544472uv7lQ08ylF25Z260Fd26u3c/rv88su3zxnqS5khWI5yC/GkSTaWHsrJ83Mm0FqGMmuvXbXRmd4/Zy26mgABAgQIECBAgACBfheYMCE56aQqizJpYJqVq/o9PfETGBaB0cPSikZqK7DQQgvl29/+dj73uc/l5tac6O985zvtP1MH/IpXvCJbbbVVNt1006mfTtkApHN0ioid76f9u3PrcNkE5Mknn8wCCyww7Sm+JzDHAuUu9jKd/6MfTb7//eRrX0tay1A6CBAgQIAAAQIECBAYYIFf/7pMRklr2aukc9fQAHNIncB0BcwAnC5Ls55caaWV8sUvfjGvec1rppvY/fffnzvvvDMTyq9NpjrKbcOdo7PGX+f7af8um4F0jlIAdBDolkBrI+uUpS0ffDA5//xu9aJdAgQIECBAgAABAgT6RaAz+2+zzZKXvKRfohYngd4KKAD21ntEejvjjDOy3Xbbtdfz22effVozp76fH//4x60p0ie1fjuyY6uQ8mBOOOGEHHzwwZm66OdW3hEZLp2+gMCLXpS8613VSW4DfgEsLxMgQIAAAQIECBBouMBDDyXnnFMludNODU9WegTmQEABcA7w+uHSs846K8cee2xGjx7dvhX4va390FdYYYUsvPDCrcVRX5oddtghX/rSl9qp/PnPf85pp502Oa0xY8ZMflzWDJzR8fTTT09+eerrJj/pAYFhFNhll6qxn/88ufXWYWxYUwQIECBAgAABAgQI9JVAa75LysfRRRdN3vOevgpdsAR6KqAA2FPu3nb27LPPtmf7lV43a82FXnnllacbwHrrrZdXv/rV7dcuvPDCyZt4LFr+C/rv46Hya5UZHA8//HD71Xla92bOagHwsccey6OPPjrkn6mLizMIwUsDJPCWtyQrrpjWezWtjWwGKHGpEiBAgAABAgQIECDwHIHO7b8f+EBan0Wf89JAfVM+Nw/1ubp85nYQUABs8HvglltuSecf+uqrrz7DTDuvl40/OsW8pZZaavJmHmWNwBkdd911V/vlst7gqLLy6iwcZefhUmwc6k/ZvdhBYGqBueeesrhvuQ144sSpX/WYAAECBAgQIECAAIFBEPjrX5Mrr6wyHfTbf8vn5qE+U5fP3A4CCoANfg9MPXNuVtbzm7qAt+qqq7aF/v73vw8pVW4PvvHGG9uvr7baakOeN9QL1157bXvH4VJ8nN6fT37yk0Nd6vkBFuj8D75V585vfjPAEFInQIAAAQIECBAgMKACndl/r3xl8trXDijCv9Mun5un93m6PFc+czsIKAA2+D2w5JJLTs7u+uuvn/x4eg+uu+669tPl9t1FFllk8ikbbrhh+3GZAThUG5dddlk6awRutNFGk6+d2QdlPcLS51B/pt5heGbb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sF5hheTd7x5oCskTaJSAAmCjhlMyBAjUUeBVr0re+MYqsjIL0EGAAAECBAgQIECgjgJPPZWUtavLseeeyTzzVI99JUCg/wUUAPt/DGVAgEAfCOy3XxXkuecmt97aBwELkQABAgQIECBAYOAEzjorue++ZN55k912G7j0JUyg0QIKgI0eXskRIFAXgXe+M3nJS5KJE5Ojj65LVOIgQIAAAQIECBAgUAmUtaqPOKJ6vO22ydJLkyFAoEkCCoBNGk25ECBQW4HRo5O9967CO+645IknahuqwAgQIECAAAECBAZQoKxVffXVVeL77z+AAFIm0HABBcCGD7D0CBCoj8AuuyRjxiQPPpj84Af1iUskBAgQIECAAAECBDqz/974xuTVr+ZBgEDTBBQAmzai8iFAoLYCSyyRbLddFV7ZDKTcZuEgQIAAAQIECBAgMNICN9+cnHdeFYXZfyM9Gvon0B0BBcDuuGqVAAEC0xXYd9/q6b/9Lfntb6d7iicJECBAgAABAgQI9FTgyCOrX06/7GXJFlv0tGudESDQI4HWqlSOQRL4W6vqcNFFF+Waa67JAw88kLnnnjtLtKYlrbLKKq1p3q/OlltuOSTHFVdckfPPPz/XX399Hn300Sy++OJZe+21s9VWW2WttdYa8jovECAwReCVr0w23TT59a+TMgvwjW+c8ppHBAgQIECAAAECBHot0PpolxNOqHrdb7+0PiP2OgL9ESDQCwEFwF4o16CP8ePH5/DDD8/FF1/8vGjGjRuX2267LZdccsmQBcAjW78SOuecc55z7b333ptf/epX7et23333bLPNNs953TcECExfoPxgVQqArXp6brkleelLp3+eZwkQIECAAAECBAh0W+Ckk5LHHksWWSTZeedu96Z9AgRGSkABcKTke9jvhAkT8pnPfCZ//OMf271uttlmecc73pEXv/jFGd3amvTOO+9Mmd3385//fLpRnXXWWZOLfxtssEF22GGHLLfccvnnP/+Z41rbmV577bU55phj2s9tvPHG023DkwQITBEot1WUol8p/h11VPKNb0x5zSMCBAgQIECAAAECvRJofVRs35VS+isb1i28cK961g8BAr0WmKvXHeqv9wJnn3325OLfQQcdlEMOOSTrrrtullxyySy66KJZc80120W9008//XnBPfLIIznllFPaz5drvvzlL2eNNdZoX1duGS6zCldaaaX262PHjs0zzzzzvDY8QYDAcwXKbRWdtQBbNfT2b1yfe4bvCBAgQIAAAQIECHRf4Cc/ScoGIHO1KgOdn0+736seCBAYCQEFwJFQ72Gfjz/++OQC3qathcfKzL9ZOcotw0888UT7knKb71zl/wxTHfPNN1922mmn9jN333335ELjVKd4SIDAdATKb1gXWiit9TSTctuFgwABAgQIECBAgECvBY44ourxXe9KVl65173rjwCBXgo8t5rTy5711ROBX/ziF3nqqafafb3//e+f5T4vu+yy9jXllt8y8296x0YbbZR55523/dKll146vVM8R4DANAKtybfZddfqyfKDV7n9wkGAAAECBAgQIECgVwJ/+Uvym99UvX30o73qVT8ECIyUgALgSMn3qN/Oun9LL710Vl111cm9lnUBJ06cOPn7oR7ceOON7ZdmtMtvKf512r7hhhuGasrzBAhMI1A2AymTalvLaebHP57mRd8SIECAAAECBAgQ6KJAZ/bfa16TvP71XexI0wQI1ELAJiC1GIbuBXHddde1G1999dXz7LPP5kc/+lEuuuii3H777Zk0aVKWWmqpvPa1r02ZHbjiiis+J5D77rtv8u2/yy+//HNem/abMkPw//7v/9q7CZd2R40aNe0pvidAYBqBcpvFu9+d1iY7ybe+lbznPdOc4FsCBAgQIECAAAECXRBord6UM86oGt5//7Q+v3WhE00SIFArATMAazUcwxvM008/nbKJRzkWae3pvl9rutH3vve9/Otf/2rdbljNALznnnty4YUXtnZ82iW//e1vnxNA59ry5OKLL/6c16b9ZrHFFms/VTYBefLJJ6d92fcECAwhcMAB1Qu//31y5ZVDnORpAgQIECBAgAABAsMocMwxyfjxybLLJltvPYwNa4oAgdoKKADWdmjmPLBx48ZNbuTnP/95/v73v6fs3Pvd7343ZXOP8847L2VX4IVaOxGMb/3Xv+zwe9NNN02+prN2YHmis8bf5BeneVA2A+kcCoAdCX8TeGGBDTdM/vM/q/PKLEAHAQIECBAgQIAAgW4KlCXix46tethrr2Sqj3Ld7FbbBAiMsIAC4AgPQDe7n3qNvzIzb80118zXv/71lPX8SkFv0dYuBGVX4MMOO6y9u28556SptiMtt/I6CBDorkC53aKz6PJZZ6V1e353+9M6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wlcCBOoooABYx1EREwECBGoucMABycILJw88YBZgzYdKeAQIECBAgECXBMrsv0MOqRrffPPkDW/oUkeaJUCAwDAIKAAOA6ImCBAgMGgCZgEO2ojLlwABAgQIEJhW4MILk7L7bznK2n8OAgQI1FlAAbDOoyM2AgQI1FigzAJcZJHkwQeT73ynxoEKjQABAgQIECAwzAITJyadnX+33DJZb71h7kBzBAgQGGYBBcBhBtUcAQIEBkVgiSWS/fevsi1rAT700KBkLk8CBAgQIEBg0AXOPTe5+upKwey/QX83yJ9AfwgoAPbHOImSAAECtRQoswAXXzx55JHkG9+oZYiCIkCAAAECBAgMq8CECVNm/229dbLOOsPavMYIECDQFQEFwK6wapQAAQKDIbDoosnBB1e5fvvbyT33DEbesiRAgAABAgQGV+DMM5Nrr03man2a/tznBtdB5gQI9JeAAmB/jZdoCRAgUDuBffZJllkmGTcuOfTQ2oUnIAIECBAgQIDAsAk8++yUot8HP5isueawNa0hAgQIdFVAAbCrvBonQIBA8wUWXDD51KeqPMeOTW67rfk5y5AAAQIECBAYTIFTT01uuimZe+7ks58dTANZEyDQnwIKgP05bqImQIBArQR23z158YuT8eOTL36xVqEJhgABAgQIECAwLAJPP518/vNVUzvvnLz85cPSrEYIECDQEwEFwJ4w64QAAQLNFphvvim/BT/xxOo3483OWHYECBAgQIDAoAmccEJy663JvPMmhxwyaNnLlwCBfhdQAOz3ERQ/AQIEaiKw/fbJaqslZWc8t8TUZFCEQYAAAQIECAyLwJNPJl/+ctVU586HYWlYIwQIEOiRgAJgj6B1Q4AAgaYLjB495baYM85I/vd/m56x/AgQIECAAIFBETjmmOTOO5P550/++78HJWt5EiDQJAEFwCaNplwIECAwwgJbb5286lXJpEnJpz89wsHongABAgQIECAwDAKPP54cemjV0D77JMstNwyNaoIAAQI9FlAA7DG47ggQINBkgbla/1f50peqDM87L7niiiZnKzcCBAgQIEBgEASOOiq5775kwQWTj398EDKWIwECTRRQAGziqMqJAAECIyiwxRbJ+utXAVggewQHQtcECBAgQIDAHAs88kjyta9Vzey/f7LUUnPcpAYIECAwIgIKgCPCrlMCBAg0V2DU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t00+97l2OsiaAAECvSSgANhLvSkXAgQIEKiVwPTTJz/9aTJZ3/9t//KX5NBDaxWeYAgQIECAwJsERoxINt00efHF5H3vS4444k2neIIAAQIEGiigANjAThMyAQIECDRHYJllkr33ruI95JDk+uubE7tICRAgQKB9AkOHJtdemwwZkpx6ajLDDO0zkDEBAgR6UUABsBd7VU4ECBAgUCuB/fZLllgiKaMqylTgF16oVXiCIUCAAAEC/QK33JKU/2eVY9ddkxVWqB77TIAAAQLNF1AAbH4fyoAAAQIEai4w1VTVVOCpp07GXlep5mELjwABAgRaJPDKK8mXv1ytV/uhDyUHH9yi5KVKgACBFggoALagk6VIgAABApNeYNFFk299q4rj+OOTSy6Z9DGJgAABAgQIjBY46KDkb39LJp88Oe20ZJppRr/iKwECBAj0goACYC/0ohwIECBAoBECO+6YrLxyFepmmyVPPdWIsAVJgAABAj0ucMUVyeGHV0l+4xvJkkv2eMLSI0CAQAsFFABb2OlSJkCAAIFJI1B2Az7llGSmmZIHH0y2337SxKFVAgQIECAwWuDpp5ONN05GjkyWXjrZd9/Rr/hKgAABAr0koADYS70pFwIECBCovcD88ydlCnA5fv7z5Mwzq8c+EyBAgACBbguMGpVss03yn/9Uu/2ecUYy5ZTdjkJ7BAgQINANAQXAbihrgwABAgQIjCVQRlqsu271xLbbVqMBx3rZQwIECBAg0BWBn/40OeusqqkTTkgWWqgrzWqEAAECBCaBgALgJEDXJAECBAi0W2DIkOSkk5I550zK1KuvfKWaetVuFdkTIECAQDcF/vWvMUtRfOlLySabdLN1bREgQIBAtwUUALstrj0CBAgQINAn8O53V+sBFoxLL02OPBILAQIECBDojsDw4clGGyXPPZeUpSlOPDEpb045CBAgQKB3BRQAe7dvZUaAAAECNRdYffVk552rIMuui9dfX/OAhUeAAAECPSFw8MHJddclZXOq009PZpmlJ9KSBAECBAhMQEABcAI4XiJAgAABAoMt8K1vJYsvnrz6arLhhsmwYYPdovsTIECAQJsFrrgiOfTQSmCffZIVVmizhtwJECDQHgEFwPb0tUwJECBAoIYCU09d7QY83XTJ2Osx1TBUIREgQIBAwwXKurNlI6qRI5Oll07226/hCQmfAAECBCZaQAFwoqmcSIAAAQIEBkdgkUWS446r7l2mYpVdGR0ECBAgQGAgBUaNSsrO8//5TzLDDMkZZyRTTjmQLbgXAQIECNRZQAGwzr0jNgIECBBojcBmmyXrr1+lu912yd13tyZ1iRIgQIBAFwTKG0xnnlk1dMIJyUILdaFRTRAgQIBAbQQUAGvTFQIhQIAAgTYLlN0XTzopee97q10ZN9ggeeWVNovInQABAgQGSuDf/0623766W3mzaZNNBurO7kOAAAECTRFQAGxKT4mTAAECBHpeoOzC+LOfJZNPntx4Y7Lvvj2fsgQJECBAYJAFhg9PNtooefbZZP75qzebyptODgIECBBol4ACYLv6W7YECBAgUHOBZZdNDjywCnLo0OTii2sesPAIECBAoNYCBx2UXHttMlnfX35lGnB5s8lBgAABAu0TUABsX5/LmAABAgRqLrDXXslKK1VBfvnLyaOP1jxg4REgQIBALQUuuSQ59NAqtH32SVZYoZZhCooAAQIEuiCgANgFZE0QIECAAIG3I1CmAJdRGrPNVhX/vvKVZOTIt3MH5xIgQIBA2wUeeqia+lt2/y2Fv/33b7uI/AkQINBuAQXAdve/7AkQIECgpgLveU/y4x9Xwf3+98kxx9Q0UGERIECAQO0EXn012XDD5LHHkne/O/n5z5MppqhdmAIiQIAAgS4K+N9AF7G73dSIESNy00035YYbbshtt92W+++/P88991ymmWaazDPPPFlyySWz1lprZa655pqo0K6//vqcd955ufPOOzNs2LDMOuusWWyxxbLOOutk0UUXnah7OIkAAQIEJl7g85+vdm084YSkTAteccXkE5+Y+OudSYAAAQLtFCjr/l1+eZV7GVFe3lRyECBAgEC7BYZcdtllfYPCHb0osMUWW+Tf//73BFMrxcCddtopq6222gTPO+6443LOOeeM85zJ+lYU3mqrrbL++uuP8/VxPflY39uR6623Xv9LpTA577zzjus0zxEgQKD1Ai++mCy9dHLLLclCC1W7A888c+tZABAgQIDAeATKun+rrpqUqb9l3b/RawCO53RPEyDQAoEHHngg8803X3+mZ599dmafffYWZC3FNwoYAfhGkR76/vnnn+/b7WuyLLHEEn2jRlbMhz/84bzrXe9Kef66667LKaec0j+S74gjjujbDWyWLLPMMuPMvvwDMbr4V87ZdNNNM/fcc+eee+7JD37wg/7RhSeddFL/c5/+9KfHeQ9PEiBAgEBnAtNOm5x5ZrLUUsm//pVstlnyq18lQ4Z0dj9XESBAgEDvCrxx3b/Ru8r3bsYyI0CAAIGJFbAG4MRKNfC8lVZaKaeeemqGDh2aNddcMwsuuGBmmmmm/kLd2muvnTKqr4wAHNX39mAp4I3reOaZZ/KTn/yk/6WPf/zjfe8gHppFFlkkM/cNP1l88cVz9NFHv/ZOwoknnpjhw4eP6zaeI0CAAIF3IFBWWTj55OoG555rPcB3QOlSAgQI9KyAdf96tmslRoAAgQERUAAcEMZ63mSbbbZ5rTg3rgjnn3/+rL766v0v3XfffXnkkUfedNpFF12UF154of/5Ms23jCgc+5h66qn7RqP0DUfpO8r1ZWShgwABAgQGXmCjjZKtt67uu8ceydVXD3wb7kiAAAECzRWw7l9z+07kBAgQ6IbA66s53WhRG7USWGCBBV6L54knnnjt8egHV//fX5hlym8Z+TeuY7nllstUU03V/9JVV101rlM8R4AAAQIDIFB2Au5b1SFllEdZRrXs7uggQIAAAQJl3b9DDqkcyrp/ZQ1ABwECBAgQGFtAAXBsjRY+fuqpp17Levrpp3/t8egHd999d//DCe3yW4p/Cy+8cP95d9111+hLfSVAgACBARboW7Uhv/hF+pZhSB58MNl446Rvw3cHAQIECLRYYOx1/8py3Nb9a/EPg9QJECAwAQEFwAngtOGlK664oj/Nsjbg6F2BRuddduodPf13nnnmGf30OL+WEYLlKDv6ljUFHQQIECAwOALve1/61mat7n3xxXZ3HBxldyVAgEAzBMZe969s6vnznydT2OaxGZ0nSgIECHRZQAGwy+B1au7CCy/s21Gyb0vJvqNsEjL55JO/LryyAcjoY9ZZZx39cJxfyy7C5SibgLz44ovjPMeTBAgQIDAwAp//fLL77tW9DjggKVO/HAQIECDQPoHR6/6VneFPPz15i/fs2wckYwIECBB4TUAB8DWKdj249957+3cBLlnPOeec2WCDDd4E8NJLL7323Og1/l574g0PymYgow8FwNESvhIgQGDwBPo2Zc/yy6dv1HVSNggpU4IdBAgQINAegTeu+/e5z7Und5kSIECAwNsXUAB8+2aNv6Ks+/eNb3yjf6TelFNOmX333TczzDDDm/IylfdNJJ4gQIBAbQT6/vnOWWclc8xRbQay/vplFHZtwhMIAQIECAyiwH33pe8N/OpNoLLuXxkN7iBAgAABAhMSUACckE4Pvvbcc89ljz32yEN9qwVPNtlk/YXAj3zkI+PMdNppp33t+VdeeeW1x+N68PLLL7/29NjXvfakBwQIECAw4AJlqtfPfpaUqV9lE/a99x7wJtyQAAECBGomUFbbWWed5Iknkrnmsu5fzbpHOAQIEKitgCVia9s1Ax9YmZq711575Z///GffH4tDsttuu2XFFVccb0Mzl20m/+8Ye7fg0c+N/fXpp5/u/7aMKHy7BcBnn302w4YNG/t2r3tcphePPcX4dS/6hgABAi0X+Oxnqx0f99svOeqoalrw2mu3HEX6BAgQ6FGBsuzDdtslf/1rtdlH2Rneun892tnSIvA2BcqgnLEH5ox9efmb20HACMCW/AyUEXxl2u+tt97an/HXvva1rL766hPMfva+rcSmm266/nPKiMEJHQ8//HD/y2Un4VJcfDvHoosumlJsHN/H4Ycf/nZu51wCBAi0TqDvn/esumqV9le+kr4NnlpHIGECBAi0QuCkk5JTT61S/c53qjd9WpG4JAkQeEuB8nfz+P6mLn9zOwgYAdiCn4FXX301+/UNDbnpppv6s91yyy3zhS98YaIyX3jhhXPzzTfn9ttvH+/5pbh4991397/+gQ98YLznje+F2267Le95z3vG97LRf+OV8QIBAgQqgb4VHfp3f/z4x5MHHkjWXbeaEjz99IQIECBAoFcErr462WmnKpsvfznZfvteyUweBAgMhMDefWvB7LLLLuO81YN9u8UpAo6TplVPGgHY4909YsSIHHLIIbnuuuv6M91kk02y4YYbTnTWyy67bP+5ZQTgnXfeOc7rru77bWT0GoHLLbfcOM+Z0JMzzjhjZppppvF+mP47IT2vESBAoBJ497uTMhWsbA7S975NttiiWhyeDwECBAg0X6BMtvmf/6k2e1p88aSMBHybk26ajyADAgQmKFD+bh7f39Xlb24HAQXAHv4ZKLv4Dh06NJdffnl/lv/T91vD5ptv/rYyXrVvTtnoacAnn3xyRo4c+brrS+Hv1P+bhzBX3yrESy+99Ote9w0BAgQIdE9gmWWS732vaq/sENz3vwAHAQIECDRcoOzF98UvJqUIONtsyTnnpG/N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QRMgQIAAgbctMMXbvsIFBAgQIECAAIEBFJii77eR005LSjHw1FOTsgvnSy9V6wIOGTKADbkVAQKtFXj00Wrd0b/9LZmsbwjE97+ffPWrreWQOAECBAi0UMAIwBZ2upQJECBAgEDdBCafPPnRj5KttqoiO+aYZNttkxEj6hapeAgQaJrAvfcmK6yQlOLflFMmZ52l+Ne0PhQvAQIECLxzAQXAd27oDgQIECBAgMAACJRROSedlHzta9XNygid9devRgMOwO3dggCBFgrcdluy/PLJ3XcnZQfyMv33f/6nhRBSJkCAAIHWCygAtv5HAAABAgQIEKiPQJnye+yxyX77VTH96lfVtL2nn65PjCIhQKAZAtdfX438e/DBZNZZkz/8Ifmv/2pG7KIkQIAAAQIDLaAAONCi7keAAAECBAi8I4FSBCybgXzve0l5fPnlyYorJg899I5u62ICBFokUIp9K6+cPPlkMs88yRVXJEsv3SIAqRIgQIAAgTcIKAC+AcS3BAgQIECAQD0EyhqAZ59dbQ7y978nyy6b3HlnPWITBQEC9RU455zkv/87ef755P3vT666Kvnwh+sbr8gIECBAgEA3BBQAu6GsDQIECBAgQKAjgbJW10UXJTPNlNx3X7LcckmZ1ucgQIDAuAR+/OPki19MXnkl+djHkiuvTBZYYFxneo4AAQIECLRLQAGwXf0tWwIECBAg0DiBlVZK/vznZK65kieeSD7zmeTCCxuXhoAJEBhEgVGjkm9/O9lii2TkyGrjjz/9KZlzzkFs1K0JECBAgECDBBQAG9RZQiVAgAABAm0VKCN5rr46WXjh5IUXkrXWSk47ra0a8iZAYGyB4cOTbbZJ9tqrerZM/y0jh2eZZeyzPCZAgAABAu0WUABsd//LngABAgQINEZgwQWrtbyWWip59dVk002TI49sTPgCJUBgEASeeSZZY43k5JOrm2++efLrXyfTTTcIjbklAQIECBBosIACYIM7T+gECBAgQKBtArPPnvzxj8mqq1aZ7757svPOyYgRbZOQLwECo9cFveSSyuKww5If/jCZcko2BAgQIECAwBsFFADfKOJ7AgQIECBAoNYCM8yQ/OY3ycYbV2Eee2w1JXjYsFqHLTgCBAZQ4IYbkqWXTm69NZl66uTMM5O9906GDBnARtyKAAECBAj0kIACYA91plQIECBAgEBbBMoIn5/8JNl33yrj3/0uWXbZ5J572iIgTwLtFTj33GTFFZNHH03e/e5qVPD667fXQ+YECBAgQGBiBBQAJ0bJOQQIECBAgEDtBCbr+y3m4IOTM86oRgCVkUCf/GRy5ZW1C1VABAgMgEDZ6ffoo5N1101efDH54AeTa6+tiv8DcHu3IECAAAECPS2gANjT3Ss5AgQIECDQ+wIbbphcfnky55zJ448nK6+cnHpq7+ctQwJtEigb/2y/fbLrrkkpBK60UnLNNclCC7VJQa4ECBAgQKBzAQXAzu1cSYAAAQIECNREoKwFdv31ycc+lgwfnmy2WbLHHjYHqUn3CIPAOxIo63v+v/+XnHhidZuyA/hFFyWzzvqObutiAgQIECDQKgEFwFZ1t2QJECBAgEDvCsw/fzX9d+21qxyHDk3WWSd59tnezVlmBHpd4O67qym+v/99lWmZ9n/KKclUU/V65vIjQIAAAQIDK6AAOLCe7kaAAAECBAhMQoGyQ/CvflXtBlrCOP/8ZLnlkvvum4RBaZoAgY4Eym7fSy45Zqffst5n2fjHTr8dcbqIAAECBFouoADY8h8A6RMgQIAAgV4TKJuDHHZYctpp1SihW26pNge5+upey1Q+BHpTYOTIZP/9k7XWSsr03/nmq0b3lvU+HQQIECBAgEBnAgqAnbm5igABAgQIEKi5wCabJJddlsw+e/K//1ttGnDccdUGAjUPXXgEWivw9NPVen8HHVQRlE19bryxGgnYWhSJEyBAgACBARBQABwARLcgQIAAAQIE6imw7LLJDTckiy9ebQ6y447Jl75kXcB69pao2i5QRuuWKb+/+10lsdtu1WYfpYjvIECAAAECBN6ZgALgO/NzNQECBAgQIFBzgfe+NynTf7fYogr07LOTpZaq1hWreejCI9AagTPPTJZZJvnXv5Lpp0/OOispG/lMMUVrCCRKgAABAgQGVUABcFB53ZwAAQIECBCog8C00yY//GHy4x8n00yT3HlntS5g2VTAQYDApBN49dWkjPTbYIPkhReS978/ufbaZL31Jl1MWiZAgAABAr0ooADYi70qJwIECBAgQGCcApttVhUXSpGhFBs23jjZbrvk5ZfHebonCRAYRIHHHks+97nkqKOqRtZcs5qy/5GPDGKjbk2AAAECBFoqoADY0o6XNgECBAgQaKvAxz6W/OUvyRe+UAmceGKy/PLJvfe2VUTeBLov8Mc/Vmtzlo16hgxJDjwwOe+8ZJZZuh+LFgkQIECAQBsEFADb0MtyJECAAAECBF4nMPPMya9+lRx5ZDL55FVBcIklxmw+8LqTfUOAwIAJDB+e7L13ssoqyUMPVQW/3/wm2W+/ZDJ/mQyYsxsRIECAAIE3Cvjf7BtFfE+AAAECBAi0QqCMOtp116SMQJp77uSpp5I11kj22Sd55ZVWEEiSQFcFygYfZbTtt76VjBqVrLBCcvPN1X93XQ1EYwQIECBAoIUCCoAt7HQpEyBAgAABAmMEShHippuSz3ymeu7ww5Nll03uuGPMOR4RIPDOBE4/Pfn4x5Prr69G+pUpv6X4Pv/87+y+riZAgAABAgQmTkABcOKcnEWAAAECBAj0sMCccyYXX5zsv381JfjGG5MyJfiEE6qRSj2cutQIDKrAsGHJJptUH88+WxX8/vznaspvmX7vIECAAAECBLojoADYHWetECBAgAABAjUXmGKK5IADkquuSsouwS++mOywQzU98ZFHah688AjUUKCM9iuj/srov3Kst1415Xe55arvfSZAgAABAgS6J6AA2D1rLREgQIAAAQINEFh66WpK8FZbVcFeeGHykY8k557bgOCFSKAGAiNHVuv8lULfv/+dTDdd8qMfJWeeaZffGnSPEAgQIECgpQIKgC3teGkTIECAAAEC4xeYYYbk+99PzjsvmX325IknknXWSTbfPCnTGB0ECIxboGz08dnPVjv9vvpqsvjiyV//Wv23UzbecRAgQIAAAQKTRkABcNK4a5UAAQIECBBogMBaayW33DJml9JTTqkKGldf3YDghUigiwIjRiTf+U6y2GLJn/5UNfz1ryfXXpt88INdDERTBAgQIECAwDgFFADHyeJJAgQIECBAgEAlUDYI+c1vkpNOqqYylimNZefgffZJXnqJEgECt9+eLL98sssu1dqZCy6Y/OEPydFHJ1NPzYcAAQIECBCog4ACYB16QQwECBAgQIBArQXK1MWtt67WBlxqqaSscXb44clHP5pcdlmtQxccgUETGD68+u+gTPMtI/3Kfyc77VSNml155UFr1o0JECBAgACBDgQUADtAcwkBAgQIECDQToEPfKDaJfjgg6uRTXffnZRCx2abVesEtlNF1m0U+NvfkrJhThkJ+8or1TTfK69MjjkmmX76NorI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rJNMOWXy9NNVYXCFFaoi0je/mdx55wA27FYDKlCKtDfeWO0CPc88SdnUoxRzy/He9yYHHJCU0YBlGvB661V93P+iTwQIECBAgACBtxCY4i1e9zIBAgQIECBAgEBDBMr04M98pvp48slqqujppydXXVWtFXjIIUn5WGqparOIL30pmWOOhiTXo2GOLvqde25SPm6/fUyiZQOYUswtaz+Wfi1rPjoIECBAgAABAp0IKAB2ouYaAgQIECBAgEDNBWabrdoUpGwM8u9/J6UQWD7uvju54YbqY5ddks9+NlljjepjoYVqnlSPhFfW77viiqrg9+tfVzv4jp3aEkskm2+ebLhhtb7j2K95TIAAAQIECBDoREABsBM11xAgQIAAAQIEGiRQ1pDbb7+kTAG+/vqqEHjmmcnjj1fTScuU0p12ShZZZEwxcPnlTTEdyC4ua/pdcklV9PvNb5Innnj93RdbLCk7O6+7bvLRj77+Nd8RIECAAAECBN6pgALgOxVs2fXX9/3VcN555/WtH3Rnhg0b1rfr4KxZrO831nX65qcsuuiiLdOQLgECBAgQaJZAmSK89NLVx9FHV8W/889Pfvvb5MEHkzvuqD6OOqraWKLsOFtGB66+uqnCb7enR4xIbr45ufzy5E9/qtbye/75MXcpfbHsslXRb+21E6Mvx9h4RIAAAQIECAy8gALgwJv27B2PO+64nHPOOa/L73//93/7Fqf+Qy677LJstdVWWX/99V/3um8IECBAgACBegqUTUJGT/0t69D9/e/JBRdUxcBrr03fG33JL35RfZRi1eKLJ8stVxWtPvWpalOK8ryjEigFv7/9bUzB789/Tp555vU6xbxMuS4j/dZaq9ql+fVn+I4AAQIECBAgMDgCCoCD49pzdz377LNfK/4ts8wy2XTTTTP33HP37UR3T37wgx/ktttuy0knndT/3Kc//emey19CBAgQIECglwVKIe9jH6s+vvGNamrw739fFQQvuqjaTfimm5LycfzxlUTfrwH9I9jKKLby8fGPJ2XTirYczz6b3HJLcs011Qi/sqbfGwt+xeIDH0hWXDFZeeVqJOXMM7dFSJ4ECBAgQIBAnQSG9I3c6nvP10Fg/ALP9P02u2HfKtQvvPBC3y/3H8+RRx7ZtwvdZK9d8PLLL2fLLbfM/fffn7nmmiunnXZapixvcU/geOyxx7Le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AQIECBBohoACYDP6SZQECBAgQIAAAQIECBAgQIAAAQIEOhJQAOyIzUUECBAgQIAAAQIECBAgQIAAAQIEmiGgANiMfhIlAQIECBAgQIAAAQIECBAgQIAAgY4EpujoKhc1RuD+++/PNddck5tvvjn//ve/8+STT/bHPttss2XRRRfNaqutlqWWWmqi8nnsscdy9tln59prr015PPXUU2f++efPf/3Xf2WNNdbI5JNPPlH3cRIBAgQIECBAgAABAgQIECBAgED3BBQAu2fd9ZZKse7EE0/8/+3de7BVZf0H4JerXEJBNBQUJkYRSMSISQJDaWTK7A9yGi2pgaZwmEG7aI06FpfSEVOb0i5UY4lTGTalTjbkqMEwSmFIU4CiNRZegMALcpGLAb/e9Zu9O8A+h3XOOufs9Z7zrJk9Z+213net73pet5vzOetSc79btmwJ8fWHP/whTJ48Odx4442hZ8+eNdvGhWvWrAnz5s0Lu3btqrbZt29fWLduXfZ67LHHwsKFC0OfPn2q680QIECAAAECBAgQIECAAAECBAjUX0AAWP8xaLMK3nrrrWzbgwcPzs7SGzduXBgyZEjo3r17eP7558PPfvaz8Le//S2sWLEiO3tv7ty5NWvZtGlTiOt2794dBg4cGObMmRPGjh0b4vYffvjhsGTJkrB27dpw8803Z6+aG7GQAAECBAgQIECAAAECBAgQIECgLgICwLqwt89OY9g3f/787Ay/Ll26HLbTeNlvDASvv/76sHr16rBs2bJw2WWXhZEjRx7WLr65++67s/AvniF4xx13hGHDhmVt4mXEs2fPzi4Fvvfee8PKlSuzbY0fP/6obVhAgAABAgQIECBAgAABAgQIECBQHwEPAamPe7vsNd6b74ILLghHhn+Vncd79n3uc5+rvA2rVq2qzldm3nzzzbB8+fLs7cUXX1wN/yrr48/p06eHfv36ZYsefPDBhqvMEyBAgAABAgQIECBAgAABAgQI1FlAAFjnAaj37t/1rndVS3j11Ver85WZ+ACRgwcPZm+nTJlSWXzYz3hm4KRJk7Jl8WzCeG9AEwECBAgQIECAAAECBAgQIECAQDkEBIDlGIe6VfHGG29U9923b9/qfGUm3iswTl27dg2jRo2qLD7qZ3yicJxi+Ldx48aj1ltAgAABAgQIECBAgAABAgQIECBQHwEBYH3cS7PX+ACQynT22WdXZqs/X3zxxWw+PvyjqacExweNVKZKn8p7PwkQIECAAAECBAgQIECAAAECBOonIACsn33d9xzv7xefBBynQYMGhfPOO++ommKbOA0YMOCodQ0X9O/fv/p2x44d1XkzBAgQIECAAAECBAgQIECAAAEC9RUQANbXv257P3DgQLjppptCJay76qqrQo8ePY6qZ+/evdmyps7+iw2OO+64at89e/ZU580QIECAAAECBAgQIECAAAECBAjUV6B7fXdv7xWB/fv3hy1btlTetujnCSecEOIrz/S9730vxAd2xOljH/tYOP/882t2O3ToULa8sScJ1+xkIQECBAgQIECAAAECBAgQIECAQGkEBIAlGYp437xZs2YVqmbGjBlh5syZx9zG4sWLwwMPPJC1+8AHPhDmzJnTaJ/evXtn6471ZN+G6yt9Gt2oFQQIECBAgAABAgQIECBAgAABAu0mIABsN+py7OhXv/pVuOeee7Jixo8fH772ta+Fbt26NVpc5YzChk8LrtV4+/bt1cXHH398dT7PzM6dO6uXItdqHy8vbniJca02lhEgQIAAAQIECBAgQIAAgc4qEE/KaXhiTkOH+Du3iYAAsCT/DZxxxhlh2bJlbVrNb3/72/D9738/28c555wTvvGNb9S871/DIoYOHRqefvrp8Nprr4V4mXJj9wLcvHlztVvs05xp9OjRTTafN29emD9/fpNtrCRAgAABAgQIECBAgAABAp1V4JZbbgkLFizorIfvuHMICABzIHWEJo8++mj49re/nR3KyJEjQ/yfQ69evY55aCNGjMjaHDx4MGzYsCHE4LDWtH79+mxxPFNv2LBhtZo0uuyZZ54JQ4YMaXS9s/8apbGCAAECBAgQIECAAAECBAiEG264IVxzzTU1JV555ZVwrBNvana0sEMJCAA71HDWPpgVK1aEhQsXhhjiDR8+PNx6662hT58+tRsfsXTChAmha9euWd94hmKtADCeGbhy5cqsZ7ysuLmBXb9+/UJzLxs+okxvCRAgQIAAAQIECBAgQIBApxWIv4c39rv4jh07Oq2LA/+fQNf/zZrriAJPPfVUuOmmm7IA7/TTTw+33357s8K2/v37hwsvvDCjWbp0aYgPKzlyuu+++6r38Js2bdqRq70nQIAAAQIECBAgQIAAAQIECBCoo4AAsI74bb3rtWvXhrlz54a33347nHTSSVkQGC/73bNnT81XYzcM/exnPxv69u2b3VD02muvDcuXLw+vv/56iKcR//CHPwzxqcJxmjhxYohnAJoIECBAgAABAgQIECBAgAABAgTKI+AS4PKMRatX8rvf/a76FKBXX301zJgxo8l9jB07tnqfwIYNBw8eHL7+9a+H+DCOuJ1aNxYdM2ZMuPHGGxt2M0+AAAECBAgQIECAAAECBAgQIFACAQFgCQYhhRLGjRsXfvKTn4QlS5aEVatWha1bt2b3F4gP/Jg6dWq45JJLQrdu3VI4FDUSIECAAAECBAgQIECAAAECBDqVQJf/PtjhUKc6YgdbCoFt27aFyy67LKvlpZdeCqeddlop6lIEAQIECBAgQIAAAQIECBDoSAIvv/xyiM8EiNP9998fTj755I50eI4lp4B7AOaE0owAAQIECBAgQIAAAQIECBAgQIBAigICwBRHTc0ECBAgQIAAAQIECBAgQIAAAQIEcgoIAHNCaUaAAAECBAgQIECAAAECBAgQIEAgRQEBYIqjpmYCBAgQIECAAAECBAgQIECAAAECOQUEgDmhNCNAgAABAgQIECBAgAABAgQIECCQooAAMMVRUzMBAgQIECBAgAABAgQIECBAgACBnAICwJxQmhEgQIAAAQIECBAgQIAAAQIECBBIUUAAmOKoqZkAAQIECBAgQIAAAQIECBAgQIBATgEBYE4ozQgQIECAAAECBAgQIECAAAECBAikKCAATHHU1EyAAAECBAgQIECAAAECBAgQIEAgp4AAMCeUZgQIECBAgAABAgQIECBAgAABAgRSFBAApjhqaiZAgAABAgQIECBAgAABAgQIECCQU0AAmBNKMwIECBAgQIAAAQIECBAgQIAAAQIpCggAUxw1NRMgQIAAAQIECBAgQIAAAQIECBDIKSAAzAmlGQECBAgQIECAAAECBAgQIECAAIEUBQSAKY6amgkQIECAAAECBAgQIECAAAECBAjkFBAA5oTSjAABAgQIECBAgAABAgQIECBAgECKAgLAFEdNzQQIECBAgAABAgQIECBAgAABAgRyCggAc0JpRoAAAQIECBAgQIAAAQIECBAgQCBFAQFgiqOmZgIECBAgQIAAAQIECBAgQIAAAQI5BQSAOaE0I0CAAAECBAgQIECAAAECBAgQIJCigAAwxVFTMwECBAgQIECAAAECBAgQIECAAIGcAgLAnFCaESBAgAABAgQIECBAgAABAgQIEEhRQACY4qipmQABAgQIECBAgAABAgQIECBAgEBOAQFgTijNCBAgQIAAAQIECBAgQIAAAQIECKQoIABMcdTUTIAAAQIECBAgQIAAAQIECBAgQCCngAAwJ5RmBAgQIECAAAECBAgQIECAAAECBFIUEACmOGpqJkCAAAECBAgQIECAAAECBAgQIJBTQACYE0ozAgQIECBAgAABAgQIECBAgAABAikKCABTHDU1EyBAgAABAgQIECBAgAABAgQIEMgpIADMCaUZAQIECBAgQIAAAQIECBAgQIAAgRQFBIApjpqaCRAgQIAAAQIECBAgQIAAAQIECOQUEADmhNKMAAECBAgQIECAAAECBAgQIECAQIoCAsAUR03NBAgQIECAAAECBAgQIECAAAECBHIKCABzQmlGgAABAgQIECBAgAABAgQIECBAIEUBAWCKo6ZmAgQIECBAgAABAgQIECBAgAABAjkFBIA5oTQjQIAAAQIECBAgQIAAAQIECBAgkKKAADDFUVMzAQIECBAgQIAAAQIECBAgQIAAgZwCAsCcUJoRIECAAAECBAgQIECAAAECBAgQSFFAAJjiqKmZAAECBAgQIECAAAECBAgQIECAQE4BAWBOKM0IECBAgAABAgQIECBAgAABAgQIpCggAExx1NRMgAABAgQIECBAgAABAgQIECBAIKeAADAnlGYECBAgQIAAAQIECBAgQIAAAQIEUhQQAKY4amomQIAAAQIECBAgQIAAAQIECBAgkFNAAJgTSjMCBAgQIECAAAECBAgQIECAAAECKQoIAFMcNTUTIECAAAECBAgQIECAAAECBAgQyCkgAMwJpRkBAgQIECBAgAABAgQIECBAgACBFAUEgCmOmpoJECBAgAABAgQIECBAgAABAgQI5BQ7vimwAAAZF0lEQVQQAOaE0owAAQIECBAgQIAAAQIECBAgQIBAigICwBRHTc0ECBAgQIAAAQIECBAgQIAAAQIEcgoIAHNCaUaAAAECBAgQIECAAAECBAgQIEAgRQEBYIqjpmYCBAgQIECAAAECBAgQIECAAAECOQUEgDmhNCNAgAABAgQIECBAgAABAgQIECCQooAAMMVRUzMBAgQIECBAgAABAgQIECBAgACBnAICwJxQmhEgQIAAAQIECBAgQIAAAQIECBBIUUAAmOKoqZkAAQIECBAgQIAAAQIECBAgQIBATgEBYE4ozQgQIECAAAECBAgQIECAAAECBAikKCAATHHU1EyAAAECBAgQIECAAAECBAgQIEAgp4AAMCeUZgQIECBAgAABAgQIECBAgAABAgRSFBAApjhqaiZAgAABAgQIECBAgAABAgQIECCQU0AAmBNKMwIECBAgQIAAAQIECBAgQIAAAQIpCggAUxw1NRMgQIAAAQIECBAgQIAAAQIECBDIKSAAzAmlGQECBAgQIECAAAECBAgQIECAAIEUBQSAKY6amgkQIECAAAECBAgQIECAAAECBAjkFBAA5oTSjAABAgQIECBAgAABAgQIECBAgECKAgLAFEdNzQQIECBAgAABAgQIECBAgAABAgRyCggAc0JpRoAAAQIECBAgQIAAAQIECBAgQCBFAQFgiqOmZgIECBAgQIAAAQIECBAgQIAAAQI5BQSAOaE0I0CAAAECBAgQIECAAAECBAgQIJCigAAwxVFTMwECBAgQIECAAAECBAgQIECAAIGcAgLAnFCaESBAgAABAgQIECBAgAABAgQIEEhRQACY4qipmQABAgQIECBAgAABAgQIECBAgEBOAQFgTijNCBAgQIAAAQIECBAgQIAAAQIECKQoIABMcdTUTIAAAQIECBAgQIAAAQIECBAgQCCngAAwJ5RmBAgQIECAAAECBAgQIECAAAECBFIUEACmOGpqJkCAAAECBAgQIECAAAECBAgQIJBTQACYE0ozAgQIECBAgAABAgQIECBAgAABAikKCABTHDU1EyBAgAABAgQIECBAgAABAgQIEMgpIADMCaUZAQIECBAgQIAAAQIECBAgQIAAgRQFBIApjpqaCRAgQIAAAQIECBAgQIAAAQIECOQUEADmhNKMAAECBAgQIECAAAECBAgQIECAQIoCAsAUR03NBAgQIECAAAECBAgQIECAAAECBHIKCABzQmlGgAABAgQIECBAgAABAgQIECBAIEUBAWCKo6ZmAgQIECBAgAABAgQIECBAgAABAjkFBIA5oTQjQIAAAQIECBAgQIAAAQIECBAgkKKAADDFUVMzAQIECBAgQIAAAQIECBAgQIAAgZwCAsCcUJoRIECAAAECBAgQIECAAAECBAgQSFFAAJjiqKmZAAECBAgQIECAAAECBAgQIECAQE4BAWBOKM0IECBAgAABAgQIECBAgAABAgQIpCggAExx1NTcpMC+ffvC/PnzQ/xpIkCgYwn4fHes8XQ0BBoK+Hw31DBPoGMJ+Hx3rPF0NAQIpCkgAExz3FTdhED8B8aCBQsEgE0YWUUgVQGf71RHTt0Eji3g831sIy0IpCrg853qyKmbAIGOJCAA7Eij6VgIECBAgAABAgQIECBAgAABAgQIHCEgADwCxFsCBAgQIECAAAECBAgQIECAAAECHUlAANiRRtOxECBAgAABAgQIECBAgAABAgQIEDhCQAB4BIi3BAgQIECAAAECBAgQIECAAAECBDqSgACwI42mYyFAgAABAgQIECBAgAABAgQIECBwhED3I957S6BdBA4cOFDdz+bNm6vzrTGzc+fObDOvvPJK2LFjR2ts0jYIECiJgM93SQZCGQTaQMDnuw1QbZJASQR8vksyEMrotAINf+du+Lt4pwXppAcuAOykA1/vw96+fXu1hPe9733V+dacGT16dGtuzrYIECiRgM93iQZDKQRaWcDnu5VBbY5AiQR8vks0GErptALxd/FTTjml0x5/Zz5wlwB35tF37AQIECBAgAABAgQIECBAgAABAh1eoMuyZcsOdfijdIClE9i/f3944YUXsrr69+8funXrVroaFUSAAAECBAgQIECAAAECBFIXiJf9Vq7CGz58eOjZs2fqh6T+FggIAFuApgsBAgQIECBAgAABAgQIECBAgACBVARcApzKSKmTAAECBAgQIECAAAECBAgQIECAQAsEBIAtQNOFAAECBAgQIECAAAECBAgQIECAQCoCAsBURkqdBAgQIECAAAECBAgQIECAAAECBFogIABsAZouBAgQIECAAAECBAgQIECAAAECBFIREACmMlLqJECAAAECBAgQIECAAAECBAgQINACAQFgC9B0IUCAAAECBAgQIECAAAECBAgQIJCKQPdUClUngWMJbN++PTz77LNhw4YN1deOHTuybjNmzAgzZ8481iaq67dt2xbuv//+8Kc//SnE+eOOOy4MHTo0TJ06NVxyySWhW7du1bZmCBCov8AXv/jF8Ne//vWYhUybNi184QtfOGY7DQgQaD+Bp556Kjz00EPhueeeC/F7e8CAAWHMmDHh0ksvDaNHj26/QuyJAIFWEdiyZUv45Cc/mWtbixYtCmeddVauthoRIECAQDEB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BAgQIFBqAQFgqYdHcQQIECBAgAABAgQIECBAgAABAgSKCQgAi/npTYAAAQIECBAgQIAAAQIECBAgQKDUAgLAUg+P4ggQIECAAAECBAgQIECAAAECBAgUExAAFvPTmwABAgQIECBAgAABAgQIECBAgECpBQSApR4exREgQIAAAQIECBAgQIAAAQIECBAoJiAALOanNwECBAgQIECAAAECBAgQIECAAIFSCwgASz08iiNAgAABAgQIECBAgAABAgQIECBQTEAAWMxPbwIECBAgQIAAAQIECBAgQIAAAQKlFhAAlnp4FEeAAAECBAgQIECAAAECBAgQIECgmIAAsJif3gQIECBAgAABAgQIECBAgAABAgRKLSAALPXwKI4AAQIECBAgQIAAAQIECBAgQIBAMQEBYDE/vQkQIECAAAECBAgQIECAAAECBAiUWkAAWOrhURwBAgQIECBAgAABAgQIECBAgACBYgICwGJ+ehMgQIAAAQIECBAgQIAAAQIECBAotYAAsNTDozgCBAgQIECAAAECBAgQIECAAAECxQQEgMX89CZAgAABAgQIECBAgAABAgQIECBQagEBYKmHR3EECBAgQIAAAQIECBAgQIAAAQIEigkIAIv56U2AAAECBAgQIECAAAECBAgQIECg1AICwFIPj+IIECBAgAABAgQIECBAgAABAgQIFBMQABbz05sAAQIECBAgQIAAAQIECBAgQIBAqQUEgKUeHsURIECAAAECBAgQIECAAAECBAgQKCYgACzmpzcBAgQIECBAgAABAgQIECBAgACBUgsIAEs9PIojQIAAAQIECBAgQIAAAQIECBAgUExAAFjMT28CBAgQIECAAAECBAgQIECAAAECpRYQAJZ6eBRHgAABAgQIECBAgAABAgQIECBAoJiAALCYn94ECBAgQIAAAQIECBAgQIAAAQIESi0gACz18CiOAAECBAgQIECAAAECBAgQIECAQDEBAWAxP70JECBAgAABAgQIECBAgAABAgQIlFpAAFjq4VEcAQIECBAgQIAAAQIECBAgQIAAgWICAsBifnoTIECAAAECBAgQIECAAAECBAgQKLWAALDUw6M4AgQIECBAgAABAgQIECBAgAABAsUEBIDF/PQmQIAAAQIECBAgQIAAAQIECBAgUGoBAWCph0dxBAgQIECAAAECBAgQIECAAAECBIoJCACL+elNgAABAgQIECBAgAABAgQIECBAoNQCAsBSD4/iCBAgQIAAAQIECBAgQIAAAQIECBQTEAAW89ObAAECBAgQIECAAAECBAgQIECAQKkFBIClHh7FESBAgAABAgQIECBAgAABAgQIECgmIAAs5qc3AQIECBAgQIAAAQIECBAgQIAAgVILCABLPTyKI0CAAAECBAgQIECAAAECBAgQIFBMQABYzE9vAgQIECBAgAABAgQIECBAgAABAqUWEACWengUR4AAAQIECBAgQIAAAQIECBAgQKCYgACwmJ/eBAgQIECAAAECBAgQIECAAAECBEotIAAs9fAojgABAgQIECBAgAABAgQIECBAgEAxAQFgMT+9CRAgQIAAAQIECBAgQIAAAQIECJRaQABY6uFRHAECBAgQIECAAAECBAgQIECAAIFiAgLAYn56EyBAgAABAgQIECBAgAABAgQIECi1gACw1MOjOAIECBAgQIAAAQIECBAgQIAAAQLFBASAxfz0JkCAAAECBAgQIECAAAECBAgQIFBqAQFgqYdHcQQIECBAgAABAgQIECBAgAABAgSKCQgAi/npTYAAAQIECBAgQIAAAQIECBAgQKDUAgLAUg+P4ggQIECAAAECBAgQIECAAAECBAgUExAAFvPTmwABAgQIECBAgAABAgQIECBAgECpBQSApR4exREgQIAAAQIECBAgQIAAAQIECBAoJiAALOanNwECBAgQIECAAAECBAgQIECAAIFSCwgASz08iiNAgAABAgQIECBAgAABAgQIECBQTEAAWMxPbwIECBAgQIAAAQIECBAgQIAAAQKlFhAAlnp4FEeAAAECBAgQIECAAAECBAgQIECgmIAAsJif3gQIECBAgAABAgQIECBAgAABAgRKLSAALPXwKI4AAQIECBAgQIAAAQIECBAgQIBAMQEBYDE/vQkQIECAAAECBAgQIECAAAECBAiUWkAAWOrhURwBAgQIECBAgAABAgQIECBAgACBYgICwGJ+ehMgQIAAAQIECBAgQIAAAQIECBAotYAAsNTDozgCBAgQIECAAAECBAgQIECAAAECxQQEgMX89CZAgAABAgQIECBAgAABAgQIECBQaoH/A0OGuJ4QZ3DdAAAAAElFTkSuQmCC" width="640">



    interactive(children=(FloatSlider(value=1.0, description='A', max=4.0, min=-4.0), FloatSlider(value=0.0, descr…



```python

```
