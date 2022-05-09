import matplotlib.pyplot as plt
import pandas as pd
nsteps = int( (2400-700)/10)
X = [700+nsteps*i for i in range(0,nsteps+1) if i <11]

Y = [(10*(t**2))+2*t for t in X]
plt.plot(X,Y,'ro--', label= 'size of house vs price')
plt.legend()
plt.xlabel('size of house')
plt.ylabel('price')
plt.title('size of house vs price')
plt.grid()
plt.show()
with open("graph.txt","w") as file:
    file.write(f"X cordinates, Y cordinates \n")
    for i in range(0,len(X)):
        file.write(f"{str(X[i])},{str(Y[i])} \n")

read_file = pd.read_csv (r'graph.txt')
read_file.to_csv (r'graph.csv', index=None)
