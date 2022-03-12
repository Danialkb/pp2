a, cnt1, cnt2 = input(), 0, 0


cnt1 = sum(1 for i in a if i.isupper())
cnt2 = sum(1 for j in a if j.islower())


print(f'Upper case: {cnt1}\nLower case: {cnt2}')