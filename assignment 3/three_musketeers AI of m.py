# The Three Musketeers Game
# by <insert your names here>.

# In all methods,
#   A 'location' is a two-tuple of integers, each in the range 0 to 4.
#        The first integer is the row number, the second is the column number.
#   A 'direction' is one of the strings "up", "down", "left", or "right".
#   A 'board' is a list of 5 lists, each containing 5 strings: "M", "R", or "-".
#        "M" = Musketeer, "R" = Cardinal Richleau's man, "-" = empty.
#        Each list of 5 strings is a "row"
#   A 'player' is one of the strings "M" or "R" (or sometimes "-").
#
# For brevity, Cardinal Richleau's men are referred to as "enemy".
# 'pass' is a no-nothing Python statement. Replace it with actual code.

def create_board():
    global board
    """Creates the initial Three Musketeers board. 'M' represents
    a Musketeer, 'R' represents one of Cardinal Richleau's men,
    and '-' denotes an empty space."""
    m = 'M'
    r = 'R'
    _ = '-'
    board = [ [r, r, r, r, m],
              [r, r, r, r, r],
              [r, r, m, r, r],
              [r, r, r, r, r],
              [m, r, r, r, r] ]

def set_board(new_board):
    """Replaces the global board with new_board."""
    global board
    board = new_board
    
def get_board():
    """Just returns the board. Possibly useful for unit tests."""
    return board

def string_to_location(s):
    """Given a two-character string (such as 'A5') return the designated
       location as a 2-tuple (such as (0, 4))."""
    assert s[0] >= 'A' and s[0] <= 'E'
    assert s[1] >= '1' and s[1] <= '5'
    location = (ord(s[0]) - ord('A'), ord(s[1]) - ord('1'))
    return location

def location_to_string(location):
    """Return the string representation of a location."""
    assert location[0] >= 0 and location[0] <= 4
    assert location[1] >= 0 and location[1] <= 4
    x = str(chr((location[0]) + 65))
    y = str((location[1]) + 1)
    return x + y
               
def at(location):
    """Returns the contents of the board at the given location."""
    return board[location[0]][location[1]]

def all_locations():
    """Returns a list of all 25 locations on the board."""
    location_list = []
    for x in range(0, 5):
        for y in range(0, 5):
            location_list.append((x, y))
            y += 1
    x += 1
    return location_list
    
def adjacent_location(location, direction):
    """Return the location next to the given one, in the given direction.
       Does not check if the location returned is legal on a 5x5 board."""
    (row, column) = location
    if direction == 'up':
        return (row - 1, column)
    elif direction == 'down':
        return (row + 1, column)
    elif direction == 'left':
        return (row, column - 1)
    elif direction == 'right':
        return (row, column + 1)

def is_legal_move_by_musketeer(location, direction):
    """Tests if the Musketeer at the location can move in the direction."""
    assert at(location) == 'M'
    assert is_legal_location(location)
    assert is_within_board(location, direction)
    if at(adjacent_location(location, direction)) == 'R':
        return True
    else:
        return False
    
def is_legal_move_by_enemy(location, direction):
    """Tests if the enemy at the location can move in the direction."""
    assert at(location) == 'R'
    assert is_legal_location(location)
    assert is_within_board(location, direction) 
    if at(adjacent_location(location, direction)) == '-':
        return True
    else:
        return False

def is_legal_move(location, direction):
    """Tests whether it is legal to move the piece at the location
    in the given direction."""
    if not is_legal_location(location):
        return False
    elif not is_within_board(location, direction):
        return False
    elif at(location) == 'R':
        return is_legal_move_by_enemy(location, direction)
    elif at(location) == 'M':
        return is_legal_move_by_musketeer(location, direction)
    else:
        return False

def has_some_legal_move_somewhere(who):
    """Tests whether a legal move exists for player "who" (which must
    be either 'M' or 'R'). Does not provide any information on where
    the legal move is."""
    locations = all_locations()
    i = 0
    while i <= 24:
        if board[locations[i][0]][locations[i][1]] == who:
            if can_move_piece_at(locations[i]):
                return True
        i += 1
    return False

def possible_moves_from(location): 
    """Returns a list of directions ('left', etc.) in which it is legal
       for the player at location to move. If there is no player at
       location, returns the empty list, []."""
    possible_directions = []
    if is_legal_move(location, 'left'):
        possible_directions.append('left')
    if is_legal_move(location, 'right'):
        possible_directions.append('right')
    if is_legal_move(location, 'up'):
        possible_directions.append('up')
    if is_legal_move(location, 'down'):
        possible_directions.append('down')
    return possible_directions


def can_move_piece_at(location): 
    """Tests whether the player at the location has at least one move available."""
    if is_legal_move(location, 'left') or is_legal_move(location, 'right'):
        return True
    elif is_legal_move(location, 'up') or is_legal_move(location, 'down'):
        return True
    else:
        return False

def is_legal_location(location):
    """Tests if the location is legal on a 5x5 board."""
    if location[0] > 4 or location[0] < 0 or location[1] > 4 or location [1] < 0:
        return False
    else:
        return True

def is_within_board(location, direction):
    """Tests if the move stays within the boundaries of the board."""
    return is_legal_location(adjacent_location(location, direction))

def all_possible_moves_for(player): 
    """Returns every possible move for the player ('M' or 'R') as a list
       (location, direction) tuples."""
    possible_moves = []
    if player != 'M' and player != 'R':
        print "Error, Player must be 'M' or 'R'!"
        return possible_moves
    player_locations = []
    locations = all_locations()
    i = 0
    count = 0
    for i in range(0, 25):
        if at(locations[i]) == player:
            player_locations.append(locations[i])
            count += 1
    i = 0

    direction = '?'
    for i in range(0, count):
        for direction in ['left', 'right', 'up', 'down']:
            if is_legal_move(player_locations[i], direction):
                possible_moves.append((player_locations[i], direction))
    return possible_moves

def make_move(location, direction): 
    """Moves the piece in location in the indicated direction."""
    assert is_legal_move(location, direction)
    new_location = adjacent_location(location, direction)
    board[new_location[0]][new_location[1]] = board[location[0]][location[1]]
    #replace the piece on new_location by that on old location
    board[location[0]][location[1]] = '-'
    #the old location is now empty

def choose_computer_move(who):
    """The computer chooses a move for a Musketeer (who = 'M') or an
       enemy (who = 'R') and returns it as the tuple (location, direction),
       where a location is a (row, column) tuple as usual."""
    if who == 'R':
        return choose_enemy_move()
    if who == 'M':
        return choose_muketeers_move()
    

def choose_enemy_move():
    directions = ['up', 'right', 'down', 'left']
    prefer_dir = directions[0]
    moves = all_possible_moves_for('R')#what if no possible moves?
    for prefer_dir in directions:
        for (location, direction) in moves:
            if direction == prefer_dir:
                return (location, direction)

        
    

def choose_muketeers_move():
    moves = all_possible_moves_for('M')
    locations = all_locations()
    i = 0
    musketeers = []
    count = 0
    for i in range (0, 25):
        if 'M' == at(locations[i]):
            musketeers.append(locations[i])
            count += 1
        if count == 3:
            break
    m_aftermove = []
    for one_move in moves:
        for i in range (0, 3):
            if one_move[0] == musketeers[i]:
                m_aftermove.append(adjacent_location(one_move[0], one_move[1]))
            else:
                m_aftermove.append(one_move)
    

def is_enemy_win():
    """Returns True if all 3 Musketeers are in the same row or column."""
    locations = all_locations()
    i = 0
    musketeers = []
    count = 0
    for i in range (0, 25):
        if 'M' == at(locations[i]):
            musketeers.append(locations[i])
            count += 1
        if count == 3:
            break
    if musketeers[0][0] == musketeers[1][0] == musketeers[2][0]:
        return True
    elif  musketeers[0][1] == musketeers[1][1] == musketeers[2][1]:
        return True
    else:
        return False

#---------- Communicating with the user ----------

def print_board():
    print "    1  2  3  4  5"
    print "  ---------------"
    ch = "A"
    for i in range(0, 5):
        print ch, "|",
        for j in range(0, 5):
            print board[i][j] + " ",
        print
        ch = chr(ord(ch) + 1)
    print

def print_instructions():
    print
    print """To make a move, enter the location of the piece you want to move,
and the direction you want it to move. Locations are indicated as a
letter (A, B, C, D, or E) followed by an integer (1, 2, 3, 4, or 5).
Directions are indicated as left, right, up, or down (or simply L, R,
U, or D). For example, to move the Musketeer from the top right-hand
corner to the row below, enter 'A5 left' (without quotes).

For convenience in typing, you may use lowercase letters."""
    print

def choose_users_side():
    """Returns 'M' if user is playing Musketeers, 'R' otherwise."""
    user = ""
    while user != 'M' and user != 'R':
        answer = raw_input("Would you like to play Musketeer (M) or enemy (R)? ")
        answer = answer.strip()
        if answer != "":
            user = answer.upper()[0]
    return user

def get_users_move():
    """Gets a legal move from the user, and returns it as a
       (location, direction) tuple."""    

    directions = {'L':'left', 'R':'right', 'U':'up', 'D':'down'}
    move = raw_input("Your move? ").upper().replace(' ', '')
    if len(move) < 3:
        print "illegal input, specify a location and direction"
        return get_users_move()
    if move[0] in 'ABCDE' and move[1] in '12345' and move[2] in 'LRUD':
        location = string_to_location(move[0:2])
        direction = directions[move[2]]
        if is_legal_move(location, direction):
            return (location, direction)
    print "Illegal move--'" + move + "'"
    print_instructions()
    return get_users_move()

def move_musketeer(users_side):
    """Gets the Musketeer's move (from either the user or the computer)
       and makes it."""
    if users_side == 'M':
        (location, direction) = get_users_move()
        if at(location) == 'M':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Musketeer", location, direction)
        else:
            print "You can't move there!"
            return move_musketeer(users_side)
    else: # Computer plays Musketeer
        (location, direction) = choose_computer_move('M')         
        make_move(location, direction)
        describe_move("Musketeer", location, direction)
        
def move_enemy(users_side):
    """Gets the enemy's move (from either the user or the computer)
       and makes it."""
    if users_side == 'R':
        (location, direction) = get_users_move()
        if at(location) == 'R':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Enemy", location, direction)
        else:
            print "You can't move there!"
            return move_enemy(users_side)
    else: # Computer plays enemy
        (location, direction) = choose_computer_move('R')         
        make_move(location, direction)
        describe_move("Enemy", location, direction)
        return board

def describe_move(who, location, direction): 
    """Prints a sentence describing the given move."""
    new_location = adjacent_location(location, direction)
    print who, 'moves', direction, 'from',\
          location_to_string(location), 'to',\
          location_to_string(new_location) + ".\n"

def start():
    """Plays the Three Musketeers Game."""
    users_side = choose_users_side()
    board = create_board()
    print_instructions()
    print_board()
    while True:
        if has_some_legal_move_somewhere('M'):
            board = move_musketeer(users_side)
            print_board()
            if is_enemy_win():
                print "Cardinal Richleau's men win!"
                break
        else:
            print "The Musketeers win!"
            break
        if has_some_legal_move_somewhere('R'):
            board = move_enemy(users_side)
            print_board()
        else:
            print "The Musketeers win!"
            break
