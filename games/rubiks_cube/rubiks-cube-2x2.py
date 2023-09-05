import argparse
parser = argparse.ArgumentParser(description="Solve a 2x2 Rubik's Cube")

# Key Concepts
#  - Pick the right data structures for the problem domain
#  - Structure list/array indexes to make most cases easy
#  - Create appropriate abstractions using classes and methods
#  - Be careful with repetitive function definitions
#  - Debug with full info, even if question only asks for partial info

class Cube2x2(object):
   # +---+
   # | U |
   # +---+---+---+---+
   # | F | R | B | L |
   # +---+---+---+---+
   # | D |
   # +---+
   
   # +---+---+
   # | W | W |
   # +---+---+
   # | W | W |
   # +---+---+---+---+---+---+---+---+
   # | G | G | R | R | B | B | O | O |
   # +---+---+---+---+---+---+---+---+
   # | G | G | R | R | B | B | O | O |
   # +---+---+---+---+---+---+---+---+
   # | Y | Y |
   # +---+---+
   # | Y | Y |
   # +---+---+
   
   # +---+---+
   # | 0 | 1 |
   # +---U---+
   # | 2 | 3 |
   # +---+---+---+---+---+---+---+---+
   # | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |
   # +---F---+---R---+---B---+---L---+
   # | 2 | 3 | 2 | 3 | 2 | 3 | 2 | 3 |
   # +---+---+---+---+---+---+---+---+
   # | 0 | 1 |
   # +---D---+
   # | 2 | 3 |
   # +---+---+
   def __init__(self):
      self.front = ['G', 'G', 'G', 'G']
      self.left = ['O', 'O', 'O', 'O']
      self.right = ['R', 'R', 'R', 'R']
      self.back = ['B', 'B', 'B', 'B']
      self.up = ['W', 'W', 'W', 'W']
      self.down = ['Y', 'Y', 'Y', 'Y']
   
   def rotateFront90CW(self):
      front_temp = list(self.front)
      up_temp = list(self.up)
      right_temp = list(self.right)
      down_temp = list(self.down)
      left_temp = list(self.left)
      # Front face rotates one position CW
      self.front[0] = front_temp[2]
      self.front[1] = front_temp[0]
      self.front[2] = front_temp[3]
      self.front[3] = front_temp[1]
      # Part of the right side goes to the bottom face
      self.down[0] = right_temp[2]
      self.down[1] = right_temp[0]
      # Part of the bottom face goes to the left face
      self.left[1] = down_temp[0]
      self.left[3] = down_temp[1]
      # Part of the left face goes to the top face
      self.up[2] = left_temp[3]
      self.up[3] = left_temp[1]
      # Part of the top face goes to the right face
      self.right[0] = up_temp[2]
      self.right[2] = up_temp[3]
   
   def rotateTop90CW(self):
      up_temp = list(self.up)
      front_temp = list(self.front)
      right_temp = list(self.right)
      back_temp = list(self.back)
      left_temp = list(self.left)
      # Top face rotates one position CW
      self.up[0] = up_temp[2]
      self.up[1] = up_temp[0]
      self.up[2] = up_temp[3]
      self.up[3] = up_temp[1]
      # Part of the right side goes to the front face
      self.front[0] = right_temp[0]
      self.front[1] = right_temp[1]
      # Part of the front face goes to the left face
      self.left[0] = front_temp[0]
      self.left[1] = front_temp[1]
      # Part of the left face goes to the back face
      self.back[0] = left_temp[0]
      self.back[1] = left_temp[1]
      # Part of the back face goes to the right face
      self.right[0] = back_temp[0]
      self.right[1] = back_temp[1]
   
   def rotateRight90CW(self):
      right_temp = list(self.right)
      up_temp = list(self.up)
      front_temp = list(self.front)
      back_temp = list(self.back)
      down_temp = list(self.down)
      # Right face rotates one position CW
      self.right[0] = right_temp[2]
      self.right[1] = right_temp[0]
      self.right[2] = right_temp[3]
      self.right[3] = right_temp[1]
      # Part of the bottom face goes to the front face
      self.front[1] = down_temp[1]
      self.front[3] = down_temp[3]
      # Part of the front face goes to the top face
      self.up[1] = front_temp[1]
      self.up[3] = front_temp[3]
      # Part of the top face goes to the back face
      self.back[0] = up_temp[3]
      self.back[2] = up_temp[1]
      # Part of the back face goes to the bottom face
      self.down[1] = back_temp[2]
      self.down[3] = back_temp[0]
   
   def rotateBottom90CW(self):
      down_temp = list(self.down)
      front_temp = list(self.front)
      right_temp = list(self.right)
      back_temp = list(self.back)
      left_temp = list(self.left)
      # Bottom face rotates one position CW
      self.down[0] = down_temp[2]
      self.down[1] = down_temp[0]
      self.down[2] = down_temp[3]
      self.down[3] = down_temp[1]
      # Part of the front face goes to the right face
      self.right[2] = front_temp[2]
      self.right[2] = front_temp[3]
      # Part of the right face goes to the back face
      self.back[2] = right_temp[2]
      self.back[3] = right_temp[3]
      # Part of the back face goes to the left face
      self.left[2] = back_temp[2]
      self.left[3] = back_temp[3]
      # Part of the left face goes to the front face
      self.front[2] = left_temp[2]
      self.front[3] = left_temp[3]
    
   def rotateLeft90CW(self):
      left_temp = list(self.left)
      up_temp = list(self.up)
      front_temp = list(self.front)
      back_temp = list(self.back)
      down_temp = list(self.down)
      # Left face rotates one position CW
      self.left[0] = left_temp[2]
      self.left[1] = left_temp[0]
      self.left[2] = left_temp[3]
      self.left[3] = left_temp[1]
      # Part of the bottom face goes to the back face
      self.back[1] = down_temp[0]
      self.back[3] = down_temp[2]
      # Part of the back face goes to the top face
      self.up[0] = back_temp[3]
      self.up[2] = back_temp[1]
      # Part of the top face goes to the front face
      self.front[0] = up_temp[0]
      self.front[2] = up_temp[2]
      # Part of the front face goes to the bottom face
      self.down[0] = front_temp[0]
      self.down[2] = front_temp[2]
      
   def rotateBack90CW(self):
      back_temp = list(self.back)
      up_temp = list(self.up)
      right_temp = list(self.right)
      down_temp = list(self.down)
      left_temp = list(self.left)
      # Back face rotates one position CW
      self.back[0] = back_temp[2]
      self.back[1] = back_temp[0]
      self.back[2] = back_temp[3]
      self.back[3] = back_temp[1]
      # Part of the right side goes to the top face
      self.up[0] = right_temp[1]
      self.up[1] = right_temp[3]
      # Part of the top face goes to the left face
      self.left[2] = up_temp[0]
      self.left[0] = up_temp[1]
      # Part of the left face goes to the bottom face
      self.down[3] = left_temp[2]
      self.down[2] = left_temp[0]
      # Part of the bottom face goes to the right face
      self.right[1] = down_temp[3]
      self.right[3] = down_temp[2] 
   
   def printFrontFace(self):
      #self.printFullCube()
      print(self.front[0] + ' ' + self.front[1])
      print(self.front[2] + ' ' + self.front[3])
   
   def printFullCube(self):
      print('+---+---+')
      print('| ' + self.up[0] + ' | ' + self.up[1] + ' |')
      print('+---U---+')
      print('| ' + self.up[2] + ' | ' + self.up[3] + ' |')
      print('+---+---+---+---+---+---+---+---+')
      print('| ' + self.front[0] + ' | ' + self.front[1] + ' | ' + self.right[0] + ' | ' + self.right[1] + ' | ' + self.back[0] + ' | ' + self.back[1] + ' | ' + self.left[0] + ' | ' + self.left[1] + ' |')
      print('+---F---+---R---+---B---+---L---+')
      print('| ' + self.front[2] + ' | ' + self.front[3] + ' | ' + self.right[2] + ' | ' + self.right[3] + ' | ' + self.back[2] + ' | ' + self.back[3] + ' | ' + self.left[2] + ' | ' + self.left[3] + ' |')
      print('+---+---+---+---+---+---+---+---+')
      print('| ' + self.down[0] + ' | ' + self.down[1] + ' |')
      print('+---D---+')
      print('| ' + self.down[2] + ' | ' + self.down[3] + ' |')
      print('+---+---+')

def process_command(command, cube):
    if command == 'U':
        print("\n" + command)
        cube.rotateTop90CW()
        cube.printFrontFace()
    elif command == 'F':
        print("\n" + command)
        cube.rotateFront90CW()
        cube.printFrontFace()
    elif command == 'R':
        print("\n" + command)
        cube.rotateRight90CW()
        cube.printFrontFace()
    elif command == 'L':
        print("\n" + command)
        cube.rotateLeft90CW()
        cube.printFrontFace()
    elif command == 'B':
        print("\n" + command)
        cube.rotateBack90CW()
        cube.printFrontFace()
    elif command == 'D':
        print("\n" + command)
        cube.rotateBottom90CW()
        cube.printFrontFace()

def main():
    parser.add_argument("-i", "--input", help="JSON input file with parameters")

    args = parser.parse_args()

    f = open(args.input, "r")
    statements = f.readlines()
    f.close()

    cube = Cube2x2()
    print('\nStart')
    cube.printFrontFace()

    for statement in statements:
        command = statement.strip()
        process_command(command, cube)
    
    print('\nEnd')

if __name__ == "__main__":
    main()
        