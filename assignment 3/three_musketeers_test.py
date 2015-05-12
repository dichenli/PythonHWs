## Dichen Li and Matthias (Boon Liang) Chia
import unittest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

class TestThreeMusketeers(unittest.TestCase):

    def setUp(self):
        set_board([ [_, _, _, M, _],
                    [_, _, R, M, _],
                    [_, R, M, R, _],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ])

    def test_create_board(self):
        print "\ncreate_board"
        create_board()
        self.assertEqual(at((0, 0)), 'R')
        self.assertEqual(at((0, 4)), 'M')

    def test_set_board(self):
        print "\nset_board"
        self.assertEqual(at((0, 0)), '-')
        self.assertEqual(at((1, 2)), 'R')
        self.assertEqual(at((1, 3)), 'M')

    def test_get_board(self): 
        print "\nget_board"
        self.assertEqual([ [_, _, _, M, _],
                           [_, _, R, M, _],
                           [_, R, M, R, _],
                           [_, R, _, _, _],
                           [_, _, _, R, _] ],
                         get_board())

    def test_string_to_location(self): 
        print "\nstring_to_location"
        self.assertEqual((0, 4), string_to_location('A5'))
        self.assertEqual((2, 2), string_to_location('C3'))
        self.assertEqual((1, 3), string_to_location('B4'))
        self.assertEqual((3, 1), string_to_location('D2'))
        self.assertEqual((4, 0), string_to_location('E1'))
        self.assertRaises(AssertionError, string_to_location, 'A6')
        self.assertRaises(AssertionError, string_to_location, 'F1')
        self.assertRaises(AssertionError, string_to_location, '#.')
        
    def test_location_to_string(self):
        print "\nlocation_to_string"
        self.assertEqual(('A5'), location_to_string((0, 4)))
        self.assertEqual(('C3'), location_to_string((2, 2)))
        self.assertEqual(('B4'), location_to_string((1, 3)))
        self.assertEqual(('D2'), location_to_string((3, 1)))
        self.assertEqual(('E1'), location_to_string((4, 0)))
        self.assertRaises(AssertionError, location_to_string, 'A6')
        self.assertRaises(AssertionError, location_to_string, 'F1')
        self.assertRaises(AssertionError, location_to_string, '#.')

    def test_at(self):
        print "\ntest_at"
        self.assertEqual('M', at((0, 3)))
        self.assertEqual('-', at((1, 1)))
        self.assertEqual('R', at((1, 2)))
        self.assertEqual('M', at((2, 2)))
        self.assertEqual('-', at((4, 4)))

    def test_all_locations(self):
        print "\nall_locations"
        self.assertEqual([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)], all_locations())
        
    def test_adjacent_location(self):
        print "\nadjacent_location"
        self.assertEqual((0, 4), adjacent_location((0, 3), 'right'))
        self.assertEqual((0, 0), adjacent_location((0, 1), 'left'))
        self.assertEqual((0, 2), adjacent_location((1, 2), 'up'))
        self.assertEqual((4, 3), adjacent_location((3, 3), 'down'))
        
    def test_is_legal_move_by_musketeer(self):
        print "\ntest_is_legal_move_by_musketeer"
        self.assertEqual(False, is_legal_move_by_musketeer((0, 3),'down'))
        self.assertEqual(True, is_legal_move_by_musketeer((1, 3),'down'))
        self.assertEqual(False, is_legal_move_by_musketeer((1, 3),'right'))
        self.assertEqual(True, is_legal_move_by_musketeer((2, 2),'left'))
        self.assertEqual(False, is_legal_move_by_musketeer((2, 2),'down'))
        self.assertRaises(AssertionError, is_legal_move_by_musketeer, (0, 0), 'down')
        self.assertRaises(AssertionError, is_legal_move_by_musketeer, (0, 3), 'up')
        self.assertRaises(AssertionError, is_legal_move_by_musketeer, (-1, 3), 'down')
        self.assertRaises(AssertionError, is_legal_move_by_musketeer, (-1, 4), 'right')
        self.assertRaises(AssertionError, is_legal_move_by_musketeer, (1, 2), 'right')
        
    def test_is_legal_move_by_enemy(self):
        print "\ntest_is_legal_move_by_enemy"
        self.assertEqual(False, is_legal_move_by_enemy((1, 2),'down'))
        self.assertEqual(True, is_legal_move_by_enemy((2, 1),'left'))
        self.assertEqual(True, is_legal_move_by_enemy((2, 3),'right'))
        self.assertEqual(True, is_legal_move_by_enemy((4, 3),'up'))
        self.assertRaises(AssertionError, is_legal_move_by_enemy, (0, 3), 'up')
        self.assertRaises(AssertionError, is_legal_move_by_enemy, (0, 3), 'down')
        self.assertRaises(AssertionError, is_legal_move_by_enemy, (3, 3), 'down')
        self.assertRaises(AssertionError, is_legal_move_by_enemy, (-1, 3), 'down')

    def test_is_legal_move(self):
        print "\ntest_is_legal_move"
        self.assertEqual(False, is_legal_move((4, 3),'down'))
        self.assertEqual(True, is_legal_move((2, 1),'left'))
        self.assertEqual(True, is_legal_move((4, 3),'right'))
        self.assertEqual(False, is_legal_move((0, 1),'up'))
        self.assertEqual(False, is_legal_move((0, 3),'down'))
        self.assertEqual(True, is_legal_move((2, 2),'up'))

    def test_can_move_piece_at(self):
        print "\ncan_move_piece_at"
        self.assertEqual(True, can_move_piece_at((1, 2)))
        self.assertEqual(False, can_move_piece_at((1, 1)))
        self.assertEqual(False, can_move_piece_at((0, 3)))
        self.assertEqual(True, can_move_piece_at((1, 3)))
        self.assertEqual(False, can_move_piece_at((-1, 1)))
        self.assertEqual(False, can_move_piece_at((6, 5)))
        
    def test_has_some_legal_move_somewhere(self):
        print "\nhas_some_legal_move_somewhere"
        set_board([ [_, _, _, M, _],
                    [_, R, _, M, _],
                    [_, _, M, _, R],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ] )
        self.assertFalse(has_some_legal_move_somewhere('M'))
        self.assertTrue(has_some_legal_move_somewhere('R'))
        set_board([ [R, R, M, _, _],
                    [M, M, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertTrue(has_some_legal_move_somewhere('M'))
        self.assertFalse(has_some_legal_move_somewhere('R'))

    def test_possible_moves_from(self):
        print "\npossible_moves_from"
        self.assertEqual(['left', 'down'], possible_moves_from((1, 3)))
        self.assertEqual(['right', 'down'], possible_moves_from((2, 3)))
        self.assertEqual([], possible_moves_from((3, 4)))
        self.assertEqual([], possible_moves_from((0, 3)))
        
    def test_can_move_piece_at(self):
        print "\ncan_move_piece_at"
        set_board([ [_, _, _, M, R],
                    [_, _, _, M, M],
                    [_, _, R, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertTrue(can_move_piece_at((0, 3)))
        self.assertFalse(can_move_piece_at((0, 4)))
        self.assertTrue(can_move_piece_at((2, 2)))
        self.assertFalse(can_move_piece_at((1, 3)))
        self.assertFalse(can_move_piece_at((-1, 3)))
        self.assertFalse(can_move_piece_at((5, 7)))
        self.assertFalse(can_move_piece_at((0, 0)))
                
    def test_is_legal_location(self):
        print "\ntest_is_legal_location"
        self.assertEqual(True, is_legal_location((4, 3)))
        self.assertEqual(True, is_legal_location((0, 0)))
        self.assertEqual(False, is_legal_location((5, 4)))
        self.assertEqual(False, is_legal_location((0, -1)))
        self.assertEqual(False, is_legal_location((3, 6)))
                         
    def test_is_within_board(self):
        print "\nis_within_board"
        self.assertEqual(False, is_within_board((4, 3), 'down'))
        self.assertEqual(False, is_within_board((0, 0), 'up'))
        self.assertEqual(True, is_within_board((5, 4), 'up'))
        self.assertEqual(True, is_within_board((0, -1), 'right'))
        self.assertEqual(True, is_within_board((3, 2), 'left'))

    def test_all_possible_moves_for(self):
        print "\nall_possible_moves_for"
        set_board([ [_, _, R, M, R],
                    [_, _, _, M, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertEqual([((0, 3),'left'), ((0, 3),'right'), ((1, 4),'up')], all_possible_moves_for('M'))
        self.assertEqual([((0, 2),'left'), ((0, 2),'down')], all_possible_moves_for('R'))
        self.assertEqual([], all_possible_moves_for('r'))        
        set_board([ [_, _, _, M, R],
                    [_, _, _, M, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertEqual([((0, 3),'right'), ((1, 4),'up')], all_possible_moves_for('M'))
        self.assertEqual([], all_possible_moves_for('R'))
        
    def test_make_move(self): 
        print "\nmake_move"
        make_move((1, 3), 'left')
        current_board = get_board()
        self.assertEqual('M', current_board[1][2])
        self.assertEqual('-', current_board[1][3])
        make_move((4, 3), 'left')
        current_board = get_board()
        self.assertEqual('R', current_board[4][2])
        self.assertEqual('-', current_board[4][3])
        
    def test_choose_computer_move(self):
        print "\nchoose_computer_move"
        self.assertEqual(((1, 3), left), choose_computer_move('M'))
        self.assertEqual(((1, 2), left), choose_computer_move('R'))

    def test_is_enemy_win(self):
        print "\nis_enemy_win"
        set_board([ [_, _, _, M, R],
                    [_, _, _, M, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )        
        self.assertEqual(False, is_enemy_win())
        set_board([ [_, _, M, M, M],
                    [_, _, _, R, R],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] ) 
        self.assertEqual(True, is_enemy_win())
        set_board([ [_, _, R, _, M],
                    [_, _, _, _, M],
                    [_, _, _, _, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] ) 
        self.assertEqual(True, is_enemy_win())

        
unittest.main()
