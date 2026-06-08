# Proyecto de Robótica: Navegación Autónoma de un Robot Diferencial

**Integrantes:** Ignacio Javier Carrillo Ramírez

**Curso:** ICI4150-1 Robótica y Sistemas Autónomos

**Línea de desarrollo:** Línea A - Planificación de rutas 

---

## Índice de Contenidos

1. [Objetivo del proyecto](#objetivo-del-proyecto)
2. [Descripción del robot, sensores y actuadores](#descripción-del-robot-sensores-y-actuadores)
3. [Descripción de los escenarios de prueba](#descripción-de-los-escenarios-de-prueba)
4. [Algoritmo implementado](#algoritmo-implementado)

---

## Objetivo del proyecto

Este proyecto implementa un sistema de navegación autónoma para un robot móvil diferencial en el simulador Webots. El robot e-puck se debe desplazar desde una posición inicial definida hasta cierta meta dentro de un entorno con obstáculos, sin la intervención de un ser humano durante la ejecución.

La solución alcanzada integra tres capas de funcionamiento: **control cinemático diferencial** para la ejecución de movimiento, **odometría basada en encoders de rueda** para la estimación continua de posición, y **planificación global de rutas** mediante el algoritmo A* sobre una grilla de ocupación 2D. Además, se incorpora una capa de navegación reactiva que permite al robot responder rápidamente ante obstáculos no contemplados en el mapa.

Este trabajo extiende los conceptos desarrollados en los Laboratorios 1 y 2 del curso de Robótica y Sistemas Autónomos, integrando el modelo de control de ruedas, la lectura y filtrado de sensores de distancia, y la estimación de movimiento por odometría, dentro de una arquitectura de navegación completa.

---

## Descripción del robot, sensores y actuadores

El robot usado en las pruebas de Webots es el **e-puck**, un robot móvil diferencial de dos ruedas. Sus características esenciales son:

- **Actuadores:** cuenta con dos motores DC con control independiente de velocidad angular (en rueda izquierda y derecha), que permiten un movimiento recto, rotación en el lugar y trayectorias curvas mediante diferencia de velocidades.
- **Sensores de distancia:** cuenta con ocho sensores infrarrojos de proximidad (PS0 - PS7) distribuidos perimetralmente, utilizados para la detección de obstáculos en la navegación reactiva local del robot.
- **Encoders de rueda:** cuenta con sensores de posición angular integrados en cada motor, utilizados para calcular el desplazamiento incremental y estimar la posición del e-puck mediante **odometría**.

---

## Descripción de los escenarios de prueba

El sistema fue evaluado en dos escenarios de prueba en Webots con distinta dificultad: simple y complejo. Ambos escenarios utilizan un robot e-puck sobre un suelo plano sencillo.

### Escenario 1 — Habitación con obstáculos dispersos (simple)

| Parámetro           | Valor                             |
|---------------------|-----------------------------------|
| Dimensiones mundo   | 3 × 3 m                           |
| Grilla de ocupación | 30 × 30 celdas (0.1 m/celda)      |
| Posición inicial    | (0.3, 0.3) — esquina SOE          |
| Meta                | (2.8, 2.8) — esquina NE           |
| Paredes internas    | 2 segmentos de pared (`Wall`)     |
| Obstáculos sueltos  | 4 cajas (`SolidBox`) dispersas    |

**Descripción del escenario:** El entorno está compuesto de dos paredes internas que crean unos pasillos amplios, con cuatro cajas dispersas que generan situaciones de evasión local. La ruta entre el inicio y la meta requiere de al menos un giro, pero la complejidad del escenario es baja y útil para verificar el comportamiento correcto del controlador de movimiento y el planificador de algoritmo A*.

**Objetivo:** Sirve como base para métricas (ejemplo: tiempo de navegación, longitud de la ruta, posibles colisiones) con las cuales comparar los resultados obtenidos en el escenario complejo.

### Escenario 2 — Habitación mixta con zona bloqueada (complejo)

| Parámetro           | Valor                                   |
|---------------------|-----------------------------------------|
| Dimensiones mundo   | 3 × 3 m                                 |
| Grilla de ocupación | 30 × 30 celdas (0.1 m/celda)            |
| Posición inicial    | (0.2, 0.2) — esquina SOE                |
| Meta                | (2.8, 2.8) — esquina NE                 |
| Paredes internas    | 4 segmentos (4 pasillos con obstáculos) |
| Obstáculos sueltos  | 7 cajas-barriles                        |

**Descripción del escenario:** El entorno se conforma por cuatro segmentos delimitados por pared y obstáculos que forman zonas parcialmente bloqueadas, forzando al planificador a hallar otras rutas. Algunos espacios entre paredes y obstáculos son bastante angostos para que el e-puck pueda atravesarlos sin chocar, pero exigen precisión elevada. Los obstáculos están posicionados de forma que el e-puck deba activar la capa de evasión reactiva durante la navegación de su ruta óptima.

**Objetivo:** Exigir al máximo el sistema de navegación con mayor complejidad en la posición de los obstáculos y verificar que el robot es capaz de navegar en estos tipos de escenarios sin colisiones y de forma eficiente.

### Objetos de Webots utilizados

| Objeto           | Uso                      | Parámetros clave                  |
|------------------|--------------------------|-----------------------------------|
| `RectangleArena` | Suelo y bordes           | floorSize = (3,3)         |
| `Wall`           | Paredes internas         | size = (0.05, largo variado, 0.2)          |
| `SolidBox`            | Obstáculos rectangulares | size = (0.3, 0.3, 0.3)              |
| `OilBarrel`       | Obstáculos cilindricos    | radius = 0.1, height = 0.3          |

Todos los obstáculos son **objetos sólidos y estáticos**, es decir, no se mueven de su posición si el e-puck choca con ellos.

---

## Algoritmo implementado

### Grilla de Ocupación

### Algoritmo A*

### Conversión de ruta a waypoints
