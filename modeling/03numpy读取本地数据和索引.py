import numpy as np

#假装有一个数据储存
file_path="/home/sgwf/Downloads/data_b_train.csv"
# numpy读取数据
t1=np.loadtxt(file_path,delimiter=",",dtype="int",unpack=True)
#unpack这里是转置的功能
#这里编译不起嘿嘿
t2=np.arange(24).reshape(4,6)
t2.transpose()
t2.T
t2.swapaxes
#转置

#取连续多行
t1[2:,:]
#取不连续的多行
t1[[2,8,10],:]
#后面的冒号可省略，因为表示每列都想要

#取列
t1[:,0]
t1[:,2:]
t1[:,[2,4,9]]

#取多个不相邻的点
c=t1[[0,1,8],[2,3,4]]
#取出来的结果是(0,2)(1,3)(8,4)

#numpy中的bool索引
t1[t1>10]=0
#三元运算符
np.where(t1<10,0,10)
#小于10的替换成10，大于18的替换成18
t1.clip(10,18)