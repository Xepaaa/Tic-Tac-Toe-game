# Tic Tac Toe

def welcome_message():
    print('\nWelcome to Tic Tac Toe')
    print('Find an opponent and challenge them for Victory!!!')
    print('\nYou will have to imagine the input for the Tic Tac Toe board corresponding to numbers on your numpad (1-9)')
    print('\n')
    
    P1 = 'A'
    P2 = 'B'
     
    while len(P1) < 2:
        P1 = input('\nPlayer 1, Please enter your name: ')
        if len(P1) < 2:
            print("\nSorry, that name doesn't meet the character limit!")
    while len(P2) < 2 or P1 == P2:
        P2 = input('\nPlayer 2, Please enter your name: ')
        if len(P2) < 2:
            print("\nSorry, that name doesn't meet the character limit!")
        elif P1 == P2:
        	print('\nSorry, that name is already taken... ')
        
    return(P1,P2)

'''
Series of print statements welcoming the player to the game, following on, an input for the names of player 1 and 2 respectively are requested
In final block of called as: P1,P2 = welcome_message()
'''

def display_board(board):
    
    print(' _______________________')
    print('|       |       |       |')
    print('|   '+board[7]+'   |   '+board[8]+'   |   '+board[9]+'   |')
    print('|_______|_______|_______|')
    print('|       |       |       |')
    print('|   '+board[4]+'   |   '+board[5]+'   |   '+board[6]+'   |')
    print('|_______|_______|_______|')
    print('|       |       |       |')
    print('|   '+board[1]+'   |   '+board[2]+'   |   '+board[3]+'   |')
    print('|_______|_______|_______|')

'''
Made this as the board for the tic tac toe game, decided to go with a fully enclosed board as it looks most aesthetic imo.
As can be seen, the the index for each postion are placed inside the print of the board, made the whole thing alot less tricky as opposed to using strings
only to be followed by the replace method.
'''

def first_player():
    # In the final block of code will be called by: turn = first_player()
    if random.randint(1,2) == 1:
        return P1
    else:
        return P2


def marker_assign():
	# In the final block of code will be called by: p1_marker,p2_marker = marker_assign()

    player1 = ''
    player2 = ''
    acceptable_parameters = ['X','O']
    
    
    while player1 not in acceptable_parameters:

        player1 = input('\n(Player 1) {} : Do you want to be an X or an O? '.format(P1)).upper()

        if player1 not in acceptable_parameters:
            print("\nThat's an incorrect selection, please choose either X or O")
        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'
            
            
    return(player1,player2)


def place_marker(board,marker,position):
    board[position] = marker

'''
 This function relates the board, marker and position, placing a marker of choice at that given position on the board
 In final block of code will be called by: place_marker(board, marker of respective player, chosen position)
'''

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) # across the top
           or (board[4] == mark and board[5] == mark and board[6] == mark) # across the middle
           or (board[1] == mark and board[2] == mark and board[3] == mark) # across the bottom
           or (board[7] == mark and board[4] == mark and board[1] == mark) # top left to bottom left
           or (board[8] == mark and board[5] == mark and board[2] == mark) # top to bottom middle
           or (board[9] == mark and board[6] == mark and board[3] == mark) # top right to bottom right
           or (board[7] == mark and board[5] == mark and board[3] == mark) # top left to bottom right
           or (board[9] == mark and board[5] == mark and board[1] == mark) # top right to bottom left
           )

'''
This function checks the board with respect to a marker to see if a player has won the game, as can be seen, the combination of every possible winning method is listed
In final block of code will be called by: win_check(board, marker of player)
'''

def space_check(board, position):
    
    if board[position] == ' ':
        return True
    else:
        return False


'''
This function returns a bool value, checks if a position on a board is free (' ').
In final block of code will be called by: space_check(board, chosen position)
'''

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

'''
This function also returns a bool value, but checks whether there are any spaces left on the entire board, uses the range
method to achieve this by going through numbers 1-10 which is corresponding to the list at time of play.
In final block of code will be called by: full_board_check(board)
'''

def player_choice(board):
    position = 0
    

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        try:
            position = int(input('\nChoose a position on the board between 1-9: '))
        except ValueError:
            print("\nSorry, thats an invalid choice! Please select a number between 1 and 9")
        if position not in range(1,10):
            print("\nSorry, that's out of range!")
        else:
            print("\nSorry, that position is already taken")
            
    return position


'''
This function asks a player to choose a position on the board at which they would like to place their marker, as mentioned in welcome_message(),
the numbers/positions correspond to how they would appear on a keybaords numpad.
In final block of code will be called by: player_choice(board)
'''


def play_again():
    
    choice = "NOTHINGCHIEF"
    acceptable_range = ['Y','N']
    
    while choice not in acceptable_range:
        
        choice = input('\nWould you like to play again (Y/N)? ').upper()
        
        if choice not in acceptable_range:
            print("\nSorry, i didn't quite get that, can you enter Y or N")
    
    return choice == "Y"

'''
Returns a bool value which can be used to determine if we break out of the while True loop or play it again
In final block of code will be called by: play_again()
'''

def randomiser_delay():
    print('Please hold while the Computer decides who goes first....')
    time.sleep(3)

'''
Just a little quirk to delay the game so that it doesnt feel rushed, would be even cooler if the ellipsis occurred one after the other with the passage of time
In final block of code will be called by: randomiser_delay()
'''

# So, to run the quiz >>>

import time
import random

P1,P2 = welcome_message()

while True: # "while true" loop in python runs without any conditions until the break statement executes inside the loop.
    board = [' ']*10 # Initially, the board is an empty list which will update as players input positions, the list is given a length of 10 as item number 0 cannot be a user’s choice.
    p1_marker,p2_marker = marker_assign()
    turn = first_player()
    print('\n')
    randomiser_delay()
    print('\n')
    print('The Computer has chosen, ' + turn + ' will go first!')
    print('\n')
    play_game = input('Are you ready to play? Enter Yes or No: ')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on == True:
        if turn == P1:
    
            display_board(board)
            print("\n{}'s Turn, your marker is {}".format(P1,p1_marker))
            position = player_choice(board)
            place_marker(board, p1_marker, position)

            if win_check(board, p1_marker):
                display_board(board)
                print('\nCongratulations {}, You have won the game!'.format(P1))
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('\nClose!, The game is a draw')
                    break
                else:
                    turn = P2

        else:

            display_board(board)
            print("\n{}'s Turn, your marker is {}".format(P2,p2_marker))
            position = player_choice(board)
            place_marker(board, p2_marker, position)

            if win_check(board, p2_marker):
                display_board(board)
                print('\nCongratulations {}, You have won the game!'.format(P2))
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('Good challenge! The game is a draw!')
                    break
                else:
                    turn = P1
    
    if not play_again():
        break



