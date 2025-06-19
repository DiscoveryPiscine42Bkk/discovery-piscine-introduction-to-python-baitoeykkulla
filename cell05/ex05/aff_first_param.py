# import sys

# # print(sys.argv[3])

# if len(sys.argv) > 1:
#     print(sys.argv[1])
# else:
#     print("none")
std1 = {"name": "aa", "code": 1234}
std2 =  {"name": "bb", "code": 2356}
name = [std1, std2]

std2["code"] = 77777
print(std2["code"])