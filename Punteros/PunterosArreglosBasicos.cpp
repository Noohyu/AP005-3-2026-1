#include <iostream> /* Incluye la biblioteca necesaria para std::cout. */

int main(void) { /* Funcion principal del programa. */
    int datos[3] = {10, 20, 30}; /* Arreglo de tres enteros. */
    int *p = datos;              /* p apunta al primer elemento del arreglo. */

    std::cout << "datos[0] = " << datos[0] << "\n"; /* Acceso mediante indice. */
    std::cout << "*p       = " << *p << "\n";       /* Acceso mediante puntero. */
    std::cout << "*(p + 1) = " << *(p + 1) << "\n"; /* Acceso al segundo elemento. */
    std::cout << "*(p + 2) = " << *(p + 2) << "\n"; /* Acceso al tercer elemento. */

    return 0; /* Finalizacion exitosa. */
}