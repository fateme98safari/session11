import numpy as np
rug=[]
n=int(input("Enter an odd number: "))
if n % 2 != 0:
    rug=np.array(range(1,(n**2)+1)).reshape(n,n)
    rug[n//2][n//2]=0
    for i in range(1,(n+1)//2,1):
        rug[(n//2)+i]=i
        rug[(n//2)-i]=i
        rug[:,(n//2)-i]=i
        rug[:,(n//2)+i]=i
    print(rug)
else:
    print("Sorry!Even number is not available")

              