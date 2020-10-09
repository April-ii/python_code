from matplotlib import pyplot as plt
from matplotlib.pyplot import MultipleLocator

x=["movie1","movie2","movie3","movie4","movie5"]
y=[56.01,26.94,17.53,16.49,15.45]


plt.figure(figsize=(20,8),dpi=60)


plt.yticks(range(len(x)),x,rotation=45)
#plt.xlabel("MOVIE")
#plt.ylabel("SCORE")
#plt.title("piaofang")

#plt.bar(range(len(x)),y,width=0.3)
#这是竖着的条形图

plt.grid(alpha=4)
plt.barh(range(len(x)),y,height=0.3,color="y")

plt.legend(loc="upper left")

plt.show()

