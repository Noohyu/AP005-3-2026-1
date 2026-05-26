#include <iostream> /* Incluye la biblioteca necesaria para std::cout. */

void cambiar(int n) { /* n recibe una copia del valor enviado desde main. */
    n = 100; /* Se modifica la copia local, no la variable original. */

    std::cout << "Dentro de cambiar: n = " << n << "\n"; /* Muestra la copia modificada. */
}

int main(void) { /* Funcion principal del programa. */
    int x = 5;   /* Variable original. */

    std::cout << "Antes: x = " << x << "\n"; /* Muestra x antes de llamar la funcion. */

    cambiar(x); /* Se envia el valor de x. La funcion recibe una copia. */

    std::cout << "Despues: x = " << x << "\n"; /* x no cambia porque solo se modifico la copia. */

    return 0; /* Finalizacion exitosa. */
}