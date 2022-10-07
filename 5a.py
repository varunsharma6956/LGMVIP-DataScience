for num in range(11,101):
    x=num
    sx=num*num
    flag=0
    while(x > 0):
        if(x%10!=sx%10):
          flag=1
          break
        x=x//10
        sx=sx//10
    if(flag==0):
      print("The Number is automorphic "+str(num))
