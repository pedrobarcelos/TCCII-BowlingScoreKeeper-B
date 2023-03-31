import unittest

from bowling.game import BowlingGame
from bowling.frame import Frame

class TestFrames(unittest.TestCase):
    def test_frame_is_spare(self):
        game = BowlingGame()
        frame = Frame(9,1)
        result = frame.is_spare()
        self.assertEqual(result, True)
    
    def test_frame_is_strike(self):
        game = BowlingGame()
        frame = Frame(9,1)
        result = frame.is_strike()
        self.assertEqual(result, False)

    def test_frame_is_last_frame(self):
        game = BowlingGame()
        game.init_frames()
        frame = Frame(9,1)
        for i in range(9):
            game.add_frame(frame)
        frame = Frame(9,1)
        number_of_past_frames = game.frame_list_size()
        result = frame.is_last_frame(number_of_past_frames)
        self.assertEqual(result, True)

    def test_frame_score(self):
        frame = Frame(2,1)
        result = frame.score()
        self.assertEqual(result,3)



if __name__ == '__main__':
    unittest.main()
