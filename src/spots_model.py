# Sophia Tao, 20293428, stao3@uci.edu


import point



class Spot:
    def __init__(self, top_left: point.Point, bottom_right:point.Point):
        
        self._top_left = top_left
        self._bottom_right = bottom_right


    def top_left_point(self) -> point.Point:
        '''Returns the top left point of the spot'''
        return self._top_left

    def bottom_right_point(self) -> point.Point:
        '''Returns the bottom right point of the spot'''
        return self._bottom_right

    def contains(self, point: point.Point) -> bool:
        '''Returns true if the specified point is within the spot'''
        return self._top_left._frac_x < point._frac_x < self._bottom_right._frac_x and self._top_left._frac_y < point._frac_y < self._bottom_right._frac_y
