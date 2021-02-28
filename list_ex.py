fruits=["Apple","Banana","Mango","Pineapple","Kiwi","Orange","Watermelon","Plum"]
print(f'Current List of fruits: {fruits}')
print (fruits)

new_item = input("Enter the new fruit to add:")
#fruits.append(new_item)
fruits.insert(2,new_item)
print(fruits)
print(fruits.count("Apple"))
fruits.sort(reverse=False)
print(fruits)


#print(fruits[5])
#fruits.remove("Banana")
#print(fruits)
#fruits.pop(1)
#print(fruits)