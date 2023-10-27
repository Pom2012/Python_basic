s='Python'

for each in s:
    print('\t'+each)

print('-----------------------------------------')

for i in range(5,10):
    print(i)

print('-----------------------------------------')
s='Python programming'
for i in range(-len(s),0):
    # print(s[i].lower())
    print(s[i].upper())


print('-----------------------------------------')
s='Python programming'
for i in reversed(range(0,len(s))):
    print(s[i])


print('-----------------------------------------')
s='Python programming'
result=''
for x in s[::-1]:
    result+=x

print(result)

print('-----------------------------------------')
s='Python programming'

for x in range(1,11):
    print(s)