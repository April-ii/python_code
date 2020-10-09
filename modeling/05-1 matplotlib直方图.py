from matplotlib import pyplot as plt
from matplotlib.pyplot import MultipleLocator

a=[31,45,34,67,89,26,39,28,38,90,98,67,56,49,38,28,48,39,49,28,23,22,34,90,28,77,56]

#计算组数
d=4 #组距
num_bins=(max(a)-min(a))//d

plt.figure(figsize=(20,8),dpi=60)

plt.xticks(range(min(a),max(a)+d,d))


plt.hist(a,num_bins,density=True)
#hist需要的是原始数据，也就是它在绘图之前先要做一个统计

plt.grid(alpha=4)


plt.show()