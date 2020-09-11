from ctypes import c_longlong as long
l=[5,7,7,9,9,10]
target_value=eval(input("target value="))
first=0
last=len(l)-1
mid=first+int((last-first)/2)

flag=0
while last>=first:
	# print(first,mid,last)
	if l[mid]==target_value:
		flag=1;
		# //print("mid=",mid)
		first_range=last_range= search_index=mid
		break
	elif l[mid]>target_value:
		last=mid-1;
		mid=first+int((last-first)/2)
	elif l[mid]<target_value:
		first=mid+1;
		mid=first+int((last-first)/2)
if flag==1:
	c1=1;
	while(search_index+c1<len(l) and l[search_index+c1]==target_value):
		last_range=search_index+c1
		c1+=1
	c2=1
	while(l[search_index-c2]==target_value):
		first_range=search_index-c2
		c2+=1
	print("[",first_range,last_range,"]")
else:
	print("[",0,0,"]")
