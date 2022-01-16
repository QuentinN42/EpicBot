with open("jeuxYolo.txt", "r") as yolo:
    entree = yolo.read().split("\n")

with open("../BotPromo-Master/epic.txt", "r") as epic:
    sortie = epic.read()


for e in entree:
    if e not in sortie:
        with open("../BotPromo-Master/epic.txt", "a") as f:
            f.write(e+"\n")
