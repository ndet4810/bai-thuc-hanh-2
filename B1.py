s = input("Nhập chuỗi: ")

print(f"Độ dài của chuỗi: {len(s)}")

dem_ky_tu = {}
for char in s:
    if char in dem_ky_tu:
        dem_ky_tu[char] += 1
    else:
        dem_ky_tu[char] = 1

print("\nSố lần xuất hiện của mỗi ký tự:")
for char, count in dem_ky_tu.items():
    ten_char = "' '" if char == " " else char
    print(f"Ký tự {ten_char}: {count} lần")