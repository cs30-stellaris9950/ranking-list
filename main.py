# investment




def main():
    # create list =
    with open("ranking_list_storage.txt", "r") as ranking_list_output:
        read = ranking_list_output.read()
        ranking = read.split('-')
    # ranking = []
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

        if menu_choice == 0:
            ranking = ['pizza', 'hamburger', 'good degrees']
            print("List Preseted")
            storage_writing(ranking)

        # Print List
        elif menu_choice == 1:
            print("RANK LIST")
            if not ranking:
                print("No Items in the Rank List")
            else:
                list_print(ranking)



        # Add Item to End
        elif menu_choice == 2:
            new_rank_item = input("Enter item: ")
            ranking.append(new_rank_item)
            list_print(ranking)
            storage_writing(ranking)

        # Remove Last Item
        elif menu_choice == 3:
            print(f"{ranking[len(ranking) - 1]} is removed from list")
            ranking.pop()
            list_print(ranking)
            storage_writing(ranking)

        # Insert at Position
        elif menu_choice == 4:
            insert_position = int(input("Insert Position: ")) - 1
            insert_item = input("Item to Insert: ")
            ranking.insert(insert_position, insert_item)
            list_print(ranking)
            storage_writing(ranking)

        # Remove at Position
        elif menu_choice == 5:
            remove_position = int(input("Position to Remove: ")) - 1
            print(f"{ranking[remove_position]} removed from position {remove_position}")
            ranking.remove(ranking[remove_position])
            list_print(ranking)
            storage_writing(ranking)

        # Move to Position
        elif menu_choice == 6:
            old_position = int(input("Move item from: ")) - 1
            new_position = int(input("Move Item to: ")) - 1
            thing = ranking.pop(old_position)
            ranking.insert(new_position, thing)
            list_print(ranking)
            storage_writing(ranking)

        # Edit Item
        elif menu_choice == 7:
            index_for_replace = int(input("Enter Position: ")) - 1
            replace = input("Replace with: ")
            ranking[index_for_replace] = replace
            list_print(ranking)
            storage_writing(ranking)

        # Exit
        elif menu_choice == 8:
            loop = False

        else:
            print("NOT IN MENU OPTION")


def list_print(ranking_list):
    for item in ranking_list:
        print(f"{ranking_list.index(item) + 1}. {item}")


def storage_writing(list_to_write):
    with open('ranking_list_storage.txt', 'w') as write_into:
        write_into.writelines(('-'.join(list_to_write)))
        # write_into.writelines(('-'.join(list_to_write)))
        # ('\n'.join(items))



# Call Function
main()
