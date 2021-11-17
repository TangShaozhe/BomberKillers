
import pygame
from pygame.locals import *


pygame.init()
#Function for setting the caption of game
pygame.display.set_caption("Bomberman")
heigh,width = 720,540
#Function for dispalying the screen 
screen = pygame.display.set_mode((heigh,width))

#Define the font that will be used in game
font = pygame.font.SysFont("Aguda", 32)

#Function used to load the image at background

background = pygame.image.load("bg.jpg")
#Bool variable to turn on the screen
screen_On = True

#Defined some famous colors
red = (255,0,0)
black = "#000000"
white = (255,255,255)

#define the goble variable
clicked = False
cnt = 0

# #Here Button class is defined
class Button():
    
    
    button_color ="#58D68D"
    hover_color = "#87ceeb"
    mouse_clicked_color = "#0E6655"
    text_color = black
    btn_width,btn_height = 350,60
    #constructor of Button class(x,y at which postion our button will start)
    def __init__(self,x,y,text):
        self.x = x    
        self.y = y
        self.text = text

    #functon to draw the Button
    def draw_Button(self):
        global clicked
        action = False

        #For getting the position of mouse
        position = pygame.mouse.get_pos()

        #For creating the Pygame rectangular area of the object (Button)
        button_Rect = Rect(self.x,self.y,self.btn_width,self.btn_height)
        #For checking the Mouse over
        if button_Rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked  = True
                pygame.draw.rect(screen,self.mouse_clicked_color,button_Rect)
            
            elif pygame.mouse.get_pressed()[0] == 0 and (clicked == True):
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_color, button_Rect)
        else:
            pygame.draw.rect(screen, self.button_color, button_Rect)

        #adding the shadow to the Button 
        pygame.draw.line(screen, white, (self.x, self.y), (self.x + self.btn_width, self.y), 2)
        pygame.draw.line(screen, white, (self.x, self.y), (self.x, self.y + self.btn_height), 2)
        pygame.draw.line(screen, white, (self.x, self.y + self.btn_height), (self.x + self.btn_width, self.y + self.btn_height), 2)
        pygame.draw.line(screen, white, (self.x + self.btn_width, self.y), (self.x + self.btn_width, self.y + self.btn_height), 2)

        #add text to button
        text_img = font.render(self.text, True, self.text_color)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.btn_width / 2) - int(text_len / 2), self.y + 25))
        return action
#play  = Button(75,100,"Play")
play_again = Button(75,100, "Play Again")
play_vs_bot = Button(75,175,"Player vs Bot")
instruction = Button(75,250,"Instruction")
quit = Button(75,325,"Quit")


def showInstruction():
    pygame.init()


 # activate the pygame library
    pygame.init()


    # white,black, gray, blue colour .
    white = "#FFFFFF"
    gray = "#808080"
    blue = "#0000FF"
    black = "#000000"
    # assigning values to Height and Width variable
    Height = 720
    Width = 540

    # create the display surface object
    # of specific dimension..e(Height, Width).
    display_surface = pygame.display.set_mode((Height, Width))

    # set the pygame window name
    pygame.display.set_caption('Instruction')

    # create a font object.
    # 1st parameter is the font file
    # which is present in pygame.
    # 2nd parameter is size of the font
    font = pygame.font.Font('freesansbold.ttf', 32)
    font1 = pygame.font.Font('freesansbold.ttf', 22)
    # create a text surface object,
    # on which text is drawn on it.
    text = font.render('Instruction How to Play the Game', True, white, black)
    text1 = font1.render('Instructions for One Player - Kill the AI monsters!',True,white,black)
    text2 = font1.render('Instructons for Two Players - Fight off each other!',True,white,black)
    text3 = font.render('---ONE PLAYER---',True,white,black)
    text4 = font1.render('Use Arrow keys to move the Player',True,white,black)
    text5 = font1.render('Use Space Bar in order to drop balloons',True,white,black)
    text6 = font1.render('Use Left Shift to use the items',True,white,black)
    text7 = font.render('---TWO PLAYER---',True,white,black)
    text8 = font1.render('Use Arrow Keys and (W,A,S,D) keys for move',True,white,black)
    text9 = font1.render('Use Left Shift and Right Shift to drop balloons',True,white,black)
    text10 = font1.render('Use Left control and space bar to use items',True,white,black)
    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()
    textRect1 = text1.get_rect()
    textRect2 = text2.get_rect()
    textRect3 = text3.get_rect()
    textRect4 = text4.get_rect()
    textRect5 = text5.get_rect()
    textRect6 = text6.get_rect()
    textRect7 = text7.get_rect()
    textRect8 = text8.get_rect()
    textRect9 = text9.get_rect()
    textRect10 = text10.get_rect()
    # set the location  of the rectangular object.
    textRect = (0,0)
    textRect1 = (0,40)
    textRect2 =(0,70)
    textRect3 =(0,100)
    textRect4 = (0,130)
    textRect5 = (0,160)
    textRect6 = (0,190)
    textRect7 = (0,220)
    textRect8 = (0,250)
    textRect9 = (0,280)
    textRect10 = (0,310)
    # infinite loop
    while True:

    	# completely fill the surface object
    	# with white color
    	display_surface.fill(black)

    	# copying the text surface object
    	# to the display surface object
    	# at the center coordinate.
    	display_surface.blit(text, textRect)
    	display_surface.blit(text1,textRect1)
    	display_surface.blit(text2,textRect2)
    	display_surface.blit(text3,textRect3)
    	display_surface.blit(text4,textRect4)
    	display_surface.blit(text5,textRect5)
    	display_surface.blit(text6,textRect6)
    	display_surface.blit(text7,textRect7)
    	display_surface.blit(text8,textRect8)
    	display_surface.blit(text9,textRect9)
    	display_surface.blit(text10,textRect10)
    	# iterate over the list of Event objects
    	# that was returned by pygame.event.get() method.
    	for event in pygame.event.get():

    		# if event object type is QUIT
    		# then quitting the pygame
    		# and program both.
    		if event.type == pygame.QUIT:

    			# deactivates the pygame library
    			pygame.quit()

    			# quit the program.
    			quit()

    		# Draws the surface object to the screen.
    		pygame.display.update()


while screen_On:
    screen.blit(background,(0,0))
    #if the Player want to play game again
    if play_again.draw_Button():
        print("Play Again")

    #if playe want to quit the Game    
    if quit.draw_Button():
        print("Quit")
        pygame.quit()
    #if player and bot want to play game between them
    if play_vs_bot.draw_Button():
        print("Player and Bot are palying the game")    
    #if you want to see the instructions and rules for the game    
    if instruction.draw_Button():
        print("instruction")
        showInstruction()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            screen_On = False    
    pygame.display.update()
pygame.quit()
