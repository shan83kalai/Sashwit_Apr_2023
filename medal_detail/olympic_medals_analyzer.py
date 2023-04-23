def createListMedals(file_path):
    data = []
    with open(file_path, 'r') as f:
        # Skip the header line
        f.readline()
        for line in f:
            # Remove the newline character at the end of the line and split by comma
            values = line.strip().split(',')
            # Convert numeric values to integers
            values[1:] = map(int, values[1:])
            data.append(values)
    return data


def total_medals_by_country(olympic_games, country):
    for entry in olympic_games:
        if entry[0] == country:
            return entry[-1]
    return 0


def highest_gold_medals(olympic_games):
    return max(olympic_games, key=lambda x: x[2])[0]


def save_countries_with_min_games(olympic_games, min_games):
    with open('countries.txt', 'w') as f:
        for entry in olympic_games:
            if entry[1] >= min_games:
                f.write(f"{entry[0]}\n")


# Example usage
file_path = 'medals.csv'
olympic_games = createListMedals(file_path)

country = 'Great Britain'
total_medals = total_medals_by_country(olympic_games, country)
print(f'Total medals for {country}: {total_medals}')

top_gold_medal_country = highest_gold_medals(olympic_games)
print(f'Country with the highest number of gold medals: {top_gold_medal_country}')

min_games = 27
save_countries_with_min_games(olympic_games, min_games)
