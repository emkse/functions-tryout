def getallenreeks():
    a,b = 0,1
    for x in range(20):
        print('fibonacci getal ' + str(x+1) + ': ' + str(a))
        a,b = b,a+b
        print('ratio: ' + str(a/b))
getallenreeks()