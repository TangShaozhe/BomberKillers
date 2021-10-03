
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
quit = Button(75,180,"Quit")
instruction = Button(75,260,"Instruction")


while screen_On:
    screen.blit(background,(0,0))
    if play_again.draw_Button():
        print("Play Again")
        cnt = 0
    if quit.draw_Button():
        print("Quit")
        pygame.quit()
    if instruction.draw_Button():
        print("Instruction")


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            screen_On = False    
    pygame.display.update()
pygame.quit()
