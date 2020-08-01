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
2. 注意此处，返回一个list时的格式

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

