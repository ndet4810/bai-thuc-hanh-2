s = input("Nhập chuỗi: ")

dem = {}

for chuoi in s:
    if chuoi in dem:
        dem[chuoi] += 1
    else:
        dem[chuoi] = 1

print("Kết quả:")
for chuoi, count in dem.items():
    print(f"{chuoi}: {count}")