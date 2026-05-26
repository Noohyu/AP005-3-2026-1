#include <iostream> /* Incluye la biblioteca necesaria para std::cout. */

int main(void) { /* Funcion principal del programa. */
    int x = 25;  /* Variable entera con valor inicial 25. */
    int *p = &x; /* p guarda la direccion de x. */

    std::cout << "x = " << x << "\n";   /* Muestra el valor directo de x. */
    std::cout << "*p = " << *p << "\n"; /* Muestra el valor encontrado en la direccion guardada en p. */

    *p = 99; /* Modifica x indirectamente mediante el puntero p. */

    std::cout << "x despues = " << x << "\n"; /* Muestra x despues de la modificacion indirecta. */

    return 0; /* Finalizacion exitosa. */
}
