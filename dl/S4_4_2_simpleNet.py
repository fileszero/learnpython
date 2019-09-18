import numpy as np
import dl


class simpleNet:

    def __init__(self):
        self.W = np.random.randn(2, 3)
        # will be like
        # [
        #   [ 1.70060158  2.02770172  0.82255354]
        #   [-0.10525568  0.24024871 -1.21071375]
        # ]

    def predict(self, x):
        '''
        予測メソッド
        '''
        return np.dot(x, self.W)

    def loss(self, x, t):
        '''
        損失関数
        x: 入力データ(Not 予測済み)
        t: 教師データ
        '''
        z = self.predict(x)
        y = dl.softmax(z)
        loss = dl.cross_entropy_error(y, t)
        return loss