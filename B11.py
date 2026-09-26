s = list(map(int, input('nhập danh sách số nguyên: ').split()))
tong = 0
for so in s:
    if so % 2 == 0:
        tong += so
print("Tổng các số chẵn trong danh sách là:", tong)