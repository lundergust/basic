friends = ["Chandler", "Monica", "Joey", "Pheobe", "Ross", "Rachel"]
# change an item in the list:  friends[1] = "Richard"
# print only items from 1 up to 3  print(friends[1:3])
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends.extend(lucky_numbers)
print(friends)
friends.append("Mike")
print(friends)
friends.insert(1, "ur mom")
print(friends)
friends.remove("Ross")
print(friends)
friends.pop()   #removes last item in list
print(friends)
print(friends.index("Joey"))
friends.append("Chandler")
print(friends.count("Chandler"))
friends.sort()
print(friends)
lucky_numbers.reverse()
print(lucky_numbers)
friends2 = friends.copy()


print(friends.index("Michael"))
friends.clear
