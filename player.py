import numpy as np



class Player:


    def setup(self):
        """
        This method will be called once at the beginning of the game so the player
        can conduct any setup before the move timer begins. The setup method is
        also timed.
        """
        pass


    def play(self, board: np.ndarray):
        """
        Given a 2D array representing the game board, return a tuple of ints corresponding to
        the coordinates that you want to play. The (0, 0) if upper left corner of the board. 
        The coordinates increase along the right and down directions. 

        Parameters
        ----------
        board : np.ndarray
            A 2D array where 0s represent empty slots, +1s represent your pieces,
            and -1s represent the opposing player's pieces.

                `index   0   1   2   . column` \\
                `--------------------------` \\
                `0   |   0.  0.  0.  top` \\
                `1   |   -1  0.  0.  .` \\
                `2   |   +1  -1  -1  .` \\
                `.   |   -1  +1  +1  .` \\
                `row |   left        bottom/right`

        Returns
        -------
        tuple of ints as (row_index, column_index)
            the coordinates of the square you want to put your piece in 
        """
        raise NotImplementedError()


__all__ = ['Player']