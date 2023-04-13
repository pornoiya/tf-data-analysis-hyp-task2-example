import pandas as pd
import numpy as np
from hyppo.ksample import MMD

chat_id = 146155552 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    stat, pvalue = MMD().test(x, y)
    return pvalue < 0.06
