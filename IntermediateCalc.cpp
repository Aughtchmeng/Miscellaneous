#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

int main() {
    vector<string> history;
    bool running = true;

    cout << "=================================\n";
    cout << "      ADVANCED CALCULATOR\n";
    cout << "=================================\n";

    while (running) {
        cout << "\nChoose an operation:\n";
        cout << "1. Addition (+)\n";
        cout << "2. Subtraction (-)\n";
        cout << "3. Multiplication (*)\n";
        cout << "4. Division (/)\n";
        cout << "5. Modulo (%)\n";
        cout << "6. Power (^)\n";
        cout << "7. Square Root (sqrt)\n";
        cout << "8. View History\n";
        cout << "9. Quit\n";

        int choice;
        cout << "\nEnter choice: ";
        cin >> choice;

        double a, b, result;

        switch (choice) {

            case 1:
                cout << "First number: ";
                cin >> a;
                cout << "Second number: ";
                cin >> b;

                result = a + b;

                cout << "Result: " << result << endl;

                history.push_back(
                    to_string(a) + " + " +
                    to_string(b) + " = " +
                    to_string(result)
                );
                break;

            case 2:
                cout << "First number: ";
                cin >> a;
                cout << "Second number: ";
                cin >> b;

                result = a - b;

                cout << "Result: " << result << endl;

                history.push_back(
                    to_string(a) + " - " +
                    to_string(b) + " = " +
                    to_string(result)
                );
                break;

            case 3:
                cout << "First number: ";
                cin >> a;
                cout << "Second number: ";
                cin >> b;

                result = a * b;

                cout << "Result: " << result << endl;

                history.push_back(
                    to_string(a) + " * " +
                    to_string(b) + " = " +
                    to_string(result)
                );
                break;

            case 4:
                cout << "First number: ";
                cin >> a;
                cout << "Second number: ";
                cin >> b;

                if (b == 0) {
                    cout << "Error: Cannot divide by zero.\n";
                } else {
                    result = a / b;

                    cout << "Result: " << result << endl;

                    history.push_back(
                        to_string(a) + " / " +
                        to_string(b) + " = " +
                        to_string(result)
                    );
                }
                break;

            case 5: {
                int x, y;

                cout << "First integer: ";
                cin >> x;

                cout << "Second integer: ";
                cin >> y;

                if (y == 0) {
                    cout << "Error: Cannot modulo by zero.\n";
                } else {
                    int modResult = x % y;

                    cout << "Result: " << modResult << endl;

                    history.push_back(
                        to_string(x) + " % " +
                        to_string(y) + " = " +
                        to_string(modResult)
                    );
                }
                break;
            }

            case 6:
                cout << "Base: ";
                cin >> a;

                cout << "Exponent: ";
                cin >> b;

                result = pow(a, b);

                cout << "Result: " << result << endl;

                history.push_back(
                    to_string(a) + " ^ " +
                    to_string(b) + " = " +
                    to_string(result)
                );
                break;

            case 7:
                cout << "Number: ";
                cin >> a;

                if (a < 0) {
                    cout << "Error: Cannot square root a negative number.\n";
                } else {
                    result = sqrt(a);

                    cout << "Result: " << result << endl;

                    history.push_back(
                        "sqrt(" +
                        to_string(a) + ") = " +
                        to_string(result)
                    );
                }
                break;

            case 8:
                cout << "\n===== HISTORY =====\n";

                if (history.empty()) {
                    cout << "No calculations yet.\n";
                } else {
                    for (size_t i = 0; i < history.size(); i++) {
                        cout << i + 1 << ". "
                             << history[i] << endl;
                    }
                }
                break;

            case 9:
                running = false;
                cout << "\nGoodbye!\n";
                break;

            default:
                cout << "Invalid choice.\n";
        }
    }

    return 0;
}