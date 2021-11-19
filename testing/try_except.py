try:
    a = 1
    b = 0
    c = a / b
except:
    a = 0
    b = 1

print(a, b)

d = [1,2,None,4,5]

for i in d:
    try:
        print(1/i)
    except:
        print("error")
        continue
    print("next ------------------")