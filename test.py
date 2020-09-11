
import csv

with open("pressure.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    l=[]
    for lines in list(csv_reader):
    	print()
    	l.append((lines[0]))
    l1=[]
    c=0
    for i in range(2,len(l)):
    	l1.append(eval(l[i]))
    	print(type(l1[c]))
    	c=c+1;
    with open('employee_file.csv', mode='w') as employee_file:
    	employeewriter = csv.writer(employee_file, delimiter=',')
    	
    	for lines in list(csv_reader):
    		print((lines[0]))
    	
    
    



    

# import matplotlib.pyplot as plt
# plt.plot([1, 2, 3, 4])
# plt.ylabel('some numbers')
# plt.show()