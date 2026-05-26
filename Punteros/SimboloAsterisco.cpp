#include <iostream> /* Incluye la biblioteca necesaria para std::cout. */

int main(void) { /* Funcion principal del programa. */
    int x = 5;   /* Variable entera con valor inicial 5. */

    int *p = &x; /* Declaracion de puntero: aqui el * forma parte de la declaracion. */

    *p = 40; /* Desreferenciacion: aqui el * accede al contenido apuntado por p. */

    std::cout << "x = " << x << "\n"; /* Muestra el valor final de x. */

    return 0; /* Finalizacion exitosa. */
}
