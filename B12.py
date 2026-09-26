s = input('Nhập chuỗi: ')
kt = max(s, key=s.count)
print("Ký tự xuất hiện nhiều nhất trong chuỗi là:", kt)
print("Số lần xuất hiện của ký tự", kt, "là:", s.count(kt))