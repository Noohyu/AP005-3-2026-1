#include <iostream> /* Incluye la biblioteca necesaria para std::cout. */

int main(void) { /* Funcion principal del programa. */
    int x = 10;  /* Variable entera con valor inicial 10. */

    std::cout << "Valor de x = " << x << "\n";     /* Muestra el valor de x. */
    std::cout << "Direccion de x = " << &x << "\n"; /* Muestra la direccion de x. */

    return 0; /* Finalizacion exitosa. */
}
