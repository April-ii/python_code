from matplotlib import pyplot as plt
from matplotlib.pyplot import MultipleLocator
b_1=[1,1,1,1,0,2,3,4,2,2,7,5,4,3,2,2,2,2,2,2]
b_2=[2,3,3,1,2,3,4,5,6,4,3,2,2,3,4,4,3,2,2,3]
a=range(11,31)

plt.figure(figsize=(20,10),dpi=80)
#大小

_atick_labels=["{}age".format(i) for i in list(a)]
plt.xticks(a,_atick_labels)
plt.ylim((0,12))

x_locator=MultipleLocator(1)
y_locator=MultipleLocator(1)

ax=plt.gca()
ax.yaxis.set_major_locator(y_locator)
ax.xaxis.set_major_locator(x_locator)

# 调整坐标轴

plt.legend(loc="upper left")
#设置图例

plt.grid(alpha=0.4,linestyle=":")
#绘制网格
plt.plot(a,b_1,label="me",color="r",linestyle="--")
plt.plot(a,b_2,label="deskmate",color="y",linestyle=":")
#画图