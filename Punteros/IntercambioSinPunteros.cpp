#include <iostream> /* Incluye la biblioteca necesaria para std::cout. */

void intercambiar(int a, int b) { /* a y b son copias locales. */
    int temp = a; /* Guarda temporalmente el valor de a. */

    a = b;      /* Cambia la copia a. */
    b = temp;   /* Cambia la copia b. */

    std::cout << "Dentro de intercambiar: a = " << a << ", b = " << b << "\n"; /* Muestra las copias. */
}

int main(void) { /* Funcion principal del programa. */
    int x = 10;  /* Primera variable original. */
    int y = 20;  /* Segunda variable original. */

    std::cout << "Antes: x = " << x << ", y = " << y << "\n"; /* Valores antes del intercambio. */

    intercambiar(x, y); /* Envia valores; la funcion recibe copias. */

    std::cout << "Despues: x = " << x << ", y = " << y << "\n"; /* Las variables originales no cambian. */

    return 0; /* Finalizacion exitosa. */
}
