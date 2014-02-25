#!/usr/bin/python
import pieces
import board
import branch

foo = board.Board()

piece = pieces.Pawn()
print str(piece.points) + ": " + piece.name

foo.add_piece(piece)
bar = branch.Branch(piece, (1, 1))
foo.apply_branch(bar)

piece = pieces.Knight()
print str(piece.points) + ": " + piece.name

foo.add_piece(piece)
bar = branch.Branch(piece, (2, 2))
foo.apply_branch(bar)

piece = pieces.Bishop()
print str(piece.points) + ": " + piece.name

foo.add_piece(piece)
bar = branch.Branch(piece, (3, 3))
foo.apply_branch(bar)

piece = pieces.Rook()
print str(piece.points) + ": " + piece.name

foo.add_piece(piece)
bar = branch.Branch(piece, (4, 4))
foo.apply_branch(bar)

piece = pieces.Queen()
print str(piece.points) + ": " + piece.name

foo.add_piece(piece)
bar = branch.Branch(piece, (5, 5))
foo.apply_branch(bar)

spaz = board.Board()
spaz.add_piece(piece)

piece = pieces.King()
print str(piece.points) + ": " + piece.name

foo.add_piece(piece)
bar = branch.Branch(piece, (6, 6))
foo.apply_branch(bar)
bap = foo.create_branch_board(branch.Branch(piece, (7, 7)))
bap.add_piece(piece)

print foo.pieces
print bap.pieces
print foo.evaluate(0)
print foo.check_tile_empty((5,5))
print foo.check_tile_empty((5,3))

print foo.get_possible_moves(0)[0].pieces[(1,2)]

boards = [foo, spaz, bap]
boards.sort(key=board.Board.compare_board, reverse=True)

print boards[0].evaluate()
print boards[1].evaluate()
print boards[2].evaluate()

