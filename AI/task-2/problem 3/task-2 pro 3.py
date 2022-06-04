import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set()

plt.rcParams['font.size'] = 2

fig,axes = plt.subplots(3)
list_y = []
list_x = []
list_z = []
list_sum = []
for i in range(0,36):
    list_x.append(i)
    y=np.sin(i)
    list_y.append(y)
    z=np.cos(i)
    list_z.append(z)
    sum= y+z
    list_sum.append(sum)

axes[0].plot(list_x,list_y)
axes[0].set_title("sinx")

axes[1].plot(list_x,list_z)
axes[1].set_title("cosx")

axes[2].plot(list_x,list_sum)
axes[2].set_title("cosx + sinx")

plt.show()
