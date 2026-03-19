#include <iostream>

using namespace std;
int main() {
    cout << "Welcome to the Fahrenheit Converter!";
    cout << "\n Made by Nathan T. Slone";
    cout << "\n Fahrenheit: ";
    int fahrenheit;
    cin >> fahrenheit;
    double celsius = (fahrenheit - 32) / 1.8;
    cout << "Celsius: " << celsius << ".";
    cout << "\n Please restart the program to do another input";
    return 0;
}
