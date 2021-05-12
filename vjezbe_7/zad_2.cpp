#include <iostream>
#include <particle.h>
#include <math.h>
using namespace std;

int main(){
    Particle p1(15,60,0,20,0.01);
    cout << "Domet je: " << p1.range() << " m\n" ;
    cout << "Vrijeme je: " << p1.time() << " s\n" ;

    Particle p2(132,43,4,45,0.01);
    cout << "Domet je: " << p2.range() << " m\n" ;
    cout << "Vrijeme je: " << p2.time() << " s\n" ;

    Particle p3(4,4,4,4,0.01);
    cout << "Domet je: " << p3.range() << " m\n" ;
    cout << "Vrijeme je: " << p3.time() << " s\n" ;
    
    return 0;
}