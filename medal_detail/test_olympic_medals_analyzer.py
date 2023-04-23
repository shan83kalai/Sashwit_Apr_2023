import unittest
from unittest.mock import patch

# Assuming the functions are in a file called olympic_medals_analyzer.py
from olympic_medals_analyzer import createListMedals, total_medals_by_country, highest_gold_medals, save_countries_with_min_games


class TestOlympicMedalsAnalyzer(unittest.TestCase):

    def setUp(self):
        self.sample_data = [
            ["Afghanistan", 14, 0, 0, 2, 2],
            ["Algeria", 13, 5, 4, 8, 17],
            ["Argentina", 24, 21, 25, 28, 74],
            ["Armenia", 6, 2, 6, 6, 14]
        ]

    def test_read_data(self):
        with patch("builtins.open", unittest.mock.mock_open(
                read_data="Team,Summer Games,Gold,Silver,Bronze,TOTAL\nAfghanistan,14,0,0,2,2\nAlgeria,13,5,4,8,17\nArgentina,24,21,25,28,74\nArmenia,6,2,6,6,14\n")):
            data = createListMedals("test.csv")
            self.assertEqual(data, self.sample_data)

    def test_total_medals_by_country(self):
        country = "Argentina"
        total_medals = total_medals_by_country(self.sample_data, country)
        self.assertEqual(total_medals, 74)

    def test_highest_gold_medals(self):
        top_gold_medal_country = highest_gold_medals(self.sample_data)
        self.assertEqual(top_gold_medal_country, "Argentina")

    def test_save_countries_with_min_games(self):
        with patch("builtins.open", unittest.mock.mock_open()) as mock_file:
            save_countries_with_min_games(self.sample_data, 10)
            mock_file().write.assert_any_call("Afghanistan\n")
            mock_file().write.assert_any_call("Algeria\n")
            mock_file().write.assert_any_call("Argentina\n")


if __name__ == '__main__':
    unittest.main()
