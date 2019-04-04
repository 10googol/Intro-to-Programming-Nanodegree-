# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

apollo13 = media.Movie('Apollo 13', '''Houston we have a problem. On the way to
                       the moon a million things can go wrong, one does.''',
                       'apollo13.jpg',
                       'https://www.youtube.com/watch?v=e3ZtOS4MCkk', 'PG')
django = media.Movie('Django Unchained', '''A freed slave sets out to rescue his wife from
                      a brutal Mississippi plantation owner.''',
                     'Django.jpg',
                     'https://www.youtube.com/watch?v=0fUCuvNlOCg&t=2s', 'R')
flagsofourfathers = media.Movie('Flags of Our Fathers', '''The life stories of
                                the six men who raised the flag at the Battle
                                of Iwo Jima.''',
                                'Flags of Our Fathers.jpg',
                                'https://www.youtube.com/watch?v=RYZDVrkDi-8', 'R')
lettersfromiwojima = media.Movie('Letters from Iwo Jima', '''The story of the
                                  battle of Iwo Jima as told from the perspective
                                  of the Japanese who fought it.''',
                                 'Letters from Iwo Jima.jpg',
                                 'https://www.youtube.com/watch?v=JoOZjSHYsro',
                                 'R')
ingloriousbasterds = media.Movie('Inglorious Basterds', '''In Nazi-occupied
                                  France a plan to assassinate Nazi leaders by
                                  Jewish U.S. soldiers.''',
                                 'Inglorious Basterds.jpg',
                                 'https://www.youtube.com/watch?v=qRYDNWXuip8', 'R')
imitationgame = media.Movie('The Imitation Game', '''During World War II, the
                            English mathematical genius Alan Turing tries to
                            crack the German Enigma code.''', 'Imitation Game.jpg',
                            'https://www.youtube.com/watch?v=S5CjKEFb-sM', 'PG13')
officespace = media.Movie('Office Space', '''Three company workers who hate their
                          jobs decide to rebel against their greedy boss.''',
                          'Office Space.jpg',
                          'https://www.youtube.com/watch?v=dMIrlP61Z9s', 'R')
savingprivateryan = media.Movie('Saving Private Ryan', '''A group of U.S. soldiers
                                go behind enemy lines to retrieve a paratrooper
                                whose brothers have been killed in action.''',
                                'Saving Private Ryan.jpg',
                                'https://www.youtube.com/watch?v=RYExstiQlLc', 'R')
glory = media.Movie("Glory", '''Robert Gould Shaw leads the U.S. Civil War's
                    first all-black volunteer company.''', 'Glory.jpg',
                    'https://www.youtube.com/watch?v=0hVrYRqeT5M', 'R')


movies = [apollo13, django, flagsofourfathers, lettersfromiwojima, ingloriousbasterds, imitationgame, officespace, savingprivateryan, glory]
fresh_tomatoes.open_movies_page(movies)
