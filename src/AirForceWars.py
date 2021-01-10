# Zaamin Rattansi
# AirForce Wars

# Import required library's
import pygame
import random
import time

# initiate pygame
pygame.init()

# set displayg
screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption('AirForce wars')

#load all audio files
crashSound = pygame.mixer.Sound("Audio/crashSound.wav")
introMusic = pygame.mixer.Sound("Audio/IntroMenuMusic.wav")
pygame.mixer.music.load("Audio/gameAudio.wav")

# open and read highscore text file
fileHandle = open("HighScore.txt", "r")
highScore = float(fileHandle.readline())
fileHandle.close()

# set clock
clock = pygame.time.Clock()

# Colours
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 180, 0)
red = (180, 0, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)


# Intro Menu
def intro_menu():
    # Play Intro menu music
    pygame.mixer.Sound.play(introMusic)
    #load background image
    introMenu = pygame.image.load("GameImages/introscreen.jpg").convert()

    # Re-open highscore (update highscore after playing)
    fileHandle = open("HighScore.txt", "r")
    highScore = float(fileHandle.readline())
    fileHandle.close()

    global bgG
    bgG = False

    # Intro menu loop
    intro = True
    while intro:

        # check if event quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()



        # display background image to screen
        screen.blit(introMenu,(0,0))


        # get position of mouse and/or check in mouse click
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()

        # check if Easter Egg button has been pressed
        if keys[pygame.K_c] and keys[pygame.K_m]:
            bgG = True
            gameLoop()


        # draw play button green button, if mouse over green button, button becomes bright green, if not, button is a darker green
        if 170 + 230 > mouse[0] > 170 and 420 + 80 > mouse[1] > 420:
            pygame.draw.rect(screen, bright_green, (170, 420, 230, 80))
            # if mouse click while hovering over button, go to gameLoop (play  game) function
            if click[0] == 1:
                intro = False
                gameLoop()
        else:
            pygame.draw.rect(screen, green, (170, 420, 230, 80))

        # displaying "play" on the green button
        smallText = pygame.font.Font("freesansbold.ttf", 35)
        textSurf, textRect = text_objects("Play", smallText)
        textRect.center = ( (170 + (230 / 2)) , (420 + (80/2)) )
        screen.blit(textSurf, textRect)


        # draw a red button for instructions, If mouse is hovering over button, a bright red button in drawn, if not, a darker red button
        if 800 + 230 > mouse[0] > 800 and 420 + 80 > mouse[1] > 420:
            pygame.draw.rect(screen, bright_red, (800, 420, 230, 80))
            # if mouse click while hovering over button, go to instructions function
            if click[0] == 1:
                instructions()
        else:
            pygame.draw.rect(screen, red, (800, 420, 230, 80))

        # display "instructions" on red button
        smallText = pygame.font.Font("freesansbold.ttf", 35)
        textSurf, textRect = text_objects("Instructions", smallText)
        textRect.center = ((800 + (230 / 2)), (420 + (80 / 2)))
        screen.blit(textSurf, textRect)


        # draw quit button red button, if mouse over red button, button becomes bright red, if not, button is a darker red
        if 1140 + 80 > mouse[0] > 1120 and 15 + 80 > mouse[1] > 15:
            pygame.draw.rect(screen, bright_red, (1140, 15, 50, 50))
            # if mouse click while hovering over button, go to gameLoop (play  game) function
            if click[0] == 1:
                intro = False
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(screen, red, (1140, 15, 50, 50))



        # displaying "quit" on the red button
        smallText = pygame.font.Font("freesansbold.ttf", 25)
        textSurf, textRect = text_objects("quit", smallText)
        textRect.center = ((1140 + (50 / 2)), (15 + (50 / 2)))
        screen.blit(textSurf, textRect)

        # display highscore in middle on intro menu screen
        message_display("High Score: " + str(round(highScore, 0)), 40)

        # update display every loop
        pygame.display.update()
        # set FPS
        clock.tick(30)


# instruction menu
def instructions():
    # get instructions menu image
    instructionImg = pygame.image.load("GameImages/instructions.jpg").convert()

    # intructions menu loop
    instructionScreen = True
    while instructionScreen:
        # check if user quits
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # display intructions menu image
        screen.blit(instructionImg,(0,0))

        # get mouse position and/or check if mouse click
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # draw a green button for instructions, If mouse is hovering over button, a bright green button in drawn, if not, a darker green button
        if 1010 + 150 > mouse[0] > 1010 and 530 + 60 > mouse[1] > 530:
            pygame.draw.rect(screen, bright_green, (1010, 530, 150, 60))
            if click[0] == 1:
                instructionScreen = False
        else:
            pygame.draw.rect(screen, green, (1010, 530, 150, 60))

        # display "back" on button
        small1Text = pygame.font.Font("freesansbold.ttf", 35)
        text1Surf, textRect = text_objects("back", small1Text)
        textRect.center = ( (970 + (230 / 2)) , (520 + (80/2)) )
        screen.blit(text1Surf, textRect)

        # update display every loop
        pygame.display.update()
        # set FPS
        clock.tick(30)

# fucntion used for displaying words
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

# fucntion used for displaying words
def message_display(text, size):
    largeText = pygame.font.Font('freesansbold.ttf', size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((1200/ 2), (600/2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()

# function to keep score
def score(count):
    font = pygame.font.SysFont(None, 45)
    text = font.render("Score: " +str(round(count, 0)), True, white)
    screen.blit(text, (0,0))

# crash function, display crashed, update highscore, play crash audio, return to intro menu
def crash(scoreCount, highScore):
    # play crash audio
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crashSound)
    # display "you crashed"
    message_display("You Crashed", 115)
    # update highscore
    if scoreCount > highScore:
        highScore = scoreCount
        addToFile(highScore)
    # wait 3 seconds
    time.sleep(3)
    # go to intro menu
    intro_menu()

# function to add highscore to file
def addToFile(highScore):
    fileHandle = open('HighScore.txt', 'w')
    fileHandle.writelines(str(highScore))
    fileHandle.close()

# player function, get and display player plane image
def player(playerX, playerY):
    playerImg = pygame.image.load("GameImages/flying-cartoon-plane.png").convert_alpha()
    screen.blit(playerImg,(playerX, playerY))

# missile function, get and display missile image
def missile(missileX, missileY):
    missileImg = pygame.image.load("GameImages/missile.png").convert_alpha()
    screen.blit(missileImg, (missileX, missileY))

# second missile function, get and display missile image
def missile2(missile2X, missile2Y):
    missile2Img = pygame.image.load("GameImages/missile.png").convert_alpha()
    screen.blit(missile2Img, (missile2X, missile2Y))

# enemy plane function, get and display enemy plane image
def enemyPlanes(enemyX, enemyY):
    enemyImg = pygame.image.load("GameImages/enemyPlane.png").convert_alpha()
    screen.blit(enemyImg, (enemyX, enemyY))

# enemy plane descending function, get and display descending plane plane image
def enemyPlanesDown(downX, downY):
    downPlaneImg = pygame.image.load("GameImages/PlaneDown.png").convert_alpha()
    screen.blit(downPlaneImg, (downX, downY))

# enemy plane ascending function, get and display ascending plane plane image
def enemyPlanesUp(UpX, UpY):
    UpPlaneImg = pygame.image.load("GameImages/fighter-plane.png").convert_alpha()
    screen.blit(UpPlaneImg, (UpX, UpY))

# Define what to do when paused
def paused():
    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((1200 / 2), (600 / 2))
    screen.blit(TextSurf, TextRect)

    pause = True

    # Run a loop to continue pause until pause is false
    while pause:
        # Check if player quits
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Check if space is pressed to unpause
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            pause = False

        # Update the display and set FPS
        pygame.display.update()
        clock.tick(15)

#The game loop
def gameLoop():

    # load Background image
    bg = pygame.image.load("GameImages/bg2.jpg").convert()

    # Play in game sound
    pygame.mixer.Sound.stop(introMusic)
    pygame.mixer.music.play(-1)

    # Variables
    crashed = False
    playerX = 30
    playerY = 350

    playerMove = 0
    bgX = 0

    fps = 30

    scoreCount = 0

    missileStartX = 10000
    missileStartY = random.randrange(0,600)
    missileSpeed = -15

    missile2StartX = 10000
    missile2StartY = random.randrange(0, 600)
    missile2Speed = -15

    enemyStartX = 1500
    enemyStartY = random.randrange(0,500)
    enemySpeed = -15

    planeDownStartX = 4500
    planeDownStartY = -900
    planeDownXSpeed = -30
    planeDownYSpeed = 8.5

    planeUpStartX = 5000
    planeUpStartY = 1500
    planeUpXSpeed = -30
    planeUpYSpeed = -8.5

    scoreIncrease = 0.2

    bgSpeed = 7

    # MR G MOSE EASTER EGG
    if bgG == True:
        # Display message
        message_display("CHEAT MODE :D", 60)
        time.sleep(2)
        # Change score increase
        scoreIncrease = 1
        # Change background image
        bg = pygame.image.load("GameImages/cheatMode.jpg").convert()


    # While loop for game
    while not crashed:

        # Allow player to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # Controlling player. Press up to move plane up, press down to move player down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    playerMove = -20

                if event.key == pygame.K_DOWN:
                    playerMove = 20
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    playerMove = 0

        playerY += playerMove

        # Check if Key P is pressed
        keys = pygame.key.get_pressed()

        if keys[pygame.K_p]:
            paused()


        # Draw rectangles behind each image, for collision, behind background so it is not visible
        playerRect1X = playerX
        playerRect1Y = playerY + 25
        playerRect2X = playerX + 90
        playerRect2Y = playerY + 10
        playerRect3X = playerX
        playerRect3Y = playerY + 5

        enemyPlaneRect1X = enemyStartX
        enemyPlaneRect1Y = enemyStartY + 50
        enemyPlaneRect2X = enemyStartX + 50
        enemyPlaneRect2Y = enemyStartY

        missileRectX = missileStartX
        missileRectY = missileStartY + 9

        missile2RectX = missile2StartX
        missile2RectY = missile2StartY + 9

        planeUpRect1X = planeUpStartX
        planeUpRect1Y = planeUpStartY + 40
        planeUpRect2X = planeUpStartX + 150
        planeUpRect2Y = planeUpStartY + 20

        planeDownRect1X = planeDownStartX + 20
        planeDownRect1Y = planeDownStartY + 140
        planeDownRect2X = planeDownStartX + 30
        planeDownRect2Y = planeDownStartY + 120
        planeDownRect3X = planeDownStartX + 100
        planeDownRect3Y = planeDownStartY + 100
        planeDownRect4X = planeDownStartX + 130
        planeDownRect4Y = planeDownStartY + 80
        planeDownRect5X = planeDownStartX + 150
        planeDownRect5Y = planeDownStartY
        planeDownRect6X = planeDownStartX + 60
        planeDownRect6Y = planeDownStartY + 50


        playerRect1 = pygame.draw.rect(screen, black, (playerRect1X, playerRect1Y, 190, 30))
        playerRect2 = pygame.draw.rect(screen, black, (playerRect2X, playerRect2Y, 50, 80))
        playerRect3 = pygame.draw.rect(screen, black, (playerRect3X, playerRect3Y, 25, 20))

        enemyPlaneRect1 = pygame.draw.rect(screen, black, (enemyPlaneRect1X, enemyPlaneRect1Y, 190, 30))
        enemyPlaneRect2 = pygame.draw.rect(screen, black, (enemyPlaneRect2X, enemyPlaneRect2Y, 30, 130))

        missileRect = pygame.draw.rect(screen, black, (missileRectX, missileRectY, 250, 30))

        missile2Rect = pygame.draw.rect(screen, black, (missile2RectX, missile2RectY, 250, 30))

        planeUpRect1 = pygame.draw.rect(screen, black, (planeUpRect1X, planeUpRect1Y, 150, 40))
        planeUpRect2 = pygame.draw.rect(screen, black, (planeUpRect2X, planeUpRect2Y, 35, 35))

        planeDownRect1 = pygame.draw.rect(screen, black, (planeDownRect1X, planeDownRect1Y, 30, 30))
        planeDownRect2 = pygame.draw.rect(screen, black, (planeDownRect2X, planeDownRect2Y, 50, 50))
        planeDownRect3 = pygame.draw.rect(screen, black, (planeDownRect3X, planeDownRect3Y, 50, 50))
        planeDownRect4 = pygame.draw.rect(screen, black, (planeDownRect4X, planeDownRect4Y, 50, 50))
        planeDownRect5 = pygame.draw.rect(screen, black, (planeDownRect5X, planeDownRect5Y, 30, 100))
        planeDownRect6 = pygame.draw.rect(screen, black, (planeDownRect6X, planeDownRect6Y, 50, 50))


        # Background
        rel_x = bgX % bg.get_rect().width
        screen.blit(bg, (rel_x - bg.get_rect().width, 0))
        if rel_x < 1200:
            screen.blit(bg, (rel_x, 0))

        bgX -= bgSpeed

        bgSpeed += 0.0125


        # Score
        score(scoreCount)
        scoreCount += scoreIncrease
        if scoreCount % 100 == 0:
            scoreIncrease += 0.1


        # Call on player function
        player(playerX, playerY)


        # if player gone over top edge, moved to bottom, if gone below bottom, moved to top
        if playerY < -30:
            playerY = 560

        if playerY > 560:
            playerY = -20


        # Missile function, move missile X to simulate it is coming towards player plane.
        missile(missileStartX, missileStartY)
        missileStartX += missileSpeed
        missileSpeed -= 0.025

        # re pasting the missile image to come back into the screen
        if missileStartX < -200:
            missileStartX = 10000
            missileStartY = random.randrange(0, 500)

        # check if each rectangle behind the missile image collides with the player rectangles
        if playerRect1.colliderect(missileRect):
            crashed = True
            crash(scoreCount, highScore)
        elif playerRect2.colliderect(missileRect):
            crashed = True
            crash(scoreCount, highScore)

        elif playerRect3.colliderect(missileRect):
            crashed = True
            crash(scoreCount, highScore)

        # Missile function, move missile X to simulate it is coming towards player plane.
        missile2(missile2StartX, missile2StartY)
        missile2StartX += missile2Speed
        missile2Speed -= 0.0375

        # re pasting the missile image to come back into the screen
        if missile2StartX < -200:
            missile2StartX = 10000
            missile2StartY = random.randrange(0, 500)

        # check if each rectangle behind the missile image collides with the player rectangles
        if playerRect1.colliderect(missile2Rect):
            crash(scoreCount, highScore)

        elif playerRect2.colliderect(missile2Rect):
            crash(scoreCount, highScore)

        elif playerRect3.colliderect(missile2Rect):
            crash(scoreCount, highScore)

        # Enemy plane function, move enemy plane X to simulate it is coming towards player plane.
        enemyPlanes(enemyStartX, enemyStartY)
        enemyStartX += enemySpeed
        enemySpeed -= 0.025

        # re pasting the enemy plane image to come back into the screen
        if enemyStartX < -200:
            enemyStartX = 5000
            enemyStartY = random.randrange(0,500)

        # check if each rectangle behind the enemy plane image collides with the player rectangles
        if playerRect1.colliderect(enemyPlaneRect1):
            crash(scoreCount, highScore)

        elif playerRect1.colliderect(enemyPlaneRect2):
            crash(scoreCount, highScore)

        elif playerRect2.colliderect(enemyPlaneRect1):
            crash(scoreCount, highScore)

        elif playerRect2.colliderect(enemyPlaneRect2):
            crash(scoreCount, highScore)

        elif playerRect3.colliderect(enemyPlaneRect1):
            crash(scoreCount, highScore)

        elif playerRect3.colliderect(enemyPlaneRect2):
            crash(scoreCount, highScore)

        # Enemy plane down function, move enemy plane X to simulate it is coming towards player plane.
        enemyPlanesDown(planeDownStartX, planeDownStartY)
        planeDownStartX += planeDownXSpeed
        planeDownStartY += planeDownYSpeed

        # re pasting the enemy plane down image to come back into the screen
        if planeDownStartX < -200:
            planeDownStartX = 4500
            planeDownStartY = -900

        # check if each rectangle behind the Plane Down image collides with the player rectangles
        if playerRect1.colliderect(planeDownRect1):
            crash(scoreCount, highScore)

        elif playerRect1.colliderect(planeDownRect2):
            crash(scoreCount, highScore)

        elif playerRect1.colliderect(planeDownRect3):
            crash(scoreCount, highScore)

        elif playerRect1.colliderect(planeDownRect4):
            crash(scoreCount, highScore)

        elif playerRect1.colliderect(planeDownRect5):
            crash(scoreCount, highScore)

        elif playerRect1.colliderect(planeDownRect6):
            crash(scoreCount, highScore)

        elif playerRect2.colliderect(planeDownRect1):
            crash(scoreCount, highScore)

        elif playerRect2.colliderect(planeDownRect2):
            crash(scoreCount, highScore)

        elif playerRect2.colliderect(planeDownRect3):
            crash(scoreCount, highScore)

        elif playerRect2.colliderect(planeDownRect4):
            crash(scoreCount, highScore)

        elif playerRect2.colliderect(planeDownRect5):
            crash(scoreCount, highScore)

        elif playerRect2.colliderect(planeDownRect6):
            crash(scoreCount, highScore)

        elif playerRect3.colliderect(planeDownRect1):
            crash(scoreCount, highScore)

        elif playerRect3.colliderect(planeDownRect2):
            crash(scoreCount, highScore)

        elif playerRect3.colliderect(planeDownRect3):
            crash(scoreCount, highScore)

        elif playerRect3.colliderect(planeDownRect4):
            crash(scoreCount, highScore)

        elif playerRect3.colliderect(planeDownRect5):
            crash(scoreCount, highScore)

        elif playerRect3.colliderect(planeDownRect6):
            crash(scoreCount, highScore)

        # Enemy plane Up function, move enemy plane X to simulate it is coming towards player plane.
        enemyPlanesUp(planeUpStartX, planeUpStartY)
        planeUpStartX += planeUpXSpeed
        planeUpStartY += planeUpYSpeed


        # re pasting the enemy plane up image to come back into the screen
        if planeUpStartX < -200:
            planeUpStartX = 5000
            planeUpStartY = 1500


        # check if each rectangle behind the plane up image collides with the player rectangles
        if playerRect1.colliderect(planeUpRect1):
            crash(scoreCount, highScore)

        elif playerRect1.colliderect(planeUpRect2):
            crash(scoreCount, highScore)

        elif playerRect2.colliderect(planeUpRect1):
            crash(scoreCount, highScore)

        elif playerRect2.colliderect(planeUpRect2):
            crash(scoreCount, highScore)

        elif playerRect3.colliderect(planeUpRect1):
            crash(scoreCount, highScore)

        elif playerRect3.colliderect(planeUpRect2):
            crash(scoreCount, highScore)


        pygame.display.flip()
        pygame.display.update()
        clock.tick(fps)

intro_menu()

quit()
