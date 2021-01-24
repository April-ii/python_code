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
#Q：radint里面的参数是啥意思捏
print(name)
```

### 42

