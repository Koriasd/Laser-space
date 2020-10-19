import sys, pygame
# Inicializamos pygame
pygame.init()
	# Muestro una ventana de 800x600
size = 800, 600
screen = pygame.display.set_mode(size)
# Cambio el título de la ventana
Pygame.display.set_caption("asd")
# Inicializamos variables
width, height = 800, 600
speed = [1, 1]
white = 255, 255, 255
# Crea un objeto imagen pelota y obtengo su rectángulo
ball = pygame.image.load(“ball.png”)
ballrect = ball.get_rect()
# Crea un objeto imagen bate y obtengo su rectángulo
bate = pygame.image.load(“bate.png”)
baterect = bate.get_rect()
# Pongo el bate en el centro de la pantalla
baterect.move_ip(400, 260)
# Comenzamos el bucle del juego
run=True
while run:
	# Espero un tiempo (milisegundos) para que la pelota no vaya muy rápida
	pygame.time.delay(0)
	# Capturamos los eventos que se han producido
	for event in pygame.event.get():
		#Si el evento es salir de la ventana, terminamos
		if event.type == pygame.QUIT: run = False
	# Compruebo si se ha pulsado alguna tecla
	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP]:
		baterect=baterect.move(0, -1)
	if keys[pygame.K_DOWN]:
		baterect=baterect.move(0, 1)
	# Compruebo si hay colisión
	If baterect.colliderect(ballrect):
		speed[0] = - speed[0]
	# Muevo la pelota
	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width:
		speed[1] = -speed[1]
	#Pinto el fondo de blanco, dibujo la pelota y actualizo la pantalla
	screen.fill(white)
	screen.blit(ball, ballrect)
	pygame.display.flip()
	# Salgo de pygame
pygame.quit()