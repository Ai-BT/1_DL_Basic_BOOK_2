import numpy as np


def load_data(seed=1984):
    np.random.seed(seed)
    N = 100  # 각 클래스당 데이터 포인트 수
    DIM = 2  # 데이터의 차원
    CLS_NUM = 3  # 클래스 수

    x = np.zeros((N*CLS_NUM, DIM))
    t = np.zeros((N*CLS_NUM, CLS_NUM), dtype=int)  # 여기를 int로 수정

    for j in range(CLS_NUM):
        for i in range(N):
            rate = i / N
            radius = 1.0 * rate
            theta = j * 4.0 + 4.0 * rate + np.random.randn() * 0.2
            ix = N*j + i
            x[ix] = np.array([radius*np.sin(theta), radius*np.cos(theta)])
            t[ix, j] = 1

    print("t 배열 생성:", t)

    return x, t
