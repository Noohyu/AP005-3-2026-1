#include <iostream> /* Incluye la biblioteca necesaria para std::cout. */
#include <cstddef>  /* Incluye la definicion de NULL en C++ (opcional si usas nullptr). */

void cambiar(int *p) { /* p recibe una copia de una direccion. */
    if (p == nullptr) { /* Verifica si la direccion recibida no es valida (nullptr es preferido en C++). */
        return; /* Sale de la funcion para evitar usar un puntero invalido. */
    }

    *p = 100; /* Escribe 100 en la variable ubicada en la direccion recibida. */
}

int main(void) { /* Funcion principal del programa. */
    int x = 5;   /* Variable original. */

    std::cout << "Antes: x = " << x << "\n"; /* Muestra x antes de llamar la funcion. */

    cambiar(&x); /* Envia la direccion de x. */

    std::cout << "Despues: x = " << x << "\n"; /* x cambia porque la funcion escribio en su direccion. */

    return 0; /* Finalizacion exitosa. */
}