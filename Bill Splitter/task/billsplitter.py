# Hyperskill - BillSplitter - 'The Lucky One' - Stage 3/4

"""
Created on: Thu Feb 29 2024
Last Modified: Mon Mar 06 2024
@author: diffloc

# OBJECTIVE:

In this stage your program should perform the following steps:

    1.  Take user input — how many people want to join, including the user;
    2.  In case of an invalid number of people (zero or negative),
        "No one is joining for the party" is expected as an output;
    3.  Otherwise, take the friends' names as input, iteratively;
    4.  Store them in a dictionary initialized with zeros;
    5.  Take user input - bill total.
    6.  Ask user if they want to use the "Who is lucky?" feature
        - if 'Yes': Choose random friend from dict
            - Distribute bill across unlucky friends, lucky friend pays zero
        - if 'No' (or not 'Yes'): Output "No one is going to be lucky"
            - Distribute bill equally across all friends
    7.  Print out the dictionary.
"""
import random
import sys
from typing import NoReturn


class FriendsList:
    def __init__(self) -> None:
        """
        Initialize the FriendsList class with an empty dictionary for storing friends.
        """
        self.number_of_friends: int = 0
        self.friends_dict: dict[str, float] = {}
        self.bill_total: int = 0
        self.lucky_friend: str = ""

    def get_number_of_friends(self) -> None:
        """
        Prompt the user for the number of friends joining the party and return it.
        Exit the program for any value not > 0.
        """
        try:
            number: int = int(input('Enter the number of friends joining (including you):\n'))
            if number <= 0:
                raise ValueError
            self.number_of_friends = number
        except ValueError:
            print("\nNo one is joining for the party")
            sys.exit()

    def add_friends(self) -> None:
        """
        Add friends' names to the dictionary with an initial value of 0 (zero).
        """
        print('\nEnter the name of every friend (including you), each on a new line:')
        for _ in range(self.number_of_friends):
            name: str = input()
            self.friends_dict[name] = 0.0

    def get_bill_total(self) -> None:
        self.bill_total: float = float(input("\nEnter the total bill value:\n"))

    def choose_lucky_friend(self) -> None:
        """
        Option to select a lucky friend from the list and update the lucky_friend attribute.
        """
        option_lucky_friend: str = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')
        if option_lucky_friend == "Yes":
            self.lucky_friend = random.choice(list(self.friends_dict.keys()))
            print(f"\n{self.lucky_friend} is the lucky one!\n")
        else:
            print("No one is going to be lucky")

    def distribute_bill(self) -> None:
        """
        Calculate and store the split amount each friend has to pay.
        Take into account if a lucky friend has been chosen.
        """
        if self.lucky_friend == "":
            split_amount = self.bill_total / self.number_of_friends
            scrubbed_amount = round(split_amount, 2) if not split_amount.is_integer() else int(split_amount)
            for name in self.friends_dict:
                self.friends_dict[name] = scrubbed_amount
        else:
            split_amount = self.bill_total / (self.number_of_friends - 1)
            scrubbed_amount = round(split_amount, 2) if not split_amount.is_integer() else int(split_amount)
            for name in self.friends_dict:
                if name != self.lucky_friend:
                    self.friends_dict[name] = scrubbed_amount
                else:
                    self.friends_dict[name] = 0

    def print_friends(self) -> None:
        """Print the dictionary of friends and how much each has to pay."""
        print(self.friends_dict)


def main() -> NoReturn:
    """
    The main function to run the BillSplitter program.
    """
    friends_list: FriendsList = FriendsList()
    friends_list.get_number_of_friends()
    friends_list.add_friends()
    friends_list.get_bill_total()
    friends_list.choose_lucky_friend()
    friends_list.distribute_bill()
    friends_list.print_friends()


if __name__ == "__main__":
    main()
