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
                choice = input(f"\nChoose one link (1-{LINKS_SHOWN}): ")
                if choice.isdigit() and 1 <= int(choice) <= LINKS_SHOWN:
                    page = wiki.page(title_list[int(choice) - 1])
                    break
                else:
                    print("Please enter a valid number.")

            steps += 1
        else:
            break

    print(f"\nCongratualtions. You needed {steps} steps to get to {destination_page.title}.")


def main():
    wiki = wikipediaapi.Wikipedia(user_agent='WikiHackathon (https://github.com/karmuslami/wiki-hackathon.git)',
                                  language='en')
    print("Welcome to the Wiki-Game.")
    play_round(wiki)


if __name__ == "__main__":
    main()