income=int(input("enter the income:"))
if(income<0):
 print("rate=0.00:",income)
elif(income<8925):
 print("rate=0.10:",income)
elif(income<36250):
 print("rate=0.150:",income)
elif(income<87850):
 print("rate=0.2000:",income)
else:
 print("rate=0.2500:",income)