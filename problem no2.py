import csv
import matplotlib.pyplot as plt
f=open("pressure.csv", "r")
f2=open("pascalToMegapascal.vsv","w")
csv_reader = csv.reader(f, delimiter=',')
l=[]
ll=[]
for lines in csv_reader:
	l.append((lines[1]))
	ll.append((lines[0]))
	
	# f2.write(lines[0]+"1000000\n")

print("li=",l[1])
l1=[]
l2=[]
c=0
f2.write("Megapascal\n")
for i in range(2,len(l)):
	l1.append(eval(l[i]))
	l2.append(eval(ll[i]))
	print((l1[c])*1000000)
	f2.write(str((l1[c])*1000000)+"\n")
	c=c+1;

plt.plot(l2,l1)
plt.xlabel('KP value')
plt.ylabel('pressure value')
plt.show()
f.close()
f2.close()