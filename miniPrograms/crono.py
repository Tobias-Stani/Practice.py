import time
import os
import shutil  # Para obtener el ancho de la consola

# Definición de los números en ASCII
numeros_ascii = {
    '0': [
        " ##### ",
        "#     #",
        "#     #",
        "#     #",
        "#     #",
        "#     #",
        " ##### "
    ],
    '1': [
        "   #   ",
        "  ##   ",
        "   #   ",
        "   #   ",
        "   #   ",
        "   #   ",
        " ##### "
    ],
    '2': [
        " ##### ",
        "#     #",
        "      #",
        " ##### ",
        "#      ",
        "#      ",
        "#######"
    ],
    '3': [
        " ##### ",
        "#     #",
        "      #",
        "  #### ",
        "      #",
        "#     #",
        " ##### "
    ],
    '4': [
        "#    # ",
        "#    # ",
        "#    # ",
        "#######",
        "     # ",
        "     # ",
        "     # "
    ],
    '5': [
        "#######",
        "#      ",
        "#      ",
        "###### ",
        "      #",
        "#     #",
        " ##### "
    ],
    '6': [
        " ##### ",
        "#     #",
        "#      ",
        "###### ",
        "#     #",
        "#     #",
        " ##### "
    ],
    '7': [
        "#######",
        "     # ",
        "    #  ",
        "   #   ",
        "  #    ",
        " #     ",
        "#      "
    ],
    '8': [
        " ##### ",
        "#     #",
        "#     #",
        " ##### ",
        "#     #",
        "#     #",
        " ##### "
    ],
    '9': [
        " ##### ",
        "#     #",
        "#     #",
        " ######",
        "      #",
        "#     #",
        " ##### "
    ],
    ':': [
        "       ",
        "   #   ",
        "       ",
        "       ",
        "   #   ",
        "       ",
        "       "
    ]
}

# Función para mostrar un número en formato grande y centrado
def mostrar_numero_grande(numero):
    numero_str = str(numero)
    filas = [''] * 7  # Creamos una lista para las 7 filas de la representación

    for digito in numero_str:
        for i in range(7):
            filas[i] += numeros_ascii[digito][i] + '  '  # Añadimos espacio entre números
    
    # Obtén el ancho de la consola
    ancho_consola = shutil.get_terminal_size().columns

    # Centra el número
    for fila in filas:
        espacios = (ancho_consola - len(fila)) // 2
        print(' ' * espacios + fila)

# Función para mostrar el mensaje de bienvenida dentro del dibujo ASCII
def mostrar_mensaje_bienvenida():
    dibujo_ascii = [
        "                                                 ",
        "                                                 ",
        "                                                 ",
        "                                                 ",
        "              ..,uod8BBBBBBBBBBBBBBBBRPFT?l!i:.",
        "         ,=m8BBBBBBBBBBBBBBBRPFT?!||||||||||||||",
        "         !...:!TVBBBRPFT||||||||||!!^^\"'   ||||",
        "         !.......:!?|||||!!^^\"'            ||||",
        "         !.........||||                     ||||",
        "         !.........||||  Bienvenido al      ||||",
        "         !.........||||  cronómetro!        ||||",
        "         !.........||||  Presiona ENTER para ||||",
        "         !.........||||  empezar...         ||||",
        "         !.........||||                     ||||",
        "         !.........||||                     ||||",
        "         !.........||||                     ||||",
        "         !.........||||                     ||||",
        "         !.........||||                     ||||",
        "         `.........||||                    ,||||",
        "          .;.......||||               _.-!!|||||",
        "   .,uodWBBBBb.....||||       _.-!!|||||||||!:",
        "!YBBBBBBBBBBBBBBb..!|||:..-!!|||||||!iof68BBBBBb....",
        "!..YBBBBBBBBBBBBBBb!!||||||||!iof68BBBBBBRPFT?!::   `.",
        "!....YBBBBBBBBBBBBBBbaaitf68BBBBBBRPFT?!:::::::::     `.",
        "!......YBBBBBBBBBBBBBBBBBBBRPFT?!::::::;:!^\"`;:::       `.",
        "!........YBBBBBBBBBBRPFT?!::::::::::^''...::::::;         iBBbo.",
        "`..........YBRPFT?!::::::::::::::::::::::::;iof68bo.      WBBBBbo.",
        "  `..........:::::::::::::::::::::::;iof688888888888b.     `YBBBP^'",
        "    `........::::::::::::::::;iof688888888888888888888b.     `",
        "      `......:::::::::;iof688888888888888888888888888888b.",
        "        `....:::;iof688888888888888888888888888888888899fT!",
        "          `..::!8888888888888888888888888888888899fT|!^\"'",
        "            `' !!988888888888888888888888899fT|!^\"'",
        "                `!!8888888888888888899fT|!^\"'",
        "                  `!988888888899fT|!^\"'",
        "                    `!9899fT|!^\"'",
        "                      `!^\"'"
    ]
    
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla
    for linea in dibujo_ascii:
        print(linea)
    
    input()  # Espera a que el usuario presione ENTER
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla nuevamente

def mostrar_mensaje_salida(horas, minutos, segundos):
    dibujo_ascii = [
        "⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀ ⣀⣀⣀⣀⣀⣀⣀⣀⣀                 ",
        "⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀              ",
        "⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆             ",
        "⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆            ",
        "⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆ ",
        "⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠸⣼⡿  ",
        "⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉          ",
        "⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇           ",
        "⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇           ",
        "⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇           ",
        "⠀⠀ ⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠇           ",
        "⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇            ",
        "⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃  Tiempo total: {0:.0f} horas, {1:.0f} minutos y {2:.2f} segundos.".format(horas, minutos, segundos),
    ]
    
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla
    for linea in dibujo_ascii:
        print(linea)
    
    input()  # Espera a que el usuario presione ENTER
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla nuevamente


# Función principal del cronómetro
def cronometro():
    mostrar_mensaje_bienvenida()  # Muestra el mensaje de bienvenida

    inicio = time.time()  # Captura el tiempo de inicio
    print("Cronómetro iniciado. Presiona ENTER para detener.")
    
    try:
        while True:
            tiempo_actual = time.time() - inicio  # Calcula el tiempo transcurrido
            horas, minutos, segundos = (
                tiempo_actual // 3600,
                (tiempo_actual % 3600) // 60,
                tiempo_actual % 60
            )  # Convierte a horas, minutos y segundos
            tiempo_formateado = f"{int(horas):02d}:{int(minutos):02d}:{int(segundos):02d}"  # Formatea en HH:MM:SS
            
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla
            mostrar_numero_grande(tiempo_formateado)  # Muestra el tiempo en formato grande
            
            if os.name == 'nt':
                import msvcrt
                if msvcrt.kbhit() and msvcrt.getch() == b'\r':  # Espera ENTER en Windows
                    break
            else:
                import select
                import sys
                if select.select([sys.stdin], [], [], 0)[0]:
                    input()  # Espera a que se presione ENTER
                    break
            
            time.sleep(1)  # Espera 1 segundo entre actualizaciones
    except KeyboardInterrupt:
        pass
    
    tiempo_transcurrido = time.time() - inicio
    horas, minutos, segundos = (
        tiempo_transcurrido // 3600,
        (tiempo_transcurrido % 3600) // 60,
        tiempo_transcurrido % 60
    )
    print(f"\nCronómetro detenido. Tiempo total: {int(horas)} horas, {int(minutos)} minutos y {segundos:.2f} segundos.")
    mostrar_mensaje_salida(int(horas), int(minutos), segundos)

# Ejecuta el cronómetro
cronometro()
