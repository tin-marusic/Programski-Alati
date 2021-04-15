#include <iostream>
#include<math.h>
#define pdd pair<double, double>
using namespace std;

void lineFromPoints(pdd P, pdd Q)
{
    double a = Q.second - P.second;
    double b = P.first - Q.first;
    double c = a * (P.first) + b * (P.second);
 
    if (b < 0) {
        cout << "The line passing through points P and Q "
                "is: "
             << a << "x - " << b << "y = " << c << endl;
    }
    else {
        cout << "The line passing through points P and Q "
                "is: "
             << a << "x + " << b << "y = " << c << endl;
    }
}
 
int main()
{
    pdd P = make_pair(3, 2);
    pdd Q = make_pair(2, 6);
    lineFromPoints(P, Q);
    return 0;
}