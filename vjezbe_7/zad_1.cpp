#include <iostream>
#include <math.h>
using namespace std;

class Particle{
    private:
        double v0;
        double theta;
        double x0;
        double y0;
        double vx;
        double vy;
        double x;
        double y;
        double dt;
        
        void pomak(){
            vy = vy - 9.81*dt;
            x = x + vx * dt;
            y = y + vy * dt;
        };

        void restart(){
            vx = v0 * cos(theta);
            vy = v0 * sin(theta);
            x = x0;
            y = y0;
        };
    
    public:
        Particle (double brzina, double kut, double polozaj_x, double polozaj_y ,double vrijeme){
            v0 = brzina;
            theta = (kut/180)*3.14159;
            x0 = polozaj_x;
            y0 = polozaj_y;
            vx = v0 * cos(theta);
            vy = v0 * sin(theta);
            x = x0;
            y = y0;
            dt = vrijeme;
        };

        double range(){
            while (y >= 0){
                pomak();
            }
            double d = x - x0;
            restart();
            return d;
        };

        double time(){
            double t = 0.0;
            while (y >= 0){
                pomak();
                t = t + dt;
            }
            restart();
            return t;
        };
};

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