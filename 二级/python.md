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

### 46(1)

```python
fi=open("sensor.txt",'r')
fo=open("PY2.txt",'w')
txt=fi.readlines()
for line in txt:
    ls=line.strip("\n").split(",")
    if ' earpa001' in ls:
        #debug的时候发现转为list之后，品牌名前有个空格
       fo.write("{},{},{},{}\n".
                format(ls[0],ls[1],ls[2],ls[3]))
fi.close()
fo.close()
```

### 46(2)

```python
from collections import Counter
# 这里第三方库不晓得能不能用哦
fi=open("PY2.txt",'r')
fo=open("PY.txt",'w')
txt=fi.readlines()
lis=[]
for line in txt:
    ls=line.strip("\n").split(",")
    lis.append("{}-{}".format(ls[2],ls[3]))
d=dict(Counter(lis))
lis=list(d.items())
for i in range(len(lis)):
    fo.write("{},{}\n".format(lis[i][0],lis[i][1]))
fi.close()
fo.close()
```

```python
fi=open("PY2.txt",'r')
fo=open("PY.txt",'w')
txt=fi.readlines()
d={}
for line in txt:
    ls=line.strip("\n").split(",")
    data=ls[-2]+"-"+ls[-1]
    d[data]=d.get(data,0)+1
lis=list(d.items())
for i in range(len(lis)):
    fo.write("{},{}\n".format(lis[i][0],lis[i][1]))
fi.close()
fo.close()
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

### 46(1)

```python
fi=open("arrogant.txt",'r')
fo=open("PY2.txt",'w')
txt=fi.read()
d={}
for s in txt:
    #统计的是英文字符数，而不是英文单词数
    d[s]=d.get(s,0)+1
del d['\n']
ls=list(d.items())
for i in range(len(ls)):
    fo.write("{}:{}\n".format(ls[i][0],ls[i][1]))
fi.close()
fo.close()
```

### 46(2)

```python
fi=open("arrogant.txt",'r')
fo=open("PY2.txt",'w')
txt=fi.read()
d={}
for s in txt:
    d[s]=d.get(s,0)+1
del d['\n']
ls=list(d.items())
ls=sorted(ls,key=lambda x:x[1],reverse=True)
for i in range(10):
    fo.write("{}:{}\n".format(ls[i][0],ls[i][1]))
fi.close()
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

### 46

```python
fi=open("score.csv",'r')
fo=open("PY.txt",'w')
ls=[]
avg=[]
sum=0
avg_score=0
for s in fi:
    ls.append(s.strip("\n").split(","))
for line in ls[1:]:
    sum=0
    for i in line[1:]:
        sum+=int(i)
        avg_score=sum/3
    fo.write("{}:{:.2f}\n".format(line[0],avg_score))
fi.close()
fo.close()
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

### 46(1)

```python
fo=open("PY2.txt",'w')
class Horse:
    def __init__(self,category,gender,age):
        self.age=age
        self.category=category
        self.gender=gender
        self.horse_speed=0
    def get_descriptive(self):
        info=("the category is:{},the gender is:{},the age is:{}\n".format(self.category,self.gender,self.age))
        fo.write(info)
    def update_speed(self,new_speed):
        self.horse_speed=new_speed
        fo.write("the new speed is "+str(self.horse_speed))
        #注意数值类型转化为字符类型

horse=Horse("Arab","male","12")
horse.get_descriptive()
horse.update_speed(50)
fo.close()
```

### 46(2)

```python
fo=open("PY2.txt",'w')
class Horse:
    def __init__(self,category,gender,age):
        self.age=age
        self.category=category
        self.gender=gender
        self.horse_speed=0
    def get_descriptive(self):
        info="the category is:{},the gender is:{},the age is:{}\n".format(self.category,self.gender,self.age)
        fo.write(info)
    def update_speed(self,new_speed):
        self.horse_speed=new_speed
        fo.write("the new speed is {}.".format(self.horse_speed))

class Camel(Horse):
    #Camel是Horse的子类
    def __init__(self, category, gender, age, hump):
        super().__init__(category, gender, age)
        self.hump_size=hump
    def describe_hump_size(self):
        fo.write("this camel has {} humps.".format(self.hump_size))


camel=Camel("Double Hump","female","20","4")
camel.get_descriptive()
camel.update_speed(40)
camel.describe_hump_size()
```

## 第八套

### 41

```python
animals=["duck","hen","monkey","cat"]
animals.reverse()
print(animals)
# 逆序输出
```

### 42

```python
s="   shisjwdeifhref      "
print(s.strip())
```

### 44

```python
import turtle
# 画四叶草
for i in range(4):
    turtle.seth(90*(i+1))
    turtle.circle(50,90)
    turtle.seth(90*(i-1))
    turtle.circle(50,90)
turtle.hideturtle()
# 绘制复杂图形时，隐藏海龟可以加快绘图速度
```

### 45

```python
import math
# 异常处理结构
try:
    a=eval(input("请输入底数："))
    b=eval(input("请输入真数："))
    c=math.log(b,a)
except ValueError:
    #传入无效参数
    if a<=0 and b>0:
        print("底数不能小于0")
    elif b<=0 and a>0:
        print("真数不能小于0")
    elif a<=0 and b<=0:
        print("真数和底数都不能小于等于0")
except ZeroDivisionError:
    #除零
    print("底数不能为1")
except NameError:
    #未声明/初始化对象
    print("底数必须为实数")
else:
    print(c)
```

### 46

```python
intxt=input("请输入明文：")
for p in intxt:
    if "a"<=p<="z":
        print(chr(ord("a")+(ord(p)-ord("a")+3)%26),end="")
    elif "A"<=p<="Z":
        print(chr(ord("A")+(ord(p)-ord("A")+3)%26),end="")
    else:
        print(p,end="")
```



## 第九套

### 41

```python
import calendar
year=eval(input("请输入年份："))
table=calendar.calendar(year)
print(table)
```

### 42

```python
s=input("请输入绕口令：")
print(s.replace("兵","将"))
```

### 44

```python
import turtle as tt
def curvemove():
    for i in range(200):
        tt.right(1)
        tt.forward(1)
    
tt.setup(600,600,400,400)
tt.hideturtle()
tt.pencolor("black") #笔的颜色
tt.fillcolor("red") #填充色
tt.pensize(2)
tt.begin_fill()
tt.left(140)
tt.forward(111.65)
curvemove()
tt.left(120)
curvemove()
tt.forward(111.65)
tt.end_fill()
tt.penup()
tt.goto(-27,85)
tt.pendown()
tt.done()
```

### 45

```python
for i in range(1,10):
    for j in range(i):
        print("{}*{}={}".format(j+1,i,i*(j+1)),end=" ")
    print("\n")
```

### 46(1)

```python
fi=open("关山月.txt",'r')
fo=open("PY.txt",'w')
txt=fi.read()
ls=txt.split("。")
fo.write("。\n".join(ls))
fi.close()
fo.close()
```

### 46(2)

```python
fi=open("PY.txt",'r')
fo=open("PY2.txt",'w')
txt=fi.readlines()
txt.reverse()
for row in txt:
    fo.write(row)
fi.close()
fo.close()
```



## 第十套

### 43

```python
import time
t=time.localtime()
print(time.strftime("%Y年%m月%d日%H时%M分%S秒",t))
```

### 44

```python
for i in range(4):
    for y in range(4-i):
        print(" ",end="")
    print("* "*i)

for i in range(4):
    for y in range(i):
        print(" ",end="")
    print("* "*(4-i))
# 用*画一个实心菱形
```

### 45

```python
import turtle as tt
tt.pensize(5)
for i in range(6):
    tt.fd(100)
    tt.right(60)
tt.color("red")
tt.circle(60,steps=6)
```

### 46

```python
import random
letter_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
            'o','p','q','r','s','t','u','v','w','x','y','z']
letter=letter_list[random.randint(0,25)]
cnt=0
while True:
    w=input("请输入一个小写英文字母：")
    if w==letter:
        print("回答正确")
        break
    elif w>letter:
        print("太大了")
        cnt+=1
    elif w<letter:
        print("太小了")
        cnt+=1
    elif cnt>=5:
        print("游戏失败")
        break
    else:
        print("未知错误")

```

## 第十一套

### 41

```python
fi=open("poem.txt",'r')
result=[]
for line in fi.readlines():
    line=line.strip()
    if len(line)!=0 and line[0]!="#":
        result.append(line)
result.sort()
for line in result:
    print(line)
fi.close()
```

### 42

```python
a=[]
for i in range(8):
    a.append([])
    for j in range(8):
        a[i].append(0)
for i in range(8):
    a[i][0]=1
    a[i][i]=1
for i in range(2,8):
    for j in range(1,i):
        a[i][j]=a[i-1][j-1]+a[i-1][j]
for i in range(8):
    for j in range(i+1):
        print("{:3d}".format(a[i][j]),end=" ")
    print()
	#print("\n")的话每行之间会有空行
```

### 43

```python
def proc(strings):
    m=0
    ls=[]
    for i in range(len(strings)):
        if len(strings[i])>m:
            m=len(strings[i])
    for i in range(len(strings)):
        if len(strings[i])==m:
            ls.append(strings[i])
    return ls

strings=["cat","python","MATLAB","cad","hello","world"]
result=proc(strings)
print("The longest word are:")
for word in result:
    print("{:>25}".format(word))
```

### 44

```python
strings={'cad','PE','Windows','FM','hello','world','flowers'}
n=0
for word in strings:
    if word.islower():
        #islower判断是否小写
        n+=1
print(n)
```

### 45

```python
def proc(stu_list):
    d={}
    for item in stu_list:
        r=item.split("_")
        a,b=r[0],r[1].strip()
        if a in d:
            d[a]+=[b]
        else:
            d[a]=[b]
    lst=sorted(d.items(),key=lambda d:len(d[1]),reverse=True)
    return lst

f=open("signup.txt","r")
stu_list=f.readlines()
result=proc(stu_list)
for item in result:
    print(item[0],'->',item[1])
f.close()
```

### 46

```python
d={"yuanyuan":80,"taotao":90,"fangfang":100,"mama":98,"baba":60}
ls=sorted(d.items(),key=lambda x:x[1],reverse=True)
for i in range(3):
    print("{}:{}".format(ls[i][0],ls[i][1]))
```



## 第十二套

### 41

```python
ls=input().split(",")
for num in ls:
    print("{:>10}".format(num),end="")
```

### 42

```python
scale=0.0001
def calv(base,day):
    val=base*pow(scale+1,day*11)
    return val

print("5年后的成就值是{}".format(int(calv(1,5*365))))
year=1
while calv(1,year*365)<100:
    year+=1
print("{}年后的成就值是100".format(year))
```

### 43

```python
while True:
    try:
        a=eval(input("请输入一个正整数："))
        if a>0 and type(a)==int:
            print(a)
            break
    except:
        print("请输入一个正整数")
```

```python
num=eval(input("请输入正整数："))
while type(num)!=int or num<=0:
    num=eval(input("请输入正整数："))
print(num)
```

### 44

```python
import turtle as tt
ls=[69,292,33,131,61,254]
X_len=400
Y_len=300
x0=-200
y0=-100
tt.penup()
# 画笔抬起——移动时不画线
tt.goto(x0,y0)
# 将画笔移动到坐标为(x0,y0)的位置
tt.pendown()
tt.fd(X_len)
tt.fd(-X_len)
tt.seth(90)
tt.fd(Y_len)
tt.fd(-Y_len)
tt.pencolor("red")
tt.pensize(5)
for i in range(len(ls)):
    tt.penup()
    tt.goto(x0+50*(1+i),-100)
    tt.seth(90)
    tt.pendown()
    tt.fd(ls[i])
tt.done()
```

## 第十三套

### 41

```python
ls=list(input("请输入一串字符"))
n_cnt=0
s_cnt=0
for i in ls:
    if i.isnumeric():
        n_cnt+=1
    elif i.isalpha():
        s_cnt+=1
print("数字的个数是{}，字母的个数是{}".format(n_cnt,s_cnt))
```



