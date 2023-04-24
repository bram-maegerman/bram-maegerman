class Cube_Piece(object):
    def __init__(self):
        self.spawn_positions = [[0, 4], [0, 5], [1, 4], [1, 5]]
        self.absolute_pos = [[0, 0], [0, 1], [1, 0], [1, 1]]

    def cancelRotation(self):
        pass
        
    def getRotation(self, currentPos):
        return currentPos

class T_Piece(object):
    def __init__(self):
        self.spawn_positions = [[0, 4], [1,3], [1, 4], [1, 5]]
        self.current_rotation = 0
        self.absolute_pos = [[0, 0], [0, 1], [1, 0], [1, 1]]

    def cancelRotation(self):
        self.current_rotation -= 1
        if self.current_rotation == -1:
            self.current_rotation = 3
        
    def getRotation(self, currentPos):
        c = currentPos
        self.current_rotation += 1
        if self.current_rotation > 3:
            self.current_rotation = 0
        self.rotation_positions = [
            [c[0], c[1], c[2], [c[3][0] - 1, c[3][1] + 1]],
            [c[0], [c[1][0] + 1, c[1][1] + 1], c[2], c[3]],
            [[c[0][0] + 1, c[0][1] - 1], c[1], c[2], c[3]],
            [c[0], c[1], [c[2][0] - 1, c[2][1] - 1], c[3]]
        ]
        return self.rotation_positions[self.current_rotation]

class I_Piece(object):
    def __init__(self):
        self.spawn_positions = [[1, 3], [1,4], [1, 5], [1, 6]]
        self.current_rotation = 0
        self.absolute_pos = [[0, 0], [0, 1], [1, 0], [1, 1]]

    def cancelRotation(self):
        self.current_rotation -= 1
        if self.current_rotation == -1:
            self.current_rotation = 3
        
    def getRotation(self, currentPos):
        c = currentPos
        self.current_rotation += 1
        if self.current_rotation > 3:
            self.current_rotation = 0
        self.rotation_positions = [
            [[c[0][0] + 1, c[0][1] + 2], c[1], [c[2][0] - 1, c[2][1] + 1], [c[3][0] - 2, c[3][1] - 1]],
            [[c[0][0] - 1, c[0][1] + 2], [c[1][0] + 1, c[1][1] + 1], c[2], [c[3][0] + 2, c[3][1] - 1]],
            [[c[0][0] + 2, c[0][1] - 2], [c[1][0] + 1, c[1][1] - 1], c[2], [c[3][0] - 1, c[3][1] + 1]],
            [[c[0][0] - 2, c[0][1] + 1], c[1], [c[2][0] - 1, c[2][1] - 1], [c[3][0] + 1, c[3][1] - 2]]
        ]
        return self.rotation_positions[self.current_rotation]   

class L_Piece(object):
    def __init__(self):
        self.spawn_positions = [[0, 5], [1,3], [1, 4], [1, 5]]
        self.current_rotation = 0
        self.absolute_pos = [[0, 0], [0, 1], [1, 0], [1, 1]]

    def cancelRotation(self):
        self.current_rotation -= 1
        if self.current_rotation == -1:
            self.current_rotation = 3
        
    def getRotation(self, currentPos):
        c = currentPos
        self.current_rotation += 1
        if self.current_rotation > 3:
            self.current_rotation = 0
        self.rotation_positions = [
            [[c[0][0] + 1, c[0][1]], [c[1][0], c[1][1] + 1], c[2], [c[3][0] - 1, c[3][1] + 1]],
            [[c[0][0], c[0][1] - 1], [c[1][0] + 1, c[1][1] + 1], c[2], [c[3][0] + 1, c[3][1]]],
            [[c[0][0] + 1, c[0][1] - 1], c[1], [c[2][0], c[2][1] - 1], [c[3][0] - 1, c[3][1]]],
            [[c[0][0] - 1, c[0][1] ], c[1], [c[2][0] - 1, c[2][1] - 1], [c[3][0], c[3][1] + 1]]
        ]
        return self.rotation_positions[self.current_rotation]   

class J_Piece(object):
    def __init__(self):
        self.spawn_positions = [[0, 3], [1,3], [1, 4], [1, 5]]
        self.current_rotation = 0
        self.absolute_pos = [[0, 0], [0, 1], [1, 0], [1, 1]]

    def cancelRotation(self):
        self.current_rotation -= 1
        if self.current_rotation == -1:
            self.current_rotation = 3
        
    def getRotation(self, currentPos):
        c = currentPos
        self.current_rotation += 1
        if self.current_rotation > 3:
            self.current_rotation = 0
        self.rotation_positions = [
            [[c[0][0], c[0][1] - 1], c[1], [c[2][0] - 1, c[2][1]], [c[3][0] - 1, c[3][1] + 1]],
            [[c[0][0], c[0][1] + 1], [c[1][0] + 1, c[1][1] + 1], c[2], [c[3][0] - 1, c[3][1]]],
            [[c[0][0] + 1, c[0][1] - 1], [c[1][0] + 1, c[1][1]], c[2], [c[3][0], c[3][1] + 1]],
            [[c[0][0] + 1, c[0][1]], c[1], [c[2][0] - 1, c[2][1] - 1], [c[3][0], c[3][1] - 1]]
        ]
        return self.rotation_positions[self.current_rotation]   

def getPieces():
    return [Cube_Piece(), T_Piece(), I_Piece(), L_Piece(), J_Piece()]