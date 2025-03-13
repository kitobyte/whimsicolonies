import random

malenames = ["Abner", "Bert", "Chester", "Dolgrim", "Ernest", "Fenrir",
             "Gimli", "Harold", "Isaiah", "Jeb", "Kurt", "Lester", "Mo",
             "Newt", "Obie", "Penfold", "Quentin", "Remus", "Stanley",
             "Tim", "Ulysses", "Vig", "Wendell", "Xavier", "Yesley",
             "Zeb"]

femalenames = ["Abbie", "Blythe", "Callie", "Doris", "Ethel", "Fergie",
               "Gertie", "Helen", "Isabelle", "Jenna", "Kit", "Lily",
               "Myrtle", "Nellie", "Opal", "Penny", "Quayle", "Ruby",
               "Sophia", "Tillie", "Uma", "Violet", "Willa", "Xanthe",
               "Yedda", "Zara"]

surnames = ["Appleton", "Bartlett", "Beasley", "Bismuth", "Bogsworth", "Bugrattle", "Calavera", "Cheapskate", "Cindersap", "Cobblestone", "Cullimore", "Dalhousie", "Denver", "Dinnerbone", "Dover", "Dunkirk", "Elmwood",
            "Farthingwood", "Fellerman", "Finch", "Ford", "Fullerman", "Gamgee", "Geller", "Ginsberg", "Godfrey", "Gordon", "Gutenberg", "Harris", "Heaton", "Hill", "Hobbler", "Hummingbird", "Immer", "Jones", "Kleiner",
            "Lambert", "Mendelssohn", "Nickels", "Oakwood", "Pickles",
            "Quinlan", "Ripley", "Smith", "Tinker", "Underhill", "Vance",
            "Whitaker", "Xylem", "Yellowknife", "Zither"]

acreprefixes = ["Apple", "Basil", "Crow", "Dusten", "Earthen", "Fern", "Green", "Hammer", "Iron", "June", "Kettle",
                "Loom", "Mud", "Nettle", "Oaken", "Petal", "Quinn", "Red", "Sacks", "Tin", "Under", "Vine",
                "White", "Wind", "Yellow", "Zincen"]

acresuffixes = [" Alley", "burg", "bury", " City", "don", "dorf", "ford", "forge", "guild", "haven", "helm", "more",
                "port", "quarry", "silt", "ton", "tower", "town", "vale", "valley", "ville", "way"]

# songs and art

classicalsongprefixes = ["Allegro In", "Canon In ", "Etude In ", "Fugue In ", "Gavotte In ", "Minuet In ", "Nocturne In ", "Prelude In ", "Sonata In ", "Suite In ", "Symphony In " "Waltz In ",]

keys = ["C Major", "A Minor", "G Major", "E Minor", "D Major", "B Minor", "A Major", "F# Minor", "E Major", "C# Minor", "B Major", "G# Minor", "F# Major", "D# Minor",
        "F Major", "D Minor", "Bb Major", "G Minor", "Eb Major", "C Minor", "Ab Major", "F Minor", "Db Major", "Bb Minor", "Gb Minor", "Eb Minor"]

adjectives = ["Ancient ", "Awful ", "Black ", "Blue", "Beautiful ", "Boring ", "Charming ", "Crumbling ", "Dark", "Dry", "Dying ", "Demonic ", "Doubtful ", "Elegant ", "Evil ", "Falling ", "Filthy ", "Gorgeous ", "Grimy ",
                "Green", "Heavenly ", "Horrible ", "Indescribable ", "Intrepid ", "Joyful ", "Jaded ", "Killer ", "Kindhearted", "Lovely ",  "Lonely ", "Little ", "Loathesome ", "Magnificent ", "Miserable ", "Orange ", "Old ",
                "Omnipotent ", "Pretty ", "Putrid ", "Quaint ", "Quick ", "Questionable ", "Repulsive ", "Regal ", "Red ", "Sneaky ", "Soft ", "Traveling ", "Terrible ", "Tipsy ", "Tiny ", "Unhappy ", "Undying ", "Vile ",
                "Voluptuous ", "Wise ", "Wicked ", "Yellow ", "Yearning ", "Zealous "]

nouns = ["Alchemist", "Angel", "Bishop", "Bird", "Basilisk", "Carpenter", "Card", "Creature", "Doctor", "Daughter", "Dog", "Dagger", "Elephant", "Farmer", "Father", "Flower", "Fool", "Goblin", "Girl", "God", "Hammer", "Hag",
        "Invokation", "Idea", "Island",  "Jewel", "Kobold", "King", "Lover", "Liar", "Lumberjack", "Meadow", "Mother", "Miner", "Newt", "Ogre", "Oracle", "Promise", "Pilgrim", "Prophet", "Priest", "Painter", "Pickaxe",
        "Pig", "Quill", "Question", "Rabbit", "Reaper", "Ring", "Sea", "Sword", "Sinner", "Storm", "Tankard", "Traveler", "Undertaker", "Uncle", "Vine", "Vow", "Wall", "Wizard", "Whiskey", "Whore", "Woman",
        "Wyvern", "Yam", "Yarrow"]

suffixes = [" Of All Kingdoms", " Of Better Days", " Of The Cold", " Of The Century", " Of Death", " Of Eternal Life", " Of Everlasting Life", " Of Freedom", " Of God", " Of Heaven",  " Of Hell", " Of Intuition", " Of Joy",
            " Of Kings", " Of Love", " Of Murder", " Of Mischief", " Of The Night", " Of Old", " Of Pain", " Of Questions", " Of Rivers", " Of Spring ", " Of Summer", " Of The Trees", " Of Undying Love", " Of Victory",
            " Of Winter", " Of Years Gone By", " In The Attic", " In The Bathtub", " In A Coffin", " In The Dust", " In The Elm", " In The Fog", " In The Forest", " In The Garden", " In The Graveyard", " In The Hall",
            " In My Heart", " In The Inn", " In The Jar", " In The Kitchen", " In The Lake", " In The Mud", " In The Nunnery", " In The Orchard", " In The Palace", " In The Quilt", " In The River", " In The Sand",
            " In The Tavern", " In The Underworld", " In The Vineyard", " In The Woods", " In The Yeast", " At The Anvil", " At The Bar", " At The Creek", " At Death's Door", " At Every Turn", " At The Gallows",
            " At The Inn", " At Noon", " At Odds With The World", " At The Port", " At Rest", " At The Shop", " At The Table", " At The Water's Edge"]

verbs = [" Anointing", " Beating", " Carrying", " Dancing with", " Eating", " Fighting", " Growling At", " Howling At", " Irritating", " Joking With", " Killing", " Leading", " Murdering", " Nurturing", " Ogling", " Praying To",
         " Questioning", " Resting With", " Stabbing", " Talking To", " Usurping", " Venerating", " Worshipping", " Yelling At"]

jobs = ["Alchemist", "Blacksmith", "Brewer", "Carpenter", "Doctor",
        "Farmer", "Guard",
        "Lumberjack", "Miner", "Musician", "Painter", "Priest", "Scribe", "Sweeper",
        "Teacher", "Writer"]

citizens = []

acres = []

# core stats

year = 0
coins = 100000
pop = len(citizens)

# item stats

ale = 0
food = 10
ore = 0
stardust = 0
wood = 0
weapons = 0

# job building stats

churches = 0
farms = []
forges = 0
houses = 0
observatories = 0
schools = 0
taverns = 0
workshops = 0

# art stats

songs = []
paintings = []
books = []

# qualifiable stats

cleanliness = 100
immigrationrate = 2

# conditions

colonycreated = False

# core game loop

def colonyinit():
    colonyname = random.choice(acreprefixes)
    colonyname = colonyname + random.choice(acresuffixes)
    acres.append(colonyname)
    print("The colony of ", colonyname, "has been founded!")
    for i in range(5):
        create_immigrant(colonyname)
    colonycreated = True
    calibrate(adjectives, ale, books, churches, classicalsongprefixes, cleanliness, colonyname, farms, food, forges, houses, immigrationrate, keys,
              nouns, observatories, ore, paintings, schools, songs, stardust, suffixes, taverns, verbs, weapons, wood, workshops, year)

def gameloop(colonyname, food, pop, year):
    print("----------------")
    print("year: ", year)
    print("population: ", pop)
    print("coins: ", coins)
    print("food: ", food)
    inp = input("> ")
    if inp == "next":
        print("Turn ended.")
        calibrate(adjectives, ale, books, churches, classicalsongprefixes, cleanliness, colonyname, farms, food, forges, houses, immigrationrate, keys,
              nouns, observatories, ore, paintings, schools, songs, stardust, suffixes, taverns, verbs, weapons, wood, workshops, year)
        gameloop(colonyname, food, pop, year)
    elif inp =="create immigrant":
        create_immigrant(colonyname)
        gameloop(colonyname, food, pop, year)
    elif inp == "help":
        print("help, next")
        gameloop(colonyname, food, pop, year)
    else:
        print("Command not recognised. Try again.")
        gameloop(colonyname, food, pop, year)

def calibrate(adjectives, ale, books, churches, classicalsongprefixes, cleanliness, colonyname, farms, food, forges, houses, immigrationrate, keys,
              nouns, observatories, ore, paintings, schools, songs, stardust, suffixes, taverns, verbs, weapons, wood, workshops, year):
    
    # citizen changes
    for i in citizens:
        i["age"] += 1
        if i["age"] > 60:
            deathchance = int(i["age"] / 5)
            if random.randint(0, 100) < deathchance:
                print(i["name"], i["surname"], " died of natural causes at the age of ", i["age"])
                citizens.remove(i)
    # immigration
    immigrationrate = int(cleanliness/10)
    if random.randint(0,100) < immigrationrate:
        create_immigrant(colonyname)
    # job survey
    alchemists = 0
    blacksmiths = 0
    brewers = 0
    carpenters = 0
    doctors = 0
    farmers = 0
    guards = 0
    lumberjacks = 0
    miners = 0
    musicians = 0
    painters = 0
    priests = 0
    scribes = 0
    sweepers = 0
    teachers = 0
    writers = 0
    other = 0
    for i in citizens:
        if i["job"] == "Alchemist":
            alchemists += 1
        elif i["job"] == "Blacksmith":
            blacksmiths += 1
        elif i["job"] == "Brewer":
            brewers += 1
        elif i["job"] == "Carpenter":
            carpenters += 1
        elif i["job"] == "Doctor":
            doctors += 1
        elif i["job"] == "Farmer":
            farmers += 1
        elif i["job"] == "Guard":
            guards += 1
        elif i["job"] == "Lumberjack":
            lumberjacks += 1
        elif i["job"] == "Miner":
            miners += 1
        elif i["job"] == "Musician":
            musicians += 1
        elif i["job"] == "Painter":
            painters += 1
        elif i["job"] == "Priest":
            priests += 1
        elif i["job"] == "Scribe":
            scribes += 1
        elif i["job"] == "Sweeper":
            sweepers += 1
        elif i["job"] == "Teacher":
            teachers += 1
        elif i["job"] == "Writer":
            writers += 1
        elif i["job"] == "Other":
            other += 1
    # citizen actions
    for i in citizens:
        painting_made_this_turn = False
        song_made_this_turn = False
        book_made_this_turn = False
        if i["job"] == "Alchemist":
            productionchance = int(i["level"]*1.5)
            if food >= 5 and random.randint(0, 100) < productionchance:
                if observatories >= alchemists:
                    observatories += 1
                    print(i["name"], i["surname"], "built an observatory! It will start producing stardust next turn.")
                    cleanliness -= 10
                    i["xp"] += 20
                else:
                    amount = i["level"]*(random.randint(1, 5))
                    i["xp"] += int(amount/2)
                    cleanliness -= 1
                    print(i["name"], i["surname"], "conjured", amount, "stardust!")
        elif i["job"] == "Blacksmith":
            productionchance = int(i["level"]*1.5)
            amount = i["level"]*(random.randint(1, 5))
            if forges >= blacksmiths and ore >= amount*5 and random.randint(0, 100) < productionchance:
                weapons += amount
                ore -= amount*5
                i["xp"] += int(amount/2)
                cleanliness -= 1
                print(i["name"], i["surname"], "forged", amount, "weapons!")
        elif i["job"] == "Brewer":
            productionchance = int(i["level"]*1.5)
            amount = i["level"]*(random.randint(1, 5))
            if taverns >= brewers and food >= amount*3 and random.randint(0, 100) < productionchance:
                ale += amount
                food -= amount*3
                i["xp"] += int(amount/2)
                cleanliness -= 3
                print(i["name"], i["surname"], "brewed", amount, "barrels of ale!")
        elif i["job"] == "Farmer":
            productionchance = int(i["level"]*1.5)
            amount = i["level"]*(random.randint(2, 10))
            if farmers > len(farms):
                farmname = i["surname"] + " Farm"
                i["xp"] += 20
                farms.append(farmname)
                cleanliness -= 10
                print(i["name"], i["surname"], "built", farmname, "! It will start producing food next turn.")
            elif random.randint(0, 100) < productionchance:
                food += amount
                i["xp"] += int(amount/4)
                cleanliness -= 3
                print(i["name"], i["surname"], "produced", amount, "food!")
        elif i["job"] == "Lumberjack":
            productionchance = int(i["level"]*1.5)
            amount = i["level"]*(random.randint(2, 10))
            if random.randint(0, 100) < productionchance:
                wood += amount
                i["xp"] += int(amount/4)
                cleanliness -= 3
                print(i["name"], i["surname"], "chopped", amount, "wood!")
        elif i["job"] == "Miner":
            productionchance = int(i["level"]*1.5)
            amount = i["level"]*(random.randint(1, 5))
            if random.randint(0, 100) < productionchance:
                ore += amount
                i["xp"] += int(amount/2)
                cleanliness -= 3
                print(i["name"], i["surname"], "mined", amount, "ore!")
        elif i["job"] == "Musician":
            if i["inspiration"] > 1000 / i["level"]:
                songstructure = random.choice(1, 10)
                if songstructure == 1:
                    songname = random.choice(classicalsongprefixes + keys)
                elif songstructure == 2:
                    songname = "The " + random.choice(nouns)
                elif songstructure == 3:
                    songname = "The " + random.choice(nouns) + "s"
                elif songstructure == 4:
                    songname = random.choice(nouns) + "s"
                elif songstructure == 5:
                    songname = "The " + random.choice(adjectives) + random.choice(nouns)
                elif songstructure == 6:
                    songname = "The " + random.choice(adjectives), random.choice(nouns) + "s"
                elif songstructure == 7:
                    songname = "The Ballad Of " + random.choice(citizens["name"]["surname"])
                elif songstructure == 8:
                    songname = "The " + random.choice(nouns), random.choice(suffixes)
                elif songstructure == 9:
                    songname = "The " + random.choice(nouns) + "s" + random.choice(suffixes)
                elif paintingstructure == 10:
                    songname = "The " + random.choice(nouns) + " And The " + random.choice(nouns)
                songs.append(dict(name=songname, author=i[name][surname]))
                song_made_this_turn = True
                i["xp"] += 25
                i["inspiration"] = 0
                cleanliness -= 1
                print(i["name"], i["surname"], "composed", songname)
        elif i["job"] == "Painter":
            if i["inspiration"] > 1000 / i["level"]:
                paintingstructure = random.choice(1, 9)
                if paintingstructure == 1:
                    paintingname = "The " + random.choice(nouns) + random.choice(verbs) + " The " + random.choice(nouns)
                elif paintingstructure == 2:
                    paintingname = "The " + random.choice(nouns) + " And The " + random.choice(nouns)
                elif paintingstructure == 3:
                    paintingname = "The " + random.choice(nouns)
                elif paintingstructure == 4:
                    paintingname = random.choice(nouns) + "s"
                elif paintingstructure == 5:
                    paintingname = "The ", random.choice(adjectives) + random.choice(nouns) + random.choice(verbs) + " The " + random.choice(adjectives), random.choice(nouns)
                elif paintingstructure == 6:
                    paintingname = "The " + random.choice(nouns) + random.choice(verbs) + random.choice(nouns) + "s"
                elif paintingstructure == 7:
                    paintingname = "Portrait Of " + random.choice(citizens([name][surname]))
                elif paintingstructure == 8:
                    paintingname = "The " + random.choice(adjectives) + random.choice(nouns) + random.choice(verbs) + " The " + random.choice(adjectives) + random.choice(nouns)
                elif paintingstructure == 9:
                    paintingname = random.choice(nouns)
                paintings.append(dict(name=paintingname, author=i[name][surname]))
                painting_made_this_turn: True
                i["xp"] += 25
                i["inspiration"] = 0
                cleanliness -= 5
                print(i["name"], i["surname"], "painted", paintingname)
        elif i["job"] == "Writer":
            if i["inspiration"] > 1000 / i["level"]:
                bookstructure = random.choice(1, 9)
                if bookstructure == 1:
                    bookname = "The " + random.choice(nouns)
                elif bookstructure == 2:
                    bookname = "The " + random.choice(nouns) + "And The" + random.choice(nouns)
                elif bookstructure == 3:
                    bookname = "The " + random.choice(adjectives) + random.choice(nouns)
                elif bookstructure == 4:
                    bookname = "The " + random.choice(nouns) + "s" + random.choice(suffixes)
                elif bookstructure == 5:
                    bookname = "The " + random.choice(nouns) + random.choice(suffixes)
                elif bookstructure == 6:
                    bookname = "The Tale Of The ", random.choice(adjectives) + random.choice(nouns)
                elif bookstructure == 7:
                    bookname = "Biography Of " + random.choice(citizens([name][surname]))
                elif bookstructure == 8:
                    bookname = random.choice(nouns)
                elif bookstructure == 9:
                    bookname = random.choice(nouns) + "s"
                books.append(dict(name=bookname, author=i[name][surname]))
                book_made_this_turn: True
                i["xp"] += 25
                i["inspiration"] = 0
                cleanliness -= 2
                print(i["name"], i["surname"], "wrote", bookname)
        elif i["job"] == "Priest":
            productionchance = int(i["level"]*1.5)
            amount = i["level"]*(random.randint(1, 5))
            if churches >= priests and random.randint(0, 100) < productionchance:
                for i in citizens:
                    i[inspiration] += amount
                i["xp"] += int(amount/2)
                cleanliness -= 1
        elif i["job"] == "Scribe":
            stories = ["nothing", "cleanliness", "stormcoming"]
            if song_made_this_turn == True:
                stories.append("badsong", "goodsong")
            if painting_made_this_turn == True:
                stories.append("badpainting", "goodpainting")
            if book_made_this_turn == True:
                stories.append("badbook", "goodbook")
                
            productionchance = int(i["level"]*1.5)
            chroniclename: "The " + i["surname"] + " Chronicle: "
            story: random.choice(stories)
            if random.randint(0, 100) < productionchance:
                if story == "barfight":
                    person1 = random.choice(citizens["name"]["surname"])
                    person2 = random.choice(citizens["name"]["surname"])
                    if person1 == person2:
                        print(chroniclename, person1, "Gets Into Bar Fight With Self In Shocking Display Of Drunkenness!")
                    else:
                        print(chroniclename, person1, "And", person2, "Get Into Bar Fight Resulting In Minor Injuries To Both Parties!")
                elif story == "cleanliness":
                    if cleanliness < 40:
                        print(chroniclename, colonyname, "Ranked Among The Filthiest Places In The World!")
                    elif cleanliness > 60:
                        print(chroniclename, colonyname, "Ranked Among The Cleanest Places In The World!")
                    else:
                        print(chroniclename, colonyname, "Reportedly Of Average Cleanliness!")
                elif story == "stormcoming":
                    print(chroniclename, "Big Storm Coming, According To Ominous Clouds On The Horizon!")
                elif story == "nothing":
                    print(chroniclename, "Nothing Interesting Happened Today, According To New Survey!")
                elif story == "badbook":
                    print(chroniclename, books[-1]["name"], "By", books[-1]["author"], "Panned By Critics For Lack Of Substance!")
                elif story == "goodbook":
                    print(chroniclename, books[-1]["name"], "By", books[-1]["author"], "Praised By Critics For Enthralling Plot!")
                elif story == "badpainting":
                    print(chroniclename, paintings[-1]["name"], "By Local Painter", paintings[-1][author], "Deemed 'Amateurish' By Critics!")
                elif story == "goodpainting":
                    print(chroniclename, "Townsfolk Amazed By", paintings[-1]["name"], ", The Latest Painting By", paintings[-1]["author"])
                elif story == "badsong":
                    print(chroniclename, songs[-1]["name"], "By", songs[-1]["author"], "Sparks Controversy Due To Obscene Lyrics!")
                elif story == "goodsong":
                    print(chroniclename, songs[-1]["name"], "By", songs[-1]["author"], "Deemed 'The Song Of The Summer' By Critics!")
                i["xp"] += 10
                cleanliness -= 1
        elif i["job"] == "Carpenter":
            productionchance = int(i["level"]*1.5)
            amount = i["level"]*(random.randint(1, 5))
            to_build = []
            if priests > churches:
                to_build.append("church")
            if blacksmiths > forges:
                to_build.append("forge")
            if schools == 0:
                to_build.append("school")
            if brewers > taverns:
                to_build.append("tavern")
            if carpenters > workshops and wood >= 15:
                workshops += 1
                wood -= 15
                cleanliness -= 10
            buildchoice = random.randint(1, 2)
            if buildchoice == 1 and wood >= 15 and random.randint(0, 100) < productionchance:
                buildingchoice = random.choice(to_build)
                if buildingchoice == "church":
                    churches += 1
                    wood -= 15
                    i["xp"] += 25
                    cleanliness -= 10
                    print(i[name], i[surname], "built a church!")
                elif buildingchoice == "forge":
                    forges += 1
                    wood -= 15
                    ii["xp"] += 25
                    cleanliness -= 10
                    print(i[name], i[surname], "built a forge!")
                elif buildingchoice == "school":
                    schools += 1
                    wood -= 15
                    i["xp"] += 25
                    cleanliness -= 10
                    print(i[name], i[surname], "built a school!")
                elif buildingchoice == "tavern":
                    taverns += 1
                    wood -= 15
                    i["xp"] += 25
                    cleanliness -= 10
                    print(i["name"], i["surname"], "built a tavern!")
            elif buildchoice == 2 and wood >= amount*10 and random.randint(0, 100) < productionchance:
                houses += amount
                wood -= amount*10
                i[xp] += int(amount/2)
                cleanliness -= amount*8
                print(i[name], i[surname], "built", amount, "houses!")
        elif i["job"] == "Sweeper":
            productionchance = int(i["level"]*1.5)
            amount = i["level"]*(random.randint(1, 5))
            if random.randint(0, 100) < productionchance:
                cleanliness += amount
                i["xp"] += int(amount/2)
                
    # eating

    for i in citizens:
        if food > 0:
            food -= 1
        elif food <= 0:
            i["status"] = "malnourished"
            i["hunger"] += 1
            print(i["hunger"])
        elif i["hunger"] > 3:
            print(i["name"], i["surname"], "has died of hunger at the age of", i["age"])
            citizens.remove(i)
        elif food > 0 and i["status"] == "malnourished":
            food -= 1
            i["status"] = "healthy"
                          
    # leveling up
    for i in citizens:
        if i["xp"] >= i["level"]**2*4:
            i["xp"] = i["xp"] - i["level"]**2*4
            i["level"] +=1
            print(i["name"], i["surname"], "leveled up to level", i["level"])
    # updates
    pop = len(citizens)
    year += 1
    gameloop(colonyname, food, pop, year)

# game processes

def create_immigrant(colonyname):
    firstname = None
    surname = None
    gender = random.choice(("male", "female"))
    if gender == "male":
        firstname = random.choice(malenames)
    else:
        firstname = random.choice(femalenames)
    surname = random.choice(surnames)
    job = random.choice(jobs)
    age = random.randint(20, 60)
    level = random.randint(1, 5)
    status = "healthy"
    is_immigrant = True
    citizens.append(dict(name=firstname, surname=surname, job=job, age=age, gender=gender, level=level, xp=0, status=status, inspiration=0, hunger=0, is_immigrant=is_immigrant))
    print(firstname, surname, "Has arrived in", colonyname)
    print("job: ", job)
    print("level: ", level)
    print("age: ", age)
    print("gender: ", gender)
    if colonycreated == True:
        gameloop(colonyname, food, pop, year)

colonyinit()
gameloop(colonyname, food, pop, yearr)
    
