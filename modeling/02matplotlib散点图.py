from matplotlib import pyplot as plt
from matplotlib.pyplot import MultipleLocator

y_3=[11,17,16,11,12,11,12,6,6,7,8,9]
y_10=[26,26,28,19,21,17,16,19,18,20,20,19]
x_3=range(1,13)
x_10=range(21,33)



plt.figure(figsize=(200,100),dpi=60)

_x=list(x_3)+list(x_10)
_xtick_labels=["3.{}".format(i) for i in x_3]
_xtick_labels+=["10.{}".format(i-20) for i in x_10]

plt.xticks(_x,_xtick_labels,rotation=45)
plt.xlabel("TIME")
plt.ylabel("TEMPERATURE")
plt.title("Change of Temperature")

plt.scatter(x_3,y_3,label="3rd month")
plt.scatter(x_10,y_10,label="10th month")

plt.legend(loc="upper left")

plt.show()