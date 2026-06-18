Total War — Juego en Python con Pygame

Juego de tipo shooter vertical desarrollado en Python utilizando Pygame. Proyecto personal para practicar Programación Orientada a Objetos (POO).


Cómo se juega


Controlás un cubo azul que se mueve por la pantalla
Enemigos rojos caen desde arriba a velocidad constante
Disparás balas amarillas para eliminarlos antes de que te toquen
Cada enemigo que pasa por abajo de la pantalla suma un punto
Tenés 5 vidas — si un enemigo te golpea, perdés una


Controles:

TeclaAcciónWMover arribaSMover abajoAMover izquierdaDMover derechaSPACEDisparar


Estructura del código

El juego está organizado en tres clases principales:

Cubo        → jugador controlado por el usuario
Enemigo     → entidades que caen desde arriba, con movimiento propio
Bala        → proyectiles disparados por el jugador

Cada clase encapsula sus propios atributos (posición, velocidad, color, tamaño) y métodos (dibujar, movimiento). La detección de colisiones se maneja con pygame.Rect.colliderect.


Tecnologías


Python 3
Pygame
POO (clases, atributos, métodos)
Gestión de eventos y ciclo de juego (game loop)
Detección de colisiones



Requisitos

bashpip install pygame

Cómo ejecutar

bashpython juego.py
