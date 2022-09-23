from utils import is_even, is_prime, is_multiple_10, create_account, update_bank, get_bank_data # importing utils
import random

class MainGame(object): # classes inherit from object by default
    def __init__(self):
        self.first_menu()

    def first_menu(self):
        while True:
            try:
                try:
                    getattr(self, "username")
                    user_input = input("\n____________________\n1. Main Menu\n2. Log Out\n___________________\nEnter your choice 1-2: ")
                    user_input = int(user_input)
                    if user_input == 1:
                        self.second_menu()
                    elif user_input == 2:
                        delattr(self, "username")
                        delattr(self, "balance")
                        delattr(self, "bets_made")
                        print("You have been Logged out...")
                except AttributeError:
                    user_input = input("\n____________________\n1. Register\n2. Log in\n___________________\nEnter your choice 1-2: ")
                    user_input = int(user_input)
                    if user_input == 1:
                        self.user_creation()
                    elif user_input == 2:
                        self.login()
                    else:
                        print("Please enter a valid option\nTo quit type quit, exit or stop!")
            except ValueError:
                if user_input.lower() in ["quit", "exit", "stop"]:
                    exit()
    
    def second_menu(self):
        while True:
            try:
                user_input = input("\n____________________\n1. Start Betting\n2. View Balance\n___________________\nType return to return home!\nEnter your choice 1-2: ")
                user_input = int(user_input)
                if user_input == 1:
                    self.main_game()
                elif user_input == 2:
                    print(f"\n\nYour Balance is £{self.balance:,}\n")
                else:
                    print("Please enter a valid option\nTo quit type quit, exit or stop!")
            except ValueError:
                if user_input.lower() in ["quit", "exit", "stop"]:
                    exit()
                elif user_input.lower() == "return":
                    self.first_menu()
                    break

    def user_creation(self):
        while True:
            username = input("\nenter a username to create a account,\nType quit/return to return to previous menu: ")
            if username.lower() in ["quit", "return"]:
                break
            res = create_account(username)
            if not res:
                print("unsuccessful, a account with this username already exists")

            else:
                print("created account successfully, please navigate to login and enter the username to continue")
                break

        self.first_menu()
    
    def login(self):
        while True:
            username = input("\nenter a account username to log in to,\nType quit/return to return to previous menu: ")
            if username.lower() in ["quit", "return"]:
                self.first_menu()
                break
            res = get_bank_data(username)
            if not res:
                print("unsuccessful, this account does not exist!")

            else:
                print("Logged in successfully, redirecting you to the Game Menu.")
                balance = get_bank_data(username)
                if balance == None:
                    balance = 0
                self.balance = balance
                self.username = username
                self.bets_made = {}
                self.second_menu()
                break
    
    def auth_multi(self, money: int) -> int:
        multi_stack = 1
        if is_even(money) == True:
            multi_stack = multi_stack * 2
        if is_multiple_10(money) == True:
            multi_stack = multi_stack * 3
        if is_prime(money) == True:
            multi_stack = multi_stack * 5
        if money < 5:
            multi_stack = multi_stack * 2
        return money * multi_stack
            


    
    def main_game(self):
        print("Started Game!\nTo return to previous menu at any time type \"return\"")
        BETS_DONE = False
        RUN_GAME = True
        while RUN_GAME == True:
            while BETS_DONE != True:
                try:
                    user_input_num = input("\nWould you like to add a bet on any number between 1-30?\nIf you are finished type \"done\" :")
                    user_input_num = int(user_input_num)         
                    user_input_bet = int(input(f"How much would you like to bet on number {user_input_num}? £1-10 :"))   
                    if user_input_bet > self.balance:
                        print(f"You dont have enough money to bet this amount!\nYour balance is £{self.balance:,}")
                    if str(user_input_num) not in self.bets_made.keys() and user_input_num >= 0 and user_input_num <= 30 and user_input_bet >= 1 and user_input_bet <=10 and user_input_bet <= self.balance:
                        self.bets_made[str(user_input_num)] = user_input_bet
                        self.balance = update_bank(self.username, -user_input_bet)
                        print("added bet!")
                    else:
                        print("\nInvalid bet or number entered or you have already added a bet for this number!, Try again!")
                except ValueError:
                    if user_input_num.lower() == "done":
                        BETS_DONE = True
                    if user_input_num.lower() == "return":
                        RUN_GAME = False
                        BETS_DONE = True
                        self.second_menu()
                        break
            random_number = random.randint(0, 30)
            if str(random_number) in self.bets_made.keys():
                money_betted = self.bets_made[str(random_number)]
                money_made = self.auth_multi(money_betted)
                self.balance = update_bank(self.username, money_betted)
                self.balance = update_bank(self.username, money_made)
                print(f"You won the bet for number {random_number} which you placed a bet of £{money_betted:,} on!\nMoney Made: £{money_made:,}\nNew Balance: £{self.balance:,}")
                maybe_continue = input("Press any Key to continue with a new game!\nType \"return\" to return to the previous menu!: ")
                if maybe_continue.lower() == "return":
                    self.second_menu()
                    break
                else:
                    self.bets_made = {}
                    BETS_DONE = False

            elif self.bets_made != {}:
                print(f"You Lost the number chosen was {random_number}, new balance: {self.balance:,}")
                maybe_continue = input("Press any Key to continue with a new game!\nType \"return\" to return to the previous menu!: ")
                if maybe_continue.lower() == "return":
                    self.second_menu()
                    break
                else:
                    self.bets_made = {}
                    BETS_DONE = False    
            else:
                maybe_continue = input("You did\'t make any bets!\nType \"return\" to return to the previous menu!\nPress any Key to start a new game!: ")
                if maybe_continue.lower() == "return":
                    self.second_menu()
                    break
                else:
                    self.bets_made = {}
                    BETS_DONE = False

MainGame()
