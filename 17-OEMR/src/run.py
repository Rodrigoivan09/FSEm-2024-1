import keyboard
import inputs
import pygame
import sys
import os
import subprocess


import inputs
import keyboard  

# Configura el botón de tu mando que quieres asignar
boton_a = 'BTN_SELECT'  # Puedes verificar el nombre del botón usando un código de prueba (más abajo)


def enviar_esc():
    # Ejecutar el comando xdotool para enviar la tecla "Esc"
    subprocess.run(['xdotool', 'key', 'Escape'])

# Coloca tu código principal aquí



# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((1800, 1000))
pygame.display.set_caption('Menú con mando de PlayStation')

#Cargar sonido
button_sound = pygame.mixer.Sound("/home/sonido2.wav")
button_sound2 = pygame.mixer.Sound('/home/sonido1.wav')  


# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Fuente y texto
font = pygame.font.Font(None, 36)
options = ["1. Super Mario Bros 3", "2. Super Mario World", "3. Captan America", "4. Chip 'n Dale - Rescue Rangers 2",
           "5. Donkey Kong Classics", "6. DuckTales", "7. Flintstones 2", "8. Ninja Gaiden",
           "9. Shadow Warriors 2", "10. Simpsons, The - Bartman Meets Radioactive Man", "11. Teenage Mutant Ninja Turtles", "12. Terminator",
           "13. Tiny Toon Adventures", "14. Legend of Zelda", "15. Metroid", "APAGAR","REINICIAR"]
selected_option = 0
change_speed = 1
delay = 160
BUTTON_TO_EXIT = 6 

def close_mednafen():
    subprocess.run(['pkill', 'mednafen']) 
    
def play_rom(rom_path): 
    print("Iniciando Mednafen...")
    subprocess.call(["/usr/games/mednafen", rom_path])  # Ejecutar Mednafen con la ruta de la ROM
    
# Código correspondiente al botón que deseas asignar como F12

BOTON_A_ASIGNAR = 'BTN_SELECT'

def verificar_botones():
    events = inputs.get_gamepad()
    for event in events:
        if event.ev_type == 'Key' and event.code == BOTON_A_ASIGNAR:
            if event.state == 1:  # Verifica si el botón está siendo presionado
                #keyboard.press_and_release('F12')
                close_mednafen()
                
# Loop principal
while True:
    
    screen.fill(BLACK)
    
    
    # Dibujar las opciones
    for i, option in enumerate(options):
        text = font.render(option, True, WHITE if i != selected_option else GREEN)
        text_rect = text.get_rect(center=(1000, 50 * i + 50))
        screen.blit(text, text_rect)

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Detección del mando de PlayStation
    joystick_count = pygame.joystick.get_count()
    if joystick_count > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()

        # Lectura de los botones del mando
        up_button = joystick.get_button(3)
        down_button = joystick.get_button(1)
        select_button= joystick.get_button(0)
   
        if up_button:
            selected_option = (selected_option - change_speed) % len(options)
            button_sound.play()
            pygame.time.wait(delay)
            
        if down_button:
            selected_option = (selected_option + change_speed) % len(options)
            button_sound.play()
            pygame.time.wait(delay)

        # Botón de selección (puedes cambiar el número de botón según el mando)
        select_button = joystick.get_button(0)
        if select_button:
            print(f"Seleccionaste la opción: {options[selected_option]}")
            button_sound2.play()
            #selected = True
            if selected_option == 0:
                play_rom("/home/rms/SMB3.nes")          
            elif selected_option == 1:
              play_rom("/home/rms/SMW.nes")
            elif selected_option == 2:
              play_rom("/home/rms/CAPAME.nes.nes")
            elif selected_option == 3:
              play_rom("/home/rms/Chip 'n Dale - Rescue Rangers 2 (USA).nes")
            elif selected_option == 4:
              play_rom("/home/rms/Donkey Kong Classics (USA, Europe).nes")
            elif selected_option == 5:
              play_rom("/home/rms/DuckTales (USA).nes")
            elif selected_option == 6:
              play_rom("/home/rms/Flintstones 2 - The Surprise at Dinosaur Peak!, The (U).nes")
            elif selected_option == 7:
              play_rom("/home/rms/Ninja Gaiden (USA).nes")
            elif selected_option == 8:
              play_rom("/home/rms/Shadow Warriors 2 (E) [!].nes")
            elif selected_option == 9:
              play_rom("/home/rms/Simpsons, The - Bartman Meets Radioactive Man (USA).nes")
            elif selected_option == 10:
              play_rom("/home/rms/Teenage Mutant Ninja Turtles (USA).nes")
            elif selected_option == 11:
              play_rom("/home/rms/Terminator, The (USA, Europe).nes")
            elif selected_option == 12:
              play_rom("/home/rms/Tiny Toon Adventures (USA).nes")
            elif selected_option == 13:
              play_rom("/home/rms/Legend of Zelda, The (U) (PRG1) [!].nes")
            elif selected_option == 14:
              play_rom("/home/rms/Metroid (U).nes")
            elif selected_option == 15:
               print("Apagando...")
               os.system("sudo shutdown now")
            elif selected_option == 17:
              print("Reiniciando...")
              os.system("sudo reboot")
            
            #if not select_button:
             #     selected = False	   


               
    # Actualizar la pantalla
    pygame.display.flip()
    #verificar_botones()
    
    

    
