import csv

with open('marvel.csv', 'w', newline='') as f:
    fieldnames = ['name', 'alias', 'nationality', 'biological_mother',
    'biological_father', 'franchise', 'spouse',
    'species', 'height', 'weight', 'gender']
    thewriter = csv.DictWriter(f, fieldnames=fieldnames)

    thewriter.writeheader()
    thewriter.writerow({'name': 'Tony Stark', 'alias': 'Iron Man',
        'nationality': 'American', 'biological_mother': 'Amanda Armstrong',
        'biological_father': 'Jude', 'franchise': 'The Avengers', 'spouse': '',
        'species': 'human', 'height':'6\'1', 'weight':'225 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'T\'Challa', 'alias': 'Black Panther',
        'nationality': 'Wakandan', 'biological_mother': 'N\'Yami',
        'biological_father': 'T\'Chaka', 'franchise': 'The Avengers', 'spouse': '',
        'species': 'human', 'height':'6\'', 'weight':'200 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Dane Whitman', 'alias': 'Black Knight',
        'nationality': 'American', 'biological_mother': '',
        'biological_father': '', 'franchise': 'The Avengers', 'spouse': '',
        'species': 'human', 'height':'6\'', 'weight':'190 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Natalia Romanova', 'alias': 'Black Widow',
        'nationality': 'Russian', 'biological_mother': '',
        'biological_father': '', 'franchise': 'The Avengers', 'spouse': '',
        'species': 'human', 'height':'5\'7', 'weight':'131 lbs',
        'gender': 'female'})
    thewriter.writerow({'name': 'Steven Rogers', 'alias': 'Captain America',
        'nationality': 'American', 'biological_mother': 'Sarah Rogers',
        'biological_father': 'Joseph Rogers', 'franchise': 'The Avengers',
        'spouse': '', 'species': 'human', 'height':'6\'2', 'weight':'220 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Anthony Druid', 'alias': 'Doctor Druid',
        'nationality': 'American', 'biological_mother': '',
        'biological_father': '', 'franchise': 'The Avengers', 'spouse': '',
        'species': 'human', 'height':'6\'5', 'weight':'311 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Samuel Wilson', 'alias': 'Falcon',
        'nationality': 'American', 'biological_mother': 'Darlene Wilson',
        'biological_father': 'Paul Wilson', 'franchise': 'The Avengers', 'spouse': '',
        'species': 'human', 'height':'6\'2', 'weight':'240 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Henry Pym', 'alias': 'Giant Man',
        'nationality': 'American', 'biological_mother': 'Doris Pym',
        'biological_father': 'Brad Pym', 'franchise': 'The Avengers', 'spouse': '',
        'species': 'human', 'height':'6\'', 'weight':'185 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Clinton Barton', 'alias': 'Hawkeye',
        'nationality': 'American', 'biological_mother': 'Edith Barton',
        'biological_father': 'Harold Barton', 'franchise': 'The Avengers', 'spouse': '',
        'species': 'human', 'height':'6\'3', 'weight':'230 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Maria Hill', 'alias': '',
        'nationality': 'American', 'biological_mother': '',
        'biological_father': 'Ed Vernon', 'franchise': 'The Avengers', 'spouse': '',
        'species': 'human', 'height':'5\'10', 'weight':'135 lbs',
        'gender': 'female'})
    thewriter.writerow({'name': 'Pietro Maximoff', 'alias': 'Quicksilver',
        'nationality': 'American', 'biological_mother': 'Natalya Maximoff',
        'biological_father': '', 'franchise': 'The Avengers', 'spouse': '',
        'species': 'human', 'height':'6\'', 'weight':'175 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Monica Rambeau', 'alias': 'Spectrum',
        'nationality': 'American', 'biological_mother': 'Maria Rambeau',
        'biological_father': 'Frank Rambeau', 'franchise': 'The Avengers',
        'spouse': '', 'species': 'human mutate', 'height':'5\'10',
        'weight':'130 lbs', 'gender': 'female'})
    thewriter.writerow({'name': 'Wanda Maximoff', 'alias': 'Scarlet Witch',
        'nationality': 'American', 'biological_mother': 'Natalya Maximoff',
        'biological_father': '', 'franchise': 'The Avengers', 'spouse': '',
        'species': 'human genetically altered', 'height':'5\'7', 'weight':'132 lbs',
        'gender': 'female'})
    thewriter.writerow({'name': 'Thor Odinson', 'alias': 'Thor'
        'nationality': 'American', 'biological_mother': 'Gaea',
        'biological_father': 'Odin Borson', 'franchise': 'The Avengers',
        'spouse': '', 'species': 'Asgardian', 'height':'6\'6', 'weight':'640 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'The Vision', 'alias': 'Vision',
        'nationality': 'American', 'biological_mother': '',
        'biological_father': 'Ultron', 'franchise': 'The Avengers', 'spouse': '',
        'species': 'human', 'height':'6\'3', 'weight':'300 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Janet van Dyne', 'alias': 'Wasp',
        'nationality': 'American', 'biological_mother': '',
        'biological_father': 'Dr. Vernon Van Dyne', 'franchise': 'The Avengers',
        'spouse': '', 'species': 'human mutate', 'height':'5\'4', 'weight':'110 lbs',
        'gender': 'female'})
'''    thewriter.writerow({'name': 'Tony Stark', 'alias': 'Iron Man',
        'nationality': 'American', 'biological_mother': 'Amanda Armstrong',
        'biological_father': 'Jude', 'franchise': 'The Avengers', 'spouse': '',
        'species': 'human', 'height':'6\'1', 'weight':'225 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Tony Stark', 'alias': 'Iron Man',
        'nationality': 'American', 'biological_mother': 'Amanda Armstrong',
        'biological_father': 'Jude', 'franchise': 'The Avengers', 'spouse': '',
        'species': 'human', 'height':'6\'1', 'weight':'225 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Tony Stark', 'alias': 'Iron Man',
        'nationality': 'American', 'biological_mother': 'Amanda Armstrong',
        'biological_father': 'Jude', 'franchise': 'The Avengers', 'spouse': '',
        'species': 'human', 'height':'6\'1', 'weight':'225 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Tony Stark', 'alias': 'Iron Man',
        'nationality': 'American', 'biological_mother': 'Amanda Armstrong',
        'biological_father': 'Jude', 'franchise': 'The Avengers', 'spouse': '',
        'species': 'human', 'height':'6\'1', 'weight':'225 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Tony Stark', 'alias': 'Iron Man',
        'nationality': 'American', 'biological_mother': 'Amanda Armstrong',
        'biological_father': 'Jude', 'franchise': 'The Avengers', 'spouse': '',
        'species': 'human', 'height':'6\'1', 'weight':'225 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Tony Stark', 'alias': 'Iron Man',
        'nationality': 'American', 'biological_mother': 'Amanda Armstrong',
        'biological_father': 'Jude', 'franchise': 'The Avengers', 'spouse': '',
        'species': 'human', 'height':'6\'1', 'weight':'225 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Tony Stark', 'alias': 'Iron Man',
        'nationality': 'American', 'biological_mother': 'Amanda Armstrong',
        'biological_father': 'Jude', 'franchise': 'The Avengers', 'spouse': '',
        'species': 'human', 'height':'6\'1', 'weight':'225 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Tony Stark', 'alias': 'Iron Man',
        'nationality': 'American', 'biological_mother': 'Amanda Armstrong',
        'biological_father': 'Jude', 'franchise': 'The Avengers', 'spouse': '',
        'species': 'human', 'height':'6\'1', 'weight':'225 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Tony Stark', 'alias': 'Iron Man',
        'nationality': 'American', 'biological_mother': 'Amanda Armstrong',
        'biological_father': 'Jude', 'franchise': 'The Avengers', 'spouse': '',
        'species': 'human', 'height':'6\'1', 'weight':'225 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Tony Stark', 'alias': 'Iron Man',
        'nationality': 'American', 'biological_mother': 'Amanda Armstrong',
        'biological_father': 'Jude', 'franchise': 'The Avengers', 'spouse': '',
        'species': 'human', 'height':'6\'1', 'weight':'225 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Tony Stark', 'alias': 'Iron Man',
        'nationality': 'American', 'biological_mother': 'Amanda Armstrong',
        'biological_father': 'Jude', 'franchise': 'The Avengers', 'spouse': '',
        'species': 'human', 'height':'6\'1', 'weight':'225 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Tony Stark', 'alias': 'Iron Man',
        'nationality': 'American', 'biological_mother': 'Amanda Armstrong',
        'biological_father': 'Jude', 'franchise': 'The Avengers', 'spouse': '',
        'species': 'human', 'height':'6\'1', 'weight':'225 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Tony Stark', 'alias': 'Iron Man',
        'nationality': 'American', 'biological_mother': 'Amanda Armstrong',
        'biological_father': 'Jude', 'franchise': 'The Avengers', 'spouse': '',
        'species': 'human', 'height':'6\'1', 'weight':'225 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Tony Stark', 'alias': 'Iron Man',
        'nationality': 'American', 'biological_mother': 'Amanda Armstrong',
        'biological_father': 'Jude', 'franchise': 'The Avengers', 'spouse': '',
        'species': 'human', 'height':'6\'1', 'weight':'225 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Tony Stark', 'alias': 'Iron Man',
        'nationality': 'American', 'biological_mother': 'Amanda Armstrong',
        'biological_father': 'Jude', 'franchise': 'The Avengers', 'spouse': '',
        'species': 'human', 'height':'6\'1', 'weight':'225 lbs',
        'gender': 'male'})
    thewriter.writerow({'name': 'Tony Stark', 'alias': 'Iron Man',
        'nationality': 'American', 'biological_mother': 'Amanda Armstrong',
        'biological_father': 'Jude', 'franchise': 'The Avengers', 'spouse': '',
        'species': 'human', 'height':'6\'1', 'weight':'225 lbs',
        'gender': 'male'})

def add_row():
    while True:
        name = input("What is their name?")
        if name == 'x':
            break
        alias = input("What is their hero name?")
        if name == 'x':
            break
        nationality = input("What is their nationality?")
        if name == 'x':
            break
        biological_father = input("Who is their biological father?")
        if name == 'x':
            break
        biological_mother = input("Who is their biological mother?")
        if name == 'x':
            break
        franchise = input("What franchise are they from?")
        if name == 'x':
            break
        spouse = input("To whom are they married?")
        if name == 'x':
            break
        species = input('What is their species?')
        if name == 'x':
            break
        height = input("What is their height?")
        if name == 'x':
            break
        weight = input("What is their weight?")
        if name == 'x':
            break
        gender = input("What is their gender?")
        if name == 'x':
            break
        thewriter.writerow({'name': name, 'alias': alias,
            'nationality': nationality, 'biological_mother': biological_mother,
            'biological_father': biological_father, 'franchise': franchise,
            'spouse': spouse, 'species': species, 'height': height,
            'weight': weight, 'gender': gender})
    else:
        break
