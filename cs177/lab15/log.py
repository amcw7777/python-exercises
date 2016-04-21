def log(x,y):
    if(x==1):
        return 0
    else:
        return 1+log(x/y,y)
             
              
print(log(16,2))
