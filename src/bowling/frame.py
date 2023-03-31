class Frame:
    def __init__(self, first_throw: int, second_throw: int) -> None:
        self.first_throw = first_throw
        self.second_throw = second_throw
        self.scorepoints = self.first_throw + self.second_throw

    def score(self) -> int:
        """ The score of a single frame """
        return self.first_throw + self.second_throw

    def is_strike(self) -> bool:
        """ Return whether the frame is a strike or not """
        if(self.first_throw == 10 or self.second_throw == 10):
            return True
        else:
            return False
        

    def is_spare(self) -> bool:
        """ Return whether the frame is a spare or not """
        if (self.first_throw + self.second_throw == 10):
            if(self.first_throw != 10 or self.second_throw != 10):
                return True
            else :
                return False
        else:
            return False

        

    def is_last_frame(self, number_of_past_frames: int) -> bool:
        """ Return whether the frame is a last frame of the game """
        if(number_of_past_frames == 9):
            return True
        else: False

    def bonus(self) -> int:
        """ Bonus throw """
        # To be implemented
        pass
