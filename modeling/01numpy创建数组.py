import numpy as np
import random

#使用numpy生成数组，得到ndarray的数据类型
t2=np.arange(4,10,2)
#numpy中的数据类型
t3=np.array(range(1,4),dtype="int8")
#numpy中的bool类型
t4=np.array([1,1,0,0],dtype=bool)
#调整数据类型
t5=t4.astype("int8")
#numpy中的小数
t6=np.array([random.random() for i in range(10)])
t7=np.round(t6,2)

print(round(random.random(),2))
print("%.2f" % random.random)
