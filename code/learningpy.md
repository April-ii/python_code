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

	### 1. 封装：根据职责将属性和方法封装到一个抽象的类中

1. class 后面跟着的（类名）必须用驼峰命名法

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
print("-"*50) # 在“我去了”之前打印

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



### 案例1—小明爱跑步

```python
class Person：
	def __init__(self,name,weight):
        self.name=name # 左边是属性，右边是形参
        self,weight=weight
    def __str__(self):
        return ("我的名字叫 %s,体重是 %.2f公斤" % (self.name,self.weight))
    def run(self):
        pass
    def eat(self):
        pass

xiaoming=Person("小明")
xiaoming.run()
xiaoming.eat()
print(xiaoming)
    
```

1. 在对象的方法内部，是可以直接访问对象的属性的
2. 同一个类创建的多个对象，其属性之间互不干扰

### 案例2—摆放家具

```python
class HouseItem:
    def __init__(self,name,area):
        self.name=name
        self.area=area
    def __str__(self):
        return " [%s] 占地 %.2f" % (self.name,self.area)


class House:
    def __init__(self,house_type,area):
        self.house_type=house_type
        self.area=area
        self.free_area=self.area
        self.item_list=[]
    
    def __str__(self):
        # python能够自动将一对括号内部的代码连接在一起
        return ("户型：%s\n总面积：%.2f\n[剩余：%.2f]\n家具：%s" 
                % (self.house_type,self.area,
                   self.free_area,self.item_list))
    
    def add_item(self,item):
        if item.area>self.free_area:
            print("%s 的面积太大了，无法添加" % item.name)
        else:
            self.item_list.append("%s" % item.name)
            self.free_area-=item.area

# 创建家具
bed=HouseItem("席梦思",4)
chest=HouseItem("衣柜",2)
table=HouseItem("餐桌",1.5)

print(bed,chest,table)

# 创建房子对象
my_home=House("两室一厅",60)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)

print(my_home)
```

1. 先定义家具类，再定义房子类。原因是房子类中的方法“添加家具”，需要调用家具类的对象



### 案例3 士兵突击(身份运算符)

一个对象的属性可以是另一个类创建的对象

```python
class Gun:
    def __init__(self,model):
        # 1.model of gun
        self.model=model

        # 2.number of bullet
        self.bullet_account=0

    def add_bullet(self,count):
        self.bullet_account+=count
    
    def shoot(self):
        # 1.judging number of bullet
        if self.bullet_account<=0:
            print("[%s] was out of bullet" % self.model)
            return
        # 2.fire a bullet
        self.bullet_account-=1
        # 3.prompt transmitting message
        print("[%s] tututu.. [%d] bullet left" 
             % (self.model,self.bullet_account))

ak47 = Gun("AK47")

class Soldier:
    # 定义属性时，不知道设置什么初始值，可以设置为None.
    # None 表示一个空对象，没有方法和属性，是一个特殊常量，可以将None赋值给任何一个变量
    def __init__(self,name):
        self.name=name
        self.gun=None
    def fire(self):
        # 1.judging having gun or not
        if self.gun is None:
            print("[%s] 还没有枪..." % self.name)
            return
        # 2.shouting
        print("Go! [%s]" % self.name)
        # 3.gun adds bullet
        self.gun.add_bullet(10)
        # 4.gun fires
        self.gun.shoot()
xusanduo=Soldier("许三多")
xusanduo.gun=ak47
xusanduo.fire()

```

1. python中的身份运算符： 

   is：判断两个标识符是不是引用同一个对象， x is y,类似id(x)==id(y)

   同理， is not

2. is 与== 区别：“==” 表示两个变量的值相等



### 私有属性和私有方法

```python
class Women:
    def __init__(self,name):
        self.name=name
        self.__age=18

    def secret(self):
        print("%s 的年龄是 %d" % (self.name,self.__age))

xiaofang=Women("小芳")

# 程序会报错，因为私有属性在外界不能够被直接访问 
print(xiaofang.__age)
# 在对象的方法内部，是可以访问对象私有属性的
xiaofang.secret()

# 私有方法同理 def __secret(self):
```

科普(伪私有属性、伪私有方法)：

​		python 中，并没有真正意义上的私有。在给属性、方法命名时，实际上是对名称做了一些特殊处理，使得外界无法访问到
​		处理方式：在名称前面加上` _类名 => _类名__名称`
提示：在日常开发中，不要使用这种方法，访问对象的私有属性或私有方法

### 2. 继承：实现代码的重用，相同的代码不需要重复的编写

1. 子类拥有父类的所有方法和属性 `class son(father)` 

   ```python
   class Animal:
       def eat(self)：
       	print("我会吃")
   class Dog(Animal):
       def bark(self):
           print("我会飞")
   ```

   2. 父类方法不能满足子类需求时，可以对方法进行重写：

      （1）覆盖父类的方法：在子类中定义一个和父类同名的方法并且实现，重写之后，只会调用子类中重写的方法

      （2）对父类的方法进行扩展：使用super().    调用原本在父类中的方法

      ```python
      class Animal:
          def eat(self)：
          	print("我会吃")
          
      class Dog(Animal):
          def bark(self):
              print("汪汪汪...")
          
      class XiaoTianQuan(Dog):
          print("叫得跟神一样")
          super().bark()  # 调用原本在父类中封装的方法
          # 在python 2.0+版本中 `Dog.bark(self)` 来调用
          print("@#$%^&&^%$#$*...")
      ```

   3. 父类的私有属性和私有方法：

      （1）子类不能在自己的方法内部，直接访问父类的私有属性或者私有方法

      （2）子类可以通过父类的公有方法间接访问到私有属性或私有方法

      ```python
      class Father:
          def __init__(self):
              __num=200
          def __test(self):
              print("secret")
          def test(self):
              print("%d" % __num)
              self.__test()
      
      class Son(Father):
          self.test()
          
      ```


### 多继承：子类可以拥有多个父类，并且具有所有父类的属性和方法

```python
class 子类(父类1，父类2)：
	pass  
```

### python 中的`__mro__ `---方法搜索顺序

`print(C.__mro__)`  ，主要用于在多继承时，判断方法、属性的调用路径

### 新式类和旧式类

为了保证代码能够同时在`python2.x` 和`python 3.x`  中运行，今后在定义类时，如果没有父类，建议统一继承自`object`

### 3. 多态：不同的子类对象调用相同父类的方法，产生不同的执行结果

```python
class Dog(object):
    def __init__(self,name):
        self.name=name

    def game(self):
        print("play")

class XiaoTianQuan(Dog):
    def game(self):
        print("play to sky")

class Person(object):
    def __init__(self,name):
        self.name=name
    
    def game_with_dog(self,dog):
        print("%s and %s play" % (self.name,dog.name))
        # 这里的dog是形参
        dog.game()

wangcai=Dog("旺财")
# wangcai=XiaoTianQuan("wangcai")
xiaoming=Person("小明")
# 让小明调用和狗玩的方法
xiaoming.game_with_dog(wangcai)
```



## 类属性

给类对象中定义的属性，类属性不会用于记录具体对象的特征

```python
class Tool(object):
    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count=0
    def __init__(self,name):
        self.name=name # 实例属性
        # 让类属性的值+1
        Tool.count+=1
# 调用类属性用类名.类属性。否则破坏封装性
```



## 类方法

类方法需要用修饰器`@classmethond` 来标识，告诉解释器这是一个类方法

```python
@classsmethod
def 类方法名(cls):
    pass
```

EXAMPLE

```python
class Tool(object):
    count=0
    
    @classmethod
    def show_tool_count(cls):
        print("%d" % cls.count)
    
    def __init__(self,name):
        self.name=name
        Tool.count+=1

# 创建对象
tool1=Tool("斧头")
# 调用类方法
Tool.show_tool_count()
```







