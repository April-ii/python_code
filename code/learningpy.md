## input函数
用户输入的任何内容python都认为是一个字符串，具体例子中一般需要类型转换

## if语句
语句和缩进部分是一个完整代码块，Tab相当于{}
## 类型转换函数
int(x)---将x转换为一个整数  float(x)

## python规范
Tab和空格不要混合使用，全部Tab（or 空格）

## break 和 continue
break:当某个条件成立时候，退出循环
    <!--if xxx:
            break-->
continue:当某个条件成立时，不执行后续重复代码
    <!--if xxx:
            continue-->


## 字符串中的转义字符
\t 制表符——协助文本输出时候垂直方向保持对齐
\n 换行符
\\ 反斜杠
\' 单引号
\" 双引号
\s 回车
\b 退格

## list中的增、删、查、改
查：name_list.index("zhangsan")    
改：name_list[1]="李四"  <!--修改指定索引数据-->
增：name_list.append("wangxiaoer")   <!--在末尾追加数据-->
    name_list.insert(1,"beauty")    <!--在指定位置插入数据-->
    temp_list=["sun","zhu","sha"]
    name_list.extend(temp_list)   <!--将temp_list的数据追加到列表-->
删：name_list.remove("wangwu")    <!--删除第一个出现的指定数据-->
    name_list.pop()    <!--删除末尾数据-->
    name_list.pop(2)    <!--删除索引数据-->
    name_list.clear()  <!--清空列表-->
    del name_list[1]  <!--del的本质是将一个变量从内存中删除，后续代码不再使用这个变量，日常开发中，要从列表中删除数据，建议使用列表提供的方法-->
统计：len（name_list）  <!--列表长度-->
     name_list.count("zhangsan")   <!--数据出现的次数-->
排序：name_list.sort()  <!--升序排序-->
     name_list.sort(reverse=True)   <!--降序排序-->
     name_list.reverse()   <!--逆序、反转-->


## 元祖
1. 内容不可更改
2. 只包含单元素的元祖，需要在元素末尾加逗号（否则解释器认为这是一个变量类型而非元祖类型）
3. 可以和列表相互转换 
    list(元祖)
    tuple（列表）

## 字典
1. 取值
    xiaoming_dict[key]
2. 增加/修改
    xiaoming_dict[key]=xxx
3. 删除
    xiaoming_dict.pop(key)
4. 统计键值对数量
    len(xiaoming_dict)
5. 合并字典
    temp_dict={"height":1.75} //不能出现和原有字典相同的key
    xiaoming_dict.update(temp_dict)
6. 清空字典
    xiaoming_dict.clear()
7. 应用
    card_list=[
        {
            "name":"zhangsan",
            "qq":"1234",
        },
        {
            "name":"lisi"
            "qq":"4321"
        }
    ]


## 字符串
1. 使用 isspace，全是空白字符or空格时返回True
2. 字符串切片
    num_str[2:6]
    num_str[2:]
    num_str[:6]
    num_str[:]
    num_str[-1::-1] 字符串逆序


## 内置函数
1. max、min函数针对dict时，只比较key而不比较值
2. 字典和字典不能比较大小（类似dict_1 < dict_2这样的）
3. 字典也不能进行切片



## 可变类型和不可变类型

1. 不可变：数字类型、字符串、元组
2. 可变：字典、列表
3. 字典中的key不能使用可变类型



## 在函数内修改全局变量

在函数内，使用global声明一下变量即可
再使用赋值语句时，就不会创建局部变量



## shebang(# !)

#! 后面跟上python解释器的完整路径
使用which python查询python解释器所在路径



## 全局命名

全局变量名前应该增加 g_ 或者 gl_

## 利用元祖返回多个值

```python
def measure():
    print("测量开始")
    temp=39
    wetness=50
    print("测量结束")
    
    return temp,wetness
# 元组
result=measure()
# gl_temp,gl_wetness=measure()
print(result)
print(result[0])   # 单独打印temp

```



## 多个变量接收元组(交换数字)

```python
a=1
b=2
a,b=(b,a)
a,b=b,a
```



## 函数传递的参数

1. 如果传递的是不可变类型，针对参数使用赋值语句，会在函数内部修改局部变量的引用，不会影响到外部变量的引用
2. 如果传递的是可变类型，在函数内部，使用 **方法** 修改了数据的内容，同样会影响到外部的数据



## 函数的缺省参数

```python
gl_list=[6,3,9]
# 默认按照升序排序
gl_list.sort()
# 如果需要降序排序，需要执行reverse参数
gl_list.sort(reverse=True)
```



## 函数的缺省参数定义

```python
def print_info(name,gender=True):
    gender_text="man"
    if not gender_text:
        gender_text="woman"
    print("%s 是　%s" % (name,gender_text))    
print_info("小明")　# 性别默认是男生
# 提示：在指定缺省参数的默认值时，应该使用最常见的值作为默认值
```

### 缺省参数注意事项：

1. xiaomeixiaomei位置：必须保证带有默认值的缺省参数在参数列表的末尾
2. 调用多个缺省参数，需要指定参数名。i.e. print("小美",gender=False)



## 多值参数

1. 函数名前增加一个* 　可以接收元组

   函数名前增加两个*     可以接收字典

   ```python
   def demo(num,*nums,**person):
       print(num)
       print(nums)
       print(person)
   # demo(1)
   demo(1,2,3,4,5,name="小明"，age="18")
   ```

   

   ### 多值参数求和
   
   ```python
   def sum_numbers(*args):
   # def sum_numbers(args):
       num=0
       print(args)
       
       for n in args:
           num+=n
       return num
   
   result=sum_numbers(1,2,3,4,5)
   # result=sum_numbers((1,2,3,4,5))
   print(result)
   ```



## 元组和字典的拆包

调用时，在元组前增加一个* , 在字典前增加两个*

```python
def demo(*args,**kwargs):
    print(args)
    print(kwargs)
gl_nums=(1,2,3)
gl_dict={"name":"小明"，"age":18}

demo(*gl_nums,**gl_dict)
```



## 函数的递归

```python
def sum_number(num):
    print(num)
    # 递归出口，当参数满足某个条件时，不再执行函数
    if num==1:
        return 1
    temp=sum_number(num-1)
    
    return temp+num
    
sum_number(3)
```



## 面向对象

```python
# 创建类
class Cat:
    def eat(self):
        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print("%s 小猫要吃鱼" %self.name)
    def drink(self):
        print("小猫要喝水")
# 创建猫对象
tom=Cat()
# 可以使用　.属性名直接给对象增加属性　利用赋值语句就可以了（不推荐使用）
tom.name="Tom"
# 调用对象的方法
tom.eat()
```

### 在初始化方法中定义属性

```python
class Cat:
    def _init_(self,new_name):
        print("这是一个初始化方法")
        # self.name="Tom"
        self.name=new_name
    def eat(self):
        print("%s 爱吃鱼"　% self.name)
tom=Cat("tom")
print(tom.name)
	
```

### del方法和对象的生命

```python
class Cat:
    def _init_(self,new_name):
        self.name=new_name
        print("%s 来了"　% self.name)
    def _del_(self):
        print("%s 我去了" % self.name)
        # tom是全局变量，只有所有程序结束后才会被删除
tom=Cat("Tom")
print(tom.name)
# del tom　　//在“我去了”之后打印
print("-"*50) #在“我去了”之前打印

```

### str方法定制变量输出信息

注意：_ str _ 方法必须返回一个字符串

```python
class Cat:
    def __init__(self,new_name):
        self.name=new_name
        print("%s 来了" % self.name)
    def __str__(self):
        return "我是小猫[%s]" % self.name
tom=Cat("Tom")
print(tom)
```





