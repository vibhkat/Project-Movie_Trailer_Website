# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 12:45:15 2016

@author: vibhanshu
"""
import fresh_tomatoes
from media import Movie

# Toy Story movie object
toy_story = Movie("Toy Story",
                  "A story of a boy and his toys",
                  "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                  "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                  "1h 21min",
                  "G")
# Batman V Superman movie object
BvS = Movie("Batman vs Superman: Dawn of Justice",
            "Starting of Justice League",
            "https://upload.wikimedia.org/wikipedia/en/2/20/Batman_v_Superman_poster.jpg",
            "https://www.youtube.com/watch?v=8AO19XY2rqc",
            "2hr 31min",
            "PG-13")
# The Shawshank Redemption movie object
shaw_shank = Movie("The Shawshank Redemption",
                   "Story of a wrongfully imprisoned man",
                   "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                   "https://www.youtube.com/watch?v=6hB3S9bIaco",
                   "2hr 22min",
                   "R")
movies = [toy_story, BvS, shaw_shank]
fresh_tomatoes.open_movies_page(movies)
