def işlemler(ops,x,y):

        if ops == "+":
            return (str(x) + " + " + str(y) + " = " + str(x+y))
        elif ops == "-":
            return (str(x) + " - " + str(y) + " = " + str(x-y))
        elif ops == "*":
            return (str(x) + " * " + str(y) + " = " + str(x*y))
        elif ops == "/":
            return (str(x) + " / " + str(y) + " = " + str(x/y))
        else:
            print("lütfen doğru işlemi seçiniz")
while True:
    ops = input("yapmak istediğiniz işlemi seçiniz +,-,*,/: ")
    x = int(input("ilk sayıyı giriniz: "))
    y = int(input("ikinci sayıyı giriniz: "))




    print(işlemler(ops,x,y))
    break
