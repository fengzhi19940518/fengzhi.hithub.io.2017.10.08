import random
random.seed(10000)  #随机种子固定了权重w和偏执b
class LinearUnit:
    # 符号函数
    def sign(self, v):
       return v
    # 训练函数
    def trainning(self):
        train_data =[[5, 3, 8500], [3, 1, 5000], [8, 3, 9600], [1.4, 0, 4500], [10.1, 4, 20000],
                     [6, 3, 9000], [7, 4, 18000], [9, 3, 15000], [3, 2, 10000], [5, 2, 12000]]  # 特征x（x1,x2）和标签y
        #train_data2 = [[2, -1, -3], [3, 4 - 6], [7, 4, 2], [4, 3, -8]]  # 训练副本
        #train_datas = train_data1 + train_data2  # 训练集合

        weight = [0, 0]  # 权重
        bias = 0  # 偏置
        learn_rate = 0.05

        n = int(input('迭代次数train_num:'))  # 迭代次数
        for i in range(n):
            train=train_data[random.randint(0,len(train_data)-1)]
            #train = random.choice(train_data)
            x1, x2, y = train
            predict = self.sign(weight[0] * x1 + weight[1] * x2 + bias)  # 输出预测值
            print("train data: x: (%d, %d) y: %d  ==> predict: %d" % (x1, x2, y, predict))

            if y * predict <= 0:
                weight[0] = weight[0] + learn_rate * (y-predict) * x1  # 更新权重  (y-predict) * x1==f(x)
                weight[1] = weight[1] + learn_rate * (y-predict) * x2
                bias = bias + learn_rate * (y-predict)  # 更新偏置

                print("更新之后的权重和偏置:")
                print(weight[0], weight[1], bias)

        print("stop training:")
        print(weight[0], weight[1], bias)

        return weight, bias

    # 测试函数
    def test(self):
        weight, bias = self.trainning()
        while True:
            test_data = []
            data = input("请输入测试数据(x1,x2):")
            if data == 'q': break
            test_data += [int(n) for n in data.split(',')]
            predict = self.sign(weight[0] * test_data[0] + weight[1] * test_data[1] + bias)
            print('predict===>%d' % predict)

g = LinearUnit()
g.test()



