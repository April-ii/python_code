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

## 08

```python
def solve(s):
    return s.upper() if sum(map(str.isupper, s)) * 2 > len(s) else s.lower()
```

当比较一个word里面大小写字母数量时候，可以借鉴的思路

## 09

优化后的代码

```python
def valid_parentheses(string):
    count = 0
    for i in string:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0
```

我的代码

```python
# Valid Parentheses
def valid_parentheses(s):
    p_left=0
    p_right=0
    for p in list(s):
        if p=="(":
            p_left+=1
        elif p==")":
            p_right+=1
        if p_left<p_right:
            break
    if p_right==p_left: 
        return True
    else:
        return False
```

逻辑上大体相同，但别人只有了一个count，通过加减来比较，变量更少，利用空间更小

## 10

```python
def title_case(title, minor_words=''):
    title=title.capitalize().split(" ") # 先将第一个单词的首字母大写
    # capitalize() 的作用是将字符串的首字母大写,并且其他字母全部小写
    minor_words=minor_words.lower().split(" ")
    # 将传入的exception 全部小写

    final_list=[]
    for word in title:
        if word not in minor_words:
            word=word.capitalize()
        final_list.append(word)
    return " ".join(final_list)

```

1. 没有认真审题。将第二个参数强改为列表，解释器出现错误
2. 思量再三。最后return 结果时，新建一个list，会比直接join\if\else\for\in 用在一行更美观易懂

## 11

```python
def iq_test(numbers):
    list_judge=[int(num)%2 for num in numbers.split(" ")]
    return (list_judge.index(0) if list_judge.count(0)==1 
            else list_judge.index(1))+1
```

1. spotlight: 将奇数偶数全部变成0\1 list

2. 学习到了 `list.count()` 的用法

   ```python
   # 注意这个例子
   string="recede"
   for ch in list(string):
       print(list(string).count(ch))
   # 打印结果为 1 3 1 2 1 1
   ```

   

## 12

```python
def solution(roman):
    d={'I':1, 'V':5 ,'X':10, 'L':50 ,'C':100, 'D':500,'M':1000}
    
    return reduce(lambda x,y: x+y if x>=y else y-x , (d[c] for c in roman))
```

1. `lambda` 可以接收任意数量的参数，但只能有一个表达式

   ```python
   x=lambda a,b: a*b
   print(x(5,6)) # 30
   ```

2. `reduce(function,iterable[,initializer]])` : 用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。

   python3中必须用`from functools import reduce` 



## 13

```python
def duplicate_encode(word):
    return "".join(["(" if word.count(c)==1 else ")" for c in list(word.lower())])
```

1. `str.count()` 和 `list.count()` 在`for` 循环中有区别，详情请对比11



## 14

```python
def anagrams(word, words):
    return [item for item in words if 	sorted(word)==sorted(item)]
```

1. 学习思路：通过排序更简便的比较两个单词所包含的字母是不是相同

2. `sorted()` 函数：`sorted(iterable, key=None, reverse=False) `

   补充：sort 与 sorted 的区别在于，sort 只能用于 list, 而sorted 可以用于任意可迭代对象



## 15*

寻找最大子序列和

思路1

```python
def maxSequence(arr):
    maxl = 0
    maxg = 0
    for n in arr:
        maxl = max(0, maxl + n)
        maxg = max(maxg, maxl)
    return maxg
```

1. 最开始将子序列起点设为第一个数字。在子序列和成为负数之前，可求该子序列的最大和并保存为max。成为负数后，直接从最后一个负数之后那个数字作为起点，以此类推

思路2

```python
def maxSequence(arr):
    lowest = ans = total = 0
    for i in arr:
        total += i
        lowest = min(lowest, total)
        ans = max(ans, total - lowest)
    return ans
```

1. 通过起点从第一个数开始的子序列和减去和最小的子序列，从而得到和最大的子序列



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

