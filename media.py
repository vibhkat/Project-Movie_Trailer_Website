# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 12:41:50 2016

@author: vibhanshu
"""
from video import Video


class Movie(Video):
    """This class provides a way to store movie related information"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline,
                 poster_image,
                 trailer_youtube,
                 duration,
                 ratings):
        Video.__init__(self, movie_title, duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        assert(ratings in self.VALID_RATINGS)
        self.ratings = ratings
