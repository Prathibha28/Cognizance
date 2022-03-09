import pandas as pd

ser = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai', 'campus'])
new_ser = ser.str.title()
new_string = ""
for(index,words) in new_ser.iteritems():
   new_string += words
   new_string += " "
print(new_string)
