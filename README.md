#Título proyecto: Anima Easy
+ Es una aplicación escrita en Python con la biblioteca gráfica Tcl/Tk para hacer más fácil las partidas de rol
+ Permite crear las fichas de los personajes y almacenarlas, realizar las tiradas de dados de forma sencilla a través de la ficha, cuenta con una calculadora para que realice por nosotros todas las operaciones necesarias a la hora de combatir y pone a nuestra disposición dados de diferentes caras (2, 3, 4, 6, 10, 12, 20, 100)

#Módulo "main"
+ Este módulo es donde encuentra la ventana principal de la aplicación y será el primero en ejecutarse, por ello será él quien se encargue de correr los demás módulos / ventanas
+ Desde el módulo "tkinter" importamos las clases:
    - Tk: es una biblioteca de elementos básicos para construir una interfaz gráfica de usuario (GUI)
    - Frame: es un widget, que sirve como una especie de contenedor
    - Label: genera una ventana con una etiqueta de texto
    - Button: permite crear botones
+ Desde el módulo "PIL" importamos las clases:
    - Image: nos permite crear una clase que representa una imagen, cargar imágenes desde archivos y crearlas
    - ImageTk: nos da soporte para crear y modificar objetos Tkinter BitmapImage y PhotoImage a partir de imágenes PIL
+ Desde nuestro direcotrio importamos los módulos:
    - dados: contiene toda la lógica que abre la ventana de dados y los lanza
+ La función "__init__" hará que se inicie lo primero y en ella añadimos la lógica que contendrá la ventana:
    - EL título de la aplicación
    - Las medidas de la ventana y con "resizable" no permitimos que se pueda modificar
    - El logo de la aplicación que se encuentra en "Static/logo_app.png"
    - El menú lateral donde están los botones para: crear y borrar ficha,  calculadora de combate y dados
+El bloque "if __name__ == __name__" hace que la aplicación entienda este módulo como el principal el cuál correrá toda la aplicación y, además, no ejecute todo el código del mismo. Es decir, nos permite iniciar la aplicación y utilizar cuando queramos las funciones o módulos que hemos importado

#Módulo "dices"
+ En este módulo se encuentra toda la lógica para abrir una nueva ventana con botones para lanzar los diferentes dados
+ Importamos la clase "random": nos genera variables numéricas aleatorias
+ Desde el módulo "tkinter" importamos las clases:
    - Toplevel: permite crear una ventana nueva
    - Label: genera una ventana con una etiqueta de texto
    - Button: permite crear botones
+ La función "roll" es la única donde está toda la lógica:
    - "Toplevel" nos permite abrir una ventana distinta a la principal
    - "title" el título de la ventana
    - "geometry" las dimensiones de la ventana
    - "resizable(0,0)" fija las dimensiones de la ventana y no permite modificarlas
    - La función "roll_dice(max)" lanza los dados. El resultado estará entre el 1 y el número que le pasemos como parámetro, de esta manera para cada dado usaremos la misma función
    - Para crear los botones utilizamos "label" para escribir el dado que es, creamos el botón con "Button" para cada uno de ellos y lo colocamos en la ventana donde mostramos el resultado

#Módulo "calculator_backend"
+ Este módulo tiene toda la lógica necesaria para realizar los calculos de un combate
+ Importamos la clase "random": nos genera variables numéricas aleatorias
+ La función "roll_dice()" lanza los dados del atacante y defensor
    - Si el resultado de los dados es 90+ se volverá a lanzar otro dado y sumará ambos resultados
+ La función "calculate_damage(atacker, defender, combat_result)" calcula la vida que pierde el defensor
    - Primero filtramos la armadura que quita el arma dependiendo de la calidad de la misma
    - Restamos la calidad del arma del atacante a la armadura del defensor
    - Calculamos el porcentaje de daño que debe recibir el defensor: si es inferior a 0 no ocurrirá nada, si es superior se calcula el daño 
+ La clase "Character" es la plantilla para crear los personajes 
    - La función "__init__" la utilizamos para pasarle por parámetros todos los datos al objeto cuando lo instanciemos 
    - La función "atack(self, defender)" permite a un personaje realizar un ataque. "self" es el objeto que realiza el ataque y "defender" el defensor
        Se llama a la función "roll_dice" para los dados del atacante y defensor
        Se suman o restan todos los valores de la ficha para calcular el resultado final del combate
        Si no ha introducido un mínimo de valores, se le envía un mensaje de error y, si sí lo ha hecho, se llama a la función que calcula el daño y se le muestra si ha tenido éxito o no
    - La función "defend(self, atacker)" permite a un personaje realizar una defensa. "self" es el objeto que realiza la defensa y "atacker" el atacante
        Esta funciona igual que la de ataque. La diferencia es que los datos a utilizar no son los mismos, pero el resto de la lógica es la misma
+ Instanciamos la clase "Character" y creamos los dos personajes que pelearán entre si: pj_1 y pj_2 (sus valores se establecen como 0 por defecto hasta que el usuario le introduzca los nuevos)

#Módulo "calculator_frontend"
+ Este módulo permite abrir la ventana de la calculadora de combate, contiene toda la lógica para que el diseño sea el deseado y recoger los parámetros que introduce el usuario
+ La función "calc" abre la ventana de la calculadora y aloja el resto del código
    - Insertamos, cambiamos tamaño, usamos filtros para mejorar calidad e insertamos las imagenes de jugador_1 y jugador_2 en un label (etiqueta) colocada en la primera columna y fila
    - Realizamos la misma operación con la imagen de "versus"
    - Creamos un contenedor donde añadimos una etiqueta con la información a mostrar al usuario sobre la calculadora
    - Creamos el contenedor donde mostrar al usuario el resultado del cálculo
    - Declaramos "IntVar" las variables a usar en los "inputs", es decir, donde introducirá el usuario los valores
    - Creamos la función "get_data" que recogerá los valores de los "inputs" que introduce el usuario
        Estos datos se introducen automaticamente a los atributos de nuestros objetos creados previamente en "calculator_backend", los cuales los usaremos para realizar los calculos
    - Creamos las etiquetas (label) y entrys (input) para cada uno de los datos que necesitamos del personaje y les asignamos una de las variables declaradas anteriormente
        Usamos ".place(x, y)" para colocarlos mediante coordenadas
    - Creamos los botones que realizarán la función de "atacar" y "defender" en cada personaje (se declaran al final del conjunto de datos de dicho personaje)
        Estos botones tienen su propia función la cual primero llama a la función que recoge los datos y también al método "atacar" o "defender" de la clase "Character" en el módulo "calculator_backend"



    
    