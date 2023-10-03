import pygame

pygame.init()
pygame.display.set_caption('caculadora')
LARGURA = 400
ALTURA = 600
screen = pygame.display.set_mode((LARGURA, ALTURA))
running = True
font = pygame.font.Font('Lato-Black.ttf', 42)
display = ''

def draw():
  global b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16
  pygame.draw.rect(screen, (101, 101, 112), (0,0,400,600))
  pygame.draw.rect(screen, (151, 237, 145), (40,50,320,100))
  
  b1=pygame.draw.rect(screen, (41, 51, 42), (15,220,70,40))
  b2=pygame.draw.rect(screen, (41, 51, 42), (15,280,70,40))
  b3=pygame.draw.rect(screen, (41, 51, 42), (15, 340,70,40))
  b4=pygame.draw.rect(screen, (41, 51, 42), (15,400,70,40))
  b5=pygame.draw.rect(screen, (41, 51, 42), (115,220,70,40))
  b6=pygame.draw.rect(screen, (41, 51, 42), (115,280,70,40))
  b7=pygame.draw.rect(screen, (41, 51, 42), (115,340,70,40))
  b8=pygame.draw.rect(screen, (41, 51, 42), (115,400,70,40))
  b9=pygame.draw.rect(screen, (41, 51, 42), (215,220,70,40))
  b10=pygame.draw.rect(screen, (41, 51, 42), (215,280,70,40))
  b11=pygame.draw.rect(screen, (41, 51, 42), (215,340,70,40))
  b12=pygame.draw.rect(screen, (255, 0, 17), (215,400,70,40))
  b13=pygame.draw.rect(screen, (41, 51, 42), (315,220,70,40))
  b14=pygame.draw.rect(screen, (41, 51, 42), (315,280,70,40))
  b15=pygame.draw.rect(screen, (41, 51, 42), (315,340,70,40))
  b16=pygame.draw.rect(screen, (41, 51, 42), (315,400,70,40))

def load():
  global t, t2, t3, t4, t5, t6, t7, t8, t9, t0, m1, m2, m3, m4, m5, m6

  t = font.render("1", False,(240,240,240))
  screen.blit(t, (35,215))
  t2 = font.render("4", False,(240,240,240))
  screen.blit(t2, (35,275))
  t3 = font.render("7", False,(240,240,240))
  screen.blit(t3, (35,335))
  t4 = font.render("2", False,(240,240,240))
  screen.blit(t4, (35,395))
  t5 = font.render("5", False,(240,240,240))
  screen.blit(t5, (135,215))
  t6 = font.render("8", False,(240,240,240))
  screen.blit(t6, (135,275))
  t7 = font.render("3", False,(240,240,240))
  screen.blit(t7, (135,335))
  t8 = font.render("6", False,(240,240,240))
  screen.blit(t8, (135,395))
  t9 = font.render("9", False,(240,240,240))
  screen.blit(t9, (245,215))
  t0 = font.render("*", False,(240,240,240))
  screen.blit(t0, (345,400))
  m1 = font.render("/", False,(240,240,240))
  screen.blit(m1, (345,335))
  m2 = font.render("+", False,(240,240,240))
  screen.blit(m2, (345,275))
  m3 = font.render("-", False,(240,240,240))
  screen.blit(m3, (345,215))
  m4 = font.render("AC", False,(0, 0, 0))
  screen.blit(m4,(223,395))
  m5 = font.render("0", False,(240, 240, 240))
  screen.blit(m5,(240,275))
  m6 = font.render("=", False,(240, 240, 240))
  screen.blit(m6,(240,335))
  d = font.render(display, False,(0,0,0))
  screen.blit(d, (60, 70))
load()

def conta():
  global display

  c = 0
  for i in display:
    if i in ["+", "-", "*", "/"]:
      n1 = float(display[:c])
      n2 = float(display[c+1:-1])
      sinal = i
    c+=1

  if sinal == "+":
    r = n1+n2
  if sinal == "-":
    r = n1-n2
  if sinal == "*":
    r = n1*n2
  if sinal == "/":
    r = n1/n2

  display+=str(r)



while running:
  draw()
  load()
  
    
    
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
       running = False
    if event.type ==pygame.MOUSEBUTTONDOWN:
      if b1.collidepoint(pygame.mouse.get_pos()):
        display += '1'
      if b4.collidepoint(pygame.mouse.get_pos()):
        display += '2'
      if b7.collidepoint(pygame.mouse.get_pos()):
        display += '3'
      if b2.collidepoint(pygame.mouse.get_pos()):
        display += '4'
      if b5.collidepoint(pygame.mouse.get_pos()):
        display += '5'
      if b8.collidepoint(pygame.mouse.get_pos()):
        display += '6'
      if b3.collidepoint(pygame.mouse.get_pos()):
        display += '7'
      if b6.collidepoint(pygame.mouse.get_pos()):
        display += '8'
      if b9.collidepoint(pygame.mouse.get_pos()):
        display += '9'
      if b10.collidepoint(pygame.mouse.get_pos()):
        display += '0'
      if b14.collidepoint(pygame.mouse.get_pos()):
        display += '+'
      if b13.collidepoint(pygame.mouse.get_pos()):
        display += '-'
      if b15.collidepoint(pygame.mouse.get_pos()):
        display += '/'
      if b16.collidepoint(pygame.mouse.get_pos()):
        display += '*'  
      if b12.collidepoint(pygame.mouse.get_pos()):
        display = ''
      if b11.collidepoint(pygame.mouse.get_pos()):
        display += '='
        conta()
        
  pygame.display.update()

pygame.quit()        