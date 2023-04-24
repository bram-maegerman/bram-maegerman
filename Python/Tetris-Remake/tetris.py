import pygame, tetris_pieces, random

pygame.init()

window = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Tetris Remake")

MOVEDOWNEVENT = pygame.USEREVENT

class Grid(object):
    def __init__(self):
        self.grid = []
        self.cubeGrid = []
        self.createGrid()
        self.nextPieces = []
        self.nextPieces.append(random.choice(tetris_pieces.getPieces()))

    def draw(self):
        for xs in range(len(self.cubeGrid)):
            for x in range(len(self.cubeGrid[xs])):
                self.cubeGrid[xs][x].draw(self.grid[xs][x])

    def createGrid(self):
        self.grid.clear()
        for i in range(20):
            self.grid.append(["_" for x in range(10)])
        self.cubeGrid.clear()
        for y in range(20):
            newCubeGrid = []
            for x in range(10):
                newCubeGrid.append(Cube(30, 340 + 30*(x + 1), 30*(y + 1)))
            self.cubeGrid.append(newCubeGrid)

    def printGrid(self):
        for x in self.grid:
            print(" ".join(x))
        print("\n\n")
    
    def checkLines(self):
        line_amount = 0
        for xs in range(len(self.grid)):
            if "".join(self.grid[xs]) == "XXXXXXXXXX":
                del self.grid[xs]
                self.grid.insert(0, ["_" for x in range(10)])
                line_amount += 1
        if line_amount > 0:
            hud.add_score(line_amount)
                
    def spawnPiece(self, piece):
        self.current_piece = piece
        for x in self.current_piece.spawn_positions:
            self.grid[x[0]][x[1]] = "C"
    
    def FillNextPiece(self):
        self.checkLines()
        nextPiece = self.nextPieces.pop(0)
        self.nextPieces.append(random.choice(tetris_pieces.getPieces()))
        self.spawnPiece(nextPiece)

    def move(self, direction):
        current_piece_positions = []
        for xs in range(len(self.grid)):
            for x in range(len(self.grid[xs])):
                if self.grid[xs][x] == "C":
                    current_piece_positions.append([xs, x])
                    self.grid[xs][x] = "_"
        if len(current_piece_positions) > 0:
            if direction == 0:
                self.moveDown(current_piece_positions)
            if direction == 1:
                self.moveLeft(current_piece_positions)
            if direction == 2:
                self.moveRight(current_piece_positions)
            if direction == 3:
                self.turn(current_piece_positions)
            if direction == 4:
                if self.moveDown(current_piece_positions):
                    self.move(4)

    def moveDown(self, current_piece_positions):
        canMoveDown = True
        for x in current_piece_positions:
            x[0] += 1
            if x[0] > 19:
                canMoveDown = False
            elif self.grid[x[0]][x[1]] == "X":
                canMoveDown = False

        if canMoveDown:
            for x in current_piece_positions:
                self.grid[x[0]][x[1]] = "C"
        else:
            for x in current_piece_positions:
                self.grid[x[0] - 1][x[1]] = "X"
            self.FillNextPiece()
            return False
        return True

    def moveLeft(self, current_piece_positions):
        canMoveLeft = True
        for x in current_piece_positions:
            ycoord = x[1] - 1
            if ycoord < 0:
                canMoveLeft = False
                break
            elif self.grid[x[0]][x[1]] == "X":
                canMoveLeft = False
        
        if canMoveLeft:
            for x in current_piece_positions:
                self.grid[x[0]][x[1] - 1] = "C"
        else:
            for x in current_piece_positions:
                self.grid[x[0]][x[1]] = "C"
            return False
        return True

    def moveRight(self, current_piece_positions):
        canMoveRight = True
        for x in current_piece_positions:
            ycoord = x[1] + 1
            if ycoord > 9:
                canMoveRight = False
                break
            elif self.grid[x[0]][x[1]] == "X":
                canMoveRight = False
        
        if canMoveRight:
            for x in current_piece_positions:
                self.grid[x[0]][x[1] + 1] = "C"
        else:
            for x in current_piece_positions:
                self.grid[x[0]][x[1]] = "C"
            return False
        return True

    def turn(self, current_piece_positions):
        nextRotation = self.current_piece.getRotation(current_piece_positions)
        canTurn = True
        for x in nextRotation:
            if x[0] < 0 or x[0] > 19 or x[1] < 0 or x[1] > 9:
                canTurn = False
                self.current_piece.cancelRotation()
                break
            elif self.grid[x[0]][x[1]] == "X":
                canTurn = False
                self.current_piece.cancelRotation()
                break
        if canTurn:
            for x in nextRotation:
                self.grid[x[0]][x[1]] = "C"
        else:
            for x in current_piece_positions:
                self.grid[x[0]][x[1]] = "C"
        
class Cube(object):
    def __init__(self, width, x, y):
        self.width = width
        self.x = x
        self.y = y
        self.innerrect = pygame.Rect(self.x, self.y, self.width - (width / 10), self.width - (width / 10))
        self.outerrect = pygame.Rect(self.x, self.y, self.width, self.width)

    def __getitem__(self, items):
        return self

    def draw(self, state):
        self.innerrect.center = (self.x, self.y)
        self.outerrect.center = (self.x, self.y)
        pygame.draw.rect(window, (0, 0, 0), self.outerrect)
        color = (100, 100, 100)
        if state == "X":
            color = (200, 200, 200)
        elif state == "C":
            color = (255, 0, 0)
        pygame.draw.rect(window, color, self.innerrect)

class Hud(object):
    def __init__(self):
        self.score = 0
        self.score_pos = [340, 25]
        self.score_font = pygame.font.Font('freesansbold.ttf', 32)

    def draw(self):
        score_text = self.score_font.render(str(self.score), True, (100, 100, 100))
        textRect = score_text.get_rect()
        textRect.topright = self.score_pos
        window.blit(score_text, textRect)

    def add_score(self, line_amount):
        match line_amount:
            case 1:
                self.score += 40
            case 2:
                self.score += 100
            case 3:
                self.score += 300
            case 4:
                self.score += 1200

            case _:
                pass

grid = Grid()
hud = Hud()

def render_frame():
    window.fill((0, 0, 0))
    grid.draw()
    hud.draw()

def main():
    running = True
    pygame.time.set_timer(MOVEDOWNEVENT, 1000)
    grid.FillNextPiece()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == MOVEDOWNEVENT:
                grid.move(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    grid.grid[10] = ["X" for x in range(10)]
                if event.key == pygame.K_UP:
                    grid.move(3)
                if event.key == pygame.K_LEFT:
                    grid.move(1)
                if event.key == pygame.K_DOWN:
                    pygame.time.set_timer(MOVEDOWNEVENT, 0)
                    pygame.time.set_timer(MOVEDOWNEVENT, 1000)
                    grid.move(0)
                if event.key == pygame.K_RIGHT:
                    grid.move(2)
                if event.key == pygame.K_SPACE:
                    grid.move(4)

        render_frame()
        pygame.display.flip()

if __name__ == "__main__":
    main()