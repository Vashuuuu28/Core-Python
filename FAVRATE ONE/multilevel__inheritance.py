# class game:
#     def __init__(self, Game):
#         self.gamename = Game
#
#     def get_gamename(self):
#         return self.gamename
#
#
# class userid(game):
#     def __init__(self, Game, vashuu):
#         self.userid = vashuu
#         super().__init__(self, Game)
#
#     def get_userid(self):
#         return self.userid
#
#
# class rank(userid):
#     def __init__(self, Game, vashuu, grandmaster):
#         self.rank = grandmaster
#         super().__init__(self, Game, vashuu)
#
#     def get_rank(self):
#         return self.rank
#
#
# x = rank("mobilelegend","vashuuu","grandmashu")
# print("game name is: ", x.get_gamename())
# print("player id is: ", x.get_userid())
# print("player rank is: ", x.get_rank())


class Game:
    def get_Game(self):
        self.name = input("game name")
    # def get_name(self):
    #     return self.name


class gameid(Game):
    def get_gameid(self):
        self.userid = input("user id: ")
        self.rank = input("gamerank is: ")
        self.exp = int(input("years played: "))
    # def get_userid(self):
    #     return self.userid


class result(gameid):
    def display(self):
        print("game name: ", self.name)
        print("user id: ", self.userid)
        print("current rank: ", self.rank)
        print("experience: ", self.exp)
        if self.rank == "grandmaster":
            print("esport player")
        if self.exp == 5:
            print("passed")
        else:
            print("failed")


G = result()
G.get_Game()
G.get_gameid()
G.display()
