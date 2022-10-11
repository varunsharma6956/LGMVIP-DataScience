fp=open("fibonacci.txt","w")
val=eval(input("Enter the upper bound: "))
fp.write("The fibonacci series is:\n")
f1=0
f2=1
while(f1<=val):
 m=(str(f1)+'\n')
 fp.write(m)
 f3=f2
 f2=f1+f2
 f1=f3
fp.close()
