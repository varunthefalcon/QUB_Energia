import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

raw_1 = pd.read_excel('D:/UK/assignment/DSA8023/WB1_Energia_Challenge_March_2023_Data.xlsx', sheet_name=1, index_col='accountID')
raw_2 = pd.read_excel('D:/UK/assignment/DSA8023/WB2_Energia_Challenge_March_2023_Data.xlsx', sheet_name=1, index_col='accountID')
raw_d = pd.concat([raw_1, raw_2])

raw_d.head()