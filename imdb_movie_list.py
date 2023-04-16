import requests
import json
import time
import re
import textwrap

class Movie:
    def __init__(self):
        self.loop = True

    def program(self):
        my_choose = self.menu()

        if my_choose == "1":
            self.top250()
        elif my_choose == "2":
            self.most_popular()
        elif my_choose == "3":
            self.in_theaters()
        elif my_choose == "4":
            self.coming_soon()
        elif my_choose == "5":
            self.search_movie_Top_250()
        elif my_choose == "6":
            self.exit()


    def menu(self):
        def control(my_choose):
            if re.search("[^1-6]",my_choose) or len(my_choose) != 1:
                raise Exception("Please choose between 1 and 6")
        while True:
            try:
                x = input("Welcome\n1- Top 250 Movies\n2- Most Popular Movies\n3- In Theaters\n4- Coming Soon\n5- Search Movie\n6- Exit\nYour choice: ")
                print("\n\n")
                control(x)
            except Exception as error:
                print(error)
                time.sleep(1)
            else:
                break
        return x

    def top250(self):
        txt = ("   Top 250 Movies   ").center(49,"*")
        print(txt,"\n")
        url = requests.get("https://imdb-api.com/en/API/Top250Movies/k_oyl14zrz")
        result = url.json()
        for i in result["items"]:
            print(i["rank"],"-   ",i["fullTitle"],"   imdb rating: ",i["imDbRating"])
        self.return_menu()
    def most_popular(self):
        txt = ("   Most Popular Movies   ").center(49, "*")
        print(txt,"\n")
        url = requests.get("https://imdb-api.com/en/API/MostPopularTVs/k_oyl14zrz")
        result = url.json()
        for i in result["items"]:
            print(i["rank"], "-   ", i["fullTitle"], "     imdb rating:", i["imDbRating"])
        self.return_menu()

    def in_theaters(self):
        txt = ("   In Theaters   ").center(49, "*")
        print(txt,"\n")
        url = requests.get("https://imdb-api.com/en/API/InTheaters/k_oyl14zrz")
        result = url.json()
        j = 1
        for i in result["items"]:
            print(j,"-   ", i["fullTitle"], "     ", i["runtimeStr"])
            j += 1
            #print(i)
        self.return_menu()

    def coming_soon(self):
        txt = ("   Coming Soon   ").center(49, "*")
        print(txt,"\n")
        url = requests.get("https://imdb-api.com/en/API/ComingSoon/k_oyl14zrz")
        result = url.json()
        j = 1
        for i in result["items"]:
            print(j,"-   ", i["title"], "     release state:", i["releaseState"])
            j += 1
        self.return_menu()

    def search_movie_Top_250(self):     # we need id for this function
        txt = ("   Search Movie From Top 250   ").center(49, "*")
        print(txt, "\n")
        movie_name = input("Movie name: ")
        url = requests.get("https://imdb-api.com/en/API/Top250Movies/k_oyl14zrz")
        result = url.json()

        movie_id = None
        for i in result["items"]:
            if i["title"] == movie_name:
                movie_id = i["id"]
        

        try:
            url2 = requests.get("https://imdb-api.com/en/API/Wikipedia/k_oyl14zrz/{}".format(movie_id))
            result = url2.json()
            print(result["plotShort"]["plainText"],"\n")
        except Exception as hata:
            print("Please enter a valid movie name from Top 250\n")

        self.return_menu()



    def exit(self):
        self.loop = False
        exit()

    def return_menu(self):
        while True:
            x = input("Press 7 to return to the main menu\nPress 6 to exit\n")
            if x == "7":
                time.sleep(1)
                self.program()
                break
            elif x == "6":
                self.exit()
                break
            else:
                print("Please make a valid choice")


sistem = Movie()
while sistem.loop:
    sistem.program()

api_key = "k_oyl14zrz"