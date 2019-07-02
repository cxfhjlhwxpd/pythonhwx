
# coding: utf-8

# In[20]:


import csv #导入csv模块，该模块包含于python标准库中
from matplotlib import pyplot as plt #从matplotlib中导入pyplot并重命名为plt
from datetime import datetime #导入日期模块，用以转换字符型日期为日期型

#从文件中获取数值
filename='C:/Users/hwx2018/Desktop/resultlastlast.csv' #文件名
with open(filename) as f: #打开文件文件
    reader=csv.reader(f) #读取并将内容储存在列表reader中
    header_row=next(reader)#next()函数获取第一行，即文件头

    #提取气温、日期数据存储在列表中
    stars,comments,strategys=[],[],[]  #将最高气温、最低气温、日期储存在列表中
    for row in reader: #遍历reader列表

        star=int(row[5]) #将字符型温度转换成数值型
        stars.append(star) #将最高气温附加到highs列表中

        comment=int(row[1])#同上
        comments.append(comment)
        
        strategy=int(row[6])#同上
        strategys.append(strategy)

        

    #绘制气温图表
    fig=plt.figure(dpi=128,figsize=(8,6))#添加绘图窗口，可绘制多条曲线
    plt.plot(stars,comments,c='red',alpha=0.6)#plot()函数，第一个参数x值，第二个y值，第三个图形颜色
    plt.plot(stars,strategys,c='blue',alpha=0.6)

    #设置图形的格式
    plt.title("starlevel&comments",fontsize=24)#图形标题
    plt.xlabel("Starlevel",fontsize=14)#x轴标题及字号
    #fig.autofmt_xdate()#调用fig.autofmt_xdate()绘制斜的日期标签，以防日期彼此重叠
    plt.ylabel("Comments",fontsize=14)
    plt.tick_params(axis='both',which='major',labelsize=8)#坐标轴格式

    #显示图表
    plt.show()


# In[7]:


import csv #导入csv模块，该模块包含于python标准库中
from matplotlib import pyplot as plt #从matplotlib中导入pyplot并重命名为plt

#从文件中获取数值
filename='C:/Users/hwx2018/Desktop/resultlastlast.csv' #文件 名
with open(filename) as f: #打开文件文件
    reader=csv.reader(f) #读取并将内容储存在列表reader中
    header_row=next(reader)#next()函数获取第一行，即文件头

    #提取气温、日期数据存储在列表中
    stars,comments,strategys=[],[],[]  
    for row in reader: #遍历reader列表

        star=int(row[5]) 
        stars.append(star) 

        comment=int(row[1])#同上
        comments.append(comment)
        
        strategy=int(row[6])#同上
        strategys.append(strategy)
    plt.xlabel('X')  #设置X轴标签  
    plt.ylabel('Y') #设置Y轴标签  
    plt.scatter(stars,comments,s=20,c='r') #画散点图 )
    plt.scatter(stars,strategys,s=20,c='b')
    plt.show()


# In[18]:


import csv
import matplotlib
from matplotlib import pyplot as plt #从matplotlib中导入pyplot并重命名为plt
import numpy as np
import pandas as pd


filename='C:/Users/hwx2018/Desktop/resultlastlast.csv' #文件 名
with open(filename) as f: #打开文件文件
    reader=csv.reader(f) #读取并将内容储存在列表reader中
    header_row=next(reader)#next()函数获取第一行，即文件头

    stars=[]
    for row in reader: #遍历reader列表
        star=int(row[5]) #将字符型温度转换成数值型
        stars.append(star) #将最高气温附加到highs列表中
    star1=[]
    star2=[]
    star3=[]
    star4=[]
    star5=[]
    for i in range(star):
        if 0<=i<20:
            star1.append(int(i))
        elif 20<=i<40:
            star2.append(int(i))
        elif 40<=i<60:
            star3.append(int(i))
        elif 60<=i<80:
            star4.append(int(i))
        else:
            star5.append(int(i))

index=['0~20','20~40','40~60','60~80','80~100']
values=[len(star1),len(star2),len(star3),len(star4),len(star5)]
plt.bar(index,values)
plt.show()
   

