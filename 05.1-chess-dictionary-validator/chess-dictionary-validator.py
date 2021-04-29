
def isValidChessBoard(board):

    totalWPiece = 0
    totalBPiece = 0
    wPawns = 0
    bPawns = 0
    wKingIsFound = False
    bKingIsFound = False

    for space, piece in board.items():

        # All pieces must be on a valid space from '1a' to '8h'
        if len(space) != 2 or space[0] not in '12345678' or space[1] not in 'abcdefgh':
            return False

        # The piece names begin with either a 'w' or 'b' to represent white or black
        if piece[0] not in 'wb':
            return False

        # Exactly one black king and exactly one white king
        if piece == 'wking':
            if wKingIsFound:
                return False
            wKingIsFound = True

        if piece == 'bking':
            if bKingIsFound:
                return False
            bKingIsFound = True

        # Each player can only have at most 16 pieces
        if piece[0] == 'w':
            totalWPiece += 1

        elif piece[0] == 'b':
            totalBPiece += 1

        if totalWPiece > 16 or totalBPiece > 16:
            return False

        #  Each player can only have at most 8 pawns
        if piece == 'wpawns':
            wPawns += 1
        elif piece == 'bpawns':
            bPawns += 1

        if wPawns > 8 or bPawns > 8:
            return False

    return True

# Testing the function
testBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

print(isValidChessBoard(testBoard))
