import random


class Game:
  dimension = None
  board = None
  current_x = None
  current_y = None
  monster = None
  snake = None
  brick = None
  score = None
  def __init__(self, dimension):
    self.current_x = random.randint(0,9)
    self.current_y = random.randint(0,9)
    self.current_monster_x = random.randint(0,9)
    self.current_monster_y = random.randint(0,9)
    self.dimension = dimension
    self.score = 0
    self.brick = "\33[;31m'\33[;0m"
    self.snake = "\33[;32mO\33[;0m"
    self.monster = "@"
    self.board = []
    for x in range(dimension):
      line = []
      for y in range(dimension):
        line.append(self.brick)
      self.board.append(line)
    self.board[self.current_y][self.current_x] = self.snake
    self.move_monster()  
  
  def draw(self):
    print(self)
  
  def move_monster(self):
    self.current_monster_y = random.randint(0,9)
    self.current_monster_x = random.randint(0,9)
    self.board[self.current_monster_y][self.current_monster_x] = self.monster
    

  def move_snake(self, direction):
    left = "a"
    down = "s"
    right = "d"
    up = "w"

    self.board[self.current_y][self.current_x] = self.brick  
    if direction == left:
      self.current_x -= 1
    if direction == right:
      self.current_x += 1
    if direction == down:
      self.current_y += 1
    if direction == up:
      self.current_y -= 1

    # never more then dimension
    self.current_x = min(self.current_x, self.dimension-1)
    self.current_y = min(self.current_y, self.dimension-1)

    # never less then 0
    self.current_x = max(self.current_x, 0)
    self.current_y = max(self.current_y, 0)
    
    # get what is where the snake should be placed
    current_thing = self.board[self.current_y][self.current_x]
    # check if there is a monster there
    if current_thing == self.monster:
      self.move_monster()
      self.score += 1
      
    # place the snake
    self.board[self.current_y][self.current_x] = self.snake  
    
      
  def __str__(self):
    result = "\nSCORE : {}\n\n".format(self.score)
    for line in self.board:
      for x in line:
        result += "| {} ".format(x)
      result += "\n"
    return result 
  


def main():

  some_game = Game(10)
  some_game.draw()
  inp = input("Enter asdw ")
  while inp != "q":
    some_game.move_snake(inp)
    some_game.draw()
    inp = input("Enter asdw ")

main()

