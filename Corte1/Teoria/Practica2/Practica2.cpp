#include <iostream>
#include <typeinfo> 
#include <string>

int main() {
    int n1 = 3;
    double n2 = 3.0;
    std::string n3 = "3";

    std::cout << std::endl;

    std::cout << "n1 es: " << typeid(n1).name() << std::endl;
    std::cout << "n2 es: " << typeid(n2).name() << std::endl;
    std::cout << "n3 es: " << typeid(n3).name() << std::endl;

    return 0;
}
