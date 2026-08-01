#include <iostream>
#include <cmath>
#include<conio.h>
using namespace std;

int main()
{
    int num, sum = 0, temp, remainder, n = 0;
    cout << "\nEnter an integer: ";
    cin >> num;
    temp = num;
    int k = temp;

    while (k > 0) {
        k /= 10;
        n++;
    }

    while (temp > 0) {
        remainder = temp % 10;
        sum += static_cast<int>(std::pow(remainder, n));
        temp /= 10;
    }

    if (sum == num)
        cout << num << " is an Armstrong number." << endl;
    else
        cout << num << " is not an Armstrong number." << endl;

    return 0;
}