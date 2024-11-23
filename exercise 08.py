names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

def searchName():
    search = input("Enter a name to search: ")

    if search in names:
        print(f"{search} was found in the list!")
    else:
        print(f"{search} is not in the list.")

searchName()