-----------------------------
# Título proyecto: Anima Easy
-----------------------------
+ Es una aplicación escrita en Python con la biblioteca gráfica Tcl/Tk para hacer más fácil las partidas de rol
+ Permite crear las fichas de los personajes y almacenarlas, realizar las tiradas de dados de forma sencilla a través de la ficha, cuenta con una calculadora para que realice por nosotros todas las operaciones necesarias a la hora de combatir y pone a nuestra disposición dados de diferentes caras (2, 3, 4, 6, 10, 12, 20, 100)

# Recursos utilizados:
- Tk: es una biblioteca de elementos básicos para construir una interfaz gráfica de usuario (GUI)
- os: permite realizar operaciones dependientes del sistema operativo
- Frame: es un widget, que sirve como una especie de contenedor
- Label: genera una ventana con una etiqueta de texto
- Button: permite crear botones
- Image: nos permite crear una clase que representa una imagen, cargar imágenes desde archivos y crearlas
- ImageTk: nos da soporte para crear y modificar objetos Tkinter BitmapImage y PhotoImage a partir de imágenes PIL
- Toplevel: permite crear una ventana nueva
- Random: genera un numero aleatorio
- Listbox: permite crear una caja de listas
- Separator: es un widget que nos crea una linea para separar contenido de forma visual
- OptionMenu: permite crear un menú desplegable con multiples opciones
- Text: permite crear una caja de texto
- filedialog: permite crear ventanas de selecciones de archivos/directorios

# Módulo "run" (done)
+ Aquí se inicia la aplicación
+ Utiliza los módulos: Tk, os, main_window, card_manager e history_manager
+ +El bloque "if __name__ == __name__" hace que la aplicación entienda el módulo "main" como el principal el cuál correrá toda la aplicación y, además, no ejecute todo el código del mismo.  Es decir, nos permite iniciar la aplicación y utilizar cuando queramos las funciones o módulos que hemos importado
    - Comprueba que en la ruta del proyecto existe la carpeta donde se guardan las fichas de personajes y si no está, la crea
    - Comprueba que en la ruta del proyecto existe el txt donde se guarda el historial y si no está, lo crea
    - Carga en memoria la información de los personajes creados
    - Establece a "root" como aplicación Tk y genera el mainloop para ejecutarla

# Módulo "main" (done)
+ Este módulo es donde se encuentra la ventana principal de la aplicación y será él quien se encargue de correr los demás módulos / ventanas
+ Módulos utilizados: frame, label, button, listbox, image, imageTk, separator, dice_window, calculator_window, character_window, history_window y card_manager
+ La función "__init__" hará que se inicie lo primero y en ella añadimos la lógica que contendrá la ventana:
    - Se establece la ventana como "root" para correr el programa, el título de la ventana, el tamaño, que no pueda modificar el tamaño y el color de fondo
    - Se carga el logo de la aplicación, se le da un tamaño, usamos filtros para mejor calidad y la mostramos en su label
    - Se crea el menú lateral donde se alojan los botones de las funcioens principales y el listbox donde aparecen los personajes creados
    - Se crean los botones para: abrir ficha nueva, abrir la calculadora de combate, abrir la ventana de dados y abrir el historial
    - Se crea el listbox donde se muestran los personajes creados y, clicando en ellos, se abren sus fichas
+ Se cargan los personajes creados en el listbox y se crea la referencia del mismo para poder usarlo en otros módulos

# Módulo "dice_window" (done)
+ En este módulo se encuentra toda la lógica para abrir una nueva ventana con botones para lanzar los diferentes dados
+ Única función "open" que crea la ventana
    - Se establece la ventana como secundaria, el título, tamaño, se impide cambiar el tamaño y el color de fondo
    - Se crea la función "place_dice" que llama a la función que lanza el dado y lo muestra por pantalla
    - Se crea el label donde se mostrarán los dados
    - Se crean los botones que llama a la función que lanza el dado, pasándole el resultado máximo que puede salir

# Módulo "dice_manager" (done)
+ En este módulo se encuentra toda la lógica para lanzar un dado de diferentes caras
+ Importamos: random
+ Única función "roll" (se le pasa por parámetro el número de caras del dado)
    - "random" nos genera un numero aleatorio entre 1 y el parametro que le indiquemos y si el resultado es 90+ se lanza otro dado y se suma al anterior

# Módulo "calculator_window" (done)
+ Este módulo permite abrir la ventana de la calculadora de combate, contiene toda la lógica para que el diseño sea el deseado y recoger los parámetros que introduce el usuario
+ Modulos usados: LEFT, RAISED, IntVar, Toplevel, Label, Entry, Button, Frame, Image, ImageTk, calculator_manager
+ La función "open" abre la ventana de la calculadora y aloja el resto del código
    - La definimos como secundaria, establecemos título, cambiamos el tamaño, le impedimos que pueda cambiarlo y le añadimos color de fondo
    - Abrimos las imágenes de los jugadores y el versus, le establecemos el tamaño, le pasamos unos filtros para mejorar la calidad y las establecemos en sus labels para mostrarlas
    - Creamos un contenedor donde añadimos una etiqueta con la información a mostrar al usuario sobre la calculadora
    - Creamos el contenedor donde mostrar al usuario el resultado del cálculo
    - Declaramos "IntVar" las variables a usar en los "inputs", es decir, donde introducirá el usuario los valores
    - Creamos las etiquetas (label) y entrys (input) para cada uno de los datos que necesitamos del personaje y les asignamos una de las variables declaradas anteriormente
        Usamos ".place(x, y)" para colocarlos mediante coordenadas
        Estos datos se introducen automaticamente a los atributos de nuestros objetos creados previamente en "calculator_manager", los cuales los usaremos para realizar los calculos

# Módulo "calculator_manager" (done)
+ Este módulo tiene toda la lógica necesaria para realizar los calculos de un combate
+ La función "calculate_damage(atacker, defender, combat_result)" calcula la vida que pierde el defensor 
    - Primero filtramos la armadura que quita el arma dependiendo de la calidad de la misma
    - Restamos la calidad del arma del atacante a la armadura del defensor
    - Calculamos el porcentaje de daño que debe recibir el defensor: si es inferior a 0 no ocurrirá nada, si es superior se calcula el daño 
+ La clase "Character" es la plantilla para crear los personajes 
    - La función "__init__" la utilizamos para pasarle por parámetros todos los datos al objeto cuando lo instanciemos 
    - La función "atack" permite a un personaje realizar un ataque. Se le pasa por parámetro el personaje defensor
        Se llama a la función "roll_dice" para los dados del atacante y defensor
        Se suman o restan todos los valores de la ficha para calcular el resultado final del combate
        Si no ha introducido un mínimo de valores, se le envía un mensaje de error y, si sí lo ha hecho, se llama a la función que calcula el daño y se le muestra si ha tenido éxito o no
    - La función "defend(self, atacker)" permite a un personaje realizar una defensa. "self" es el objeto que realiza la defensa y "atacker" el atacante
        Esta funciona igual que la de ataque. La diferencia es que los datos a utilizar no son los mismos, pero el resto de la lógica es la misma
+ Instanciamos la clase "Character" y creamos los dos personajes que pelearán entre si: pj_1 y pj_2 (sus valores se establecen como 0 por defecto hasta que el usuario le introduzca los nuevos por pantalla)
    - Creamos los botones que realizarán la función de "atacar" y "defender" en cada personaje (se declaran al final del conjunto de datos de dicho personaje)
        Estos botones llaman a la función "combat"
    - Creamos la función "get_data" que recogerá los valores de los "inputs" que introduce el usuario
    - Creamos la función "combat". Se le pasa por parámetro el atacante, el defensor y el tipo de acción a realizar
        Dependiendo del tipo de acción que le pasemos, llamará a un método u otro de los objetos creados en "calculator_manager"

# Módulo "card_window" (done)
+ Este módulo crea una nueva ventana con una ficha de un personaje (puede ser en blanco o con los datos de un personaje creado)
+ Módulos utilizados: CENTER, NE, RIDGE, OptionMenu, StringVar, Toplevel, Frame, Label, Button, Entry, Text, END, separator, Image, ImageTk, filedialog, card_manager, history_manager
+ Se crean variables globales para su uso en otros módulos
+ Función "open" para crear la ventana. Se le pasa por parametro si es nueva ficha para de ser así mostrarla en blanco
    - Le pasamos las variables globales para usarlas
    - Establecemos que es una ventana secundaria, el titulo de la misma, su tamaño y se bloquea el cambio de este
    - Creamos los frames para cada página y le añadimos el color del fondo
    - Creamos las funciones para cambiar entre páginas. Quitarán el anterior frame y colocarán el nuevo en pantalla
        Creamos los botones que le permitirán al usuario cambiar entre páginas (llaman a las funciones de cambio de página)
    - Añadimos un Label en la parte inferior izquierda para mostrar al usuario en qué página se encuentra 
    - Establecemos que la página 1 se muestre por defecto llamando a su función
    - Creamos los botones de guardar y borrar ficha. 
        Estas llamarán a las funciones de "guardar_personaje" y "eliminar_personaje" respectivamente, que se encuentran 
    - Creamos la función "image" que abrirá la imagen que el usuario haya seleccionado y la colocará en su label. Además, la función "open_image" le mostrará una ventana donde podrá navegar entre sus archivos para elegir la imagen
        El botón "btn_image" llama a "image" para que el usuario pueda seleccionarla
    - Se crean todos los atributos que contendrán la página 1 y 2 con sus respectivos labels para mostrar el nombre y entries donde se añadirá el valor
        Cada label tendrá el atributo "text" como referencia cuando queramos acceder a su valor
        Cada entry tendrá su atributo "name" como referencia cuando queramos acceder a su valor
        Ambos se colocan en la ventana mediante ".place(x, y)" el cuál utiliza las coordenadas que se le pasan por parámetro
    - Se crean los botones para realizar las acciones del personaje y su dropmenu con las diferentes opciones disponibles
        Todos estos botones llamarán a la función "alterar_historial" del módulo "history_manager" con un modificador como parámetro para saber qué acción debe realizar
    - Se crea una lista con sublistas que relacionan cada uno de los entries con su label para pasarla al módulo "card_manager" y pueda modificarlos desde fuera
    - Si se le ha pasado el atributo "es ficha nueva", recorrerá todos los entry y los dejará en blanco
    - Se cambia la acción que realizará cuando se cierre la ventana mediante ".protocol" y el mensaje que el S.O. envía a la aplicación
        Se captura el mensaje y se le cambia para que en lugar de hacer lo que haría normalmente, llame a la función "al_cerrar_ventana" la cual activa el listbox para poder hacer clic a los personajes que aparezcan y se puedan abrir sus fichas, y además destruya la ventana

# Módulo "card_manager" (done)
+ Este módulo contiene toda la lógica para poder operar con la ficha del personaje
+ Módulos utilizados: os, path, glob, END, INSERT, Entry, Text, re, card_window
+ Se crean variables globales para controlar el estado del programa y acceder a ellas desde otros módulos
+ Se crea la función "cargar_pjs_a_memoria"
    - Se le pasan las variables globales a utilizar
    - "lista_archivos_pj" lista que contiene los ID de los personajes creados (recorre la carpeta que contiene los personajes y saca el ID)
    - "cantidad_personajes" cantidad de personajes creados
    - si no hay personajes, el "id_último_pj_creado" será 0 y, si es 1+ creará un super diccionario con toda la información de los personajes creados
        - se abren todos los archivos de los personajes y se crea un diccionario de cada personaje
        - todos los diccionarios se unifican en "dicc_de_pjs"
+ Se crea la función "cargar_personajes_en_listbox". Se le pasa por parámetro la referencia al listbox del "card_window"
    - Se le pasan las variables globales a utilizar
    - Se limpia el listbox
    - Se recorre la lista de personajes creados y se inserta en diferentes líneas cada uno de sus nombres con el ID 
+ Se crea la función "abrir_personaje". Se le pasa por parámetro la referencia al listbox del "card_window"
    - Se le pasan las variables globales a utilizar
    - Se bloquea la función de abrir ficha al seleccionar en el listbox
    - Si se abre desde el botón "ficha nueva" se abrirá una página en blanco y, si se abre seleccionado un pj del listbox se rellenan los campos con la información del personaje:
        - "pj_en_index" es el personaje seleccionado
        - "nombre_pj" es el nombre del personaje
        - se busca en la carpeta de personajes y se accede a su diccionario
        - se abre la ventana de ficha, se le cambia el título al nombre del personaje y se recorren los entry insertándole los datos del personaje (hay que diferenciar la forma de insertar información en un entry y text)
+ Se crea la función "eliminar personaje". Se le pasa por parámetro la referencia de la ventana para poder destruirla
    - Se hace una comprobación y si la ventana es ficha nueva no hará nada la función
    - Se borra el archivo donde se almacena la información del personaje
    - Se vuelve a activar el abrir personajes desde el listbox
    - Se deselecciona el personaje, se actualiza la memoria de personajes, se actualiza el listbox y se destruye la ventana del personaje
+ Se crea la función "guardar_personaje". Se le pasa por parámetro la lista de entries y labels del "card_window"
    - Se le pasan las variables globales a utilizar
    - "nombre_pj" contiene el nombre del personaje
    - se actualiza el título de la ventana con el nombre del personaje
    - si era una ficha nueva, se crea un archivo nuevo con su información y, si existe, se edita el existente
        - se abre el archivo y se reocrren todos los entry rellenándolos con la información
    - se actualiza el diccionario de personajes, el último id de personaje seleccionado y se actualiza el listbox

# Módulo "history_window" (done)
+ Este módulo abre una nueva ventana donde mostrar todas las tiradas de los personajes. Se mantienen hasta que el usuario las borre, incluso aunque se cierre la aplicaicón
+ Módulos utilizados: EXTENDED, LEFT, RIGHT, VERTICAL, Y, Button, Entry, Listbox, Scrollbar, StringVar, Toplevel, Frame, history_manager
+ se crea la variable global "counter" la cual nos sirve para evitar que se pueda abrir más de una de estas ventanas a la vez
+ se crea la función "open_history_box" la cual crea la ventana
    - primero se le pasa la variable global counter y, si es verdadero, abrirá la ventana (cuando está falso es porque ya está abierta)
    - al abrirla se establece como ventana secundaria, el título de la ventana, el tamaño, se bloquea cambiarle el tamaño y el "counter" pasa a falso 
    - se crea el frame donde colocar todo el contenido y se fija
    - se crea la barra de scroll para movernos en el eje "y", y se fija en la ventana
    - se crea el listbox donde pintar los resultados
    - se le pasa la referencia al listbox del archivo guardado y se actualiza con el mismo
    - se crea un entry en la parte inferior de la ventana para añadir contenido de forma manual y se fija
    - se crean los botones: limpiar, eliminar, add (este será para añadir el contenido del entry de forma manual)
        Todos estos botones llamarán a la función "alterar_historial" del módulo "history_manager" y le pasarán por parámetro el tipo de modificación a realizar en el historial
    - se  Se cambia la acción que realizará cuando se cierre la ventana mediante ".protocol" y el mensaje que el S.O. envía a la aplicación
        Le decimos que en lugar de cerrarlo cuando le llegue el mensaje, ejecute la función "al cerrar historial" por la cual cerramos la aplicación nosotros y además, le pasamos a verdadero otra vez el contador para que se pueda volver a abrir

# Módulo "history_manager" (done)
+ Este módulo tiene toda la lógica para poder trabajar con la ventana del historial (history_window)
+ Módulos utilizados: ANCHOR, END, messagebox, history_window, card_window, card_manager, dice_manager, os
+ se crean las variables globales "history_file" que contiene la ruta y el nombre del archivo donde se guarda el historial e history_box como "none" ya que será una variable optativa (puede que no contenga nada el historial, es decir, esté vacío)
+ se crea la función "llenar_historial". Esta busca el archivo de historial y, si existe, insertará todas sus líneas en la ventana del historial
+ se crea la función "guardar_historial_en_archivo". Esta recoge todo lo que haya en la ventana historial y lo inserta linea a linea en el archivo donde se guardará
+ se crea la función "alterar_historial" y se le pasa el parámetro del tipo de modificación. Primero abrirá la ventana de historial si no está abierta y, dependiendo del tipo de modificación, ejecutará y después actualizará el archivo del historial:
    - tipo de modificación: "add from bar"
        Añade el contenido del entry ubicado en la propia ventana del historial en una linea nueva
    - tipo de modificación: "delete"
        Elimina la línea seleccionada en el historial
    - tipo de modificación: "clean"
        Limpia el historial
    - tipo de modificación: "turno"
        Recoge el valor de la casilla de turno, comprueba que es numérico (si no lo es, muestra un mensaje de error), lanza un dado de 100 caras (esto lo lleva a cabo llamando a la función "roll" del módulo "dice_manager"), le suma el resultado y lo inserta en el historial
    - tipo de modificación: "caracteristica"
        Recoge el valor de la casilla de caracteristica elegida, comprueba que es numérico (si no lo es, muestra un mensaje de error), lanza un dado de 10 caras (esto lo lleva a cabo llamando a la función "roll" del módulo "dice_manager"), le suma el resultado y lo inserta en el historial
    - tipo de modificación: "combate"
        En este caso dependerá de si atacamos o defendemos, la función hará una cosa u otra. 
        - Al atacar recogerá los valores de ataque (comprueba que sean numéricos o mostrará un mensaje de error); a la base le suma el bono y le resta el penalizador, lanza un dado de 100 caras (esto lo lleva a cabo llamando a la función "roll" del módulo "dice_manager"), le suma el resultado y lo inserta en el historial
        - Al defender recogerá los valores de defensa (comprueba que sean numéricos o mostrará un mensaje de error); a la base le suma el bono y le resta el penalizador, lanza un dado de 100 caras (esto lo lleva a cabo llamando a la función "roll" del módulo "dice_manager"), le suma el resultado y lo inserta en el historial
    - tipo de modificación: "secundarias"
        Recoge el valor de la casilla de secundaria elegida, se comprueba que es numérico, se lanza un dado de 100 caras (esto lo lleva a cabo llamando a la función "roll" del módulo "dice_manager"), le suma el resultado y lo inserta en el historial
    - tipo de modificación: "resistencias"
        Recoge el valor de la casilla de resistencia elegida, se comprueba que es numérico, se lanza un dado de 100 caras (esto lo lleva a cabo llamando a la función "roll" del módulo "dice_manager"), le suma el resultado y lo inserta en el historial
