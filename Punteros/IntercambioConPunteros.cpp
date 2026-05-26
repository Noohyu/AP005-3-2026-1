#include <iostream> /* Incluye la biblioteca necesaria para std::cout. */
#include <cstddef>  /* Incluye la definicion de NULL/nullptr. */

void intercambiar(int *a, int *b) { /* Recibe las direcciones de memoria de las variables. */
    if (a == nullptr || b == nullptr) { /* Validacion de seguridad para evitar punteros nulos. */
        return;
    }

    int temp = *a; /* Guarda el valor interno apuntado por a. */
    *a = *b;       /* Asigna el valor apuntado por b a la direccion de a. */
    *b = temp;     /* Asigna el valor temporal a la direccion de b. */
}

int main(void) { /* Funcion principal del programa. */
    int x = 10;  /* Primera variable original. */
    int y = 20;  /* Segunda variable original. */

    std::cout << "Antes: x = " << x << ", y = " << y << "\n"; /* Muestra valores iniciales. */

    intercambiar(&x, &y); /* Envia las direcciones de memoria de x e y (&). */

    std::cout << "Despues: x = " << x << ", y = " << y << "\n"; /* x e y ahora estan intercambiadas con exito. */

    return 0; /* Finalizacion exitosa. */
}