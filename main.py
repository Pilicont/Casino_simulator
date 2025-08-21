import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

# Generate random roulette spins
def generate_spins(size=10000):
    rng = np.random.default_rng()
    return rng.integers(1, 37, size=size)

# Count how many times the user's number came up and calculate percent
def calculate_spin_results(data, number):
    total_count = np.sum(data == number)
    percent = (total_count / len(data)) * 100
    return total_count, percent

# Return total games and average percent of wins
def session_statistic(wins, games_played):
    avg_percent = mean(wins) if wins else 0
    return games_played, avg_percent

# Draw a simple histogram comparing results with theory
def histogram(expected_count, counts, numbers):
    plt.bar(numbers, counts, color='skyblue', label='Experiment')
    plt.axhline(expected_count, color='red', linestyle='--', label='Theory')
    plt.xlabel('Roulette Number')
    plt.ylabel('Times it came up')
    plt.title('Your spins vs. theoretical expectation')
    plt.legend()
    plt.show()

def main():
    data = generate_spins()
    wins = []
    games_played = 0
    user_numbers = []

    while True:
        user_input = input('Enter a number from 1 to 36 (or "exit"): ')
        
        if user_input.lower() == 'exit':
            games_played, avg_percent = session_statistic(wins, games_played)
            print(f'\nYou played {games_played} games.')
            print(f'Average percent of wins: {avg_percent:.2f}%')

            if user_numbers:
                counts = [user_numbers.count(n) for n in range(1, 37)]
                numbers = list(range(1, 37))
                expected_count = games_played / 36
                histogram(expected_count, counts, numbers)
            break

        if not user_input.isdigit():
            print('Enter a number between 1 and 36.')
            continue

        number = int(user_input)
        if not 1 <= number <= 36:
            print('Number must be between 1 and 36.')
            continue

        total_count, percent_of_wins = calculate_spin_results(data, number)
        print(f'Number {number} appeared {total_count} times.')
        print(f'You have: {percent_of_wins:.2f}% of wins.')

        wins.append(percent_of_wins)
        games_played += 1
        user_numbers.append(number)

        data = generate_spins()

if __name__ == '__main__':
    main()
