# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064

import media
#import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "http://upload.wikipedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie()

movies = [toy_story, avatar]
#fresh_tomatoes.open_movies_page(movies)

print(toy_story.storyline)
