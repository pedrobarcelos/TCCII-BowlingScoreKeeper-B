import unittest

from bowling.game import BowlingGame
from bowling.frame import Frame

class TestGames(unittest.TestCase):
    def test_game_add_frame(self):
        game = BowlingGame()
        game.init_frames()
        size_before = game.frame_list_size()
        frame = Frame(9,1)
        game.add_frame(frame)
        size_after = game.frame_list_size()
        self.assertEqual(size_before, size_after-1)
    
    def test_game_score(self):
        game = BowlingGame()
        game.init_frames()
        frame = Frame(9,1)
        for i in range(9):
            game.add_frame(frame)
        result = game.score()
        self.assertEqual(result, 90)


if __name__ == '__main__':
    unittest.main()
