ch=int(input("press 1 for 1st , 2 for 2nd , 3 for 3rd"))
if(ch==1):
 r=eval(input("Enter the no of rows:"))
 for i in range(1,r+1):
  for j in range(1,r+1):
   if(j==i or j==r+1-i):
    print("$",end=" ")
   elif (i!=1 or i!=r) and (j==1 or j==r):
    print("*",end=" ")
   elif (i==1 or i==r) and (j!=1 or j!=r):
    print("*",end=" ")
   else:
    print(" ",end=" ")
  print("")
elif(ch==2):
 n=int(input("Enter the number of rows:"))
 c=0
 for i in range(n,0,-1):
   for j in range(i):
     print(chr(j+65),end=" ")
   for s in range(0,n-i):
     print(" ",end=" ")
   if i==n:
       for l in range(i-2,-1,-1):
         print(chr(l+65),end=" ")
   else:
      for m in range(n-i,1,-1):
         print(" ",end=" ")
      for k in range(i-1,-1,-1):
         print(chr(k+65),end=" ")
   print()


elif(ch==3):
 n=eval(input("Enter the number of rows "))
 for i in range(1,n+1):
     for sp in range(1,n-i+1):
         print(" ",end='')
 
     for num in range(1,i+1):
         print(num,end='')
        
     print()
