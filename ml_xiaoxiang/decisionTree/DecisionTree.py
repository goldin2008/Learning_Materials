#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

from sklearn.cross_validation import train_test_split
import random

def iris_type(s):
    it = {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2}
    return it[s]

# 花萼长度、花萼宽度，花瓣长度，花瓣宽度
# iris_feature = 'sepal length', 'sepal width', 'petal length', 'petal width'

def split(self, tree):
    f = self.select_feature()
    self.choose_value(f, tree)

def select_feature(self):
    n = len(data[0])
    if rf:
        return random.randint(0, n-2)
    gini_f = 1
    f = -1
    for i in range(n-1):
        g = self.gini_feature(i)
        if gini_f > g:
            gini_f = g
            f = i
    return f

class TreeNode:
    def __init__(self):
        self.sample = []
        self.feature = -1
        self.value = 0
        self.type = -1
        self.left = -1
        self.right = -1
        self.gini = 0

    def gini_coefficient(self):
        types = {}
        for i in self.sample:
            type = data[i][-1]
            if types.has_key(type):
                types[type] += 1
            else:
                types[type] = 1
        pp = 0
        m = float(len(self.sample))
        for t in types:
            pp += (float(types[t]) / m) ** 2
        self.gini = 1 - pp
        max_type = 0
        for t in types:
            if max_type < types[t]:
                max_type = types[t]
                self.type = t
        

def choose_value(self, f, tree):
    f_max = self.calc_max(f)
    f_min = self.calc_min(f)
    step = (f_max - f_min) / granularity
    if step == 0:
        return f_min
    x_split = 0
    g_split = 1
    for x in numpy.arange(f_min + step, f_max, step):
        if rf:
            x = random.uniform(f_min, f_max)
        g = self.gini_coefficient2(f, x)
        if g_split > g:
            g_split = g
            x_split = x
    if g_split < self.gini:
        self.value = x_split
        self.feature = f
        t = TreeNode()
        t.sample = self.choose_sample(f, x_split, True)
        t.gini_coefficient()
        self.left = len(tree)
        tree.append(t)
        t = TreeNode()
        t.sample = self.choose_sample(f, x_split, False)
        t.gini_coefficient()
        self.right = len(tree)
        tree.append(t)

def decision_tree():
    m = len(data)
    n = len(data[0])
    tree = []
    root = TreeNode()
    if rf:
        root.sample = random_select(alpha)
    else:
        root.sample = [x for x in range(m)]
    root.gini_coefficient()
    tree.append(root)
    first = 0
    last = 1
    for level in range(max_level):
        for node in range(first, last):
            tree[node].split(tree)
        first = last
        last = len(tree)
        print level + 1, len(tree)
    return tree

def predict_tree(d, tree):
    node = tree[0]
    while node.left != -1 and node.right != -1:
        if d[node.feature] < node.value:
            node = tree[node.left]
        else:
            node = tree[node.right]
    return node.type

def predict(d, forest):
    pd = {}
    for tree in forest:
        type = predict_tree(d, tree)
        if pd.has_key(type):
            pd[type] += 1
        else:
            pd[type] = 1
    number = 0
    type = 0.0
    for p in pd:
        if number < pd[p]:
            number = pd[p]
            type = p
    return type




if __name__ == "__main__":
    # path = u'..\\算法讲师\\机器学习升级版\\数据\\4.iris.data'  # 数据文件路径
    # path = './4.iris.data'  # 数据文件路径
    path = './monks-1.test'  # 数据文件路径

    # 路径，浮点型数据，逗号分隔，第4列使用函数iris_type单独处理
    # data = np.loadtxt(path, dtype=float, delimiter=',', converters={4: iris_type})
    data = np.loadtxt( path, dtype=str, delimiter=' ' )
    # print data
    data = data[:, 1:8]
    data = data.astype(float)
    # print data

    # 将数据的0到3列组成x，第4列得到y
    # x, y = np.split(data, (4,), axis=1)
    y , x  = np.split(data, (1,), axis=1)
    # 为了可视化，仅使用前两列特征
    # x = x[:, :2]

    # print 'y = ', y
    # print 'x = ', x

    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.25, random_state=42)
    # print 'number of training data = ', len(X_train)
    # print 'number of testing data = ', len(X_test)
    # print 'training data X = ', X_train
    # print 'testing data X = ', X_test

    # Decision Tree by own code
    # rf = 1
    # dt =  decision_tree()
    # print dt



    # 决策树参数估计
    # min_samples_split = 10：如果该结点包含的样本数目大于10，则(有可能)对其分支
    # min_samples_leaf = 10：若将某结点分支后，得到的每个子结点样本数目都大于10，则完成分支；否则，不进行分支
    clf = DecisionTreeClassifier(criterion='entropy', max_depth=30, min_samples_leaf=3)
    # dt_clf = clf.fit(x, y)
    dt_clf = clf.fit(X_train, Y_train)

    # 保存
    # dot -Tpng -o 1.png 1.dot
    # f = open("iris_tree.dot", 'w')
    # tree.export_graphviz(dt_clf, out_file=f)

    # 画图
    # N, M = 500, 500  # 横纵各采样多少个值
    # x1_min, x1_max = x[:, 0].min(), x[:, 0].max()  # 第0列的范围
    # x2_min, x2_max = x[:, 1].min(), x[:, 1].max()  # 第1列的范围
    # t1 = np.linspace(x1_min, x1_max, N)
    # t2 = np.linspace(x2_min, x2_max, M)
    # x1, x2 = np.meshgrid(t1, t2)  # 生成网格采样点
    # x_test = np.stack((x1.flat, x2.flat), axis=1)  # 测试点

    # # 无意义，只是为了凑另外两个维度
    # # 打开该注释前，确保注释掉x = x[:, :2]
    # x3 = np.ones(x1.size) * np.average(x[:, 2])
    # x4 = np.ones(x1.size) * np.average(x[:, 3])
    # x5 = np.ones(x1.size) * np.average(x[:, 4])
    # x6 = np.ones(x1.size) * np.average(x[:, 5])

    # x_test = np.stack((x1.flat, x2.flat, x3, x4, x5, x6), axis=1)  # 测试点

    # y_hat = dt_clf.predict(x_test)  # 预测值
    # y_hat = y_hat.reshape(x1.shape)  # 使之与输入的形状相同
    # plt.pcolormesh(x1, x2, y_hat, cmap=plt.cm.Spectral, alpha=0.5)  # 预测值的显示Paired/Spectral/coolwarm/summer/spring/OrRd/Oranges
    # plt.scatter(x[:, 0], x[:, 1], c=y, edgecolors='k', cmap=plt.cm.prism)  # 样本的显示
    # plt.xlabel(iris_feature[0])
    # plt.ylabel(iris_feature[1])
    # plt.xlim(x1_min, x1_max)
    # plt.ylim(x2_min, x2_max)
    # plt.grid()
    # plt.show()

    # 训练集上的预测结果
    # y_hat = dt_clf.predict(x)
    # y = y.reshape(-1)       # 此转置仅仅为了print时能够集中显示
    # print y_hat.shape       # 不妨显示下y_hat的形状
    # print y.shape
    # result = (y_hat == y)   # True则预测正确，False则预测错误
    # print y_hat
    # print y
    # print result
    # c = np.count_nonzero(result)    # 统计预测正确的个数
    # print c
    # print 'Accuracy: %.2f%%' % (100 * float(c) / float(len(result)))

    # 测试集上的预测结果
    Y_hat = dt_clf.predict(X_test)
    Y = Y_test.reshape(-1)       # 此转置仅仅为了print时能够集中显示
    print Y_hat.shape       # 不妨显示下y_hat的形状
    print Y_test.shape
    result = (Y_hat == Y)   # True则预测正确，False则预测错误
    # print Y_hat
    # print Y_test
    # print result
    c = np.count_nonzero(result)    # 统计预测正确的个数
    print 'Number of Correct predicted data', c
    print 'Number of Testing data = ', len(result)
    print 'Accuracy: %.2f%%' % (100 * float(c) / float(len(result)))


