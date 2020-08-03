while True:
    try:
        [a,b,c]=input().split()
        a=eval(a)
        b=eval(b)
        c=eval(c)
        area=(a+b)*c/2
        print('Trapezoid area:',area,sep='')
        print("123")
    except(EOFError):
        break
    
    
        
