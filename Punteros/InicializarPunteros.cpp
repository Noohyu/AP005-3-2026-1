#include <iostream> /* Incluye la biblioteca necesaria para std::cout. */
#include <cstddef>  /* Incluye la definicion de nullptr. */

int main(void) { /* Funcion principal del programa. */
    int *p = nullptr; /* El puntero se inicializa en nullptr porque aun no apunta a un int. */

    if (p != nullptr) { /* Solo se desreferencia si apunta a una direccion valida. */
        std::cout << "Valor = " << *p << "\n";
    } else {
        std::cout << "p no apunta a una direccion valida.\n";
    }

    return 0; /* Finalizacion exitosa. */
}
