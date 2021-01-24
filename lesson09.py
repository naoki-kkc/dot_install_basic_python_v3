for v in range(0, 10): # 0から10個分なので、0～9が生成される
    if(v == 5):
        break
    print(v)
else:
    print("done")

print()

for v in range(0, 10): # 0から10個分なので、0～9が生成される
    if(v % 2 == 0):
        continue # 0と偶数がスキップされる
    print(v)
else:
    print("done")