def gugudan1():
    for j in range(1,10):
        print("%d x %d = %d" %(1, j, j))

def gugudan2():
    for j in range(1,10):
        print("%d x %d = %d" %(2, j, 2*j))

def gugudan3():
    for j in range(1,10):
        print("%d x %d = %d" %(3, j, 3*j))

def gugudan4():
    for j in range(1,10):
        print("%d x %d = %d" %(4, j, 4*j))

def gugudan5():
    for j in range(1,10):
        print("%d x %d = %d" %(5, j, 5*j))

def gugudan6():
    for j in range(1,10):
        print("%d x %d = %d" %(6, j, 6*j))

def gugudan7():
    for j in range(1,10):
        print("%d x %d = %d" %(7, j, 7*j))

def gugudan8():
    for j in range(1,10):
        print("%d x %d = %d" %(8, j, 8*j))

def gugudan9():
    for j in range(1,10):
        print("%d x %d = %d" %(9, j, 9*j))

gugudic = {1:gugudan1, 2:gugudan2, 3:gugudan3, 4:gugudan4, 5:gugudan5, 6:gugudan6, 7:gugudan7, 8:gugudan8, 9:gugudan9};


while True:
    number = input("몇 단? = ")
    if number.isdecimal() == 0:
        print('다시 입력하여 주십시오')
    elif int(number) > 9 or int(number) < 1:
        print('다시 입력하여 주십시오')
    else:
        gugudic[int(number)]()
        break



