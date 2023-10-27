print('-----------break-----------------')
for i in range(0, 6):
    print(i)
    if i == 3:
        break

print('-----------continue-----------------')
for i in range(0, 6):
    if i == 3 or i == 4:
        continue
    print(i)

print('------------continue------------------')
for i in range(0, 11):
    if i % 2 != 0:
        continue
    print(i)

print('------------PASS--------------------')
for i in range(0, 6):
    if i == 3 or i == 4:
        pass
    print(i)