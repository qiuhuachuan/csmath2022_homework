'''
Author: Huachuan Qiu
Student ID: 12163193
Date: 2022-3-10
'''

import random
from typing import Tuple

import numpy as np
import pandas as pd


def set_seed_number(seed_number: int) -> None:
    '''
    固定随机种子
    '''
    random.seed(seed_number)
    np.random.seed(seed_number)

def generate_data(
    x_range: Tuple[float, float],
    sample_number: int) -> None:
    '''
    根据输入的样本数量生成样本数据
    '''
    base_func = lambda x: np.sin(2 * np.pi * x)
    X = np.linspace(x_range[0], x_range[1], num=sample_number)
    Y = base_func(X) + np.random.normal(loc=0.0, scale=0.2, size=X.shape)
    
    df = pd.DataFrame(data=np.dstack([X,Y])[0], columns=['x', 'y'])
    file_name = f'./data/examples_{sample_number}.csv'
    df.to_csv(file_name)



if __name__ == '__main__':
    set_seed_number(42)

    for num in [10, 15, 100]:
        '''
        根据列表中的数字，生成指定数量的样本数据
        '''
        generate_data((0.0, 1.0), num)

    
