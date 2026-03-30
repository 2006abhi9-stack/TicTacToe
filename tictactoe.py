board = [[1, 1, 1],
         [1, 1, 1],
         [1, 1, 1]]
 
game_over = False
 
print("Welcome to Tic Tac Toe!")
print("You are X and the computer is O")
print()
print("Positions:")
print("1 | 2 | 3")
print("--+---+--")
print("4 | 5 | 6")
print("--+---+--")
print("7 | 8 | 9")
 
while game_over == False:
 
    print()
    if board[0][0] == 1:
        r0c0 = " "
    elif board[0][0] == 2:
        r0c0 = "X"
    else:
        r0c0 = "O"
 
    if board[0][1] == 1:
        r0c1 = " "
    elif board[0][1] == 2:
        r0c1 = "X"
    else:
        r0c1 = "O"
 
    if board[0][2] == 1:
        r0c2 = " "
    elif board[0][2] == 2:
        r0c2 = "X"
    else:
        r0c2 = "O"
 
    if board[1][0] == 1:
        r1c0 = " "
    elif board[1][0] == 2:
        r1c0 = "X"
    else:
        r1c0 = "O"
 
    if board[1][1] == 1:
        r1c1 = " "
    elif board[1][1] == 2:
        r1c1 = "X"
    else:
        r1c1 = "O"
 
    if board[1][2] == 1:
        r1c2 = " "
    elif board[1][2] == 2:
        r1c2 = "X"
    else:
        r1c2 = "O"
 
    if board[2][0] == 1:
        r2c0 = " "
    elif board[2][0] == 2:
        r2c0 = "X"
    else:
        r2c0 = "O"
 
    if board[2][1] == 1:
        r2c1 = " "
    elif board[2][1] == 2:
        r2c1 = "X"
    else:
        r2c1 = "O"
 
    if board[2][2] == 1:
        r2c2 = " "
    elif board[2][2] == 2:
        r2c2 = "X"
    else:
        r2c2 = "O"
 
    print(r0c0 + " | " + r0c1 + " | " + r0c2)
    print("--+---+--")
    print(r1c0 + " | " + r1c1 + " | " + r1c2)
    print("--+---+--")
    print(r2c0 + " | " + r2c1 + " | " + r2c2)
    print()
 
    move = input("Enter your move (1-9): ")
 
    if move == "1":
        if board[0][0] == 1:
            board[0][0] = 2
        else:
            print("That spot is taken! Try again.")
            continue
    elif move == "2":
        if board[0][1] == 1:
            board[0][1] = 2
        else:
            print("That spot is taken! Try again.")
            continue
    elif move == "3":
        if board[0][2] == 1:
            board[0][2] = 2
        else:
            print("That spot is taken! Try again.")
            continue
    elif move == "4":
        if board[1][0] == 1:
            board[1][0] = 2
        else:
            print("That spot is taken! Try again.")
            continue
    elif move == "5":
        if board[1][1] == 1:
            board[1][1] = 2
        else:
            print("That spot is taken! Try again.")
            continue
    elif move == "6":
        if board[1][2] == 1:
            board[1][2] = 2
        else:
            print("That spot is taken! Try again.")
            continue
    elif move == "7":
        if board[2][0] == 1:
            board[2][0] = 2
        else:
            print("That spot is taken! Try again.")
            continue
    elif move == "8":
        if board[2][1] == 1:
            board[2][1] = 2
        else:
            print("That spot is taken! Try again.")
            continue
    elif move == "9":
        if board[2][2] == 1:
            board[2][2] = 2
        else:
            print("That spot is taken! Try again.")
            continue
    else:
        print("Invalid input! Enter a number from 1 to 9.")
        continue
 
    if board[0][0] == 2 and board[0][1] == 2 and board[0][2] == 2:
        game_over = True
    elif board[1][0] == 2 and board[1][1] == 2 and board[1][2] == 2:
        game_over = True
    elif board[2][0] == 2 and board[2][1] == 2 and board[2][2] == 2:
        game_over = True
    elif board[0][0] == 2 and board[1][0] == 2 and board[2][0] == 2:
        game_over = True
    elif board[0][1] == 2 and board[1][1] == 2 and board[2][1] == 2:
        game_over = True
    elif board[0][2] == 2 and board[1][2] == 2 and board[2][2] == 2:
        game_over = True
    elif board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2:
        game_over = True
    elif board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 2:
        game_over = True
 
    if game_over == True:
        print()
        if board[0][0] == 1:
            r0c0 = " "
        elif board[0][0] == 2:
            r0c0 = "X"
        else:
            r0c0 = "O"
        if board[0][1] == 1:
            r0c1 = " "
        elif board[0][1] == 2:
            r0c1 = "X"
        else:
            r0c1 = "O"
        if board[0][2] == 1:
            r0c2 = " "
        elif board[0][2] == 2:
            r0c2 = "X"
        else:
            r0c2 = "O"
        if board[1][0] == 1:
            r1c0 = " "
        elif board[1][0] == 2:
            r1c0 = "X"
        else:
            r1c0 = "O"
        if board[1][1] == 1:
            r1c1 = " "
        elif board[1][1] == 2:
            r1c1 = "X"
        else:
            r1c1 = "O"
        if board[1][2] == 1:
            r1c2 = " "
        elif board[1][2] == 2:
            r1c2 = "X"
        else:
            r1c2 = "O"
        if board[2][0] == 1:
            r2c0 = " "
        elif board[2][0] == 2:
            r2c0 = "X"
        else:
            r2c0 = "O"
        if board[2][1] == 1:
            r2c1 = " "
        elif board[2][1] == 2:
            r2c1 = "X"
        else:
            r2c1 = "O"
        if board[2][2] == 1:
            r2c2 = " "
        elif board[2][2] == 2:
            r2c2 = "X"
        else:
            r2c2 = "O"
        print(r0c0 + " | " + r0c1 + " | " + r0c2)
        print("--+---+--")
        print(r1c0 + " | " + r1c1 + " | " + r1c2)
        print("--+---+--")
        print(r2c0 + " | " + r2c1 + " | " + r2c2)
        print()
        print("You win! Congratulations!")
        break
 
    draw = True
    if board[0][0] == 1:
        draw = False
    elif board[0][1] == 1:
        draw = False
    elif board[0][2] == 1:
        draw = False
    elif board[1][0] == 1:
        draw = False
    elif board[1][1] == 1:
        draw = False
    elif board[1][2] == 1:
        draw = False
    elif board[2][0] == 1:
        draw = False
    elif board[2][1] == 1:
        draw = False
    elif board[2][2] == 1:
        draw = False
 
    if draw == True:
        print()
        print(r0c0 + " | " + r0c1 + " | " + r0c2)
        print("--+---+--")
        print(r1c0 + " | " + r1c1 + " | " + r1c2)
        print("--+---+--")
        print(r2c0 + " | " + r2c1 + " | " + r2c2)
        print()
        print("Its a draw!")
        break
 
    print("Computer is thinking...")
 
    if board[0][0] == 0 and board[0][1] == 0 and board[0][2] == 1:
        board[0][2] = 0
    elif board[0][0] == 0 and board[0][2] == 0 and board[0][1] == 1:
        board[0][1] = 0
    elif board[0][1] == 0 and board[0][2] == 0 and board[0][0] == 1:
        board[0][0] = 0
    elif board[1][0] == 0 and board[1][1] == 0 and board[1][2] == 1:
        board[1][2] = 0
    elif board[1][0] == 0 and board[1][2] == 0 and board[1][1] == 1:
        board[1][1] = 0
    elif board[1][1] == 0 and board[1][2] == 0 and board[1][0] == 1:
        board[1][0] = 0
    elif board[2][0] == 0 and board[2][1] == 0 and board[2][2] == 1:
        board[2][2] = 0
    elif board[2][0] == 0 and board[2][2] == 0 and board[2][1] == 1:
        board[2][1] = 0
    elif board[2][1] == 0 and board[2][2] == 0 and board[2][0] == 1:
        board[2][0] = 0
    elif board[0][0] == 0 and board[1][0] == 0 and board[2][0] == 1:
        board[2][0] = 0
    elif board[0][0] == 0 and board[2][0] == 0 and board[1][0] == 1:
        board[1][0] = 0
    elif board[1][0] == 0 and board[2][0] == 0 and board[0][0] == 1:
        board[0][0] = 0
    elif board[0][1] == 0 and board[1][1] == 0 and board[2][1] == 1:
        board[2][1] = 0
    elif board[0][1] == 0 and board[2][1] == 0 and board[1][1] == 1:
        board[1][1] = 0
    elif board[1][1] == 0 and board[2][1] == 0 and board[0][1] == 1:
        board[0][1] = 0
    elif board[0][2] == 0 and board[1][2] == 0 and board[2][2] == 1:
        board[2][2] = 0
    elif board[0][2] == 0 and board[2][2] == 0 and board[1][2] == 1:
        board[1][2] = 0
    elif board[1][2] == 0 and board[2][2] == 0 and board[0][2] == 1:
        board[0][2] = 0
    elif board[0][0] == 0 and board[1][1] == 0 and board[2][2] == 1:
        board[2][2] = 0
    elif board[0][0] == 0 and board[2][2] == 0 and board[1][1] == 1:
        board[1][1] = 0
    elif board[1][1] == 0 and board[2][2] == 0 and board[0][0] == 1:
        board[0][0] = 0
    elif board[0][2] == 0 and board[1][1] == 0 and board[2][0] == 1:
        board[2][0] = 0
    elif board[0][2] == 0 and board[2][0] == 0 and board[1][1] == 1:
        board[1][1] = 0
    elif board[1][1] == 0 and board[2][0] == 0 and board[0][2] == 1:
        board[0][2] = 0
    elif board[0][0] == 2 and board[0][1] == 2 and board[0][2] == 1:
        board[0][2] = 0
    elif board[0][0] == 2 and board[0][2] == 2 and board[0][1] == 1:
        board[0][1] = 0
    elif board[0][1] == 2 and board[0][2] == 2 and board[0][0] == 1:
        board[0][0] = 0
    elif board[1][0] == 2 and board[1][1] == 2 and board[1][2] == 1:
        board[1][2] = 0
    elif board[1][0] == 2 and board[1][2] == 2 and board[1][1] == 1:
        board[1][1] = 0
    elif board[1][1] == 2 and board[1][2] == 2 and board[1][0] == 1:
        board[1][0] = 0
    elif board[2][0] == 2 and board[2][1] == 2 and board[2][2] == 1:
        board[2][2] = 0
    elif board[2][0] == 2 and board[2][2] == 2 and board[2][1] == 1:
        board[2][1] = 0
    elif board[2][1] == 2 and board[2][2] == 2 and board[2][0] == 1:
        board[2][0] = 0
    elif board[0][0] == 2 and board[1][0] == 2 and board[2][0] == 1:
        board[2][0] = 0
    elif board[0][0] == 2 and board[2][0] == 2 and board[1][0] == 1:
        board[1][0] = 0
    elif board[1][0] == 2 and board[2][0] == 2 and board[0][0] == 1:
        board[0][0] = 0
    elif board[0][1] == 2 and board[1][1] == 2 and board[2][1] == 1:
        board[2][1] = 0
    elif board[0][1] == 2 and board[2][1] == 2 and board[1][1] == 1:
        board[1][1] = 0
    elif board[1][1] == 2 and board[2][1] == 2 and board[0][1] == 1:
        board[0][1] = 0
    elif board[0][2] == 2 and board[1][2] == 2 and board[2][2] == 1:
        board[2][2] = 0
    elif board[0][2] == 2 and board[2][2] == 2 and board[1][2] == 1:
        board[1][2] = 0
    elif board[1][2] == 2 and board[2][2] == 2 and board[0][2] == 1:
        board[0][2] = 0
    elif board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 1:
        board[2][2] = 0
    elif board[0][0] == 2 and board[2][2] == 2 and board[1][1] == 1:
        board[1][1] = 0
    elif board[1][1] == 2 and board[2][2] == 2 and board[0][0] == 1:
        board[0][0] = 0
    elif board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 1:
        board[2][0] = 0
    elif board[0][2] == 2 and board[2][0] == 2 and board[1][1] == 1:
        board[1][1] = 0
    elif board[1][1] == 2 and board[2][0] == 2 and board[0][2] == 1:
        board[0][2] = 0
    elif board[1][1] == 1:
        board[1][1] = 0
    elif board[0][0] == 1:
        board[0][0] = 0
    elif board[0][2] == 1:
        board[0][2] = 0
    elif board[2][0] == 1:
        board[2][0] = 0
    elif board[2][2] == 1:
        board[2][2] = 0
    elif board[0][1] == 1:
        board[0][1] = 0
    elif board[1][0] == 1:
        board[1][0] = 0
    elif board[1][2] == 1:
        board[1][2] = 0
    elif board[2][1] == 1:
        board[2][1] = 0
 
    if board[0][0] == 0 and board[0][1] == 0 and board[0][2] == 0:
        game_over = True
    elif board[1][0] == 0 and board[1][1] == 0 and board[1][2] == 0:
        game_over = True
    elif board[2][0] == 0 and board[2][1] == 0 and board[2][2] == 0:
        game_over = True
    elif board[0][0] == 0 and board[1][0] == 0 and board[2][0] == 0:
        game_over = True
    elif board[0][1] == 0 and board[1][1] == 0 and board[2][1] == 0:
        game_over = True
    elif board[0][2] == 0 and board[1][2] == 0 and board[2][2] == 0:
        game_over = True
    elif board[0][0] == 0 and board[1][1] == 0 and board[2][2] == 0:
        game_over = True
    elif board[0][2] == 0 and board[1][1] == 0 and board[2][0] == 0:
        game_over = True
 
    if game_over == True:
        print()
        if board[0][0] == 1:
            r0c0 = " "
        elif board[0][0] == 2:
            r0c0 = "X"
        else:
            r0c0 = "O"
        if board[0][1] == 1:
            r0c1 = " "
        elif board[0][1] == 2:
            r0c1 = "X"
        else:
            r0c1 = "O"
        if board[0][2] == 1:
            r0c2 = " "
        elif board[0][2] == 2:
            r0c2 = "X"
        else:
            r0c2 = "O"
        if board[1][0] == 1:
            r1c0 = " "
        elif board[1][0] == 2:
            r1c0 = "X"
        else:
            r1c0 = "O"
        if board[1][1] == 1:
            r1c1 = " "
        elif board[1][1] == 2:
            r1c1 = "X"
        else:
            r1c1 = "O"
        if board[1][2] == 1:
            r1c2 = " "
        elif board[1][2] == 2:
            r1c2 = "X"
        else:
            r1c2 = "O"
        if board[2][0] == 1:
            r2c0 = " "
        elif board[2][0] == 2:
            r2c0 = "X"
        else:
            r2c0 = "O"
        if board[2][1] == 1:
            r2c1 = " "
        elif board[2][1] == 2:
            r2c1 = "X"
        else:
            r2c1 = "O"
        if board[2][2] == 1:
            r2c2 = " "
        elif board[2][2] == 2:
            r2c2 = "X"
        else:
            r2c2 = "O"
        print(r0c0 + " | " + r0c1 + " | " + r0c2)
        print("--+---+--")
        print(r1c0 + " | " + r1c1 + " | " + r1c2)
        print("--+---+--")
        print(r2c0 + " | " + r2c1 + " | " + r2c2)
        print()
        print("Computer wins! Better luck next time.")
        break