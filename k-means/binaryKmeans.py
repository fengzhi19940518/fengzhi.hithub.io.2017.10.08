from numpy import *
from math import *

class BKM:
    def loadDataSet(self,path):
        f=open(path,'r')
        dataMat=[]
        for line in f.readlines():
            curline=line.strip().split('\t')
            fltline=list(map(float,curline))
            dataMat.append(fltline)
        return dataMat

    def distance(self,vec1,vec2):
        return sqrt(sum(power(vec1-vec2,2)))

    def randCent(self,dataSet,k):           #随机构建初始质心
        n=shape(dataSet)[1]         #数据列数
        centroids=mat(zeros((n,2)))
        for j in range(n):
            minJ=min(dataSet[:,j])
            maxJ=max(dataSet[:,j])
            rangeJ=float(maxJ-minJ)
            centroids=mat(minJ+rangeJ*random.rand(k,1))
        return centroids

    def kMeans(self,dataSet,k):  #k-均值算法：四个参数（数据集、簇的数目、距离、创建初始质心）
        n=shape(dataSet)[0]     #数据点的长度
        x=mat(zeros((n,2)))     #记录数据点到质心的距离的平方，簇分配结果矩阵x的两列分别是记录簇索引值，第二列存储误差，
        centroids=self.randCent(dataSet,k)      #中心点，质心
        flag=True               #聚类结束标志
        while flag:
            flag=False
            for i in range(n):
                minDist=inf        #设置两个变量，分别存放数据点到质心的距离，及数据点属于哪个质心
                minIndex=-1
                for j in range(k):  #变量整个簇，寻找最近的质心
                    distance=self.distance(centroids[j,:],dataSet[i,:])
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

    def binKmeans(self,dataSet,k):
        m=shape(dataSet)[0]
        x=mat(zeros((m,2)))
        #初始化一个簇
        centroid0=mean(dataSet,axis=0).tolist()[0]
        centlist=[centroid0]
        for j in range(m):          #计算初始误差
            x[j,1]=self.distance(mat(centroid0), dataSet[j,:])**2
        while (len(centlist))<k:
            lowestSSE=inf
            for i in range(len(centlist)):      #遍历每个簇,尝试划分每个簇
                ptsIncurrCluster=dataSet[nonzero(x[:,0].A==i)[0],:]
                centroidMat,spiltClustAss=self.kMeans(ptsIncurrCluster,2)
                # 划分后的误差平方和
                sseSpilt=sum(spiltClustAss[:,1])
                # 剩余的误差之和
                sseNotSpilt=sum(x[nonzero(x[:,0].A!=i)[0],1])
                print('sseSpilt,and notSpilt:',sseSpilt,sseNotSpilt)
                if(sseSpilt+sseNotSpilt)<lowestSSE:
                    bestCentToSpilt=i
                    bestNewCents=centroidMat
                    bestClustAss=spiltClustAss.copy()
                    lowestSSE=sseSpilt+sseNotSpilt
            # 更新分配结果
            bestClustAss[nonzero(bestClustAss[:,0].A==1)[0],0]=len(centlist)
            bestClustAss[nonzero(bestClustAss[:,0].A==0)[0],0]=bestCentToSpilt
            print('the bestCentToSpilt is:',bestCentToSpilt)
            print('the len of bestClustAss is:',len(bestClustAss))
            centlist[bestCentToSpilt]=bestNewCents[0,:]
            centlist.append(bestNewCents[1,:])
            x[nonzero(x[:,0].A==bestCentToSpilt)[0],:]=bestClustAss
        return mat(centlist),x


bkm = BKM()
path = 'D:/python/k-means/testSet.txt'
data = bkm.loadDataSet(path)  # 把数据装成一个list集合了print('data:')
print(data)
dataMat = mat(data)  # 将数据按照矩阵方式输出
print('dataMat:')
print(dataMat)
print('\n')
centroids, x = bkm.binKmeans(dataMat, 4)
print('centroids:\nx:')
print(centroids, x)

