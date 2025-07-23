roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
n = 0
num = input("Enter the roman digit")
for i in range(len(num)):
    if i < len(num) - 1 and roman[num[i]] < roman[num[i + 1]]: 
        n = n - roman[num[i]]
    
    else:
        n =n + roman[num[i]]
print(n)

