## 第一套

### 41

```python
s=input(f'请输入一个字符串')
print("{:*^30}".format(s))
# *表示填充符号, ^表示居中
# 居中对齐 (:^)
# 靠左对齐 (:<)
# 靠右对齐 (:>)
```

### 42

```python
a,b=0,1
while a<=50:
    print(a,end=',')
    a,b=b,a+b
# 错误点，只输出a，所以while的判断条件是a
```

### 43

```python
import jieba
txt=input("请输入一段中文文本：")
ls=list(jieba.cut(txt))
# 或者 ls=jieba.lcut(txt)
for i in ls[::-1]:
    print(i,end='')
#循环中使得输出结果同行
```

### 44

```python
import turtle
for i in range(3):
    turtle.seth(i*120)
    turtle.fd(100)
```

### 45

```python
txt=input("请输入类型序列:")
names=txt.split(" ")
d={}
for i in names:
    d[i]=d.get(i,0)+1
ls=list(d.items())
ls.sort(key=lambda x: x[1],reverse=True)
for k in ls:
    print("{}:{}\n".format(k[0],k[1]))
```

### 46（1）

```python
fi=open("卖火柴的小女孩.txt",'r')
txt=fi.read()
d={}
exclude='，。！？、（）【】《》<>=：+-*—“”…'
for word in txt:
    if word in exclude: continue
    else:
        d[word]=d.get(word,0)+1
ls=list(d.items())
ls.sort(key=lambda x:x[1],reverse=True)
print("{}:{}".format(ls[0][0],ls[0][1]))
fi.close()
```

### 46（2）

```python
fi=open("卖火柴的小女孩.txt",'r')
fo=open("PY.txt",'w')
txt=fi.read()
d={}
for word in txt:
    d[word]=d.get(word,0)+1
del d["\n"]
ls=list(d.items())
ls.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    fo.write(ls[i][0])
fi.close()
fo.close()
```

### 46（3）

```python
fi=open("卖火柴的小女孩.txt",'r')
fo=open("PY.txt",'w')
txt=fi.read()
d={}
for word in txt:
    d[word]=d.get(word,0)+1
del d["\n"]
del d[" "]
ls=list(d.items())
ls.sort(key=lambda x:x[1],reverse=True)
for i in range(len(ls)):
    ls[i]="{}:{}".format(ls[i][0],ls[i][1])
fo.write(",".join(ls))
fi.close()
fo.close()
```

## 第二套

### 41

```python
import random
broadlist=['三星','vivo','魅族','苹果','OPPO']
random.seed(0)
name=broadlist[random.randint(0,4)]
#radint里面的参数是指随机数的区间范围
print(name)
```

### 42

```python
import jieba
s=input("请输入一个字符串：")
m=len(s)
n=len(jieba.lcut(s))
print("中文字符数为{},中文词语数为{}".format(m,n))
```

### 43

```python
num=eval(input("请输入件数："))
#input()输入的是str,eval返回的是值
if num==1:
    cost=150
elif num>=2 and num<=3:
    cost=int(0.9*150*num)
elif num>=4 and num<=9:
    cost=int(0.8*150*num)
else:
    cost=int(0.7*150*num)
print("总额为：",cost)
```

### 44

```python
import turtle 
for i in range(5):
    turtle.fd(200)
    turtle.right(144)
```



### 45

```python
fo=open("PY.txt","w")
data=input("请输入一组人员的姓名、性别、年龄：")
woman_num=0
age_num=0
person_num=0
while data:
    name,sex,age=data.split(" ")
    if sex=='女':
        woman_num+=1
    age_num+=int(age)
    person_num+=1
    data=input("请输入一组人员的姓名、性别、年龄：")
average_age=age_num/person_num
fo.write("平均年龄是{},女性人数{}".
         format(average_age,woman_num))
fo.close()
```

### 46(1)

```python
fi=open("festival.csv",'r')
ls=[]
for line in fi:
    ls.append(line.strip("\n").split(","))
    #strip移除字符串头尾指定的字符序列。返回移除字符串头尾指定的字符生成的新字符串
fi.close()
print(ls)
i=input("请输入节日名称：")
for line in ls:
    if line[1]==i:
        print("{}的日期是{}-{}".
              format(line[1],line[2],line[3]))
```

### 46(2)

```python
fi=open("festival.csv",'r')
ls=[]
for line in fi:
    ls.append(line.strip("\n").split(","))
    #strip移除字符串头尾指定的字符序列。返回移除字符串头尾指定的字符生成的新字符串
fi.close()
nums=input("请输入节日序号：").split(" ")
while True:
    for line in ls:
        for num in nums:
            if line[0]==num:
                print("{}{}的假期是{}月{}日到{}月{}日之间".
                format(line[1],line[0],line[2][:2],
                line[2][-2:],line[3][:2],line[3][-2:]))
    nums=input("请输入节日序号：").split(" ")
```

### 46(3)

```python
fi=open("festival.csv",'r')
ls=[]
for line in fi:
    ls.append(line.strip("\n").split(","))
    #strip移除字符串头尾指定的字符序列。返回移除字符串头尾指定的字符生成的新字符串
fi.close()
nums=input("请输入节日序号：").split(" ")
while True:
    for num in nums:
        if int(num)>4:
            print("输入的序号不合理！")
        for line in ls:
            if line[0]==num:
                print("{}{}的假期是{}月{}日到{}月{}日之间".
                format(line[1],line[0],line[2][:2],
                line[2][-2:],line[3][:2],line[3][-2:]))
    nums=input("请输入节日序号：").split(" ")
```



## 第三套

### 41

```python
n=eval(input("请输入正整数"))
print("{0:@>30,}".format(n))
```

### 45

```python
import collections
fi=open("PY.txt",'w')
ls=collections.Counter(input("请输入职业：").split(" "))
ls=dict(ls)
print(ls)
print(ls.items())
ls=sorted(ls.items(),key=lambda x:x[1],reverse=True)
for elem in ls:
    fi.write("{}:{}".format(elem[0],elem[1]))
fi.close()
```

