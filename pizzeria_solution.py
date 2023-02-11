import numpy as np
import sys

def block_create(n,x,y,r):
    n=n
    x=x-1
    y=y-1
    r=r
    block=np.zeros((n,n))
    block[x][y]=1
    for i in range(n):
        for j in range(n):
            if (i==x):
                if ((j!=y)&((j>=(y-r))&(j<=(y+r)))):
                    block[i][j]=1
            if (j==y):
                if (i!=x):
                    if (i>=(x-r))&(i<=(x+r)):
                        block[i][j]=1
    for i in range(1,r):
        for j in range(0, i+1):        
            if x+i-r<n-1 and y-j<n-1 and y-j>=0 and x+i-r>=0 :
                block[x+i-r][y-j] = 1

            if x-i+r<n-1 and y+j<n-1 and y+j>=0 and x-i+r>=0 : 
                block[x-i+r][y+j] = 1

            if x+i-r<n-1 and y+j<n-1 and y+j>=0 and x+i-r>=0:
                block[x+i-r][y+j] = 1 

            if x-i+r<n-1 and y-j<n-1 and y-j>=0 and x-i+r>=0: 
                block[x-i+r][y-j] = 1
    return block



if __name__ == '__main__':
    rows=[]
    for lines_input in sys.stdin:
        rows.append(lines_input)
    spec = rows[0].split()

    n=int(spec[0])
    no_pizzerias=int(spec[1])
    if 1<=n<=10000 or 1<=no_pizzerias<=10000:
        sum=np.zeros((n,n))
        for i in range(1,no_pizzerias+1):
            pizzerias_spec=rows[i].split()
            x=int(pizzerias_spec[0])
            y=int(pizzerias_spec[1])
            r=int(pizzerias_spec[2])
            if (1<=r<=5000):
                block=block_create(n,x,y,r)
                sum=sum+block
            else:
                print("R is not in range[1:5000]")
                break()
            max=int(np.max(sum))
            print(max)
    else:
        print("N or M is not in range[1:10000]")





