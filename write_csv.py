import csv

with open('marvel.csv', 'w', newline='') as file:
    fieldnames = ['name', 'alias', 'citizenship', 'biological_mother',
    'biological_father', 'affiliation',
    'origin', 'height', 'weight', 'gender', 'universe']
    thewriter = csv.DictWriter(file, fieldnames=fieldnames)

    thewriter.writeheader()
    thewriter.writerow({'name': 'Anthony Stark', 'alias': ['Mark One', 'Iron Man'],
        'citizenship': ['American', 'Bulgarian'], 'biological_mother': 'Amanda Armstrong',
        'biological_father': 'Jude', 'affiliation': ['The Avengers', 'Guardians of the Galaxy'], 'origin': ['human', 'cyborg'], 'height':'6\'1',
        'weight':'225 lbs', 'gender': 'male'})
    thewriter.writerow({'name': 'T\'Challa', 'alias': 'Black Panther',
        'citizenship': 'Wakandan', 'biological_mother': 'N\'Yami',
        'biological_father': 'T\'Chaka', 'affiliation': 'The Avengers', 'origin': 'human', 'height':'6\'',
        'weight':'200 lbs', 'gender': 'male'})
    thewriter.writerow({'name': 'Dane Whitman', 'alias': 'Black Knight',
        'citizenship': 'American', 'biological_mother': '',
        'biological_father': '', 'affiliation': 'The Avengers',
        'origin': 'human', 'height':'6\'', 'weight':'190 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Natalia Romanova', 'alias': 'Black Widow',
        'citizenship': 'Russian', 'biological_mother': '',
        'biological_father': '', 'affiliation': 'The Avengers',
        'origin': 'human', 'height':'5\'7', 'weight':'131 lbs',
        'gender': 'female'})
    thewriter.writerow({'name': 'Steven Rogers', 'alias': 'Captain America',
        'citizenship': 'American', 'biological_mother': 'Sarah Rogers',
        'biological_father': 'Joseph Rogers', 'affiliation': 'The Avengers',
        'origin': 'human', 'height':'6\'2', 'weight':'220 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Anthony Druid', 'alias': 'Doctor Druid',
        'citizenship': 'American', 'biological_mother': '',
        'biological_father': '', 'affiliation': 'The Avengers',
        'origin': 'human', 'height':'6\'5', 'weight':'311 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Samuel Wilson', 'alias': 'Falcon',
        'citizenship': 'American', 'biological_mother': 'Darlene Wilson',
        'biological_father': 'Paul Wilson', 'affiliation': 'The Avengers',
        'origin': 'human', 'height':'6\'2', 'weight':'240 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Henry Pym', 'alias': 'Giant Man',
        'citizenship': 'American', 'biological_mother': 'Doris Pym',
        'biological_father': 'Brad Pym', 'affiliation': 'The Avengers',
        'origin': 'human', 'height':'6\'', 'weight':'185 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Clinton Barton', 'alias': 'Hawkeye',
        'citizenship': 'American', 'biological_mother': 'Edith Barton',
        'biological_father': 'Harold Barton', 'affiliation': 'The Avengers',
        'origin': 'human', 'height':'6\'3', 'weight':'230 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Maria Hill', 'alias': '',
        'citizenship': 'American', 'biological_mother': '',
        'biological_father': 'Ed Vernon', 'affiliation': 'The Avengers',
        'origin': 'human', 'height':'5\'10', 'weight':'135 lbs',
        'gender': 'female'})
    thewriter.writerow({'name': 'Pietro Maximoff', 'alias': 'Quicksilver',
        'citizenship': 'American', 'biological_mother': 'Natalya Maximoff',
        'biological_father': '', 'affiliation': 'The Avengers',
        'origin': 'human', 'height':'6\'', 'weight':'175 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Monica Rambeau', 'alias': 'Spectrum',
        'citizenship': 'American', 'biological_mother': 'Maria Rambeau',
        'biological_father': 'Frank Rambeau', 'affiliation': 'The Avengers',
        'origin': 'human mutate', 'height':'5\'10', 'weight':'130 lbs',
        'gender': 'female'})
    thewriter.writerow({'name': 'Wanda Maximoff', 'alias': 'Scarlet Witch',
        'citizenship': 'American', 'biological_mother': 'Natalya Maximoff',
        'biological_father': '', 'affiliation': 'The Avengers',
        'origin': 'human genetically altered', 'height':'5\'7', 'weight':'132 lbs',
        'gender': 'female'})
    thewriter.writerow({'name': 'Thor Odinson', 'alias': 'Thor',
        'citizenship': 'American', 'biological_mother': 'Gaea',
        'biological_father': 'Odin Borson', 'affiliation': 'The Avengers', 'origin': 'Asgardian', 'height':'6\'6', 'weight':'640 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'The Vision', 'alias': 'Vision',
        'citizenship': 'American', 'biological_mother': '',
        'biological_father': 'Ultron', 'affiliation': 'The Avengers',
        'origin': 'human', 'height':'6\'3', 'weight':'300 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Janet van Dyne', 'alias': 'Wasp',
        'citizenship': 'American', 'biological_mother': '',
        'biological_father': 'Dr. Vernon Van Dyne', 'affiliation': 'The Avengers',
        'origin': 'human mutate', 'height':'5\'4', 'weight':'110 lbs',
        'gender': 'female'})
    thewriter.writerow({'name': 'Scott Summers', 'alias': 'Cyclops',
        'citizenship': 'American', 'biological_mother': 'Katherine Summers',
        'biological_father': 'Christopher Summers', 'affiliation': 'X-Men',
        'origin': 'mutant', 'height':'6\'3', 'weight':'195 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Evan Sabahnur', 'alias': 'Genesis',
        'citizenship': 'American', 'biological_mother': '',
        'biological_father': 'Apocalypse', 'affiliation': 'X-Men',
        'origin': 'mutant', 'height':'', 'weight':'',
        'gender': 'male'})
    thewriter.writerow({'name': 'Warren Worthington III', 'alias': 'Angel',
        'citizenship': 'American', 'biological_mother': 'Kathryn Worthington',
        'biological_father': 'Warren K. Worthington Jr.', 'affiliation': 'X-Men',
        'origin': 'mutant', 'height':'6\'', 'weight':'150 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Sean Cassidy', 'alias': 'Namshee',
        'citizenship': 'Irish', 'biological_mother': '',
        'biological_father': 'Patrick Rourke', 'affiliation': 'X-Men',
        'origin': 'mutant', 'height':'6\'', 'weight':'170 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Henry McCoy', 'alias': 'Beast',
        'citizenship': 'American', 'biological_mother': 'Edna McCoy',
        'biological_father': 'Norton McCoy', 'affiliation': 'X-Men',
        'origin': 'mutant', 'height':'5\'11', 'weight':'402 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Emma Frost', 'alias': 'White Queen',
        'citizenship': 'American', 'biological_mother': 'Hazel Frost',
        'biological_father': 'Winston Frost', 'affiliation': 'X-Men',
        'origin': 'mutant', 'height':'5\'10', 'weight':'144 lbs',
        'gender': 'female'})
    thewriter.writerow({'name': 'Remy LeBeau', 'alias': 'Gambit',
        'citizenship': 'American', 'biological_mother': '',
        'biological_father': 'Jean-Luc LeBeau', 'affiliation': 'X-Men',
        'origin': 'mutant', 'height':'6\'2', 'weight':'179 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Alexander Summers', 'alias': 'Havok',
        'citizenship': 'American', 'biological_mother': 'Katherine Summers',
        'biological_father': 'Christopher Summers', 'affiliation': 'X-Men',
        'origin': 'mutant', 'height':'6\'', 'weight':'175 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Robert Drake', 'alias': 'Iceman',
        'citizenship': 'American', 'biological_mother': 'Madeline Drake',
        'biological_father': 'William Drake', 'affiliation': 'X-Men',
        'origin': 'mutant', 'height':'5\'8', 'weight':'145 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Lockheed', 'alias': '',
        'citizenship': 'Flock', 'biological_mother': '',
        'biological_father': '', 'affiliation': 'X-Men',
        'origin': 'Flock', 'height':'2\'6', 'weight':'20 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Moira Kinross', 'alias': 'Moira X',
        'citizenship': 'Scottish', 'biological_mother': 'Mrs. Kinross',
        'biological_father': 'Lord Kinross', 'affiliation': 'X-Men',
        'origin': 'mutant', 'height':'5\'7', 'weight':'135 lbs',
        'gender': 'female'})
    thewriter.writerow({'name': 'Max Eisenhardt', 'alias': 'Magneto',
        'citizenship': 'German', 'biological_mother': 'Edie Eisenhardt',
        'biological_father': 'Jakob Eisenhardt', 'affiliation': 'X-Men',
        'origin': 'mutant', 'height':'6\'2', 'weight':'190 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Lorna Dane', 'alias': 'Polaris',
        'citizenship': 'American', 'biological_mother': 'Suzanna',
        'biological_father': 'Max Eisenhardt', 'affiliation': 'X-Men',
        'origin': 'human', 'height':'5\'7', 'weight':'115 lbs',
        'gender': 'female'})
    thewriter.writerow({'name': 'Calvin Rankin', 'alias': 'Mimic',
        'citizenship': 'American', 'biological_mother': '',
        'biological_father': 'Ronald Rankin', 'affiliation': 'X-Men',
        'origin': 'mutant', 'height':'6\'2', 'weight':'225 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Danielle Moonstar', 'alias': 'Mirage',
        'citizenship': 'American', 'biological_mother': 'Peg Lonestar',
        'biological_father': 'William Lonestar', 'affiliation': 'X-Men',
        'origin': 'mutant', 'height':'5\'6', 'weight':'123 lbs',
        'gender': 'female'})
    thewriter.writerow({'name': 'Kurt Wagner', 'alias': 'Nightcrawler',
        'citizenship': 'German', 'biological_mother': 'Raven Darkholme',
        'biological_father': 'Azazel', 'affiliation': 'X-Men',
        'origin': 'mutant', 'height':'5\'9', 'weight':'161 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Jean Grey', 'alias': 'Marvel Girl',
        'citizenship': 'American', 'biological_mother': 'Elaine Grey',
        'biological_father': 'John Grey', 'affiliation': 'X-Men',
        'origin': 'mutant', 'height':'5\'6', 'weight':'130 lbs',
        'gender': 'female'})
    thewriter.writerow({'name': 'Charles Xavier', 'alias': 'Professor X',
        'citizenship': 'American', 'biological_mother': 'Sharon Xavier-Marko',
        'biological_father': 'Dr. Brian Xavier', 'affiliation': 'X-Men',
        'origin': 'mutant', 'height':'6\'0', 'weight':'190 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Changeling', 'alias': '',
        'citizenship': 'American', 'biological_mother': '',
        'biological_father': '', 'affiliation': 'X-Men',
        'origin': 'mutant', 'height':'5\'11', 'weight':'180 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Katherine Pryde', 'alias': 'Red Queen',
        'citizenship': 'American', 'biological_mother': 'Theresa Pryde',
        'biological_father': 'Carmen Pryde', 'affiliation': ['X-Men', 'Guardians of the Galaxy'],
        'origin': 'mutant', 'height':'5\'6', 'weight':'110 lbs',
        'gender': 'female', 'universe': 'Earth-616'})
    thewriter.writerow({'name': 'Elizabeth Braddock', 'alias': 'Captain Britain',
        'citizenship': 'English', 'biological_mother': 'Lady Elizabeth Braddock',
        'biological_father': 'Sir James Braddock', 'affiliation': 'X-Men',
        'origin': 'mutant', 'height':'5\'11', 'weight':'155 lbs',
        'gender': 'female'})
    thewriter.writerow({'name': 'Anna Marie LeBeau', 'alias': 'Rogue',
        'citizenship': 'American', 'biological_mother': 'Priscilla',
        'biological_father': 'Owen', 'affiliation': 'X-Men',
        'origin': 'mutant', 'height':'5\'8', 'weight':'135 lbs',
        'gender': 'female'})
    thewriter.writerow({'name': 'Ororo Munroe', 'alias': 'Storm',
        'citizenship': 'American', 'biological_mother': 'N\'Daré Munroe',
        'biological_father': 'David Munroe', 'affiliation': 'X-Men',
        'origin': 'mutant', 'height':'5\'11', 'weight':'145 lbs',
        'gender': 'female'})
    thewriter.writerow({'name': 'Gabriel Summers', 'alias': 'Vulcan',
        'citizenship': 'American', 'biological_mother': 'Katherine Summers',
        'biological_father': 'Christopher Summers', 'affiliation': 'X-Men',
        'origin': 'mutant', 'height':'6\'0', 'weight':'178 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'James Howlett', 'alias': 'Wolverine',
        'citizenship': 'Canadian', 'biological_mother': 'Elizabeth Howlett',
        'biological_father': 'Thomas Logan', 'affiliation': 'X-Men',
        'origin': 'mutant', 'height':'5\'3', 'weight':'195 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Phyla-Vell (Earth-TRN707)', 'alias': 'Captain Marvel',
        'citizenship': 'Titan', 'biological_mother': '',
        'biological_father': '', 'affiliation': 'Guardians of the Galaxy',
        'origin': 'Titanian/Kree', 'height':'', 'weight':'',
        'gender': 'female', 'universe': 'Earth-TRN707'})
    thewriter.writerow({'name': 'Noh-Varr', 'alias': 'Marvel Boy',
        'citizenship': 'Kree Empire', 'biological_mother': 'Star Splendor',
        'biological_father': 'Captain Glory', 'affiliation': 'Guardians of the Galaxy',
        'origin': 'Kree', 'height':'5\'10', 'weight':'165 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Heather Douglas (Earth-TRN707)', 'alias': 'Moondragon',
        'citizenship': 'American', 'biological_mother': '',
        'biological_father': '', 'affiliation': 'Guardians of the Galaxy',
        'origin': 'Human', 'height':'', 'weight':'',
        'gender': 'female'})
    thewriter.writerow({'name': 'Richard Rider', 'alias': 'Nova',
        'citizenship': 'American', 'biological_mother': 'Gloria Rider',
        'biological_father': 'Charles Rider', 'affiliation': 'Guardians of the Galaxy',
        'origin': 'Human', 'height':'6\'1', 'weight':'190 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Rocket Raccoon', 'alias': 'Sharpshooting Space Raccoon',
        'citizenship': 'Halfworlders', 'biological_mother': '',
        'biological_father': '', 'affiliation': 'Guardians of the Galaxy',
        'origin': ['Halfworlder Mutate', 'Cyborg'], 'height':'4\'0', 'weight':'55 lbs',
        'gender': 'male', 'universe': 'Earth-616'})
    thewriter.writerow({'name': 'Peter Quill', 'alias': 'Star-Lord',
        'citizenship': 'American', 'biological_mother': 'Meredith Quill',
        'biological_father': "J'son of Spartax", 'affiliation': 'Guardians of the Galaxy',
        'origin': 'Human', 'height':'6\'2', 'weight':'175 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Aldrif Odinsdotter', 'alias': 'Angela',
        'citizenship': 'American', 'biological_mother': 'Frigga',
        'biological_father': 'Odin Borson', 'affiliation': 'Guardians of the Galaxy',
        'origin': 'Asgardian', 'height':'6\'2', 'weight':'480 lbs',
        'gender': 'female'})
    thewriter.writerow({'name': 'Scott Lang', 'alias': 'Ant-Man',
        'citizenship': 'American', 'biological_mother': '',
        'biological_father': 'Bob Lang', 'affiliation': 'Guardians of the Galaxy',
        'origin': 'Human', 'height':'6\'0', 'weight':'190 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Beta Ray Bill', 'alias': 'Thor',
        'citizenship': 'Korbinite', 'biological_mother': '',
        'biological_father': '', 'affiliation': 'Guardians of the Galaxy',
        'origin': 'Korbinite Cyborg', 'height':'6\'7', 'weight':'480 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Bug (Insectivorid)', 'alias': 'Loverbug',
        'citizenship': 'Kaliklakian', 'biological_mother': 'Queen Esmera',
        'biological_father': 'Wartstaff', 'affiliation': 'Guardians of the Galaxy',
        'origin': 'Insectivorid', 'height':'6\'1', 'weight':'163 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Carol Danvers', 'alias': 'Captain Marvel',
        'citizenship': 'American', 'biological_mother': 'Mari-Ell / Marie Danvers',
        'biological_father': 'Joe Danvers Sr.', 'affiliation': 'Guardians of the Galaxy',
        'origin': 'Human/Kree Hybrid', 'height':'5\'11', 'weight':'124 lbs',
        'gender': 'female'})
    thewriter.writerow({'name': 'Arthur Douglas', 'alias': 'Drax the Destroyer',
        'citizenship': ['American', 'Titanian'], 'biological_mother': '',
        'biological_father': '', 'affiliation': 'Guardians of the Galaxy',
        'origin': 'Ex-human biologically enhanced. Artificial body created by Mentor',
        'height':'6\'4', 'weight':'680 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Gamora Zen Whoberi Ben Titan', 'alias': 'Most Dangerous Woman in the Galaxy',
        'citizenship': 'Zen-Whoberis', 'biological_mother': '',
        'biological_father': '', 'affiliation': 'Guardians of the Galaxy',
        'origin': 'Zen-Whoberi', 'height':'6\'', 'weight':'170 lbs',
        'gender': 'female'})
    thewriter.writerow({'name': 'Kallark', 'alias': 'Gladiator',
        'citizenship': 'Shi\'ar Empire', 'biological_mother': '',
        'biological_father': '', 'affiliation': 'Guardians of the Galaxy',
        'origin': 'Strontian', 'height':'6\'6', 'weight':'595 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Groot', 'alias': 'Child of Destruction',
        'citizenship': 'Korbinite', 'biological_mother': '',
        'biological_father': '', 'affiliation': 'Guardians of the Galaxy',
        'origin': 'Flora colossi', 'height':'23\'', 'weight':'8000 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Jack Harrison', 'alias': 'Jack Flag',
        'citizenship': 'American', 'biological_mother': 'Mrs. Harrison',
        'biological_father': 'Mr. Harrison', 'affiliation': 'Guardians of the Galaxy',
        'origin': ['Human', 'Hyde Formula'], 'height':'6\'1', 'weight':'210 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Lockjaw', 'alias': 'Slobberchops',
        'citizenship': ['Attilan', 'New Attilan'], 'biological_mother': '',
        'biological_father': '', 'affiliation': 'Guardians of the Galaxy',
        'origin': 'inhuman dog', 'height':'5\'', 'weight':'1240 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Vance Astro', 'alias': 'Major Victory',
        'citizenship': 'American', 'biological_mother': 'Norma Astrovik',
        'biological_father': 'Arnold Astrovik', 'affiliation': 'Guardians of the Galaxy',
        'origin': 'mutant', 'height':'6\'1', 'weight':'235 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Mantis', 'alias': 'Celestial Madonna',
        'citizenship': 'Vietnamese', 'biological_mother': 'Lua Brandt',
        'biological_father': 'Gustav Brandt', 'affiliation': 'Guardians of the Galaxy',
        'origin': 'human mutate', 'height':'5\'6', 'weight':'115 lbs',
        'gender': 'female'})
    thewriter.writerow({'name': 'Phyla-Vell (Earth-616)', 'alias': 'Martyr',
        'citizenship': ['Titan', 'Kree Empire', 'Hell'], 'biological_mother': 'Elysius',
        'biological_father': 'Mar-Vell', 'affiliation': 'Guardians of the Galaxy',
        'origin': 'Titanian/Kree', 'height':'5\'9', 'weight':'103 lbs',
        'gender': 'female', 'universe': 'Earth-616'})
    thewriter.writerow({'name': 'Heather Douglas (Earth-616)', 'alias': 'Moondragon',
        'citizenship': 'Korbinite', 'biological_mother': 'Yvette Steckley',
        'biological_father': 'Arthur Douglas', 'affiliation': 'Guardians of the Galaxy',
        'origin': 'human', 'height':'6\'3', 'weight':'150 lbs',
        'gender': 'female', 'universe': 'Earth-616'})
    thewriter.writerow({'name': 'Nebula', 'alias': '',
        'citizenship': '', 'biological_mother': '',
        'biological_father': 'Zorr', 'affiliation': 'Guardians of the Galaxy',
        'origin': ['Titanian', 'Cyborg'], 'height':'6\'1', 'weight':'185 lbs',
        'gender': 'female', 'universe': 'Earth-616'})
    thewriter.writerow({'name': 'Frank Castle', 'alias': 'The Rider',
        'citizenship': 'American', 'biological_mother': '',
        'biological_father': '', 'affiliation': 'Guardians of the Galaxy',
        'origin': 'human', 'height':'', 'weight':'',
        'gender': 'male', 'universe': 'Earth-TRN666'})
    thewriter.writerow({'name': 'Benjamin Grimm', 'alias': 'The Thing',
        'citizenship': 'American', 'biological_mother': 'Elsie Grimm',
        'biological_father': 'Daniel Grimm', 'affiliation': 'Guardians of the Galaxy',
        'origin': 'Human Mutate', 'height':'6\'', 'weight':'500 lbs',
        'gender': 'male', 'universe': 'Earth-616'})
    thewriter.writerow({'name': 'Eugene Thompson', 'alias': 'Agent Anti-Venom',
        'citizenship': 'American', 'biological_mother': 'Rosie Thompson',
        'biological_father': 'Harrison Thompson', 'affiliation': 'Guardians of the Galaxy',
        'origin': 'Human Cyborg', 'height':'4\'1', 'weight':'160 lbs',
        'gender': 'male', 'universe': 'Earth-616'})
    thewriter.writerow({'name': 'Adam Warlock', 'alias': 'Warlock',
        'citizenship': '', 'biological_mother': '',
        'biological_father': '', 'affiliation': 'Guardians of the Galaxy',
        'origin': 'Cosmic Being', 'height':'6\'2', 'weight':'240 lbs',
        'gender': 'male', 'universe': 'Earth-616'})
