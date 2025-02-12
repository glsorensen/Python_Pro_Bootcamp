def turn_right():
    turn_left()
    turn_left()
    turn_left()


def walk_in_circle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()


def maze_complete:
    for walk in range(10):
        move()
        turn_left()
        move()
        turn_right()
        move()
        turn_left()
        move()
        turn_right()


maze_complete()