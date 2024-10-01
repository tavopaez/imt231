#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cmath> // Para usar abs()
using namespace std;

int main() {
    // Mensaje de bienvenida
    std::cout << "***************" << endl;
    std::cout << "*Bienvenido al Juego de la Adivinanza   *!" << endl;
    std::cout << "Ingrese un Numero en el Rango : 1 a 100!" << endl;
    std::cout << "***************" << endl;

    // Selección de la dificultad
    cout << endl;
    cout << "Escoja el nivel de dificultad" << endl;
    cout << "Facil (F), Medio (M) o Dificil (D)" << endl;
    char dificultad;
    cin >> dificultad;
    
    int numero_tentativas;
    if (dificultad == 'F') {
        numero_tentativas = 15;
    } else if (dificultad == 'M') {
        numero_tentativas = 10;
    } else if (dificultad == 'D') {
        numero_tentativas = 5;
    } else {
        cout << "Dificultad no válida. Se utilizará el nivel Medio." << endl;
        numero_tentativas = 10;
    }

    // Generar el número secreto
    srand(time(0));
    const int NUMERO_SECRETO = 1 + rand() % 100; // Número aleatorio entre 1 y 100
    int adivina;
    bool no_acerto = true;
    int intentos = 0;
    double puntos = 1000.0; // Puntuación inicial

    // Bucle del juego
    while (no_acerto && intentos < numero_tentativas) {
        intentos++;
        cout << "Tentativa " << intentos << " de " << numero_tentativas << endl;
        cout << "¿Cuál es el número?" << endl;
        cin >> adivina;

        // Cálculo de los puntos perdidos
        double puntos_perdidos = abs(adivina - NUMERO_SECRETO) / 2.0;
        puntos -= puntos_perdidos;

        // Verificación de la adivinanza
        if (adivina == NUMERO_SECRETO) {
            cout << "¡Felicidades! Adivinaste el número secreto." << endl;
            no_acerto = false;
        } else if (adivina > NUMERO_SECRETO) {
            cout << "El número ingresado es mayor que el número secreto." << endl;
        } else {
            cout << "El número ingresado es menor que el número secreto." << endl;
        }
    }

    // Mensaje final y puntuación
    if (!no_acerto) {
        cout << "¡Felicidades! Adivinaste el número secreto en " << intentos << " intentos." << endl;
    } else {
        cout << "Se agotaron las tentativas. El número secreto era " << NUMERO_SECRETO << "." << endl;
    }

    // Mostrar la puntuación
    cout.precision(2);
    cout << fixed;
    cout << "Su puntuación fue de " << puntos << " puntos." << endl;

    return 0;
}
