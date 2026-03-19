#include <iostream>

using namespace std;
int main() {
    cout << "Welcome to the Celsius Converter!";
    cout << "\n Made by Nathan T. Slone";
    cout << "\n Celsius: ";
    int celsius;
    cin >> celsius;
    double fahrenheit = (celsius * 9.0) / 5.0 + 32;
    cout << "Fahrenheit: " << fahrenheit;
    cout << "Please restart the program to input another number.";
    return 0;
}
