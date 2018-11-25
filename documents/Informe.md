# II PROYECTO PROGRAMADO IA
# Connect 4 
------------------------------------------------ 
Instituto Tecnológico de Costa Rica 	      
Escuela de Ingeniería en Computación       
Curso: Inteligencia Artificial	      
Semestre 2 - 2018		 	      
Proyecto II 			      
Estudiantes: 			      
* Jonathan Martínez Camacho 	      
* Mariana Rojas Semeraro 		      
* Katerine Molina Sánchez 

Repositorio: https://github.com/ProyectoII-IA/Connect4

------------------------------------------------
## Estructura general del proyecto

### Clases de configuración

* Fit_Agents_Controller: clase que toma los parámetros que se envían por consola, y que se encarga de instanciar y ejecutar el algoritmo genético, para posterior retornar la configuración del mejor agente. 
* Game_Controller: clase que toma los parámetros que se envían por consola, y que se encarga de instanciar los dos jugadores, para posterior instanciar el juego con los jugadores creadores y permitir que se realize el proceso natural del juego.

### Clases del juego

* Board: es la clase base del juego, sobre ella se define el arreglo básico para el juego, y todas las funciones referentes a validaciones de las jugadas y la detección de los casos cuando hay ganador. 
* Player: es una interface la cual define el comportamiento básico de los tipos de jugadores, es implementada por las clases Agent, y Human.
* Agent: define la estructura básica de un agente, contiene las probabibilidades de las diferentes estrategías que cada agente utiliza. 
* Human: define la estructura básica de un jugador humano.
* Game: define la estructura del juego, y es el encargado de controlar el flujo del mismo. Posee definidos dos jugadores y utiliza una instancia de la clase Board para administrar el estado del juego.
* Strategy: es la clase que define la base para las estrategías a implementar por parte del agente. Es una generalización que debe ser adoptada por cada nueva estrategía que se desee agregar o implementar.
* Blocking2_vs_1: define la estructura y comportamiento de la primera estrategía, su objetivo es comparar si es mejor un movimiento de bloquear una secuencia de dos fichas del oponente contra bloquear una sola ficha del mismo.
* Center_vs_Extremity: define la estructura y comportamiento de la segunda estrategía, su objetivo es comparar si es mejor un movimiento de inserción al centro del tablero, en contraposición a una inserción a los extremos del tablero.
* Sequential_vs_Space: define la estructura y comportamiento de la tercera estrategía, su objetivo es comparar si es mejor un movimiento de inserción en secuencia o una inserción dejando un espacio en blanco en medio, con el objetivo de confundir al oponente.
* Horizontal_vs_Vertical: define la estructura y comportamiento de la cuarta estrategía, su objetivo es comparar y determinar si un movimiento de inserción en horizontal es mejor que un movimiento de inseción en vertical. 
* Position: clase que permite llevar el control de los diferentes filtros de estrategías que se aplican a un estado en particular del juego (board) con el único objetivo de determinar la o las columnas que ofrecen una mejor jugada. Esta clase es solo utilizada por las instancias de Agent.

### Clases del algoritmo genético
* Game_Genetics:
* Genetics_Algorithm:
* Individual:

------------------------------------------------
## Estrategía de solución del juego

* Configuración: el inicio del juego está determinado por la configuración que se le envie por consola al juego, en este sentido, el primer paso de la configuración es el parseo de los parámetros enviados al programa (ver el manual de usuario para comprender la forma en que los parámetros deben ser ingresados), según el valor de los mismos se determina el segundo paso de la configuración, en este caso, la instanciación de los jugadores, y por consecuente, el tercer y último paso de la configuración, la instanciación e inicio del juego como tal.

* Juego: una vez activado el flujo del juego desde la configuración, se inicia el ciclo del juego, básicamente este ciclo está determinado por dos posibles estados del tablero, el primero, es que se encuentre un ganador, para lo cual, con cada movimiento realizado se realiza la verificación de si existe o no un ganador, y el segundo estado posible, es que el tablero se encuentre lleno, por lo que, la condición del bucle es la verificación de que aún hayan casillas vacías.

* Búsquedas: dentro del ciclo de juego, cada jugador (agente o humano), tiene definida una función llamada "next_action" que recibe como parámetro el estado actual del juego, está función es la que es invocada en cada turno correspondiente, y se encarga de definir la siguiente acción que el jugador va a realizar. En cuanto al agente se refiere, dicha función lo que realiza es un proceso de descarte de acuerdo a las estrategías de movimiento definidas y al valor de probabilidad que las mismas poseen. Ese proceso de descarte implica, realizar una serie de búsquedas (aplicación de estrategias) para ir eliminando todas aquellas columnas que no cumplen una estrategía, y asi sucesivamente hasta llegar a la última estrategía y elegir la más optima. En caso de empate, la estrategía columna se elije al azar. En cuanto al humano, la función "next_action", lo único que realiza es solicitar la entrada de la columna a la cual se quiere realizar la inserción.


------------------------------------------------ 
## Estrategías de movimientos de los agentes

* Recorda poner el pseudo-codigo de las funciones, eso lo pide la documentación =(
* Blocking 2 vs 1:
* Center vs Extremity:
* Sequential vs Space:
* Horizontal vs Vertical:

------------------------------------------------ 
## Estrategía de solución de Algortimos Genéticos

* Configuración: el inicio del programa está determinado por la configuración que se le envie por consola al algoritmo genético, en este sentido, el primer paso de la configuración es el parseo de los parámetros enviados al programa (ver el manual de usuario para comprender la forma en que los parámetros deben ser ingresados), según el valor de los mismos se determina el segundo  y último paso de la configuración, en este caso, la instanciación del objeto Genetics_Algorithm, con el número de generaciones y la cantidad de individuos que pasan de una generación a otra. 

* Aqui la explicación de Katherine

------------------------------------------------ 
## Cobertura de las pruebas

* Revisar la carpeta htmlcov (en la raíz del proyecto) lugar donde se encuentra el archivo index.html con el reporte completo de las pruebas realizadas

------------------------------------------------ 
## Distribución de trabajo realizado y notas


#### Jonathan Martínez Camacho:
* Diseño e implementación de la solución general
* Desarrollo e implementación del board
* Desarrollo e implementación de la configuración del juego y el algoritmo genético
* Colaboración e implementación del agent
* Documentación

#### Katherine Molina Sánchez:
* Diseño e implementación de la solución general
* Desarrollo e implementación de las estrategías de movimientos
* Desarrollo e implementación de los algoritmos genéticos
* Colaboración e implementación del agent
* Documentación

#### Mariana Rojas Semeraro:
* Diseño e implementación de la solución general
* Desarrollo e implementación de las estrategías de movimientos
* Desarrollo e implementación de los jugadores (player, agent, human)
* Desarrollo e implementación del game
* Documentación

#### Notas:

* Jonathan Martínez Camacho:    100
* Katherine Molina Sánchez:     100
* Mariana Rojas Semeraro:       100
------------------------------------------------