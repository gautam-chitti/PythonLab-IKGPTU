my_list = []
my_list.append("Apple")
my_list.append("Banana")
my_list.append("Cherry")

print("Initial List:", my_list)

my_list.extend(["Date", "Elderberry", "Fig"])

print("List after extending:", my_list)

my_list.remove("Banana")

print("List after removing 'Banana':", my_list)

my_list.remove("Date")

print("List after removing 'Date':", my_list)

while "Fig" in my_list:
    my_list.remove("Fig")

print("List after removing all 'Fig's:", my_list)

my_list.pop(0)

print("List after removing the first element:", my_list)

my_list.clear()

print("List after clearing:", my_list)