n = int(input("Nhập n (1-100): "))
while n < 1 or n > 100:
    print("n không hợp lệ!")
    n = int(input("Nhập lại n (1-100): "))
tong_chan = 0
tong_le = 0
for i in range(1, n + 1):

    
    if i % 2 == 0:
        tong_chan = tong_chan + i

    
    else:
        tong_le = tong_le + i
print("Tổng các số chẵn:", tong_chan)
print("Tổng các số lẻ:", tong_le)
