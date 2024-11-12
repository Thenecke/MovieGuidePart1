# Function to display the program title
def display_program_title():
    print("\n===== The Movie List Program =====")

# Function to create a file and add initial movie titles
def create_movies_file():
    with open("movies.txt", "w") as file:
        file.write("Inception\n")
        file.write("The Matrix\n")
        file.write("Interstellar\n")

# Function to display the COMMAND MENU with abbreviated commands
def display_menu():
    print("\n===== COMMAND MENU =====")
    print("list  - List all movies")
    print("add   - Add a new movie")
    print("del   - Delete a movie")
    print("exit  - Exit the program")
    print("=========================")

# Function to load movies from the file into a list
def load_movies_from_file():
    movies = []
    try:
        with open("movies.txt", "r") as file:
            movies = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("File not found. Creating a new movies.txt file.")
        create_movies_file()
        movies = load_movies_from_file()
    return movies

# Function to display all movie titles
def list_movies(movies):
    if len(movies) == 0:
        print("\nNo movies available.")
    else:
        print("\nMovie Titles:")
        for index, movie in enumerate(movies):
            print(f"{index + 1}. {movie}")

# Function to add a movie to the list and save to file
def add_movie(movies):
    new_movie = input("Enter the title of the new movie: ")
    movies.append(new_movie)
    save_movies_to_file(movies)
    print(f"\nMovie '{new_movie}' has been added.")

# Function to save the movie list back to the file
def save_movies_to_file(movies):
    with open("movies.txt", "w") as file:
        for movie in movies:
            file.write(movie + "\n")

# Function to delete a movie by its index
def delete_movie(movies):
    list_movies(movies)
    try:
        movie_index = int(input("\nEnter the number of the movie to delete: ")) - 1
        if 0 <= movie_index < len(movies):
            deleted_movie = movies.pop(movie_index)
            save_movies_to_file(movies)
            print(f"\nMovie '{deleted_movie}' has been deleted.")
        else:
            print("\nInvalid movie number. Please try again.")
    except ValueError:
        print("\nInvalid input. Please enter a valid number.")

# Main function to manage the movie list program
def movie_management_program():
    display_program_title()  # Display program title
    movies = load_movies_from_file()  # Load movies from file

    while True:
        display_menu()  # Display COMMAND MENU
        choice = input("\nEnter a command: ").lower()

        if choice == "list":
            list_movies(movies)  # List all movies
        elif choice == "add":
            add_movie(movies)  # Add a new movie
            list_movies(movies)  # Display movies after adding
        elif choice == "del":
            delete_movie(movies)  # Delete a movie
            list_movies(movies)  # Display movies after deleting
        elif choice == "exit":
            print("\nExiting the program.")
            break
        else:
            print("\nInvalid command. Please enter a valid option.")

# Run the movie management program
create_movies_file()  # Create initial file with movies
movie_management_program()
