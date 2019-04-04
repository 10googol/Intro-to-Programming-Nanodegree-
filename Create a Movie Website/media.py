import webbrowser

class Movie():
#This class is for initilizing variables and setting up functions to deal with
#anything involving the movie object

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_rating):
    #Standard __init__ function to initialize the movie class variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = movie_rating

    def show_trailer(self):
    #This function can display a movie trailer in a webbrowser when called
        webbrowser.open(self.trailer_youtube_url)

    def check_rating(self):
    #The check_rating function provides a means to ensure the rating provided
    #in the instantation of a movie object is valid and returns a text
    #statement that can be used in html or other form of GUI to display the
    #valid movie rating.
        valid_rating = ['G', 'PG', 'PG13', 'R']
        #Assign rating in valid_rating:
        if self.rating in valid_rating:
            if self.rating == 'R':
                return 'This movie is rated R'
            elif self.rating == 'PG':
                return ' This movie is rated PG'
            elif self.rating == 'PG13':
                return ' This movie is rated PG13'
            elif self.rating == 'G':
                return ' This movie is rated G'
            else:
                return ' Not a valid movie rating'
