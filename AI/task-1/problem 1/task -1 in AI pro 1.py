import csv
import pandas as pd

list_new = []
def Reverse(list):
    return [ele for ele in reversed(list)]

with open("onelinefile.txt","r") as data_file:
  line = data_file.readline()
def slide(txt):
    global list,list_new
    f, n= [""], 1
    for c in txt:
        if not n and c.isdigit():
            n = 1
            f.append(f"{c}")
        elif (c.isdigit() or c == ".") and n:
            f[len(f)-1] += c
        else:
            if n:
                n = 0
                f.append(f"{c}")
            else:
                f[len(f)-1] += c
    for i in range(1,len(f)+1):
        list_new.append(f[len(f)-i])
    list_new_1 = Reverse(list_new)
    for i in range(1,2*(len(f)+1),2):
        list_new_1.insert(i,',')

    del list_new_1[71:]
    for i in range(1,9):
        del list_new_1[7*i]
    return list_new_1
list = slide(line)

with open("text.txt","w") as file:
    for i in range(0,63):
            if i%6==0 and i ==6:
                file.write(f"{list[i]}\n")
            elif i%7 ==0 and i>7:
                file.write(f"\n{list[i]}")
            else:
                file.write(f"{list[i]}")
read_file = pd.read_csv (r'text.txt')
read_file.to_csv (r'Filename2.csv', index=None)
