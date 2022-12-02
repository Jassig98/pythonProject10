# Author: Jasmine Singh
# Github Username: Jassig98
# Date: November 30 2022
# Description

class Movie:
    def __init__(self,title,genre,director,year):
        self.title=title
        self.genre=genre
        self.director=director
        self.year=year
    def get_title(self):
        return self.title
    def get_genre(self):
        return self.genre
    def get_director(self):
        return self.director
    def get_year(self):
        return self.year

class StreamingService:
    def __init__(self,name):
        self.name=name
        self.catalog=dict()
    def get_name(self):
        return self.name
    def get_catalog(self):
        return self.catalog
    def add_movie(self,m):
        self.catalog[m.get_title()]=m
    def delete_movie(self,title):
        if title in self.catalog.keys():
            del self.catalog[title]

class StreamingGuide:
    def __init__(self):
        self.StreamingServices= []
    def add_streaming_service(self,streamingService):
        self.StreamingServices.append(streamingService)
    def delete_streaming_service(self,name):
        for ss in self.StreamingServices:
            if (ss.get_name() == name):
                self.StreamingServices.remove(ss)
    def where_to_watch_movie(self,title):
        _1=[]
        for ss in self.StreamingServices:
            if title in ss.get_catalog().keys():
                _1.append(ss.get_name() + "("+str(ss.get_catalog()[title].get_year())+"}")
        if (len(_1)==0):
            return None
        else:
            return _1





