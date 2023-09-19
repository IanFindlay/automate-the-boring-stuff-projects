#To Do List Manager with duplicate protection

todo_list = []

def print_list():
  print()
  for item in todo_list:
    print(item)
  print()


print("Would you like to view or edit your list? ")

while True:
  menu = input("view, add or remove?: ")
  if menu == "view":
    print_list()
    print()
  elif menu == "add":
    item = input("What should I add to the todo list?: ")
    if item not in todo_list:
      todo_list.append(item)
      print()
  elif menu == "remove":
    item = input("What should I remove from the todo list?: ")
    check = input("Are you sure you want remove this item? (yes/no) ") 
    if check == "yes":
      if item in todo_list:
        todo_list.remove(item)
      else:
        print("{item} is not in the list")
      print()   
