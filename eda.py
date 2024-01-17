import pandas as pd
import matplotlib.pyplot as plt

wt=pd.read_csv(r"D:\Notes\Course\360Digitmg\2. Project - Wind Turbine Failure\Datasets\Client data\Wind_turbine.csv")

wt.head()
wt.info()

wt.isna().sum()
wt.isnull().sum()


info=wt.describe()

wt.dtypes

