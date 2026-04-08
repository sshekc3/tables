a = 1
for i in range(1,11):
    product = a * i
    if product % 2 == 0:
        print(f"{a} X {i} = {product},even")
    else:
        print(f"{a} X {i} = {product}, odd")