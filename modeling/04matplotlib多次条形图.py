from matplotlib import pyplot as plt
from matplotlib.pyplot import MultipleLocator

x=["movie1","movie2","movie3","movie4","movie5"]
y_1=[56.01,26.94,17.53,16.49,15.45]
y_2=[34.44,23.44,15.23,16.22,17.20]
y_3=[21.99,50.78,35.42,40.40,27.89]

bar_width=0.1

x_1=list(range(len(x)))
#x_1=list(range(len(2*x)))[::2]
#这里的作用只是增大每一段之间的距离
x_2=[i+bar_width for i in x_1]
x_3=[i+bar_width*2 for i in x_1]

plt.figure(figsize=(20,8),dpi=60)


plt.xticks(x_2,x,rotation=45)
#plt.xlabel("MOVIE")
#plt.ylabel("SCORE")
#plt.title("piaofang")

plt.bar(x_1,y_1,width=bar_width,label="1st")
plt.bar(x_2,y_2,width=bar_width,label="2nd")
plt.bar(x_3,y_3,width=bar_width,label="3rd")


plt.grid(alpha=4)

plt.legend(loc="upper left")

plt.show()