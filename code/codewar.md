# codewar

## 01

```python
def binary_array_to_number(arr):
  return int("".join(map(str, arr)), 2)
```

1. `str.join(sequence)`  用于将序列中的元素以指定的字符连接生成一个新的字符串。

2. `map(function, iterable..)` 对序列中的每一个元素，调用function

3. `int ("010101",2)` 二进制转十进制 

   进制转换, 新发现的print用法

   ```python
   print("十进制数为：", dec)
   print("转换为二进制为：", bin(dec))
   print("转换为八进制为：", oct(dec))
   print("转换为十六进制为：", hex(dec))
   ```

## 02

```python
def filter_list(l):
  return [i for i in l if not isinstance(i, str)]
　# return [i for i in l if isinstance(i,int)]
```

1. `isinstance(object, classinfo)` ,判断一个对象是否是一个已知的类型
2. 注意此处，返回一个list时的格式。所以要用一个[ ]。

## 03

```python
import string
def toJadenCase(NonJadenStrings):
    return string.capwords(NonJadenStrings)
```

1. `string.capwords `In Python, `string capwords()`method is used to capitalize all the words in the string using `split()` method.
2. **Syntax:** `string.capwords(string, sep=None)`
   **Return Value:** `Returns a formatted string after above operations.` e
3. `sep`意思为seperate ,用于自定义间隔符

```python
def toJadenCase(string):        
    return " ".join(w.capitalize() for w in string.split())
```

1. `mystring.capitalize()` 字符串的第一个字母变成大写,其他字母变小写。
2. `mystring.split(str="", num=string.count(str))` str--分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等；num--分割次数。默认为 -1, 即分隔所有。



## 04

```python
def reverse_words(text):
    return " ".join(word[::-1] for word in text.split(" "))
```

1. `split(" ")` 出于严谨，其括号中的“　”不能省，否则容易出现意料之外的错误情况



## 05

```python
def high_and_low(numbers):
    num_list=[int(num) for num in numbers.split(" ")]
    return "%d %d" % (max(num_list),min(num_list))
```

1. 在numbers（字符串）转换为list 之前，必须将每个num变成int 类型。否则，max、min函数对字符进行比较，最小的可能是空格



## 06

```python
def get_sum(a,b):
    return sum(xrange(min(a,b), max(a,b)+1))
```

1. sum也太便捷了...
2. `xrange()` 函数用法与`range()` 完全相同，所不同的是生成的不是一个数组，而是一个生成器。但是`xrange`只在`python2.0+`版本中存在

## 07

```python
def oddOrEven(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'
```

好好学习一下，return 里面同时有if 和 while

# python 100

## 01

```python
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=",")
print("\b")
```

1. `range(start,stop,step) ` ,默认从０开始，默认步数为１
2. ` end=','  ` 间隔符号
3. `\b` 退格

## 02

```python
n = int(input())
def shortFact(x):
    return 1 if x <= 1 else x * shortFact(x - 1)
print(shortFact(n))
```

1. 递归（自己写不来系列......

## 03

```python
n=int(input())
print(num_dict={num:num**2 for num in range(1,n+1)})
```

最精妙的写法了...我什么时候才能自己写出这样的代码呢（叹气.jpg

## 04

```python
class IOstring:
    def __init__(self):
        pass

    def get_string(self):
        self.s = input()

    def print_string(self):
        print(self.s.upper())

xx = IOstring()
xx.get_string()
xx.print_string()
```

1. `str.upper()` 将字符串的小写字母改成大写字母
2. 原来 input() 也可以加在方法里面 

