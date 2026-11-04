n = int(input("Nhập n (1-100): "))
while n < 1 or n > 100:
    print("n không hợp lệ!")
    n = int(input("Nhập lại n (1-100): "))


dem_chan = 0
for i in range(1, n + 1):
    print(i)

    
    if i % 2 == 0:
        dem_chan = dem_chan + 1
print("Số lượng số chẵn:", dem_chan)
