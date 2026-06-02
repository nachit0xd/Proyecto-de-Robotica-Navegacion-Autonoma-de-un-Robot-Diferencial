# Proyecto de Robótica: Navegación Autónoma de un Robot Diferencial

**Integrantes:** Ignacio Javier Carrillo Ramírez

**Curso:** ICI4150-1 Robótica y Sistemas Autónomos

**Línea de desarrollo:** Línea A - Planificación de rutas 

---

## Índice de Contenidos

1. [Objetivo del proyecto](#objetivo-del-proyecto)
2. [Descripción del robot, sensores y actuadores](#descripción-del-robot-sensores-y-actuadores)
3. [Descripción de los escenarios de prueba](#descripción-de-los-escenarios-de-prueba)

---

## Objetivo del proyecto

Este proyecto implementa un sistema de navegación autónoma para un robot móvil diferencial en el simulador Webots. El robot e-puck se debe desplazar desde una posición inicial definida hasta cierta meta dentro de un entorno con obstáculos, sin la intervención de un ser humano durante la ejecución.

La solución alcanzada integra tres capas de funcionamiento: **control cinemático diferencial** para la ejecución de movimiento, **odometría basada en encoders de rueda** para la estimación continua de posición, y **planificación global de rutas** mediante el algoritmo A* sobre una grilla de ocupación 2D. Además, se incorpora una capa de navegación reactiva que permite al robot responder rápidamente ante obstáculos no contemplados en el mapa.

Este trabajo extiende los conceptos desarrollados en los Laboratorios 1 y 2 del curso de Robótica y Sistemas Autónomos, integrando el modelo de control de ruedas, la lectura y filtrado de sensores de distancia, y la estimación de movimiento por odometría, dentro de una arquitectura de navegación completa.

---

## Descripción del robot, sensores y actuadores


## Descripción de los escenarios de prueba

