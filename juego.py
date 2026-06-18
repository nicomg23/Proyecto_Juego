import pygame
import random
pygame.init ()

#PERSONAJES(CLASES)

class Cubo:
     def __init__(self, x, y):
          self.x=x
          self.y=y
          self.ancho= 50
          self.alto=50
          self.velocidad= 10
          self.color= "blue"
          self.rect= pygame.Rect(self.x, self.y, self.ancho, self.alto)


     def dibujar(self, VENTANA):
         pygame.draw.rect(VENTANA, self.color, self.rect)
         self.rect= pygame.Rect(self.x, self.y, self.ancho, self.alto)

class Enemigo:
     def __init__(self, x, y):
          self.x=x
          self.y=y
          self.ancho= 50
          self.alto=50
          self.velocidad= 5
          self.color= "red"
          self.rect= pygame.Rect(self.x, self.y, self.ancho, self.alto)


     def dibujar(self, VENTANA):
         pygame.draw.rect(VENTANA, self.color, self.rect)
         self.rect= pygame.Rect(self.x, self.y, self.ancho, self.alto)
    
     def movimiento(self):
           self.y += self.velocidad



class Bala:
     def __init__(self, x, y):
          self.x=x
          self.y=y
          self.ancho= 10
          self.alto=10
          self.velocidad= 7
          self.color= "yellow"
          self.rect= pygame.Rect(self.x, self.y, self.ancho, self.alto)


     def dibujar(self, VENTANA):
         pygame.draw.rect(VENTANA, self.color, self.rect)
         self.rect= pygame.Rect(self.x, self.y, self.ancho, self.alto)
    
     def movimiento(self):
           self.y -= self.velocidad







#DEF

def crear_bala():
      global ultima_bala

      if pygame.time.get_ticks()-ultima_bala > tiempo_entre_bala:
            balas.append(Bala(cubo.rect.centerx, cubo.rect.centery))
            ultima_bala = pygame.time.get_ticks()
      

def gestionar_teclas(teclas):
    if teclas [pygame.K_w]:
            cubo.y -=cubo.velocidad
    if teclas [pygame.K_s]:
            cubo.y +=cubo.velocidad
    if teclas [pygame.K_a]:
            cubo.x -=cubo.velocidad
    if teclas [pygame.K_d]:
            cubo.x +=cubo.velocidad
    if teclas [pygame.K_SPACE]:
            crear_bala()
        



#MENUS

ancho=800
alto=600
VENTANA=pygame.display.set_mode([ancho,alto])
pygame.display.set_caption("TOTAL WAR")
VENTANA.fill((0,0,0))
fps=60
FUENTE= pygame.font.SysFont("Arial BLackaaaaad", 40)

jugando=True
cubo=Cubo (100,100)

reloj = pygame.time.Clock()

vidas= 5
puntos= 0

tiempo_pasado = 0
tiempo_entre_enemigos = 500

enemigos = []
enemigos.append(Enemigo(ancho/2, 100))

balas=[]
ultima_bala= 0
tiempo_entre_bala= 400



while jugando and vidas>0:
    tiempo_pasado += reloj.tick(fps)
    if tiempo_pasado > tiempo_entre_enemigos:
          enemigos.append(Enemigo (random.randint(0,ancho),-50))
          tiempo_pasado = 0

    eventos =pygame.event.get()

    teclas=pygame.key.get_pressed()

    texto_vida= FUENTE.render(f"Vida: {vidas}", True, "white")
    texto_puntos= FUENTE.render(f"Puntos: {puntos}", True, "white")

    gestionar_teclas(teclas)

    for evento in eventos:
                if evento.type == pygame.QUIT:
                    jugando=False

    VENTANA.fill("black")

    cubo.dibujar(VENTANA)


    for enemigo in enemigos:
          enemigo.dibujar(VENTANA)
          enemigo.movimiento()
          if pygame.Rect.colliderect(cubo.rect, enemigo.rect):
                print("HAS PERDIDO")
                vidas -= 1
                print(f"te quedan {vidas} vidas")
                enemigos.remove(enemigo)
          if enemigo.y + enemigo.alto>alto:
                puntos+= 1
                enemigos.remove(enemigo)
          for bala in balas:
                if pygame.Rect.colliderect(bala.rect, enemigo.rect):
                      enemigos.remove(enemigo)
                      balas.remove(bala)
                      

    for bala in balas:
          bala.dibujar(VENTANA)
          bala.movimiento()


    VENTANA.blit(texto_vida, (0,0))
    VENTANA.blit(texto_puntos, (0,30))
          




    pygame.display.update()



quit()