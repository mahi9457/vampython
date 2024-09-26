list = [1,2,3,9,1]

copy_list = list.copy()
copy_list.reverse() 

if( list == copy_list):
    print("Palindrom")
elif( list != copy_list):
    print(" Not Palindrom")
