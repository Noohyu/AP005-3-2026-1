#include <iostream>
using namespace std;

int main() {
    // Declaración de las variables
    int num1, num2, suma;

    // Solicitar al usuario que ingrese dos números
    cout << "Introduce el primer número: ";
    cin >> num1;

    cout << "Introduce el segundo número: ";
    cin >> num2;

    // Calcular la suma
    suma = num1 + num2;

    // Imprimir el resultado
    cout << "La suma de " << num1 << " y " << num2 << " es: " << suma << endl;

    return 0;
}

