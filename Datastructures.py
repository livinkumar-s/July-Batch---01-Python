# Slicing

a="Hello world"
# print(a[4:])
# print(a[:7])
# print(a[2:5])
# print(a[1:7:2]) #1,3,5

# print(a[::-1])

# l1=[1,2,3,4,5]
# print(l1[::-1])
# print(l1[1:2]) #[2]
# print(l1[1]) #2

# List 

# l1=[1,2,"Hello",3.14,True, False,2]
# print(len(l1))
# print(l1[4])
# l1[3]=4.44
# l1.append(99)
# l1.append(100)
# l1.append(100)
# l1.insert(-3, "Yup..!")
# l1.extend([1,2,3])

# l1.remove(2)
# l1.remove(2)

# l1.pop(2)
# l1.pop()
# l1.pop()
# l1.pop()
# l1=[1,2,"Hello",3.14,True, False,2]

# print(l1.index(3.14346))
# print(l1.count(1))

# print(1==True)

# l2=[321,423,3,4,6,6,243]
# l2.reverse()
# l2.sort(reverse=True)
# print(l2)

# Tuple
t1=(1,2,3,3,2,1,"Hello")
# print(t1[2])
# t1[5]=10

# person=("Kane",44,"FED")
# name,age,role=person

# print(age)


# Set 

# s1={4,5,6,7,8}
# s2={1,2,3,4,5,4,3,2,1}
# s1.add(999)
# s1.remove(56)
# s1.clear()
# print(s1)
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))
# print(s2.difference(s1))
# print(s1&s2)
# print(s1*s2)

# Dict 

# person1={
#     "name":"Ken",
#     "age":23,
#     "Role":"SASE",
#     "isMarried":False,
#     "isPresent":False,
# }

# person1["isPresent"]=True
# person1["favMovies"]=["24","I"]

# person1.pop("isMarried")
# person1.clear()

# print(person1.keys())
# print(person1.values())
# print(person1.items())

# for i in {1,2,3,4,4,3,2,1}:
#     print(i)

# for i in person1:
#     print(person1[i])


# l1=[
#     1,
#     2,
#     3,
#     [
#         "four",
#         "five",
#         "six",
#         [
#             "seven",
#             "eight",
#             "nine"
#         ]
#     ]
# ]

# # print(l1[3][3][2])
# print(l1[-1][-1][-1][-1])