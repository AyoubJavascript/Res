
    def reverse( x):
        x = str(x)
        num = 0
        if x[0] == "-" or x[0] =="+" :
            num = int(x[1:][::-1])
            if  -2**31 <= num < 2**31 :return -num
            else : return 0
        else :
            num = int(x[::-1])
            if  -2**31 <= num < 2**31 :return num
            else : return 0
        return num
