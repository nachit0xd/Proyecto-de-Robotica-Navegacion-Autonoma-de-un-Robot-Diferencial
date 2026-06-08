"""controlador_e-puck controller."""

import math
from controller import Robot

# Constantes del e-puck
MAX_SPEED = 6.28 # Velocidad máxima de los motores (radianes por segundo)
WHEEL_RADIUS = 0.0205   # metros (radio de las ruedas)
AXLE_LENGTH = 0.052     # metros (distancia entre ruedas)

# Función para inicializar el robot y sus dispositivos
def init_robot():
    robot = Robot()
    timestep = int(robot.getBasicTimeStep())
    
    # 1) Inicializamos los motores y los ponemos en modo velocidad 
    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')
    
    # Modo control de velocidad: setPosition a infinito
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    
    # Velocidad inicial igual a 0
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)
    
    # 2) Inicializamos los encoders (sensores de posición de las ruedas)
    left_encoder = robot.getDevice('left wheel sensor')
    right_encoder = robot.getDevice('right wheel sensor')
    left_encoder.enable(timestep)
    right_encoder.enable(timestep)
    
    # 3) Inicializamos los sensores de proximidad (ps0 a ps7)
    ps = []
    for i in range(8):
        sensor_name = f'ps{i}'
        sensor = robot.getDevice(sensor_name)
        sensor.enable(timestep)
        ps.append(sensor)
        
    return robot, timestep, left_motor, right_motor, left_encoder, right_encoder, ps

# Función para establecer la velocidad de los motores con límites
def set_speed(left_motor, right_motor, left_speed, right_speed):
    left_speed = max(min(left_speed, MAX_SPEED), -MAX_SPEED)
    right_speed = max(min(right_speed, MAX_SPEED), -MAX_SPEED)
    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)

# Función principal del controlador
def main():
    # Inicializamos los componentes del robot
    robot, timestep, left_motor, right_motor, left_encoder, right_encoder, ps = init_robot()
    
    print("Controlador e-puck inicializado correctamente.")
    print("Motores, Encoders y Sensores de Proximidad listos.")
    
    # Variables de Odometría (relativas al punto de inicio)
    x = 0.0
    y = 0.0
    theta = 0.0
    
    # Realizamos un paso de simulación para que los sensores obtengan su primer valor
    robot.step(timestep)
    prev_left_enc = left_encoder.getValue()
    prev_right_enc = right_encoder.getValue()
    
    print("Iniciando odometría...")
    
    # Bucle principal
    while robot.step(timestep) != -1:
        # --- 1) CÁLCULO DE ODOMETRÍA ---
        curr_left_enc = left_encoder.getValue()
        curr_right_enc = right_encoder.getValue()
        
        # Diferencia de lectura en los encoders (radianes)
        delta_left_enc = curr_left_enc - prev_left_enc
        delta_right_enc = curr_right_enc - prev_right_enc
        
        # Guardamos los valores actuales para el siguiente paso
        prev_left_enc = curr_left_enc
        prev_right_enc = curr_right_enc
        
        # Distancia recorrida por cada rueda (metros) = delta_angulo * radio
        dist_left = delta_left_enc * WHEEL_RADIUS
        dist_right = delta_right_enc * WHEEL_RADIUS
        
        # Desplazamiento lineal (delta_s) y rotacional (delta_theta) del robot
        delta_s = (dist_right + dist_left) / 2.0
        delta_theta = (dist_right - dist_left) / AXLE_LENGTH
        
        # Actualización de la posición (x, y) y orientación (theta)
        # Usamos theta + delta_theta / 2.0 para una aproximación más precisa
        x += delta_s * math.cos(theta + delta_theta / 2.0)
        y += delta_s * math.sin(theta + delta_theta / 2.0)
        theta += delta_theta
        
        # Normalizamos theta al rango [-pi, pi]
        theta = math.atan2(math.sin(theta), math.cos(theta))
        
        # Imprimimos los valores de odometría aproximadamente cada 1 segundo (1000 ms) de simulación
        time_ms = int(robot.getTime() * 1000)
        if time_ms % 1000 < timestep:
            print(f"[Odometría] x: {x:.3f} m, y: {y:.3f} m, theta: {theta:.3f} rad") 
        # En las próximas fases aquí irá:
        # 2. Lectura de sensores IR -> Lógica reactiva
        # 3. Seguimiento de ruta -> Velocidad a los motores
        
        # PRUEBA: Movimiento circular lento para verificar que cambian x, y, theta
        # Cambiar a 0.0 cuando queramos detenerlo
        set_speed(left_motor, right_motor, 1.0, 1.5)

if __name__ == "__main__":
    main()
