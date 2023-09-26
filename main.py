# investment




def main():
    # create list =

    ranking = []
    print(ranking)


    # loop
    loop = True
    while loop:
        print(f"***MAIN MENU***"
              "\n0. Preset the list"
              "\n1. Print List "
              "\n2. Add Item to End "
              "\n3. Remove Last Item "
              "\n4. Insert at Position "
              "\n5. Remove at Position "
              "\n6. Move to Position"
              "\n7. Edit Item "
              "\n8. Exit")
        menu_choice = int(input("Enter Option #: "))

        if  menu_choice == 0:
            ranking = ['pizza', 'hamburger', 'good degrees']
            print("List Preseted")

        # Print List
        elif menu_choice == 1:
            print("RANK LIST")
            if not ranking:
                print("No Items in the Rank List")
            else:
                list_print(ranking)
                # for item in ranking:
                #     print(f"{ranking.index(item) + 1}. {item}")

        # Add Item to End
        elif menu_choice == 2:
            new_rank_item = input("Enter item: ")
            ranking.append(new_rank_item)
            list_print(ranking)

        # Remove Last Item
        elif menu_choice == 3:
            print(f"{ranking[len(ranking) - 1]} is removed from list")
            ranking.pop()
            list_print(ranking)

        # Insert at Position
        elif menu_choice == 4:
            insert_position = int(input("Insert Position: ")) - 1
            insert_item = input("Item to Insert: ")
            ranking.insert(insert_position, insert_item)
            list_print(ranking)

        # Remove at Position
        elif menu_choice == 5:
            remove_position = int(input("Position to Remove: ")) - 1
            print(f"{ranking[remove_position]} removed from position {remove_position}")
            ranking.remove(ranking[remove_position])
            list_print(ranking)

        # Move to Position
        elif menu_choice == 6:
            old_position = int(input("Move item from: ")) - 1
            new_position = int(input("Move Item to: ")) - 1
            ranking.insert(new_position, ranking[old_position])
            # ranking.pop(old_position)
            list_print(ranking)

        # Edit Item
        elif menu_choice == 7:
            index_for_replace = int(input("Enter Position: ")) - 1
            replace = input("Replace with: ")
            ranking[index_for_replace] = replace
            list_print(ranking)

        # Exit
        elif menu_choice == 8:
            loop = False

def list_print(list):
    for item in list:
        print(f"{list.index(item) + 1}. {item}")

# Call Function
main()
