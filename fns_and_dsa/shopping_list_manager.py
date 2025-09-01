
 
 
def menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2.Remove item")
    print("3.View list")
    print("4.Exit")
    
def main():
    shopping_list=[]
    while True:
        menu()
        choice=input("Enter your choice(1-4): ")
        if choice ==1:
            item=input("Enter the item to add: ")
            shopping_list.append(item)
        elif choice ==2:
            item=input("Enterr the item you want to remove:")
            shopping_list.remove(item)
        elif choice ==3:
            print("Tgis is the current shopping list:")
            for item in shopping_list:
                print(item)
        elif choice ==4:
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__=="__main__":
    main()
            