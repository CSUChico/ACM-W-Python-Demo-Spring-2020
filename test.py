#!/usr/local/bin/python
import os
import subprocess

a = subprocess.run(["ls", "-l", "."], capture_output=True)
output = a.stdout.decode("utf-8")


# x = 3
# # if x == 1:
# #     print("True")
# #     print("Hi")
# # elif x == 2:
# #     print("bob")
# # elif x == 3:
# #     print("bob")
# # else:
# #     print("False")

# # while x > 0:
# #     print(x)
# #     x=x-1
# def awesome(n):
#     for i in range(1,n+1):
#         print(i,end="")
#     # print()

# # if __name__ == '__main__':
# #     n = int(input("Enter a number: "))
# #     awesome(n)

# arr = [1,2,3]
# arr2 = [4,5,6]
# # arr.extend(arr2)
# arr += arr2
# print(arr)
# arr += [4]
# print(arr)
# # arr.append(5)
# # arr.insert(0,6)
# # print(arr)
# # long_string = "here, is, a, longish, string"
# # print(long_string.split(","))
# # for e in long_string.split():
# #     print(e)

# # datafile = open("datafile.txt","r+")
# # sum = 0
# # for line in datafile:
# #     sum += int(line.split(",")[5])
# # print(sum)

# # touple_data = (1,2,3)
# # touple_data[0] += (4)
# # print(touple_data)

# # map_data = {"key":"value"}
# # map_data[1] = "Hi"
# # map_data["bob"]=awesome
# # print(map_data[1])


