def getMin(A):
    if(len(A)==1 or A[0]<getMin(A[1:])):
        return A[0]
    else:
        return getMin(A[1:])
             
              
A=[3,-1,5,7,2,4]    
print(getMin(A))
