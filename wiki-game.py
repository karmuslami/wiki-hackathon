import wikipediaapi
import random

LINKS_SHOWN = 50
PAGES_LIST = [
    'Python (programming language)',
    'Albert Einstein',
    'Ukulele',
    'Australia',
    'Nvidia',
    'Bible',
    'Chocolate',
    'Running',
    'Chair',
    'Michael Jordan'
]

"""
API help:
.page(text) -> gets the page object with the title used for 'text'
.exists() -> returns boolean, whether or not the page exists
.title() -> returns the title of the page
.summary() -> returns the summary at the beginning of the page
.fullurl() -> returns the url of the page
.links -> gets all links inside the page
"""


def get_link_titles(page):
    link_list = []

    for number, title in enumerate(page.links):
        if number >= LINKS_SHOWN:
            break

        link_list.append(title)

    return link_list


def print_list(lst):
    for index, item in enumerate(lst, start=1):
        print(f"{index}. {item}")


def play_round(wiki):
    page = wiki.page(random.choice(PAGES_LIST))
    destination_page = wiki.page(random.choice(PAGES_LIST))
    #page = wiki.page('Ukulele')
    #destination_page = wiki.page('Albert Einstein')
    steps = 0

    while page.title == destination_page.title:
        destination_page = wiki.page(random.choice(PAGES_LIST))

    print(f"The destination page of this round is: {destination_page.title}")

    while True:
        if page.title != destination_page.title:
            print("\nYou are on the page: %s" % page.title)
            print(f"Current count of steps: {steps}\n")

            title_list = get_link_titles(page)
            print_list(title_list)

            while True:
                choice = input(f"\nChoose one link (1-{len(title_list)}): ")
                if choice.isdigit() and 1 <= int(choice) <= len(title_list):
                    page = wiki.page(title_list[int(choice) - 1])
                    break
                else:
                    print("Please enter a valid number.")

            steps += 1
        else:
            break

    print(f"\nYou needed {steps} steps to get to {destination_page.title}.")
    return steps


def create_players(player_count):
    players = []

    for i in range(player_count):
        player_name = input(f"What is your name, Player {i+1}? ")
        player = {"name": player_name, "total_steps": 0}
        players.append(player)

    return players


def game_over(players):
    print("\nThe game is over.")
    print("Here are the results:")

    for player in players:
        print(f"{player['name']: {player['total_steps']} total steps}")

    max_points = 0
    winner = None

    for player in players:
        if player['total_steps'] > max_points:
            max_points = player['total_steps']
            winner = player['name']

    print(f"\nThe winner is: {winner}")


def get_rounds():
    while True:
        rounds = input("How many rounds would you like to play? ")

        if rounds.isdigit() and int(rounds) > 0:
            return int(rounds)
        else:
            print("Please enter a valid number.")


def get_player_count():
    while True:
        player_count = input("How many players are playing? ")

        if player_count.isdigit() and int(player_count) > 0:
            return int(player_count)
        else:
            print("Please enter a valid number.")


def main():
    wiki = wikipediaapi.Wikipedia(user_agent='WikiHackathon (https://github.com/karmuslami/wiki-hackathon.git)',
                                  language='en')
    print("Welcome to the Wiki-Game.")
    rounds = get_rounds()
    players = create_players(get_player_count())

    played_rounds = 0

    while played_rounds < rounds:
        print(f"\nRound {played_rounds + 1}")

        for player in players:
            print(f"\n{player["name"]}, it's your turn.")
            step_count = play_round(wiki)
            player["total_steps"] += step_count

        played_rounds += 1

    game_over(players)


if __name__ == "__main__":
    main()