import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# generate random input channels
x = np.linspace(-10, 10, 10)
max_series = pd.Series(np.reshape(np.sin(x) + np.random.rand(1,len(x)),-1), name='max')
min_series = pd.Series(np.reshape(np.sin(x) - np.random.rand(1,len(x)),-1), name='min')
df = pd.DataFrame(pd.concat([max_series, min_series], axis=1))
df.index = pd.date_range(start='1/1/2018', periods=len(x), freq='1d')

# another option
n_sensors = 10
t = pd.date_range(datetime.now(), datetime.now() + timedelta(0.5), freq='H')
df_2 = pd.DataFrame(np.random.uniform(low=-5, high=5, size=(len(t), n_sensors)), columns=['S' + str(i) for i in range(0, n_sensors)])
df_2['timestamp'] = t
df_2 = df_2.set_index('timestamp')