answer = []
n = 3
for i in range(1, n+1):
    a = ""
    if(i % 3 == 0):
        a+="Fizz"
    if(i % 5 == 0):
        a+= "Buzz"
    if a:
        answer.append(a)
    else:
        answer.append(i)
                
print(answer)
