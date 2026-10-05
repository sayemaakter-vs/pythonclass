_list=["apple","banana","chips","juice"]
item=input("enter: ").lower()
for i in _list:
    if item!=i:
        print("not available")
        _list.append(item)
    else:
        print("available")
        break
     
print(_list)