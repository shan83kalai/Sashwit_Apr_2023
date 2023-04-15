def read_data(file_path):
    data = []
    with open(file_path, 'r') as f:
        # Skip the header line
        f.readline()
        lines = f.readlines()
        for line in lines:
            # Remove the newline character at the end of the line and split by comma
            values = line.strip().split(',')
            # Convert numeric values to integers
            values[1:] = map(int, values[1:])
            data.append(values)
    return data


def total_medals_by_country(olympic_games, country):
    total_medals = 0
    for entry in olympic_games:
        if entry[0] == country:
            total_medals += entry[-1]
    return total_medals


def highest_gold_medals(olympic_games):
    max_gold = 0
    max_gold_country = None
    for entry in olympic_games:
        if entry[2] > max_gold:
            max_gold = entry[2]
            max_gold_country = entry[0]
    return max_gold_country


def save_countries_with_min_games(olympic_games, min_games):
    with open('countries.txt', 'w') as f:
        for entry in olympic_games:
            if entry[1] >= min_games:
                f.write(f"{entry[0]}\n")


# Example usage
file_path = 'medals.csv'
olympic_games = read_data(file_path)

country = 'United States'
total_medals = total_medals_by_country(olympic_games, country)
print(f'Total medals for {country}: {total_medals}')

top_gold_medal_country = highest_gold_medals(olympic_games)
print(f'Country with the highest number of gold medals: {top_gold_medal_country}')

min_games = 27
save_countries_with_min_games(olympic_games, min_games)
