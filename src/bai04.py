n = int(input("Nhập n (1-9): "))
while n < 1 or n > 9:
    print("n không hợp lệ!")
    n = int(input("Nhập lại n: "))
for i in range(1, n + 1):
    print("Bảng cửu chương", i)

    
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)

    print("-------------------")
