#include<iostream>
#include<iomanip>
#include<thread>
#include<chrono>
#include<string>

#include<fstream> // Para guardar los resultados en un archivo de texto

using namespace std;

// Patrones: el segundo tiene x1 = 3
const int N = 4;

const double inputs[N][3] = {
    {2,3,4}, {3,3,4}, {1,2,1}, {3,1,2}
};

const int targets[N] = {0,1,0,1};

double w1 = 0.0, w2 = 0.0, w3 = 0.0, b = 0.0;
const double eta = 0.2;
const int maxEpochs = 30;
const int pauseSeconds = 3;

int activation(double z) {
    return (z >= 0.0) ? 1 : 0;
}

double weightedSum(double x1, double x2, double x3) {
    return w1*x1 + w2*x2 + w3*x3 + b;
}

int predict(double x1, double x2, double x3) {
    return activation(weightedSum(x1, x2, x3));
}

void printTrainingHeader() {
    cout << "\nFASE 1: ENTRENAMIENTO\n";
    cout << "z_ant y y_ant: ANTES de actualizar.\n";
    cout << "w1_n w2_n w3_n b_n: DESPUES de actualizar.\n";
    cout << string(124, '-') << '\n';

    cout << setw(4) << "P" << setw(6) << "x1"
         << setw(6) << "x2" << setw(6) << "x3"
         << setw(5) << "t" << setw(9) << "z_ant"
         << setw(7) << "y_ant" << setw(5) << "e"
         << setw(9) << "dw1" << setw(9) << "dw2"
         << setw(9) << "dw3" << setw(9) << "db"
         << setw(10) << "w1_n" << setw(10) << "w2_n"
         << setw(10) << "w3_n" << setw(10) << "b_n" << '\n';

    cout << string(124, '-') << '\n';
}

// Evaluacion con parametros fijos: nunca modifica pesos.
int evaluate(bool showTable) {
    int errors = 0;

    if (showTable) {
        cout << "\nFASE 2: EVALUACION SIN APRENDIZAJE\n";
        cout << string(72, '-') << '\n';

        cout << setw(5) << "P" << setw(7) << "x1"
             << setw(7) << "x2" << setw(7) << "x3"
             << setw(6) << "t" << setw(10) << "z_final"
             << setw(9) << "y_final" << setw(8) << "e"
             << setw(10) << "Estado" << '\n';

        cout << string(72, '-') << '\n';
    }

    for (int i = 0; i < N; i++) {
        double x1 = inputs[i][0];
        double x2 = inputs[i][1];
        double x3 = inputs[i][2];
        int t = targets[i];

        double z = weightedSum(x1, x2, x3);
        int y = activation(z);
        int e = t - y;

        if (e != 0) errors++;

        if (showTable) {
            cout << setw(5) << i+1 << setw(7) << x1
                 << setw(7) << x2 << setw(7) << x3
                 << setw(6) << t << setw(10) << z
                 << setw(9) << y << setw(8) << e
                 << setw(10) << (e == 0 ? "OK" : "ERROR")
                 << '\n';
        }
    }

    if (showTable) {
        cout << string(72, '-') << '\n';
        cout << "Errores en evaluacion: " << errors
             << " de " << N << '\n';
    }

    return errors;
}

void train() {

    ofstream errorData("errores.dat");
    ofstream zData("z_por_epoca.dat");

    if (!errorData || !zData) {
        cerr << "Error al crear los archivos de datos.\n";
        return;
    }

    errorData << "# Epoca Errores\n";
    zData << "# Epoca z1 z2 z3 z4\n";

    errorData << setprecision(10);
    zData << setprecision(10);

    // Aquí continúa el código original

    for (int epoch = 1; epoch <= maxEpochs; epoch++) {
        cout << "\n========== EPOCA " << epoch
             << " ==========\n";

        printTrainingHeader();

        int corrections = 0;

        for (int i = 0; i < N; i++) {
            double x1 = inputs[i][0];
            double x2 = inputs[i][1];
            double x3 = inputs[i][2];
            int t = targets[i];

            double z = weightedSum(x1, x2, x3);
            int y = activation(z); // Antes de actualizar
            int e = t - y;

            double dw1 = eta * e * x1;
            double dw2 = eta * e * x2;
            double dw3 = eta * e * x3;
            double db = eta * e;

            w1 += dw1;
            w2 += dw2;
            w3 += dw3;
            b += db;

            if (e != 0) corrections++;

            cout << setw(4) << i+1
                 << setw(6) << x1 << setw(6) << x2
                 << setw(6) << x3 << setw(5) << t
                 << setw(9) << z << setw(7) << y
                 << setw(5) << e << setw(9) << dw1
                 << setw(9) << dw2 << setw(9) << dw3
                 << setw(9) << db << setw(10) << w1
                 << setw(10) << w2 << setw(10) << w3
                 << setw(10) << b << '\n';
        }

        cout << string(124, '-') << '\n';

        cout << "Correcciones durante entrenamiento: "
             << corrections << '\n';

        int errors = evaluate(true);

        // Guardar cantidad de errores de la epoca
    errorData << epoch << " " << errors << '\n';

    // Guardar valores de z de los cuatro patrones
    zData << epoch;

    for (int i = 0; i < N; i++) {

    double z = weightedSum(
        inputs[i][0],
        inputs[i][1],
        inputs[i][2]
    );

        zData << " " << z;
    }

        zData << '\n'; 

        cout << "\nRESUMEN DE EPOCA " << epoch << '\n';
        cout << "Correcciones: " << corrections
             << " | Errores en evaluacion: " << errors << '\n';

        cout << "w1=" << w1 << " w2=" << w2
             << " w3=" << w3 << " b=" << b << '\n';

        if (errors == 0) {
            cout << "APRENDIZAJE COMPLETADO EN "
                 << epoch << " EPOCAS\n";
            return;
        }

        cout << "Siguiente epoca en " << pauseSeconds
             << " segundos...\n";

        cout.flush();
        this_thread::sleep_for(chrono::seconds(pauseSeconds));
    }

    cout << "Se alcanzo el limite de epocas.\n";
}

int main() {
    cout << fixed << setprecision(2);

    cout << "PERCEPTRON DE TRES ENTRADAS\n";
    cout << "Tasa de aprendizaje: " << eta << '\n';

    cout << "\nESTADO INICIAL\n";
    evaluate(true);

    train();

    cout << "\nVERIFICACION FINAL\n";
    evaluate(true);

    return 0;
}