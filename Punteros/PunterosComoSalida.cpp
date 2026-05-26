#include <iostream> /* Incluye la biblioteca necesaria para std::cout. */

int main(void) { /* Funcion principal del programa. */
    int v[3] = {10, 20, 30}; /* Declaracion de un arreglo de 3 enteros. */
    int *p;                  /* Declaracion de un puntero a entero. */

    p = v; /* El nombre del arreglo 'v' equivale a la direccion de su primer elemento (&v[0]). */

    std::cout << "Elemento 0: " << *p << "\n"; /* Muestra el valor en la direccion actual (v[0] = 10). */

    p++; /* Aritmetica de punteros: avanza el puntero al siguiente elemento (v[1]). */
    std::cout << "Elemento 1: " << *p << "\n"; /* Muestra el valor en la nueva direccion (v[1] = 20). */

    p++; /* Avanza el puntero al ultimo elemento (v[2]). */
    std::cout << "Elemento 2: " << *p << "\n"; /* Muestra el valor en la nueva direccion (v[2] = 30). */

    return 0; /* Finalizacion exitosa. */
}
