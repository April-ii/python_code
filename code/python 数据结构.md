数据结构三要素：逻辑结构、存储结构、运算

## 算法的时间复杂度

1. O(1)<O(log_2 n)<O(n)<O(n log_2 n)<O(n_2)<O(n^3)<O(2^n)<O(n!)<O(n^n) 

   记忆：“常对幂指阶”

2. 顺序执行的代码可以忽略，只需要挑选循环中的一个基本操作，分析它与n的关系

## 算法的空间复杂度

1. 内存：程序代码（固定不变）、数据



## 抽象数据类型(Abstract Data Type)

含义：是指一个数学模型以及定义在此数学模型上的一组操作。即把数据类型和数据类型上的运算捆在一起，进行封装。引入抽象数据类型的目的就是把数据类型的表示和数据类型上运算的实现与这些数据类型和运算在程序中的引用隔开。

## 线性表（逻辑）

1. 相同数据类型、有限序列——位序

## 顺序表（存储）



## 栈

1. 由于栈数据结构只允许在一端进行操作，因而按照先进先出（LIFO，Last In First Out) 的原理操作。

```python
Class Stack(object):
    # 栈
    def __init__(self):
        self.__list=[]

    def push(self,item):
        self.__list.append(item)
        
    def pop(self):
        """ 从尾部操作的好处是：时间复杂度为O(1) """
        # 弹出栈顶元素
        return self.__list.pop()

    def peek(self):
        # 返回尾部元素
        if self.__list:
            return self.__list[-1]
        return None
        
    def is_empty(self):
        return self.__list==[]
        
    def size(self):
        return len(self.__list)
        

    if __name__ == "__main__":
    """ 当py文件被直接执行时，此条件为真；
        当被import进去其他文件中执行此条件为假 """
        s=Stack()
```



## 队列

1. 只允许在一端进行插入操作，而在另一端进行删除操作的线性表（FIFO，First In First Out)

   ```python
   class Queue(object):
       
       def __init__(self):
           self.__list=[]
       def enqueue(self,item):
           self.__list.append(item)
           
       def dequeue(self):
           """ 从队列头部删除一个元素 """
           self.__list.pop(0)
           
       def is_empty(self):
           return self.__list==[]
   
       def size(self):
           return len(self.__list)
   
   
    if __name__ == "__main__":
       q=Queue()
   ```

   ```python
   class Dequeue(object):
       
       def __init__(self):
           self.__list=[]
       def add_rear(self,item):
           self.__list.append(item)
       def add_front(self,item):
           self.__list.insert(0,item)
       def remove_rear(self):
           self.__list.pop
       def remove_front(self):
           """ 从队列头部删除一个元素 """
           self.__list.pop(0)
           
       def is_empty(self):
           return self.__list==[]
   
       def size(self):
           return len(self.__list)
   
   
    if __name__ == "__main__":
       q=Dequeue()
   ```

   