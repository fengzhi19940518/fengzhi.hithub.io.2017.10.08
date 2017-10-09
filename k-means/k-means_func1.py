from numpy import *
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

#调用函数过程
kmc=KMF()
path='D:/python/k-means/testSet.txt'
data=kmc.loadDataSet(path)  #把数据装成一个list集合了
print('data:',data)
dataMat=mat(data)   #将数据按照矩阵方式输出
print('dataMat:',dataMat)

min1=min(dataMat[:,0])  #矩阵的最小值
print('min:',min1)
max1=max(dataMat[:,1])  #矩阵的最大值
print('max:',max1)

#k个随机质心的集合，随机质心必须在整个数据集的边界之内，也就是在最小值和最大值之间
centroids=kmc.randCent(dataMat,2)   #包含2个随机质心
print('centroids:',centroids)

#计算随机两个质心的距离
distance=kmc.distEclud(dataMat[0],dataMat[1])   #经过多次测试，质心随机改变，但是质心之间的距离是不会该改变。
print('distance:',distance)