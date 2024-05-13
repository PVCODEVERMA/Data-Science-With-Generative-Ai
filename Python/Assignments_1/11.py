def remove_items(phone_list,laptop):
    while laptop in phone_list:
        phone_list.remove(laptop)
    return phone_list

phone_list = [1,3,4,6,5,1]
phone_to_remove = 1

result = remove_items(phone_list,phone_to_remove)
print("The list ofter removing all occurences of",phone_to_remove,":",result)
