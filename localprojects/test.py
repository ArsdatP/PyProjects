class Mangas:
    def __init__(self,genre):
        #self.name = name
        self.genre = genre

    def __pbr__(manga):
        print("Welcome to my Manga Recommendation store!")
        #reply = print(input("What is kind of manga are you looking for? "))
        
        print(manga.genre)




#Action -- Vagabond, Tokyo Ghoul, Fairy Tail, Vinland Saga
mangas = {
    "action": ["Vagabond", "Tokyo Ghoul", "Fairy Tail", "Vinland Saga"],
    "adventure": ["Fullmetal Alchemist", "Hunter x Hunter", "Solo Leveling"]
    }
#Adventure -- Fullmetal Alchemist, Hunter x Hunter, Solo Leveling, Golden Kamuy, Inuyasha
#adventure_mangas = ["""Fullmeta Alchemist,Hunter x Hunter, Solo Leveling, Golden Kamuy, Inuyasha """]

genres = Mangas(mangas)
#genres = Mangas(adventure_mangas)
genres.__pbr__()











#Award Winning -- Shingeki no Kyojin, Chainsaw Man, Bleach, One Piece
#awinning_mangas = ["""Shingeki no Kyojin,
#Chainsaw Man,
#Bleach,
#One Piece
#"""]
#Fantasy -- Kimetsu no Yaiba, Naruto, Black Clover, Jujutsu Kaisen
#fantasy_mangas = ["""Kimetsu no Yaiba,
#Naruto,ac
#Black Clover,
#Jujutsu Kaisen
#"""]