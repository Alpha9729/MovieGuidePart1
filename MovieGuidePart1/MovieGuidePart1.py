print("The Movie List program\n")

def display_menu():
    print("COMMAND MENU")
    print("list - Display all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")

def prepopulate_list():
    return ["Monty Python and the Holy Grail", "On the Waterfront", "Cat on a Hot Tin Roof"]

def display_titles(movie_list):
    for index, title in enumerate(movie_list, start=1):
        print(f"{index}. {title}")
    print()

def add_title(movie_list):
    title = input("Name: ")
    movie_list.append(title)
    print(title +" Was added " )

def delete_title(movie_list):
    display_titles(movie_list)
    try:
        number = int(input("Number: "))
        if 1 <= number <= len(movie_list):
            movie = movie_list.pop(number - 1)
            print(f"{movie} was deleted.")
        else:
            print("Invalid movie number.")
    except ValueError:
        print("Invalid movie number.")

def main():
    movie_list = prepopulate_list()
    display_menu()
    while True:
        
        command = input("\nCommand: ")

        if command == "list":
            display_titles(movie_list)
        elif command == "add":
            add_title(movie_list)
        elif command == "del":
            delete_title(movie_list)
        elif command == "exit":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Not a valid command. Please try again.")

if __name__ == "__main__":
    main()
