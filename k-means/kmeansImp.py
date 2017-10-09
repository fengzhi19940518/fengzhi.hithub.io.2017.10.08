from numpy import *
from math import *
#k-means支持函数
class KMF:
    def loadDataSet(self,path):
        f=open(path,'r')
        dataMat=[]
        for line in f.readlines():
            curline=line.strip().split('\t')    #把每一行切割成一个list集合
           # print("curline:",curline)
            fltLine=list(map(float,curline))  #将文本转化为字符类型,利用list转为数字
            #print('fltline:',fltLine)
            dataMat.append(fltLine)
            #print('datamat:',dataMat)
        return dataMat

    def distEclud(self,vec1,vec2):        #计算两个向量的欧式距离
        distance=sqrt(sum(power(vec1-vec2,2)))
        return distance

    def randCent(self,dataset,k):   #构建一个包含k个随机质心的集合
        n=shape(dataset)[1]         #数据列项
        centroids=mat(zeros((k,n))) #初始化质心
        for j in range(n):          #数据集中每一维的最小和最大值，保证随机选取的质心在边界之内，这也叫构建簇质心
            minJ=min(dataset[:,j])  #找出整个矩阵的最小值
            rangeJ=float(max(dataset[:,j])-minJ)    #最大值与最小值的差
            centroids[:,j]=mat(minJ+rangeJ*random.rand(k,1)) #生成k行1列的列表
        return centroids

    def kMeans(self,dataSet,k):  #k-均值算法：四个参数（数据集、簇的数目、距离、创建初始质心）
        m=shape(dataSet)[0]     #数据点的长度
        x=mat(zeros((m,2)))     #记录数据点到质心的距离的平方，簇分配结果矩阵x的两列分别是记录簇索引值，第二列存储误差，
        centroids=self.randCent(dataSet,k)      #中心点，质心
        flag=True               #聚类结束标志
        while flag:
            flag=False
            for i in range(m):
                minDist=inf        #设置两个变量，分别存放数据点到质心的距离，及数据点属于哪个质心
                minIndex=-1
                for j in range(k):  #变量整个簇，寻找最近的质心
                    distance=self.distEclud(centroids[j,:],dataSet[i,:])
                    if minDist>distance:
                        minDist=distance
                        minIndex=j
                # 簇分配结果发生改变，更新标志
                if x[i,0]!=minIndex:
                    flag=True
                x[i,:]=minIndex,minDist**2
                print('centroids:',centroids)
                for cent in range(k):   #更新质心
                    ptsInClust=dataSet[nonzero(x[:,0].A==cent)[0]]
                    centroids[cent,:]=mean(ptsInClust,axis=0)#axis=0表示沿矩阵的列方向进行均值计算
            return centroids,x
#调用函数过程
kmc=KMF()
path='D:/python/k-means/testSet.txt'
data=kmc.loadDataSet(path)  #把数据装成一个list集合了
print('data:')
print(data)
dataMat=mat(data)   #将数据按照矩阵方式输出
print('dataMat:')
print(dataMat)

centroids,x=kmc.kMeans(dataMat,4)
print('centroids:\nx:')
print(centroids,x)
