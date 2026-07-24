# def printSteps():
#     print("Step1")
#     print("Step2")
#     print("Step3")
#     print("Step4")
#     print("Step5")
#     print("----------------------------")

# ans=printSteps()
# print(ans)
# printSteps()
# printSteps()

# def addVal(a,b,c=100):
#     print(a)
#     print(b)
#     print(c)
#     print(a+b+c)

# addVal(23,32,2)
# addVal(b=23,c=32,a=2)
# addVal(2,3)
# addVal(9,9,9)

# def mulNum(*a): #Tuple
#     ans=1
#     for i in a:
#         ans*=i
#     print(ans)

# mulNum(1,2,3) # t1
# mulNum(1,2,3,4,5,6) #t2

# def getDetails(**person): #dict
#     print(person)

# getDetails(name="Ken",age=66,favSport="Cricket")


# l1=[1,2,3,2,1,0]
# l1.reverse() it is reverse actual list.
# print(l1.reverse())
# print(l1[::-1])
# print(l1)

# if l1==l1[::-1]:
#     print("Pal")
# else:
#     print("Not Pal")

def product(a,b):
    return a*b

# print(product(9,product(8,product(2,product(3,5)))))


# product(1,2)
# print(22)
# name=input("Enter name: ")

# print(44,2,3,4,4,3,23,end="")

# a=1,2,3,4,5 #Tuple

# a,b,c=(1,2,3)

# a,b,c = 1,2,3
# print(a)
# print(b)
# print(c)