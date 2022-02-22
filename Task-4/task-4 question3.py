"""q3----Write a python program to make a 2-dimensional list that contains represents a table of records,
for instance, student details like Roll no, Student Name, Marks; And complete the following 2 sub-tasks."""

list = [["rollno","name","marks"],[1,"Prathibha",90],[2,"Bhavana",95],[3,"Riyana",85]]
print(list)

""" i) Add some records in the list and print the list in tabular form"""

list.append([4,"Pravallika",100])
print(list)

"""ii) From created list, extract and print second record/row that contains"""

print(list[2])
