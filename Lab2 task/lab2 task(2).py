import os
os.system("clear")
movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

def calculate_average(movies):
    total_budget = 0
    for movie in movies:
        total_budget += movie[1]
    average_budget = total_budget / len(movies)
    return average_budget


def main():
    num_additions = int(input("How many movies would you like to add? "))
    for _ in range(num_additions):
        name = input("Enter movie name: ")
        budget = int(input("Enter movie budget: "))
        movies.append((name, budget))
    
    avg_budget = calculate_average(movies)
    count_above_avg = 0
    print("\nMovies with budgets higher than the average:")
    for movie, budget in movies:
        if budget > avg_budget:
            print(f"{movie} has a budget of {budget}, which is {budget - avg_budget:.2f} higher than the average.")
            count_above_avg += 1
    
    print(f"otal number of movies with budgets higher than the average: {count_above_avg}")

    
    
    
    
    
main()
