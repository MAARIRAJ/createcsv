import numpy as np
data=np.random.random((10,3))  # 10 rows 3 columns
np.savetxt("main.csv",data,fmt="%.2f",delimiter=',',header="H1, H2, H3, H4")

readcsv=np.loadtxt("main.csv",delimiter=',')
readcsv[:4, :]