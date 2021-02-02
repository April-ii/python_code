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
ls=sorted(ls.items(),key=lambda x:x[1],reverse=True)
for elem in ls:
    fi.write("{}:{}".format(elem[0],elem[1]))
fi.close()
```

### 46(1)

```python
fi=open("PY.txt",'r')
fo=open("PY2.txt",'w')
flag=False
for line in fi:
    if '【' in line:
        flag=False
    if '【原文】' in line:
        flag=True
        continue
    if flag==True:
        fo.write(line.lstrip())
fi.close()
fo.close()
```

### 46(2)

```python
fi=open("PY.txt",'r')
fo=open("PY2.txt",'w')
for line in fi:
    for i in range(1,23):
        # 分析文本可知共1~22种可能
        line=line.replace("({})".format(i),"")
        fo.write(line)
fi.close()
fo.close()
```

## 第四套

### 41

```python
nums=input("请输入四位数字：")
nls=nums.split(" ")
# 不一定是整数，所以不用int
# 但eval一般只用在字符串转数值上
x0=eval(nls[0])
y0=eval(nls[1])
x1=eval(nls[2])
y1=eval(nls[2])
print(pow(pow(x1-x0,2)+pow(y1-y0,2),0.5))
```

### 42

```python
import jieba
txt=input()
ls=jieba.lcut(txt)
print("{:.1f}".format(len(txt)/len(ls)))
```

### 43

```python
n=eval(input("请输入一个数字："))
print("{:+^11}".format(chr(n-1)+chr(n)+chr(n+1)))
```

### 45

```python
fi=open("PY.txt",'w')
d={}
sum=0
score=input().split(" ")
while score[0]!='':
    d[score[0]]=score[1]
    sum+=eval(score[1])
    score=input().split(" ")
ls=sorted(d.items())
maxi=ls[len(ls)-1][1]
mini=ls[0][1]
fi.write("最高分是{}，最低分是{}，平均分是{:.2f}".
         format(maxi,mini,sum/len(ls)))
fi.close()
```

## 第五套

### 41

```python
n=eval(input("请输入一个数字："))
ls=[0]
# 为了让ls[1]对应第一个字母而非第二个
for i in range(65,91):   #A-Z对应的Unicode
    ls.append(chr(i))
print("输出的字母是:",ls[n])
```

### 42

```python
s=input("请输入一个数字：")
num=int(s)
print("{:b}".format(num))
#十进制数字转化为二进制数字
```

### 44

```python
import turtle
turtle.color("red","yellow")
# 等同于pencolor(red)、fillcolor("yellow")
turtle.begin_fill()
for i in range(36):
    turtle.fd(200)
    turtle,turtle.left(170)
turtle.end_fill()
#画太阳花，每个尖锐角为10度
```

### 45

```python
fo=open("PY.txt",'w')
def isPrime(num):
    for i in range(2,num):
        #num=2是i取不到任何值
        if num%i==0:
            return False
    return True

ls=[51,33,54,56,67,88,431,111,141,72,45,2,78,13,15,5,69]
lis=[]
for i in ls:
    if not isPrime(i):
        lis.append(i)
fo.write("{},列表的长度{}".format(lis,len(lis)))
fo.close()
```

## 第六套

### 41

```python
line="After fresh rain in moutains bare"
print(line.title())
```

### 43

```python
num=eval(input("请输入数字："))
print("对应二进制数：{0:b}\n 八进制数：{0:o}\n 大写的十六进制数：{0:X}\n".format(num))
```

### 44

```python
import turtle
turtle.color("black","yellow")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()
```

## 第七套

### 41

```python
lis=[2,8,3,6,5,8,3]
new_lis=list(set(lis))
print(new_lis)
```

### 43

```python
def reverse_str(string):
    return string[::-1]
string='goodstudy'
print(reverse_str(string))
```

### 44

```python
import turtle
turtle.color("black","yellow")
turtle.begin_fill()
for i in range(5):
    turtle.fd(200)
    turtle.right(144)
turtle.end_fill()
#呜呜我运行出来五角星中间那块五边形是白色的
```

### 45

```python
na=eval(input("第一个整数："))
nb=eval(input("第二个整数："))
a=min(na,nb)
b=max(na,nb)
ls=[]
for i in range(a+1,b):
    for j in range(2,i):
        if i%j==0:
            break
            #跳出这一整个内层循环
    else:
        ls.append(i)
    #for else语句的else是指在正常执行了循环内部语句时执行
    #也就是没有遇到任何的break使循环终止
print(ls)
```

