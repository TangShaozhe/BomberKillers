
import pygame

# activate the pygame library
pygame.init()


# white,black, gray, blue colour .
white = "#FFFFFF"
gray = "#808080"
blue = "#0000FF"
black = "#000000"
# assigning values to Height and Width variable
Height = 540
Width = 640

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

# create a text surface object,
# on which text is drawn on it.
text = font.render('Instruction How to Play the Game', True, blue, white)

# create a rectangular object for the
# text surface object
textRect = text.get_rect()

# set the location  of the rectangular object.
textRect.center = (270,20)

# infinite loop
while True:

	# completely fill the surface object
	# with white color
	display_surface.fill(black)

	# copying the text surface object
	# to the display surface object
	# at the center coordinate.
	display_surface.blit(text, textRect)

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
