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

1. `string.capwords ` In Python, `string capwords()`method is used to capitalize all the words in the string using `split()` method.
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

思路3：我的笨方法，找出分别以数列中每个数字为起点的序列中的最大和

## 16*

```python
def sum_pairs(ints, s):
    new_set=set()
    for num in ints:
        if s-num in new_set:
            return [s-num,num]
        new_set.add(num)
```

1. 思路：对`list` 的每一个`num`进行遍历，如果`s-num`在`new_set` 里面直接`return`，如果不在，则把`num`装进去，看看能不能作为后面的`num`的`s-num`

2. `set()`函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。

   ```python
   x=set([1,2,3,3])
   y=set([3,3,3,1])
   x & y # 交集
   x | y # 并集
   x - y # 差集
   ```

3. `set.add(element)` 

4. 当没有return出口的时候，`python` 返回`None`

## 17

```python
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]
```

1. 原来`split()`括号中的字符不存在于字符串的时候不会报错
2. 多个`split()` 连用

## 18

```python
def make_readable(seconds):
    hours, seconds = divmod(seconds, 60 ** 2)
    minutes, seconds = divmod(seconds, 60)
    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)
```

1. `divmod(a,b)` 返回 `(a//b,a%b)`

2. `format`函数，基本语法是通过 `{}` 和` :` 来代替以前的 `%` 。

   `format` 函数可以接受不限个参数，位置可以不按顺序。

   ```python
   class AssignValue(object):
       def __init__(self, value):
           self.value = value
   my_value = AssignValue(6)
   print('value 为: {0.value}'.format(my_value)) # "0" 是可选的
   
   my_list = ['菜鸟教程', 'www.runoob.com']
   print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))
   print("网站名：{my_list[0]}, 地址 {my_list[1]}".format(my_list=my_list))
   # "0" 是必须的
   ```

   

## 19*

```python
def who_is_next(names, r):
    while r > len(names):
        r = (r - len(names) + 1) // 2
    return names[r-1]
```



## 20(学完面向对象回看此题)

```python
# codewar Function Addition
```







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

# Leetcode

## 01 寻找括号对

思路1：从连着的括号对开始逐一删除，如果最后s为空，则True，or False

```python
class Solution:
    def isValid(self, s: str) -> bool:
        while ("()" in s) or ("[]" in s) or ("{}" in s):
                s.replace("()","")
                s.replace("[]","")
                s.replace("{}","")
        return len(s)==0
```

思路2：当遇到每个左括号时，储存其对应的右括号于list中，如果从后面的s 中不能   **按序**  一一对应，则False, or True

```python
class Solution:
    def isValid(self,s):
        stack = []
        map = {
            "{":"}",
            "[":"]",
            "(":")"
        }
        for x in s:
            if x in map:
              stack.append(map[x])
            else:
                if len(stack)!=0:
                top_element = stack.pop()
                # 让top等于末尾数据后，再删去末尾数据
                    if x != top_element:
                        return False
                    else:
                        continue
                else:
                    return False
        return len(stack) == 0
    	# 当判断到最后一对括号也正确时从这个出口返回
```

## 02 733图像渲染

```python
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        originColor=image[sr][sc]
        if originColor==newColor:
            return image
        m,n=len(image),len(image[0])
        quenue=[(sr,sc)]
        DIR=[(0,1),(0,-1),(-1,0),(1,0)]
        # 当遍历DIR时，可以让点改变上下左右改变位置
        while queue:
            position=queue.pop()
            # 当用完该数据就删除，与while条件相对应
            image[position[0]][position[1]]=newColor
            for direct in DIR:
                x=position[0]+direct[0]
                y=position[1]+direct[1]
                if x>=0 and x<m and y>=0 and y<n:
                    if image[x][y]==originColor:
                        queue.append([x,y])
                        # 与pop操作相对应
        return image
```

spotlight: 运用了queue和DIR

## 03 1507 Reformat Date

```python
class Solution:
    def reformatDate(self, date: str) -> str:
        day, month, year = date.split(' ')
        MonthDict = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        month = MonthDict[month]
        day = day[:2] if day[1].isdigit() else '0' + str(day[0])
        return '-'.join([year,month,day])
```

常规题，主要学习写法

## 04 1337 The K Weakest Rows in a Matrix

```python
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        num_list=[]
        for i in range(0,len(mat)):
            num_list.append((i,sum(mat[i])))
        num_list=sorted(num_list,key=lambda x:(x[1],x[0]))
        # 表示先按元组第二个数排序，相同的再按第一个排序
        return [n[0] for n in num_list[:k]]
    	# 打印每个元组的第一个数字
```

用list装元组，每个元组`(i，j)`表示第`i`行，和为`j`。然后再排序，用一个`for` 循环来`return`

## 05 1260. Shift 2D Grid

二维数字网格迁移，观察到可以通过展开成一维数组逐个往后迁移，再将最后一个元素通过list切片和相加的方法合成一个新的一维数组。再用一次循环，对新的一维数组切片，装入新的二维数组

## 06 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence

```python
class Solution:
    def isPrefixOfWord(self, sentence, searchWord):
        for num, word in enumerate(sentence.split(), 1):
            if word.startswith(searchWord):
                return num
        return -1
```

1. `enumerate() `函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。

   `enumerate(sequence, [start=0])` start用于设置第一个下标的数字，默认为0

2. `str.startswith(str, beg=0,end=len(string))` bed & end 用于指定搜索范围即字符串检索的起始和终止位置。



## 07 面试题 16.07. Maximum LCCI

```python
class Solution:
    def maximum(self, a: int, b: int) -> int:
        return int(((a + b) + abs(a - b)) / 2)
```

从该题中学习了，`max(a,b)` 的本质是补齐a、b之间的相对距离

## 08 面试题 16.11. Diving Board LCCI

排列组合问题，考虑总排列数为0，或者两个组合数相同的情况，剩下的就是`range` ，从全是较小数到全是最大数，间隔为 `longer-shorter`

## 09 面试题 16.15. Master Mind LCCI

```python
class Solution:
    def masterMind(self,solution,guess):
        a = b = 0
        index = []
        count_s = collections.Counter()
        for i in range(4):
            if solution[i] == guess[i]:
                a += 1
            else:
                index.append(i)
                count_s[solution[i]] += 1
                # 空Counter可以直接进行初始化，这点与list不同
        
        for i in index:
            if count_s[guess[i]] > 0:
                count_s[guess[i]] -= 1
                b += 1
                
        return [a, b] 
```

1. Counter计数器用法:对传入的对象进行计数

   ```python
   import collections
   # 可以建立一个空counter
   c=collections.Counter()
   # 创建的时候传进去一个迭代器（数组，字符串，字典等）
   c=collections.Counter("frank")
   c=collections.Counter({"red":0,"green":1})
   c=collections.Counter(cat=4,dog=1) #传入参数，cat相当于一个对象，4代表个数
   
   c=collections.Counter(a=2,b=2)
   sorted(c.elements())
   # print['a','a','b','b']
   #elements()在元素上返回一个迭代器，as many times as its count
   ```

2. 思路总结：

   分别对猜中和伪猜中用两个变量进行记录。当不是猜中的时候，有可能是猜错或者伪猜中，此时用list记录非猜中时候的索引数，并且把solutions里面的元素分类且计数。然后对非猜中的元素，通过索引数进行遍历，如果该元素在Counter里的计数不为0，则符合一次伪猜中，记录一次伪猜中的同时，删除一次该元素对应的Counter

## 10 面试题 16.17. 连续数列

经典题。假设第一个数为最大和，对后面的数字进行遍历，在前后俩数字的和与后一个数字之间取一个最大，为的是找起点，再对之前记录的最大和与现在得到的和取一个最大值。

## 11 剑指 Offer 29. 顺时针打印矩阵

```python
class Solution:
    def spiralOrder(self, matrix):
        res=[]
        while matrix:
            res+=matrix.pop(0)
            matrix=list(zip(*matrix))[::-1]
            # matrix=[(6,9),(5,8),(4,7)]
            # matrix=[(8,7),(5,4)]
        return res
```

1. `zip()` 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。我们可以使用 `list()` 转换来输出列表。如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
2. `zip(*c)`与`zip(a,b)` 的区别是c可以是一个二维数组，而a,b是一维数组

## 12 [剑指 Offer 10- II. 青蛙跳台阶问题]

按最后一跳是跳1或者2级台阶为分类依据，可以推出斐波那契数列，
f(n)=f(n-1)+f(n-2)。设一个元组（a,b），在range(n-1)循环中，顺着数列方向逐个替换ab的值，最后用b%1000000007是为了不超出int范围