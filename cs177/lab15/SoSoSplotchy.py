def SoSoSplotchy(n):
    if n==0:
        return 1
    elif n==1:
        return 2
    else:
        return 2 * SoSoSplotchy(n-1) + SoSoSplotchy(n-2)

def main():
    print (SoSoSplotchy(5))

main()
