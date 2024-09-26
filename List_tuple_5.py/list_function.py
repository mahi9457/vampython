list = [2,3,4,6,5,7]
 
#  applying function on list(structure)
print(list)

list.append(8) # for add a new variable in list 
print(list)

list.sort() # for ascending
print("ascending",list)

list.sort(reverse=True) # for descending
print("descending",list)

list.reverse() # for reverse the list
print("reverse",list) 

list.insert(0,1) # for insert the new variable by they index value 
print("insert",list)

list.remove(1) # for remove any variable from the list 
print("remove any variable",list)

list.pop(1) # for remove any varaible at index
print(list)


