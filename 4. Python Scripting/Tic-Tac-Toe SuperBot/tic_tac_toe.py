import math
import os
import random


class TicTacToe:
    def reset_variable(self, ai: bool):
        if ai:
            player_list = ["Player 1", "Bot"]
            symbol_list = ["X", "O"]
            random.shuffle(player_list)
            self.players = {player_list[i]: symbol_list[i] for i in range(2)}
        else:
            self.players = {"Player 1": "X", "Player 2": "O"}
        self.winner = 0
        # Create the Board
        self.board = [i for i in range(1, 4)], [i for i in range(4, 7)], [i for i in range(7, 10)]

    # print the Board
    def print_board(self, board):
        for i in board:
            print(str(i[0]) + ' | ' + str(i[1]) + ' | ' + str(i[2]))
            if board.index(i) != 2:
                print("----------")

    # Get input from player
    def in_board(self, player, value):
        if player == "Bot":
            ai_choice = self.ai_computation()
            self.board[math.ceil(ai_choice / 3) - 1][ai_choice % 3 - 1] = value
        else:
            t = True
            # Allow players to choose again if wrong input
            while t:
                try:
                    player_input = int(input(f"{player}: You are {value} Please select a number from 1 - 9: "))
                    try:
                        # Check if it is already taken
                        if player_input not in self.board[math.ceil(player_input / 3) - 1]:
                            print("Sorry the spot has already been taken")
                        else:
                            self.board[math.ceil(player_input / 3) - 1][player_input % 3 - 1] = value
                            t = False
                    except IndexError:
                        print("Please enter a valid number")
                except ValueError:
                    print("Please enter a valid number")

    # Check for Wins
    def check_board(self, value):
        # Checking rows
        for row in self.board:
            if row.count(value) == 3:
                self.winner = 1

        # Checking columns
        for index in range(3):
            new_row = [self.board[rows][index] for rows in range(3)]
            if new_row.count(value) == 3:
                self.winner = 1

        # Checking diagonal
        first_diagonal = [self.board[index][index] for index in range(3)]
        second_diagonal = [self.board[index * -1][index - 1] for index in range(1, 4)]
        if first_diagonal.count(value) == 3:
            self.winner = 1

        if second_diagonal.count(value) == 3:
            self.winner = 1

        if self.winner == 0:
            self.winner = 2
            for row in self.board:
                for i in row:
                    if type(i) is int:
                        self.winner = 0
                        break
                if self.winner == 0:
                    break
        else:
            pass

    # Game Start
    def game(self, ai):
        os.system('cls')
        self.reset_variable(ai)
        game_is_running = True
        while game_is_running:
            turn = 0
            option = True
            while self.winner == 0:
                for key, values in self.players.items():
                    turn += 1
                    os.system('cls')
                    print(f"Turn: {turn}")
                    if key == "Bot":
                        pass
                    else:
                        self.print_board(self.board)
                    self.in_board(key, values)
                    self.check_board(values)
                    if self.winner > 0:
                        os.system('cls')
                        self.print_board(self.board)
                        if self.winner == 1:
                            print(f"{key} wins!")
                        else:
                            print("It is a draw")
                        break
            while option:
                user_input = input("Do you want to go again? Y/N: ").lower()
                if user_input == "n":
                    game_is_running = False
                    option = False

                elif user_input == "y":
                    option = False
                    self.reset_variable(ai)
                else:
                    print("Please select a valid option")

    def start_game(self):
        if input("Play with a player or against a bot? (player/bot): ").lower() == "player":
            self.game(ai=False)
        else:
            self.game(ai=True)

    # Testing for AI

    def ai_computation(self):
        # get the full tuple in one list
        vertical_board = [i for row in self.board for i in row]
        # Get available number from the board
        board = [i for row in self.board for i in row if type(i) == int]
        # Super bot wins or draw if bot starts first if sequence is correct
        # Always start in corner if bot starts first
        if list(map(type, vertical_board)).count(str) == 0:
            return random.choice([1, 7, 3, 9])
        # To determine that bot is indeed the leading player
        if vertical_board.count(self.players["Bot"]) == vertical_board.count(self.players["Player 1"]):
            # Find the index of the first move
            if vertical_board.count(self.players["Bot"]) == 1:
                first_move_index = vertical_board.index(self.players["Bot"])
                for i in range(1, 8, 2):
                    if vertical_board[i] == self.players["Player 1"]:
                        return 5
                if vertical_board[(first_move_index+8)-(first_move_index*2)] == self.players["Player 1"]:
                    return 5
                else:
                    return vertical_board[(first_move_index+8)-(first_move_index*2)]
            elif vertical_board.count(self.players["Bot"]) == 2:
                for i in range(0, 9, 2):
                    if i == 4:
                        continue
                    if vertical_board[i] == self.players["Bot"]:
                        first_move_num = i+1

                row_of_first_move = math.ceil(first_move_num / 3) - 1
                index_of_first_move = first_move_num % 3 - 1
                column_of_first_move = [self.board[rows][index_of_first_move] for rows in range(3)]
                if vertical_board[4] == self.players["Bot"] and self.defend_against("Bot") is None and self.defend_against("Player 1") is None:
                    # row of first_move consist player or not
                    if self.board[row_of_first_move].count(self.players["Player 1"]) == 1:
                        if row_of_first_move >= 0:
                            return self.board[(row_of_first_move+2) - (row_of_first_move*2)][index_of_first_move]
                        else:
                            return self.board[(row_of_first_move+2) + (row_of_first_move*2)][index_of_first_move]
                    elif column_of_first_move.count(self.players["Player 1"]) == 1:
                        if index_of_first_move >= 0:
                            return self.board[row_of_first_move][(index_of_first_move+2) - (index_of_first_move*2)]
                        else:
                            return self.board[row_of_first_move][(index_of_first_move + 2) + (index_of_first_move * 2)]
                    else:
                        return self.bot_attack_defend(board)
                else:
                    return self.bot_attack_defend(board)

            else:
                return self.bot_attack_defend(board)

        # First move if player starts first is randomed
        else:
            return self.bot_attack_defend(board)

    def bot_attack_defend(self, board):
        if self.defend_against("Bot") is None:
            if self.defend_against("Player 1") is None:
                return random.choice(board)
            else:
                return self.defend_against("Player 1")

        else:
            return self.defend_against("Bot")

    # Defend against "player" can be used to find the best move to win
    def defend_against(self, player):
        # Checking rows to defend
        for row in self.board:
            if row.count(self.players[player]) == 2:
                for i in row:
                    if type(i) == int:
                        return i
                    else:
                        pass

        # Checking Columns to defend
        for index in range(3):
            new_row = [self.board[rows][index] for rows in range(3)]
            if new_row.count(self.players[player]) == 2:
                for i in new_row:
                    if type(i) == int:
                        return i
                    else:
                        pass

        # Checking diagonal to defend
        first_diagonal = [self.board[index][index] for index in range(3)]
        second_diagonal = [self.board[index * -1][index - 1] for index in range(1, 4)]
        if first_diagonal.count(self.players[player]) == 2:
            for i in first_diagonal:
                if type(i) == int:
                    return i
                else:
                    pass

        if second_diagonal.count(self.players[player]) == 2:
            for i in second_diagonal:
                if type(i) == int:
                    return i
                else:
                    pass

        return None
