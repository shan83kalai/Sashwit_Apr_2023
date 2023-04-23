import tkinter as tk
from tkinter import ttk

from medal_detail.olympic_medals_analyzer import createListMedals


def get_country_data(olympic_games, country):
    for entry in olympic_games:
        if entry[0] == country:
            return entry
    return None

def create_gui(olympic_games):
    def on_search():
        country = country_entry.get()
        country_data = get_country_data(olympic_games, country)
        if country_data:
            gold_var.set(country_data[2])
            silver_var.set(country_data[3])
            bronze_var.set(country_data[4])
        else:
            gold_var.set("Not found")
            silver_var.set("Not found")
            bronze_var.set("Not found")

    root = tk.Tk()
    root.title("Summer Olympic Games Medals")

    ttk.Label(root, text="Country:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
    country_entry = ttk.Entry(root)
    country_entry.grid(row=0, column=1, sticky=tk.W, padx=10, pady=10)

    ttk.Button(root, text="Search", command=on_search).grid(row=0, column=2, sticky=tk.W, padx=10, pady=10)

    gold_var = tk.StringVar()
    silver_var = tk.StringVar()
    bronze_var = tk.StringVar()

    ttk.Label(root, text="Gold Medals:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)
    ttk.Label(root, text="Silver Medals:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=10)
    ttk.Label(root, text="Bronze Medals:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=10)

    ttk.Label(root, textvariable=gold_var).grid(row=1, column=1, sticky=tk.W, padx=10, pady=10)
    ttk.Label(root, textvariable=silver_var).grid(row=2, column=1, sticky=tk.W, padx=10, pady=10)
    ttk.Label(root, textvariable=bronze_var).grid(row=3, column=1, sticky=tk.W, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    file_path = 'medals.csv'
    olympic_games = createListMedals(file_path)
    create_gui(olympic_games)
