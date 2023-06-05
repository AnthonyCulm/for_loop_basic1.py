# Basic
for i in range(151):
    print(i)

# Multiples of Five
for j in range(5,1001,5):
    print (j)

# Counting, the Dojo Way 
for k in range(5,101):
    if (k % 5 == 0):
        print (k, "is disvable by 5")
    if (k % 10 ==0):
        print (k,  "is disvable by 10")

# Whoa. That Sucker's Huge
oddNum = 0
for l in range(0,500000):
    if l % 2 != 0:
        oddNum += l
print(oddNum)

# Countdown by Fours
for m in range (2018,0,-4):
    print(m)

# Flexible Counter
lowNum = 100
highNum = 300
mult = 3
for n in range(lowNum,highNum+1):
    if n % mult==0:
        print(n)

