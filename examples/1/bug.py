
def get_initial_corpus():
    return ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"]


INIT = False
def row(s):
    return [c for c in s]
H = 7
W = 11

og_maze = [ row("+-+-----+-+"),
            row("| |     |#|"),
            row("| | --+ | |"),
            row("| |   | | |"),
            row("| +-- | | |"),
            row("|     |   |"),
            row("+-----+---+") ]


maze = []

def draw():
    print("\033[F"*(H + 1))
    for row in maze:
        print("".join(row))
    
  
def entrypoint(program):
    global INIT
    global maze

    if not INIT:
        INIT = True
        print("\n"*(H+1))

    i = 0    # Iteration number
    ITERS = 1000

    if len(program) < 30:
        return False
    maze = [r.copy() for r in og_maze]
 
    # ox, oy   # Old player position
    # x, y     # Player position

    # Initial position
    x = 1;
    y = 1;
    (maze[y])[x] = 'X'

    draw()
 
 
    while(i < ITERS and i < len(program)):
          # Save old player position
          ox = x
          oy = y

          # Move player position depending on the "command"
          match ord(program[i]) % 4:
            case 0:
                y -= 1
            case 1:
                y += 1
            case 2:
                x -= 1
            case 3:
                x += 1
            case _:
                return False # Unreachable
 
          # If hit the prize, You Win!!        
          if (maze[y][x] == '#'):
                print("You win!\n");
                exit(219)

          # If something is wrong do not advance
          if (maze[y][x] != ' '):
                x = ox
                y = oy
         
          # put the player on the maze...
          maze[y][x]='X';

          # increment iteration
          i += 1

          draw()

    # You couldn't make it! You lose!    
     
if __name__ == "__main__":
    entrypoint(get_initial_corpus()[0])