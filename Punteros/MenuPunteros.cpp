#include <iostream> /* Incluye la biblioteca para entrada y salida en C++. */
#include <cstddef>  /* Incluye la definicion de nullptr. */

// ============================================================================
// FUNCIONES
// ============================================================================

void duplicar(int *p) { /* Recibe la direccion de un entero. */
    if (p != nullptr) { /* Verifica que el puntero sea valido. */
        *p = (*p) * 2;  /* Duplica el valor almacenado en la direccion apuntada. */
    }
}

void intercambiar(int *a, int *b) { /* Recibe dos direcciones de enteros. */
    if (a == nullptr || b == nullptr) { /* Verifica que ambas direcciones sean validas. */
        return; /* Sale si alguna direccion no es valida. */
    }

    int temp = *a; /* Guarda temporalmente el contenido apuntado por a. */
    *a = *b;       /* Copia en a el contenido apuntado por b. */
    *b = temp;     /* Copia en b el valor temporal. */
}

void analizarNumeros(int a, int b, int c, int *suma, int *mayor, int *menor) {
    if (suma == nullptr || mayor == nullptr || menor == nullptr) { /* Verifica direcciones. */
        return; /* Sale si alguna direccion no es valida. */
    }

    *suma = a + b + c; /* Escribe la suma en la direccion recibida. */

    *mayor = a; /* Supone inicialmente que a es el mayor. */
    if (b > *mayor) { /* Compara b. */
        *mayor = b;   /* Actualiza el mayor. */
    }
    if (c > *mayor) { /* Compara c. */
        *mayor = c;   /* Actualiza el mayor. */
    }

    *menor = a; /* Supone inicialmente que a es el menor. */
    if (b < *menor) { /* Compara b. */
        *menor = b;   /* Actualiza el menor. */
    }
    if (c < *menor) { /* Compara c. */
        *menor = c;   /* Actualiza el menor. */
    }
}

// ============================================================================
// FUNCIÓN PRINCIPAL
// ============================================================================

int main(void) { /* Funcion principal del programa. */
    int x = 10; /* Primera variable de trabajo. */
    int y = 20; /* Segunda variable de trabajo. */
    int z = 5;  /* Tercera variable de trabajo. */

    int *px = &x; /* px guarda la direccion de x. */

    int suma;   /* Variable para recibir la suma. */
    int mayor;  /* Variable para recibir el mayor. */
    int menor;  /* Variable para recibir el menor. */
    int opcion; /* Opcion seleccionada por el usuario. */

    do { /* Ciclo principal del menu. */
        std::cout << "\n========== MENU CORTO DE PUNTEROS ==========\n";
        std::cout << "1. Mostrar x, &x, px y *px\n";
        std::cout << "2. Duplicar x usando el puntero px\n";
        std::cout << "3. Intercambiar x y y usando punteros\n";
        std::cout << "4. Analizar x, y, z usando punteros de salida\n";
        std::cout << "0. Salir\n";
        std::cout << "Seleccione una opcion: ";
        
        std::cin >> opcion; /* Lee la opcion ingresada por el usuario. */

        switch (opcion) { /* Decide que accion ejecutar. */
            case 1:
                std::cout << "x    = " << x << "\n";
                std::cout << "&x   = " << &x << "\n";
                std::cout << "px   = " << px << "\n";
                std::cout << "*px  = " << *px << "\n";
                break;

            case 2:
                std::cout << "Antes: x = " << x << "\n";
                duplicar(px); /* Modifica x usando su direccion. */
                std::cout << "Despues: x = " << x << "\n";
                break;

            case 3:
                std::cout << "Antes: x = " << x << ", y = " << y << "\n";
                intercambiar(&x, &y); /* Envia direcciones de x y y. */
                std::cout << "Despues: x = " << x << ", y = " << y << "\n";
                break;

            case 4:
                analizarNumeros(x, y, z, &suma, &mayor, &menor);
                std::cout << "Suma  = " << suma << "\n";
                std::cout << "Mayor = " << mayor << "\n";
                std::cout << "Menor = " << menor << "\n";
                break;

            case 0:
                std::cout << "Fin del programa.\n";
                break;

            default:
                std::cout << "Opcion no valida.\n";
                break;
        }
    } while (opcion != 0); /* Repite mientras no se seleccione salir. */

    return 0; /* Finalizacion exitosa. */
}
