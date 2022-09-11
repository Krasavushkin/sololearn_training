class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def intro(self):
        print(self.name + " (Level " + self.level + ")")

gamer = input ()
lvl = input ()

play = Player (gamer, lvl)
play.intro ()