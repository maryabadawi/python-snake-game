from tkinter import *
import random

# Constants

GAME_WIDTH = 500
GAME_HEIGHT = 500
SPEED  = 100
SPACE_SIZE = 25
BODY_PARTS = 3
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "black"

# create classes for the two visible objects on screen
class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []   # Previous incorrect code misspelled coordinates as coordinate
        self.squares = []
# Create list of coordinates
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])
# create squares for the snake's body
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)


class Food:

    def __init__(self):
            # X and Y 
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
            # coordinates using x and y
        self.coordinates = [x, y]
            # Creating the circle food item with position and color
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

        # define functions for movements, collision, and ending the game
def next_turn(snake, food):

    x, y = snake.coordinates[0]

        # Conditional statements to change the snake's next coordinates 
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

        # update the list of squares after snake has moved
    snake.squares.insert(0, square)

        # Updating score after consuming food
    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1

        label.config(text="Score:{}".format(score)) # displaying updated score

        canvas.delete("food")   # Remove food after consuming

        food = Food()   # generating new food after old one has been consumed

    else:   # Keeping body of the snake the same size if food is not consumed

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]
            #if snake collides, end game
    if check_collisions(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):        # first mistake in the previous code: "new_direction" was not written between the parentheis

    global direction

    if new_direction == 'left':
        if direction != 'right':   # In the previous incorrect code this was set as "new_direction != 'right'" but it should have been "direction"
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':    # same error here last time
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':    # And here
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':      # here too
            direction = new_direction


def check_collisions(snake):        # Previous incorrect code did not have "snake" between the parenthesis

    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:    # If left or right canvas borders are hit
        return True
    elif y < 0 or y >= GAME_HEIGHT: # if top or bottom borders are hit
        return True

    for body_part in snake.coordinates[1:]: # For running into its own body
        if x == body_part[0] and y == body_part[1]:
            return True

    return False


def game_over():

    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('arial',40), text="GAME OVER", fill="red", tag="gameover")

# window to run the game inside
window = Tk()
window.title("Snake game")
window.resizable(False, False)

score = 0
direction = 'down'

    # Label to display the score
label = Label(window, text="Score:{}".format(score), font=('arial', 40))
label.pack()

    # canvas for the snake to slither inside
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

    # Centering the window upon startup
window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # binding arrow keys to snake movement
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

    # Call the functions we defined above
snake = Snake()
food = Food()

next_turn(snake, food)

    # to keep the window open and responsive
window.mainloop()