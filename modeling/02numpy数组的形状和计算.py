import numpy as np

t1=np.arange(12)
t2=np.array([[1,2,3],[4,5,6]])
t3=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(t3.shape) 
# 查看数组的形状

#print(t1)
#print(np.reshape(t1,(3,4)))
# reshape后是一个return的结果

t4=t3.reshape((2,4))
#print(t4)
print(t3)

t5=t3.reshape(t3.shape[0]*t3.shape[1]*t3.shape[2])
#简化之后
t5=t5.flatten()
#展开成一维数组
#print(t5)
# 数据降维

t6=np.arange(100,112)
print(t1+t6,t1*t6,t1-t6)
