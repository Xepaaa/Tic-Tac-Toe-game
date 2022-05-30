# Tic-Tac-Toe-game
.
# Project Notes

This project was proposed as part of jose's udemy course, my version varies a little its more personalised and contains a few quirks
I really enjoyed this project as there were many interacting functions and many variables to be aware of.

I have left notes next to all if not most funtions in the actual code to explain the rationale and what it does.

wrt. thoughts and notes after the project had been completed >>>

Regarding a few challenges:

wrt. getting the names for the players as part of the first function (welcome_message()), i ran into an error which took me a while to pick up on
and it was the fact that if the same name had been input twice, the program would fail to make it player 2's turn. This initially occurred as,
when i was testing my code i was just pressing random buttons on the keypad to run through the program, therefore i didn't realise i was putting in
the same name most commonly being (sdf) XD. Upon figuring out what was going on, i decided to separate the "while" loop that requests the players
name and wrote conditional statements to ensure that the same name wouldn't be entered twice.

For the player_choice() function, there is something i did not manage to fix which is the following, upon entering a integer value thats outside of the
range(1,10) i would get the following error; IndexError: list index out of range. Additionally, entering a str value for in for this function would
give the following error; ValueError: invalid literal for int() with base 10. I tried to correct the errors by converting the values accepted into strings
then converting them into integers before passing them back to the board, however this was also unaccepted and i would receive the following error: 
TypeError: list indices must be integers or slices, not str. Hence, the code is best left as it is, unfortunately its not unbreakable but hopefully
players only input values within the specified range (1-9).

It's been alot of fun on creating this game, and i look forward to making more :)



Edit:

Sooo, upon learning about errors and exceptions handling i realised that i could edit and correct the issues i had with the aforementioned player_choice() function.
Using the new methods that i learned, i found a way to manage the ValueError which was if a user input a str as opposed to an int.
Regarding the IndexError, i had to eliminate one conditional statement, however, this wasn't of concern as i covered the condition with an else statement.
the amended function is shown as follows:

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
    
I have uploaded the amended game file as well, called: "Tic Tac Toe - Unbreakable.py" as the game is now unbreakable :D
