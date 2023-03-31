from typing import List

from bowling.frame import Frame


class BowlingGame:
    frames: List[Frame]
    bonus: Frame

    def init_frames(self):
        self.frames = []

    def frame_list_size(self) -> int:
        """  Get the number of frames created  """
        return len(self.frames)

    def add_frame(self, frame: Frame):
        """ Add a frame to the game """
        if(self.frame_list_size() < 10):
            self.frames.append(frame)
        

    def set_bonus(self, first_throw: int, second_throw: int):
        """ The the bonus throw """
        # To be implemented
        pass

    def score(self) -> int:
        """ Get the score from the game """
        total = 0
        spare = False
        strike = False
        count = 0

        if(self.frames[0].is_spare()):
                spare = True
        elif(self.frames[0].is_strike()):
                strike = True
        for i in self.frames:
            if(spare):
                print(self.frames[0].scorepoints)
                self.frames[0].scorepoints += self.frames[count+1].first_throw
                print(self.frames[0].scorepoints)
            elif(strike):
                self.frames[count].scorepoints += self.frames[count+1].second_throw + self.frames[count+1].first_throw

            if(i.is_spare()):
                spare = True
                strike = False
            elif(i.is_strike()):
                strike = True
                spare = False
            else:
                strike = False
                spare = False
            count+=1

        for i in self.frames:
            total += i.score

        print(total)
        return total

    def is_next_frame_bonus(self) -> bool:
        """ Get if the next frame is bonus """
        # To be implemented
        pass
