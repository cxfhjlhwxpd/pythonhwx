
# coding: utf-8

# In[7]:


import requests
from bs4 import BeautifulSoup

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print('导入模块')

import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['SimHei']  
# Matplotlib中设置字体-黑体，解决Matplotlib中文乱码问题
plt.rcParams['axes.unicode_minus'] = False    
# 解决Matplotlib坐标轴负号'-'显示为方块的问题

#获取连接网页数据
def get_urls(n):
    return ['https://travel.qunar.com/p-cs299783-qingdao-jingdian-1-' + str(i+1) for i in range(n)]

    # 创建函数，获取分页网址
#获取具体需要的参数
def get_informations(u):
    ri = requests.get(u)
        # requests访问网站
    soupi = BeautifulSoup(ri.text,'lxml')
        # bs解析页面
    infori = soupi.find('ul',class_="list_item clrfix").find_all('li')
        # 获取列表内容
    
    datai = []
    n=0
    for i in infori:
        n+=1
        #print(i.text)
        dic = {}
        dic['lat'] = i['data-lat']
        dic['lng'] = i['data-lng']
        dic['scenic_spot'] = i.find('span',class_="cn_tit").text
        dic['strategy_sum'] = i.find('div',class_="strategy_sum").text
        dic['comment_sum'] = i.find('div',class_="comment_sum").text
       # dic['景点排名'] = i.find('span',class_="ranking_sum").text
        dic['star_level'] = i.find('span',class_="total_star").find('span')['style'].split(':')[1]
        datai.append(dic) #列表包字典
        # 分别获取字段内容
        #print('已采集%s条数据' %(n*10))
    return datai
    
    # 构建页面爬虫
#标准化某一指标便于对比
def normalization(dfi, col):
    dfi[col + "_nor"] = (dfi[col] - dfi[col].min())/(dfi[col].max() - dfi[col].min())


if __name__ == '__main__':
    #获取多页网页数据
    url_lst = get_urls(20)

    #将数据转化为dataframe格式便于处理
    df = pd.DataFrame()
    for u in url_lst:
        dfi = pd.DataFrame(get_informations(u))
        df = pd.concat([df,dfi])
        df.reset_index(inplace = True,drop = True)
        # 采集数据


    #对dataframe中的数据格式进行调整
    df['lng'] = df['lng'].astype(np.float)
    df['lat'] = df['lat'].astype(np.float)
    df['comment_sum'] = df['comment_sum'].astype(np.int)
    df['strategy_sum'] = df['strategy_sum'].astype(np.int)
    df['star_level'] = df['star_level'].str.replace('%','').astype(np.float)
   

    normalization(df, 'comment_sum')
    #输出为excel形式
    df.to_excel("./resultlastlast.xlsx")


# In[4]:
#检查数据是否缺失

import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  
df=pd.read_csv("C:/Users/hwx2018/Desktop/resultlastlast.csv")
df1=pd.pivot_table(df,index=["lat","lng"])
df1.isnull()


# In[ 5]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as mpl
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("C:/Users/hwx2018/Desktop/resultlastlast.csv")
fig,ax=plt.subplots(1,1,figsize=(10,20))
ax.hist(df['star_level'],bins=100)
d=df['star_level']
zsore=(d-d.mean())/d.std()
df['isOutlier']=zsore.abs()>3
df['isOutlier'].value_counts()

