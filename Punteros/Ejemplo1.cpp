#include <iostream> /* Incluye la biblioteca necesaria para std::cout. */

int main(void) { /* Funcion principal del programa. */
    int x = 25;  /* Variable entera con valor inicial 25. */
    int *p = &x; /* p guarda la direccion de x. */

    std::cout << "x = " << x << "\n";   /* Muestra el valor directo de x. */
    std::cout << "&x = " << &x << "\n"; /* Muestra la direccion de x. */
    std::cout << "p = " << p << "\n";   /* Muestra la direccion guardada en p. */
    std::cout << "*p = " << *p << "\n"; /* Muestra el contenido ubicado en la direccion guardada en p. */

    return 0; /* Finalizacion exitosa del programa. */
}