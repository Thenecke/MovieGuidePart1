# Function to display the header and menu choices for the user
def display_menu():
    print("\n===== Movie Management Menu =====")
    print("1. View all movies")
    print("2. Delete a movie")
    print("3. Exit")
    print("=================================")

# Function to pre-populate a list of movie titles
def populate_movie_list():
    movies = ["Inception", "The Matrix", "Interstellar"]
    return movies

# Function to display all movie titles
def display_movies(movies):
    if len(movies) == 0:
        print("No movies available.")
    else:
        print("\nMovie Titles:")
        for index, movie in enumerate(movies):
            print(f"{index + 1}. {movie}")

# Function to delete a movie by its index
def delete_movie(movies):
    try:
        movie_index = int(input("\nEnter the number of the movie to delete: ")) - 1
        if 0 <= movie_index < len(movies):
            deleted_movie = movies.pop(movie_index)
            print(f"\nMovie '{deleted_movie}' has been deleted.")
        else:
            print("\nInvalid movie number. Exiting the program.")
            exit()
    except ValueError:
        print("\nInvalid input. Exiting the program.")
        exit()

# Main function to handle the program logic
def movie_management_program():
    movies = populate_movie_list()  # Pre-populate movie list

    while True:
        display_menu()  # Display menu choices
        try:
            choice = int(input("\nChoose an option: "))
        except ValueError:
            print("\nInvalid command. Exiting the program.")
            break

        if choice == 1:
            display_movies(movies)  # Display all movie titles
        elif choice == 2:
            display_movies(movies)  # Show movies before deleting
            delete_movie(movies)  # Delete a movie by user input
        elif choice == 3:
            print("\nExiting the program.")
            break
        else:
            print("\nInvalid command. Exiting the program.")
            break

# Run the movie management program
movie_management_program()
