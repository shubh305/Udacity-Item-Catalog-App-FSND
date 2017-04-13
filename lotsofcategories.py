import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, Category, Item

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
db_session = DBSession()


user1 = User(name="Test User", email="test123@gmail.com")

category1 = Category(name="Action")
category2 = Category(name="Adventure")
category3 = Category(name="Racing")
category4 = Category(name="Stealth")
category5 = Category(name="Fighting")
category6 = Category(name="Horror")
category7 = Category(name="Sports")
category8 = Category(name="MultiPlayer")
category9 = Category(name="Role Playing Games (RPG)")
category10 = Category(name="First Person Shooters (FPS)")


db_session.add(category1)
db_session.add(category2)
db_session.add(category3)
db_session.add(category4)
db_session.add(category5)
db_session.add(category6)
db_session.add(category7)
db_session.add(category8)
db_session.add(category9)
db_session.commit()

item1 = Item(name="Batman: Arkham City (2011)",
             description="Batman: Arkham City is a 2011 action-adventure "
             "video game developed by Rocksteady Studios and released by "
             "Warner Bros. Interactive Entertainment for the PlayStation 3 "
             "and Xbox 360 video game consoles, and Microsoft Windows.",
             created_at=datetime.datetime.now(),
             updated_at=datetime.datetime.now(),
             category=category1,
             user=user1)

item2 = Item(name="Dead Island (2011)",
             description="Dead Island is a 2011 open world survival horror "
             "action role-playing video game developed by Polish developer "
             "Techland and published by German studio Deep Silver[5] for "
             "Microsoft Windows, Linux, OS X, PlayStation 3, and Xbox 360.",
             created_at=datetime.datetime.now(),
             updated_at=datetime.datetime.now(),
             category=category1,
             user=user1)

item3 = Item(name="Far Cry Primal (2016)",
             description="Far Cry Primal is an action-adventure video game "
             "developed by Ubisoft Montreal and published by Ubisoft. It was "
             "released for the PlayStation 4 and Microsoft Windows in 2016.",
             created_at=datetime.datetime.now(),
             updated_at=datetime.datetime.now(),
             category=category2,
             user=user1)

item4 = Item(name="Metal Gear Rising: Revengeance (2013)",
             description="Metal Gear Rising: Revengeance is an action hack "
             "and slash video game developed by PlatinumGames and produced "
             "by Kojima Productions, for the PlayStation 3, Xbox 360 "
             "and Microsoft Windows.",
             created_at=datetime.datetime.now(),
             updated_at=datetime.datetime.now(),
             category=category1,
             user=user1)

item5 = Item(name="Grand Theft Auto V (2013)",
             description="Grand Theft Auto V is an adventure video game "
             "developed by Rockstar North and published by Rockstar Games. "
             "It was released on 17 September 2013 for the PlayStation 3 and "
             "Xbox 360, on 18 November 2014 for the PlayStation 4 and "
             "Xbox One, and on 14 April 2015 for Microsoft Windows.",
             created_at=datetime.datetime.now(),
             updated_at=datetime.datetime.now(),
             category=category2,
             user=user1)

item6 = Item(name="Resident Evil 7: Biohazard (2017)",
             description="Resident Evil 7: Biohazard is a survival horror "
             "video game developed and published by Capcom. The game was "
             "released worldwide for Microsoft Windows, PlayStation 4, and "
             "Xbox One in January 2017.",
             created_at=datetime.datetime.now(),
             updated_at=datetime.datetime.now(),
             category=category6,
             user=user1)

item7 = Item(name="Dishonored (2012)",
             description="Dishonored is a 2012 stealth action-adventure video "
             "game developed by Arkane Studios and published by Bethesda "
             "Softworks. It was released worldwide in October 2012 for "
             "Microsoft Windows, PlayStation 3, and Xbox 360.",
             created_at=datetime.datetime.now(),
             updated_at=datetime.datetime.now(),
             category=category4,
             user=user1)

item8 = Item(name="Sniper Elite 4 (2017)",
             description="Sniper Elite 4 is a third-person tactical shooter "
             "stealth video game developed by Rebellion Developments. As the "
             "direct sequel to Sniper Elite III, the game was released for "
             "Microsoft Windows and PlayStation 4 on 14 February 2017.",
             created_at=datetime.datetime.now(),
             updated_at=datetime.datetime.now(),
             category=category4,
             user=user1)

item9 = Item(name="Hitman: Absolution (2012)",
             description="Hitman: Absolution is a stealth video game "
             "developed by IO Interactive and published by Square Enix. It is "
             "the fifth installment in the Hitman series, and runs on IO "
             "Interactive's proprietary Glacier 2 game engine. Before "
             "release, the developers stated that Absolution would be easier "
             "to play and more accessible, while still retaining hardcore "
             "aspects of the franchise. The game was released on 20 "
             "November 2012 (which is in the 47th week of the year in "
             "reference to the protagonist, Agent 47) for Microsoft Windows, "
             "PlayStation 3, and Xbox 360.",
             created_at=datetime.datetime.now(),
             updated_at=datetime.datetime.now(),
             category=category4,
             user=user1)

item10 = Item(name="Battlefield 4 (2013)",
              description="Battlefield 4 is a first-person shooter video game "
              "developed by video game developer EA DICE and published by "
              "Electronic Arts. It is a sequel to 2011's Battlefield 3 and "
              "was released on October 29, 2013  for Microsoft Windows, "
              "PlayStation 3, PlayStation 4, Xbox 360 and Xbox One.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category10,
              user=user1)

item11 = Item(name="BioShock Infinite (2013)",
              description="BioShock Infinite is a first-person shooter "
              "video game developed by Irrational Games and published by "
              "2K Games. It was released worldwide for the Microsoft Windows, "
              "PlayStation 3, and Xbox 360 platforms on March 26, 2013; an "
              "OS X port by Aspyr was later released on August 29, 2013 and a "
              "Linux port was released on March 17, 2015. Infinite is the "
              "third installment in the BioShock series, and though it is "
              "not immediately part of the storyline of previous BioShock "
              "games, it features similar gameplay concepts and themes.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category10,
              user=user1)

item12 = Item(name="Far Cry 4 (2014)",
              description="Far Cry 4 is an open world action-adventure "
              "first-person shooter video game developed by Ubisoft Montreal "
              "and published by Ubisoft for the PlayStation 3, PlayStation 4, "
              "Xbox 360, Xbox One, and Microsoft Windows. It is the successor "
              "to the 2012 video game Far Cry 3, and the fourth main "
              "installment in the Far Cry series. The game was "
              "released on November 18, 2014.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category10,
              user=user1)

item13 = Item(name="Pro Evolution Soccer '17 (2016)",
              description="Pro Evolution Soccer '17 (officially abbreviated "
              "as PES 2017, also known in some Asian countries as Winning "
              "Eleven 2017) is a sports video game developed by PES "
              "Productions and published by Konami for Microsoft Windows, "
              "PlayStation 3, PlayStation 4, Xbox 360 and Xbox One. ",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category7,
              user=user1)

item14 = Item(name="FIFA 17 (2016)",
              description="FIFA 17 is a sports video game in the FIFA "
              "series, released on 27 September 2016 in North America and "
              "29 September 2016 for the rest of the world. This is the first "
              "FIFA game in the series to use the Frostbite game engine. "
              "On 21 July 2016, it was announced that, after a public vote, "
              "Marco Reus would feature on the cover of the game. The demo "
              "was released on 13 September 2016. The Play First Trial was "
              "released on 22 September 2016 in Microsoft Windows's "
              "Origin Access and Xbox One's EA Access.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category7,
              user=user1)

item15 = Item(name="Dark Souls III (2016)",
              description="Dark Souls III is an action role-playing video "
              "game developed by FromSoftware and published by Bandai Namco "
              "Entertainment for PlayStation 4, Xbox One, and Microsoft "
              "Windows. The fourth entry in the Souls series, Dark Souls III "
              "was released in Japan in March 2016, and "
              "worldwide in April 2016.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category9,
              user=user1)

item16 = Item(name="The Witcher 3: Wild Hunt (2015)",
              description="The Witcher 3: Wild Hunt is an action role-playing "
              "video game developed by CD Projekt and published by CD Projekt "
              "RED. Announced in February 2013, it was released worldwide on "
              "19 May 2015 for Microsoft Windows, PlayStation 4, and Xbox "
              "One. The game is the third in the series, preceded by The "
              "Witcher and The Witcher 2: Assassins of Kings, which are based "
              "on the series of fantasy novels by Polish "
              "author Andrzej Sapkowski.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category9,
              user=user1)

item17 = Item(name="Need for Speed Rivals (2013)",
              description="Need for Speed Rivals is an open world racing "
              "video game. Developed by Ghost Games and Criterion Games, it "
              "is the twentieth installment in the Need for Speed series. "
              "The game was released for Microsoft Windows, PlayStation 3 and "
              "Xbox 360 on 19 November 2013, and for PlayStation 4 and "
              "Xbox One as launch titles in the same month.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category3,
              user=user1)

item18 = Item(name="Ride (2015)",
              description="Ride is a motorcycle racing video game developed "
              "and published by Milestone S.r.l.. The game was released on "
              "March 27, 2015, in Europe, and it was meant to be released on "
              "June 23, 2015 in North America for Microsoft Windows, "
              "PlayStation 3, PlayStation 4, Xbox One, and Xbox 360 "
              "but was delayed to October 6, 2015.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category3,
              user=user1)

item19 = Item(name="EA Sports UFC 2 (2016)",
              description="EA Sports UFC 2 is a mixed martial arts fighting "
              "video game developed by EA Canada, and published in March 2016 "
              "by Electronic Arts for the PlayStation 4 and Xbox One. "
              "The sequel to 2014's EA Sports UFC, it is based on the "
              "Ultimate Fighting Championship (UFC) brand. The game's cover "
              "features Ronda Rousey and Conor McGregor.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category5,
              user=user1)

item20 = Item(name="WWE 2K17 (2016)",
              description="WWE 2K17 is a professional wrestling video-game "
              "developed by Yuke's and Visual Concepts, and published by 2K "
              "Sports for the PlayStation 4, Xbox 360, Xbox One "
              "and Microsoft Windows. It is the eighteenth game in the WWE "
              "game series (fourth under the WWE 2K banner) and is "
              "serving as the follow up to WWE 2K16.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category5,
              user=user1)

item21 = Item(name="Outlast (2014)",
              description="Outlast is a first-person survival horror video "
              "game developed and published by Red Barrels. The game "
              "revolves around a freelance investigative journalist, "
              "Miles Upshur, who decides to investigate a remote psychiatric "
              "hospital named Mount Massive Asylum, located deep in the "
              "mountains of Lake County, Colorado. The Whistleblower DLC "
              "centers on Waylon Park, the man who led Miles there in the "
              "first place. Outlast was released for Microsoft Windows on "
              "September 4, 2013, PlayStation 4 on February 4, 2014 and for "
              "Xbox One on June 19, 2014. Outlast received generally positive "
              "reviews from critics, and it was praised for its horror "
              "elements and gameplay. Linux and OS X versions were "
              "later released on March 31, 2015.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category6,
              user=user1)

item22 = Item(name="Counter-Strike: Global Offensive (2012)",
              description="Counter-Strike: Global Offensive (abbreviated as "
              "CS:GO) is a multiplayer first-person shooter video game "
              "developed by Hidden Path Entertainment and Valve Corporation. "
              "It is the fourth game in the main Counter-Strike franchise. "
              "Counter-Strike: Global Offensive was released for Microsoft "
              "Windows, OS X, Xbox 360, and PlayStation 3 in August 2012, "
              "with the Linux version being released in September 2014",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category8,
              user=user1)

item23 = Item(name="Overwatch (2016)",
              description="Overwatch is a team-based multiplayer first-"
              "person shooter video game developed and published by Blizzard "
              "Entertainment. It was released in May 2016 for Microsoft "
              "Windows, PlayStation 4, and Xbox One.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category8,
              user=user1)

db_session.add(item1)
db_session.add(item2)
db_session.add(item3)
db_session.add(item4)
db_session.add(item5)
db_session.add(item6)
db_session.add(item7)
db_session.add(item8)
db_session.add(item9)
db_session.add(item10)
db_session.add(item11)
db_session.add(item12)
db_session.add(item13)
db_session.add(item14)
db_session.add(item15)
db_session.add(item16)
db_session.add(item17)
db_session.add(item18)
db_session.add(item19)
db_session.add(item20)
db_session.add(item21)
db_session.add(item22)
db_session.add(item23)
db_session.commit()

print "added catalog items!"
