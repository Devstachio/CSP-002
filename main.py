from pydraw import *

# declare a screen
screen = Screen(800, 600, 'Launcher')

# declares the ship at location 10,10 with a width of 100 and a height of 20
ship = Rectangle(screen, 10, 10, 100, 20, Color('blue'))

# decleres the cannon at the bottom of the screen with a width of 50 and a height of 20
cannon = Rectangle(screen, screen.width()/2, screen.height(), 50, 20)
cannon.move(dx=0, dy=-cannon.height())

# declares the projectile at a location off screen
projectile = Oval(screen, -99999,0, 5, 5)

# declares the score text at the top of the screen
score_text = Text(screen,"Score: 0", screen.width()/2, 0)
score_text.move(-score_text.width()/2, 0)
score_text.score = 0

# moves the cannon to the x location of the mouse
def mousemove(location):
    cannon.moveto(location.x() - cannon.width()/2, cannon.y())

# subtracts 1 from the score then moves the projectile to the cannon and rotates it to the same rotation as the cannon
def mousedown(button, location):
    score_text.score -= 1

    projectile.moveto(cannon.center())
    projectile.rotation(cannon.rotation())

# checks to see if the key q is pressed and if it is it sets running to false to end the game
def keydown(key):
    global running
    if key == 'q':
        running = False

# needed to listen for mouse and key events
screen.listen()

# declares the variables needed for the game
running = True
fps = 30
direction = 5
projectile_speed = 10
# main game loop
while running:
    # move box
    ship.move(dx=direction, dy=0)

    # bounce box
    if ship.x() + ship.width() >= screen.width():
        ship.move(dx=-direction, dy=direction)
        direction = -direction
    elif ship.x() <= 0:
        ship.move(dx=-direction,dy=-direction)
        direction = -direction
        # move box down
       
    # move projectile
    projectile.move(dx=0, dy=-projectile_speed)

    # check for hit
    if(projectile.overlaps(ship) and not projectile.contains(ship)):
        projectile.moveto(-999999,0)
        # changes the color of the ship and increases the score
        if(ship.color() == Color('blue')):
            ship.color(Color('green'))
            score_text.score += 1
            ship.width((2*ship.width())/3)
        elif ship.color() == Color('green'):
            ship.color(Color('purple'))
            score_text.score += 2
            ship.width(ship.width()/3)
        else:
            ship.color(Color('blue'))
            score_text.score += 3
            ship.width(100)

    # update score
    score_text.text("Score: " + str(score_text.score))  

    # updates the screen
    screen.update()
    screen.sleep(1/fps)
    