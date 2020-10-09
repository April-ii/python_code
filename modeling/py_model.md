## matplotlib

1. 在jupyter notebook下使用`matplotlib.pyplot` 中的`savefig("./xxx.png")`时，注意要将`plt.plot(x,y)`和`savefig`放在同一个框框中，否则保存的都是空白图

2. svg矢量图保存后可以从本地目录中打开查看，但不能从jupyter notebook里面打开查看

3. ```python
   fig=plt.figure(figsize=(20,8),dpi=80)
   # figure这里就是指我们画的图
   # 通过实例化一个figure并且传递参数，能够在后台自动使用该figure实例
   # 在图像模糊的时候可以传入dpi参数，让图片更加清晰
   ```

4. ```python
   plt.xticks(m)
   plt.yticks(n)
   #设置x、y轴的刻度
   #括号里也可以是list
   ```

5. ```python
   _x=x
   _xtick_labels=["10点{}分".format(i) for i in range(60)]
   _xtick_labels+=["11点{}分".format(i) for i in range(60)]
   #matplotlib默认不支持中文字符，因为默认的英文字体无法显示汉字
   plt.xticks(_x,_xtick_labels，rotation=90) 
   # rotation旋转度数
   # 数据长度要一样，确保一一对应
   # 调整刻度
   ```

6. ```python
   #添加图例
   plt.plot(a,b_1,label="me")
   plt.plot(a,b_2,label="deskmate")

   plt.legend(loc="upper")
   ```
   
7. ```python
   #设置坐标轴的刻度间隔
   import matplotlib.pyplot as plt
   from matplotlib.pyplot import MultipleLocator
   #从pyplot导入MultipleLocator类，这个类用于设置刻度间隔
   
   
   x_major_locator=MultipleLocator(1)
   #把x轴的刻度间隔设置为1，并存在变量里
   y_major_locator=MultipleLocator(10)
   #把y轴的刻度间隔设置为10，并存在变量里
   ax=plt.gca()
   #ax为两条坐标轴的实例
   ax.xaxis.set_major_locator(x_major_locator)
   #把x轴的主刻度设置为1的倍数
   ax.yaxis.set_major_locator(y_major_locator)
   #把y轴的主刻度设置为10的倍数
   plt.xlim(-0.5,11)
   #把x轴的刻度范围设置为-0.5到11，因为0.5不满一个刻度间隔，所以数字不会显示出来，但是能看到一点空白
   plt.ylim(-5,110)
   #把y轴的刻度范围设置为-5到110，同理，-5不会标出来，但是能看到一点空白
   ```

8. 如果无法用颜色字符来选取想要的颜色，可以用16进制

9. `linecolor`  `linestyle`   `linewidth` 添加文本注释、添加文字（水印）到图中

   ```python
   plt.xlabel('I am X')
   plt.ylabel('I am Y'
   # 添加x\y轴的标识
   ```

   

10. `random.randint(x,y)` 在区间内随机取数字

    `random.random()` 随机取小数

11. 绘图中发现的小tips：plt.figure只能放在绘图前面



## numpy

1. `np.reshape()` 在使用时，并不是对原有数组进行reshape，而是创建了一个新的数组来装reshape之后的数组

2. 数组的计算具有广播原则：相同形状数组可以进行计算，不同形状的数组如果某一维度一样，其他维度为1 也可以进行计算

   广播原则：如果两个数组的后缘维度（即从末尾开始算起的维度）的轴长度相符或其中一方的长度为1，则认为它们是广播兼容的。广播会在缺失或长度为1的维度上进行

   例：shape为(3,3,3)的数组不能够和(3,2)的数组进行计算，shape为(3,3,2)的数组可以和(3,2)的数组进行计算