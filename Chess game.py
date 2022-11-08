# Chess game by LZ

#################################################################################
# DO NOT USE DEBUG because some of the function is based on Exception Try/Catch #
#################################################################################

# type a 4 char long command with startpos and endpos to move piece
# char 0(letter a ~ h) and char 1(number 1 ~ 8): Start Pos
# char 2(letter a ~ h) and char 3(number 1 ~ 8): End Pos
# example:
# a2a4 will move piece at a2 to a4

from typing import List

# Board

# 1 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ \n 1st Rank(index 0 ~ 7)
# 2 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ \n 2nd Rank(index 9 ~ 16)
# 3 ⊙ ⊙ ⊙ ⊙ ⊙ ⊙ ⊙ ⊙ \n 3rd Rank(index 18 ~ 25)
# 4 ⊙ ⊙ ⊙ ⊙ ⊙ ⊙ ⊙ ⊙ \n 4th Rank(index 27 ~ 34)
# 5 ⊙ ⊙ ⊙ ⊙ ⊙ ⊙ ⊙ ⊙ \n 5th Rank(index 36 ~ 43)
# 6 ⊙ ⊙ ⊙ ⊙ ⊙ ⊙ ⊙ ⊙ \n 6th Rank(index 45 ~ 52)
# 7 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ \n 7th Rank(index 54 ~ 61)
# 8 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ \n 8th Rank(index 63 ~ 70)
#   a  b  c  d  e  f  g  h

# Because the board is a 9(8 files + \n) * 8(ranks) matrix
# so:
# move 1 square UP = index - 9
# move 1 square DOWN = index + 9
# move 1 square LEFT = index - 1
# move 1 square RIGHT = index + 1

# lower case = white
# UPPER CASE = BLACK
board = \
"""rnbqkbnr
pppppppp
........
........
........
........
PPPPPPPP
RNBQKBNR
"""
# Alternate board
board = \
"""rnbqkbnr
pppppppp
........
........
........
........
PPPPPPPP
RNBQKBNR
"""

running = True
player = "White"

print (""" Chess game by LZ
 1♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖
 2♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙
 3⊙ ⊙ ⊙ ⊙ ⊙ ⊙ ⊙ ⊙
 4⊙ ⊙ ⊙ ⊙ ⊙ ⊙ ⊙ ⊙
 5⊙ ⊙ ⊙ ⊙ ⊙ ⊙ ⊙ ⊙
 6⊙ ⊙ ⊙ ⊙ ⊙ ⊙ ⊙ ⊙
 7♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟
 8♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜
  a b c d e f g h
""")
wKingCastlingL = True
wKingCastlingR = True
bKingCastlingL = True
bKingCastlingR = True

while running:
    # Logic #
    try:
        tempboard = board
        ValidMoveIndex = list()

        # Input #
        command = input(player + " move:")
        coords = command[0].lower().replace("a", "1").replace("b", "2").replace("c", "3").replace("d", "4").replace("e", "5").replace("f", "6").replace("g", "7").replace("h", "8") + command[1]
        tgt = command[2].lower().replace("a", "1").replace("b", "2").replace("c", "3").replace("d", "4").replace("e", "5").replace("f", "6").replace("g", "7").replace("h", "8") + command[3]
        index = (int(coords[0]) + (int(coords[1])-1) * 9) - 1
        tgtindex = (int(tgt[0]) + (int(tgt[1])-1) * 9) - 1

        # Behavior #
        if board[index] == ".":
            print ("There is no piece in " + command[0] + command[1])
            raise Exception("no piece")

        # PAWN BEHAVIOR
        # move forward to the unoccupied square in front of it on the same file
        # on its first move it can advance two unoccupied squares along the same file 
        # can capture an opponent's piece on a square diagonally in front of it by moving to that square

        if board[index] == "p": # White pawn
            if player == "Black":
                print ("Cannot move white piece")
                raise Exception("wrong piece")
            enpassantR = False
            enpassantL = False
            promotion = False
            if board[index + 9] == ".":
                # Move forward
                ValidMoveIndex.append(index + 9)
                if (index <= 17 and board[index + 18] == "."):
                    #Advance
                    ValidMoveIndex.append(index + 18)
            if board[index + 10] != "." and board[index + 10].isupper():
                # Capture(R)
                ValidMoveIndex.append(index + 10)
            if board[index + 8] != "." and board[index + 8].isupper():
                # Capture(L)
                ValidMoveIndex.append(index + 8)

        # EN PASSANT CAPTURE
        # When a pawn makes a two-step advance from its starting position 
        # and there is an opponent's pawn on a square next to the destination square on an adjacent file
        # then the opponent's pawn can capture it en passant ("in passing"), moving to the square the pawn passed over. 
        # This can be done only on the turn immediately following the enemy pawn's two-square advance;

            if (index <= 44 and board[index + 1] == "P" and lastboard[index + 19] == "P" and board[index + 19] == ".") : 
                # pawn at 5th rank or lower 
                # && opponent's pawn is next to this pawn 
                # && opponent's pawn is 2 square forward and 1 square left/right at last step
                # && there's no opponent's pawn 2 square forward and 1 square left/right 

                # En Passant(R)
                ValidMoveIndex.append(index + 10)
                enpassantR = True
            if (index <= 44 and board[index - 1] == "P" and lastboard[index + 17] == "P" and board[index + 17] == ".") :
                # En Passant(L)
                ValidMoveIndex.append(index + 8)
                enpassantL = True

        # PROMOTION
        # When a pawn advances to its eighth(or first) rank, it will be promoted to a queen
        # Underpromotion is currently work in progress
            if (tgtindex >= 62): # pawn at 8th rank
                promotion = True

            #Movement and Validation
            if tgtindex in ValidMoveIndex:
                tempboard = tempboard[:index] + "." + tempboard[index + 1:]
                tempboard = tempboard[:tgtindex] + "p" + tempboard[tgtindex + 1:]
                if (enpassantR and tgtindex == index + 10):
                    tempboard = tempboard[:index + 1] + "." + tempboard[index + 2:]
                if (enpassantL and tgtindex == index + 8):
                    tempboard = tempboard[:index - 1] + "." + tempboard[index:]
                if (promotion):
                    tempboard = tempboard[:tgtindex] + "q" + tempboard[tgtindex + 1:]
            else:
                print ("Cannot move to " + command[2] + command[3])
                raise Exception("Cannot move piece")

            print ("\n\n\n\n\n" + player + " moved " + "♙ " + " from " + command[0] + command[1] + " to " + command[2] + command[3])
        
        if board[index] == "P": # Black pawn
            if player == "White":
                print ("Cannot move black piece")
                raise Exception("wrong piece")
            enpassantR = False
            enpassantL = False
            promotion = False
            if board[index - 9] == ".":
                # Move forward
                ValidMoveIndex.append(index - 9)
                if (index >= 54 and board[index - 18] == "."):
                    #Advance
                    ValidMoveIndex.append(index - 18)
            if board[index - 10] != "." and board[index - 10].islower():
                # Capture(L)
                ValidMoveIndex.append(index - 10)
            if board[index - 8] != "." and board[index - 8].islower():
                # Capture(R)
                ValidMoveIndex.append(index - 8)

        # EN PASSANT CAPTURE

            if (index <= 35 and board[index - 1] == "p" and lastboard[index - 19] == "p" and board[index - 19] == ".") : 
                # pawn at 4th rank or higher 
                # && opponent's pawn is next to this pawn 
                # && opponent's pawn is 2 square forward and 1 square left/right at last step
                # && there's no opponent's pawn 2 square forward and 1 square left/right

                # En Passant(L)
                ValidMoveIndex.append(index - 10)
                enpassantL = True
            if (index <= 35 and board[index + 1] == "p" and lastboard[index - 17] == "p" and board[index - 17] == ".") :
                # En Passant(R)
                ValidMoveIndex.append(index - 8)
                enpassantR = True

        # PROMOTION
            if (tgtindex <= 7): # pawn at 1st rank
                promotion = True


            #Movement and Validation
            if tgtindex in ValidMoveIndex:
                tempboard = tempboard[:index] + "." + tempboard[index + 1:]
                tempboard = tempboard[:tgtindex] + "P" + tempboard[tgtindex + 1:]
                if (enpassantR and tgtindex == index - 8):
                    tempboard = tempboard[:index + 1] + "." + tempboard[index + 2:]
                if (enpassantL and tgtindex == index - 10):
                    tempboard = tempboard[:index - 1] + "." + tempboard[index:]
                if (promotion):
                    tempboard = tempboard[:tgtindex] + "Q" + tempboard[tgtindex + 1:]
            else:
                print ("Cannot move to " + command[2] + command[3])
                raise Exception("Cannot move piece")
            print ("\n\n\n\n\n" + player + " moved " + "♟ " + " from " + command[0] + command[1] + " to " + command[2] + command[3])

        # KNIGHT BEHAVIOR
        # moves to any of the closest squares that are not on the same rank, file, or diagonal

        if board[index].lower() == "n": # Knight 
            if player == "Black" and board[index].islower():
                print ("Cannot move white piece")
                raise Exception("wrong piece")
            if player == "White" and board[index].isupper():
                print ("Cannot move black piece")
                raise Exception("wrong piece")
            if board[index] == "n":
                piece = "♘ "
            else:
                piece = "♞ "

            # Vertical L Move
            if index - 19 > 0:
                if board[index - 19] == "." \
                    or (board[index - 19].isupper() and player == "White") \
                    or (board[index - 19].islower() and player == "Black"):
                    ValidMoveIndex.append(index - 19)
            if index - 17 > 0:
                if board[index - 17] == "." \
                    or (board[index - 17].isupper() and player == "White") \
                    or (board[index - 17].islower() and player == "Black"):
                    ValidMoveIndex.append(index - 17)
            if index + 19 < len(board):
                if board[index + 19] == "." \
                    or (board[index + 19].isupper() and player == "White") \
                    or (board[index + 19].islower() and player == "Black"):
                    ValidMoveIndex.append(index + 19)
            if index + 17 < len(board):
                if board[index + 17] == "." \
                    or (board[index + 17].isupper() and player == "White") \
                    or (board[index + 17].islower() and player == "Black"):
                    ValidMoveIndex.append(index + 17)

            # Horizontal L Move
            if (board[index - 1] != "\n"):
                if index - 11 > 0:
                    if board[index - 11] == "." \
                        or (board[index - 11].isupper() and player == "White") \
                        or (board[index - 11].islower() and player == "Black"):
                        ValidMoveIndex.append(index - 11)
                if index + 7 < len(board):
                    if board[index + 7] == "." \
                        or (board[index + 7].isupper() and player == "White") \
                        or (board[index + 7].islower() and player == "Black"):
                        ValidMoveIndex.append(index + 7)
            if (board[index + 1] != "\n"):
                if index - 7 > 0:
                    if board[index - 7] == "." \
                        or (board[index - 7].isupper() and player == "White") \
                        or (board[index - 7].islower() and player == "Black"):
                        ValidMoveIndex.append(index - 7)
                if index + 11 < len(board):
                    if board[index + 11] == "." \
                        or (board[index + 11].isupper() and player == "White") \
                        or (board[index + 11].islower() and player == "Black"):
                        ValidMoveIndex.append(index + 11)

            #Movement and Validation
            if tgtindex in ValidMoveIndex:
                tempboard = tempboard[:index] + "." + tempboard[index + 1:]
                tempboard = tempboard[:tgtindex] + board[index] + tempboard[tgtindex + 1:]

            else:
                print ("Cannot move to " + command[2] + command[3])
                raise Exception("Cannot move piece")

            print ("\n\n\n\n\n" + player + " moved " + piece + " from " + command[0] + command[1] + " to " + command[2] + command[3])


        # QUEEN, ROOK AND BISHOP BEHAVIOR
        # move any number of squares along a rank/file, diagonal, or both 
        # cannot leap over other pieces

        if board[index].lower() == "q" or board[index].lower() == "r" or board[index].lower() == "b" : # Queen, rook or bishop
            if player == "Black" and board[index].islower():
                print ("Cannot move white piece")
                raise Exception("wrong piece")
            if player == "White" and board[index].isupper():
                print ("Cannot move black piece")
                raise Exception("wrong piece")
            if board[index] == "q":
                piece = "♕ "
            elif board[index] == "r":
                piece = "♖ "
            elif board[index] == "b":
                piece = "♗ "
            elif board[index] == "Q":
                piece = "♛ "
            elif board[index] == "R":
                piece = "♜ "
            elif board[index] == "B":
                piece = "♝ "

            if board[index] != "b" and board[index] != "B":
                for x in range(7):
                # Move UP
                    if index - (x + 1) * 9 < len(board):
                        if index - (x + 1) * 9 < len(board) and board[index - (x + 1) * 9] == ".":
                            ValidMoveIndex.append(index - (x + 1) * 9)
                            continue
                        elif (board[index - (x + 1) * 9].isupper() and player == "White") or (board[index - (x + 1) * 9].islower() and player == "Black"):
                            ValidMoveIndex.append(index - (x + 1) * 9)
                            break
                        else:
                            break

            # Move DOWN
                for x in range(7):
                    if index + (x + 1) * 9 < len(board):
                        if index + (x + 1) * 9 < len(board) and board[index + (x + 1) * 9] == ".":
                            ValidMoveIndex.append(index + (x + 1) * 9)
                            continue
                        elif (board[index + (x + 1) * 9].isupper() and player == "White") or (board[index + (x + 1) * 9].islower() and player == "Black"):
                            ValidMoveIndex.append(index + (x + 1) * 9)
                            break
                        else:
                            break

            # Move LEFT
                for x in range(7):
                    if index - (x + 1) < len(board):
                        if index - (x + 1) < len(board) and board[index - (x + 1)] == ".":
                            ValidMoveIndex.append(index - (x + 1))
                            continue
                        elif (board[index - (x + 1)].isupper() and player == "White") or (board[index - (x + 1)].islower() and player == "Black"):
                            ValidMoveIndex.append(index - (x + 1))
                            break
                        else:
                            break

            # Move RIGHT
                for x in range(7):
                    if index + (x + 1) < len(board):
                        if index + (x + 1) < len(board) and board[index + (x + 1)] == ".":
                            ValidMoveIndex.append(index + (x + 1))
                            continue
                        elif (board[index + (x + 1)].isupper() and player == "White") or (board[index + (x + 1)].islower() and player == "Black"):
                            ValidMoveIndex.append(index + (x + 1))
                            break
                        else:
                            break

            if board[index] != "r" and board[index] != "R":
            # Move DIAGONALLY UP LEFT
                for x in range(7):
                    if index - (x + 1) * 10 < len(board):
                        if board[index - (x + 1) * 10] == ".":
                            ValidMoveIndex.append(index - (x + 1) * 10)
                            continue
                        elif (board[index - (x + 1) * 10].isupper() and player == "White") or (board[index - (x + 1) * 10].islower() and player == "Black"):
                            ValidMoveIndex.append(index - (x + 1) * 10)
                            break
                        else:
                            break
            # Move DIAGONALLY DOWN LEFT
                for x in range(7):
                    if index + (x + 1) * 8 < len(board):
                        if board[index + (x + 1) * 8] == ".":
                            ValidMoveIndex.append(index + (x + 1) * 8)
                            continue
                        elif (board[index + (x + 1) * 8].isupper() and player == "White") or (board[index + (x + 1) * 8].islower() and player == "Black"):
                            ValidMoveIndex.append(index + (x + 1) * 8)
                            break
                        else:
                            break
                for x in range(7):
            # Move DIAGONALLY UP RIGHT
                    if index - (x + 1) * 8 < len(board):
                        if board[index - (x + 1) * 8] == ".":
                            ValidMoveIndex.append(index - (x + 1) * 8)
                            continue
                        elif (board[index - (x + 1) * 8].isupper() and player == "White") or (board[index - (x + 1) * 8].islower() and player == "Black"):
                            ValidMoveIndex.append(index - (x + 1) * 8)
                            break
                        else:
                            break

            # Move DIAGONALLY DOWN RIGHT
                for x in range(7):
                    if index + (x + 1) * 10 < len(board):
                        if board[index + (x + 1) * 10] == ".":
                            ValidMoveIndex.append(index + (x + 1) * 10)
                            continue
                        elif (board[index + (x + 1) * 10].isupper() and player == "White") or (board[index + (x + 1) * 10].islower() and player == "Black"):
                            ValidMoveIndex.append(index + (x + 1) * 10)
                            break
                        else:
                            break


            #Movement and Validation
            if tgtindex in ValidMoveIndex:
                tempboard = tempboard[:index] + "." + tempboard[index + 1:]
                tempboard = tempboard[:tgtindex] + board[index] + tempboard[tgtindex + 1:]
                if board[0] == "r" :
                    wKingCastlingL = False
                if board[7] == "r" :
                    wKingCastlingR = False
                if board[63] == "R" :
                    bKingCastlingL = False
                if board[70] == "R" :
                    bKingCastlingR = False

            else:
                print ("Cannot move to " + command[2] + command[3])
                raise Exception("Cannot move piece")

            print ("\n\n\n\n\n" + player + " moved " + piece + " from " + command[0] + command[1] + " to " + command[2] + command[3])



        # KING BEHAVIOR
        # moves one square in any direction
        # Check/Checkmate is currently work in progress

        if board[index].lower() == "k": # King
            if player == "Black" and board[index].islower():
                print ("Cannot move white piece")
                raise Exception("wrong piece")
            if player == "White" and board[index].isupper():
                print ("Cannot move black piece")
                raise Exception("wrong piece")
            if board[index] == "k":
                piece = "♔ "
            else:
                piece = "♚ "

            possibleoffsets = (-9,9,-1,1,10,-10,8,-8)

            for x in range(7):
                if index + possibleoffsets[x] > 0 and index + possibleoffsets[x] < len(board):
                    if board[index + possibleoffsets[x]] == "." or (board[index + possibleoffsets[x]].isupper() and player == "White") or (board[index + possibleoffsets[x]].islower() and player == "Black"):
                        ValidMoveIndex.append(index + possibleoffsets[x])

            # Castling
            # Once per game, each king can move two squares toward a rook of the same color on the same rank
            # and then placing the rook on the square that the king crossed.
            
            if player == "White":
                if wKingCastlingL and board[1] == board[2] == board[3] == ".":
                    ValidMoveIndex.append(0)

                if wKingCastlingR and board[5] == board[6] == "." :
                    ValidMoveIndex.append(7)

            if player == "Black":
                if bKingCastlingL and board[64] == board[65] == board[66] == ".":
                    ValidMoveIndex.append(63)

                if bKingCastlingR and board[68] == board[69] == ".":
                    ValidMoveIndex.append(70)
            
            #Movement and Validation
            if tgtindex in ValidMoveIndex:
                tempboard = tempboard[:index] + "." + tempboard[index + 1:]  
                if board[tgtindex].lower() == "r":
                    if tgtindex == 0:
                        tempboard = tempboard[:2] + board[index] + tempboard[3:]
                        tempboard = tempboard[:tgtindex] + "." + tempboard[tgtindex + 1:]   
                        tempboard = tempboard[:index - 1] + board[tgtindex] + tempboard[index:]       
                    if tgtindex == 7:
                        tempboard = tempboard[:6] + board[index] + tempboard[7:]  
                        tempboard = tempboard[:tgtindex] + "." + tempboard[tgtindex + 1:]  
                        tempboard = tempboard[:index + 1] + board[tgtindex] + tempboard[index + 2:]  
                    if tgtindex == 63:
                        tempboard = tempboard[:65] + board[index] + tempboard[66:]     
                        tempboard = tempboard[:tgtindex] + "." + tempboard[tgtindex + 1:]   
                        tempboard = tempboard[:index - 1] + board[tgtindex] + tempboard[index:]  
                    if tgtindex == 70:
                        tempboard = tempboard[:69] + board[index] + tempboard[70:]  
                        tempboard = tempboard[:tgtindex] + "." + tempboard[tgtindex + 1:]  
                        tempboard = tempboard[:index + 1] + board[tgtindex] + tempboard[index + 2:] 
                else:                 
                    tempboard = tempboard[:tgtindex] + board[index] + tempboard[tgtindex + 1:]

                if(player == "White"):
                    wKingCastlingL = False
                    wKingCastlingL = False
                if(player == "Black"):
                    bKingCastlingL = False
                    bKingCastlingL = False
            else:
                print ("Cannot move to " + command[2] + command[3])
                raise Exception("Cannot move piece")

            print ("\n\n\n\n\n" + player + " moved " + piece + " from " + command[0] + command[1] + " to " + command[2] + command[3])

        if player == "Black":
            player = "White"
        else:
            player = "Black"
    except:
        print()
    else:
        lastboard = board
        board = tempboard


    # Display #
    board_display = """
 Chess game by LZ
 """
    i = 1
    while i < len(board):
        if i % 9 == 1:
            board_display += (str((i-1) / 9 +1))[0]
        board_display += (board[i-1]
            .replace("r", "♖")
            .replace("n", "♘")
            .replace("b", "♗")
            .replace("q", "♕")
            .replace("k", "♔")
            .replace("p", "♙")
            .replace("R", "♜")
            .replace("N", "♞")
            .replace("B", "♝")
            .replace("Q", "♛")
            .replace("K", "♚")
            .replace("P", "♟")
            .replace(".", "⊙")
             + " ")
        i += 1



    #print (lastboard)  
    #print (board)
    #print (ValidMoveIndex)

    print (board_display + "\n  a b c d e f g h")

    if not("k" in board):
        print ("\n    CHECKMATE!!!")
        print ("    Winner:Black")
        running = False
        break
    if not("K" in board):
        print ("\n    CHECKMATE!!!")
        print ("    Winner:White")
        running = False
        break