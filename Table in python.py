films = {
    'Phase 3':  {
        6: [2012, 'Avengers'],
        5: [2011, 'Captain America: The first avenger'],
        4: [2011, 'Thor'],
        1: [2016, 'Captain Amercia: Civil War'],
        3: [2010, 'Iron Man 2'],
        2: [2008, 'The Incredible Hulk'],
    },
    'Phase 1':  {
        6: [2018, 'Black Panther'],
        9: [2019, 'Captain Marvel'],
        5: [2017, 'Thor 3: Ragnarok'],
        4: [2017, 'Spider-Man Homecoming'],
        7: [2018, 'Avengers: Infinity War'],
        1: [2008, 'Iron Man'],
        10: [2019, 'Avengers: Endgame'],
        3: [2017, 'Guardians of the Galaxy Vol. 2'],
        8: [2008, 'Ant Man and the Wasp'],
        2: [2016, 'Doctor Strange'],
    },
    'Phase 2':  {
        6: [2015, 'Ant Man'],
        5: [2015, 'Avengers 2: Age of Ultron'],
        4: [2014, 'Guardians of the Galaxy Vol. 1'],
        1: [2013, 'Iron Man 3'],
        3: [2014, 'Captain America 2: The Winter Soldier'],
        2: [2013, 'Thor 2: The Dark World'],
    },
}

print("-" * 91)
print("|{:<12}| {:<12}| {:<12}| {:<47}|".format('Phase No.', 'Sl.No', 'Year', 'Name'))
print("-" * 91)
for x, phase_values in sorted(films.items()):
    print('|{:<89}|'.format(x))
    print("-" * 91)
    for key, value in sorted(phase_values.items()):
                print("|          |{:<12}| {:<12}| {:<50}|".format(key, value[0], value[1]))
                print("-" * 91)


