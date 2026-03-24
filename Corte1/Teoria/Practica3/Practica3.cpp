#include <iostream>

int main() {
    int numero;

    std::cout << "Introduce un número: ";
    std::cin >> numero;

    if (numero % 2 == 0) {
        std::cout << "El número " << numero << " es Par" << std::endl;
    } else {
        std::cout << "El número " << numero << " es Impar" << std::endl;
    }

    return 0;
}
