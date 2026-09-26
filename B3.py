s = input('nhập chuỗi: ')
print(f"Chuỗi: {s}")
dem_nguyen_am = {char: 0 for char in 'ueoai'}
for char in s.lower():
    if char in dem_nguyen_am:
        dem_nguyen_am[char] += 1

print("Số lần xuất hiện của từng nguyên âm:")
for nguyen_am, so_lan in dem_nguyen_am.items():
    print(f"{nguyen_am}: {so_lan}")
print(f"Tổng số nguyên âm: {sum(dem_nguyen_am.values())}") 
