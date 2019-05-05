'''
Movie Project Brief
1. Application Layer
Ask user to add a new movie
View all the movie added
Allow the user to find a particular movie by its attribute
2. Storage Layer
3. Retrieval Layer
'''

movie_list = []
welcome_msg = '''
Welcome to the Movie Project App. Please select one of the below options to continue
1. Press 1 to add a new movie
2. Press 2 to view your movie library
3. Press 3 to find a movie
4. Press 4 to quit the app : '''


# Function to append a movie dict to the movie list based on user input
def add_movie():
    usr_input = 'y'
    while usr_input != 'n':

        movie_name = input('Enter the name of the movie: ')
        movie_director = input('Enter the Director of the movie: ')
        movie_year = input('Enter the year of the movie: ')
        movie_actor = input('Enter the actor of the movie: ')
        movie_list.append(movie_template(movie_name, movie_director, movie_year, movie_actor))
        msg = f'''
The movie with following attributes were added to your library: 
Movie Name: {movie_name} Movie Director: {movie_director}
Movie Year: {movie_year} Movie Actor: {movie_actor}
            '''
        print(msg)
        usr_input = input('Do you want to add another movie?(y/n): ')


def movie_template(name, director, year, actor):
    movie_dict = {
        'movie_name': name,
        'movie_director': director,
        'movie_year': year,
        'movie_actor': actor
    }
    return movie_dict


def show_movie():
    sho_input = 'n'
    while sho_input != 'y':
        print('The following movies are in your library')
        for item in movie_list:
            for key, value in item.items():
                print(f'The {key} is {value}')
            print('--------------------------')

        sho_input = input('Do you want to back to main menu?(y/n): ')


def find_movie():
    prop = input('What is the attribute you want to search for: ')
    val = input('What is value you want to search for: ')
    for movie in movie_list:
        if prop in movie.keys() and val in movie.values():
            print(movie)


user_input = 0

while user_input != 4:
    user_input = int(input(welcome_msg))
    if user_input == 1:
        add_movie()
    elif user_input == 2:
        show_movie()
    elif user_input == 3:
        find_movie()
    print(user_input)


