from pydraw import *

screen = Screen(800, 600, 'Launcher')

# declare box, and launcher

ship = Rectangle(screen, 10, 10, 100, 20, Color('blue'))

cannon = Rectangle(screen, screen.width()/2, screen.height(), 50, 20)
cannon.move(dx=0, dy=-cannon.height())

projectile = Oval(screen, -99999,0, 5, 5)

score_text = Text(screen,"Score: 0", screen.width()/2, 0)
score_text.move(-score_text.width()/2, 0)
score_text.score = 0


def mousemove(location):
    cannon.moveto(location.x() - cannon.width()/2, cannon.y())

def mousedown(button, location):
    score_text.score -= 1

    projectile.moveto(cannon.center())
    projectile.rotation(cannon.rotation())

def keydown(key):
    global running
    if key == 'q':
        running = False

screen.listen()

running = True
fps = 30
direction = 5
projectile_speed = 10
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

    score_text.text("Score: " + str(score_text.score))  

    screen.update()
    screen.sleep(1/fps)
    