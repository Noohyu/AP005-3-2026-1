#include <iostream> /* Incluye la biblioteca necesaria para std::cout. */
#include <cstddef>  /* Incluye la definicion de nullptr. */

void analizarNumeros(int a, int b, int c, int *suma, int *mayor, int *menor) {
    if (suma == nullptr || mayor == nullptr || menor == nullptr) { /* Verifica direcciones en C++. */
        return; /* Sale si alguna direccion no es valida. */
    }

    *suma = a + b + c; /* Escribe la suma en la direccion recibida. */

    *mayor = a; /* Supone inicialmente que a es el mayor. */
    if (b > *mayor) { /* Compara b con el mayor actual. */
        *mayor = b;   /* Actualiza el mayor si b es mas grande. */
    }
    if (c > *mayor) { /* Compara c con el mayor actual. */
        *mayor = c;   /* Actualiza el mayor si c es mas grande. */
    }

    *menor = a; /* Supone inicialmente que a es el menor. */
    if (b < *menor) { /* Compara b con el menor actual. */
        *menor = b;   /* Actualiza el menor si b es mas pequeno. */
    }
    if (c < *menor) { /* Compara c con el menor actual. */
        *menor = c;   /* Actualiza el menor si c es mas pequeno. */
    }
}

int main(void) { /* Funcion principal del programa. */
    int x = 8;   /* Primer dato de entrada. */
    int y = 3;   /* Segundo dato de entrada. */
    int z = 15;  /* Tercer dato de entrada. */

    int suma;  /* Variable donde se escribira la suma. */
    int mayor; /* Variable donde se escribira el mayor. */
    int menor; /* Variable donde se escribira el menor. */

    /* Envia valores y direcciones (&) a la funcion */
    analizarNumeros(x, y, z, &suma, &mayor, &menor);

    /* Muestra los resultados en consola usando los flujos de C++ */
    std::cout << "Suma  = " << suma << "\n";
    std::cout << "Mayor = " << mayor << "\n";
    std::cout << "Menor = " << menor << "\n";

    return 0; /* Finalizacion exitosa. */
}