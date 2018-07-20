#program konversi biner to decimal dan sebaliknya
import math

def DecToBiner(num):
    arr = []
    while (num > 0):
        bil = num%2
        arr.append(bil)
        num = math.floor(num/2)
    print(*arr[::-1], sep="")           #untuk ilangin bracket dan koma

def BinerToDec(num):
    x = num.split()
    y = x[::-1]
    dec = 0
    for i in range (0, len(y)):
        if y[i]=='1':
            dec = dec + 2**i
        elif y[i]=='0':
            dec = dec + 0
        else:
            print("input tidak dikenali")
    print(dec)

print("Pilih:")
print("1. desimal ke biner")
print("2. biner ke desimal")
print("3. desimal ke hexa")

inputan = input("Pilihan: ")

if inputan=="1":
    dec = int(input("Masukan bilangan desimal: "))
    DecToBiner(dec)
elif inputan=="2":
    biner = input("masukkan bilangan biner (dengan spasi): ")
    BinerToDec(biner)
    

'''
45%2 = 1
22%2 = 0
11%2 = 1
5%2 = 1
2%2 = 0
1%2 = 1

1 0 1 1 0 1
'''
