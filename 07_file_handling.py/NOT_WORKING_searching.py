with open("practice.txt","r") as f:
    data = f.read()
    if "learning" in data:
        print("Yes")
    else:
        print("No")

# line_no = 0
# with open("practice.txt","r") as f:
#     while True:
#         # data = f.read()
#         if("Python" in f.read()):
#             print(line_no)
#         line_no += 1
#  else:
#      print("mahi word is not present in the file")