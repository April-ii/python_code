from matplotlib import pyplot as plt

interval=[0,5,10,15,20,25,30,35,40,45,60,90]
width=[5,5,5,5,5,5,5,5,5,15,30,60]
quantity=[836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]

plt.figure(figsize=(40,8),dpi=40)
#偶然的机会让我发现figure只能放在前面hhh

_x=range(13)
_xtick_labels=interval+[150]
plt.xticks(_x,_xtick_labels)
#由于直方图表示的是区间的频数，所以还需根据width推算出最后一个区间的上限

plt.bar(range(12),quantity,width=1,align="edge")
#注意了，这边为了和quantity的数据个数一样，还是range(12)



plt.grid(alpha=0.4)

#我感觉本质上就是把条形图连在一起做成直方图？
plt.show()