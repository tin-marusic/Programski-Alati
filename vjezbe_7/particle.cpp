#include <particle.h>
#include <math.h>
using namespace std;

void Particle::pomak(){
        vy = vy - 9.81*dt;
        x = x + vx * dt;
        y = y + vy * dt;
        };

void Particle::restart(){
        vx = v0 * cos(theta);
        vy = v0 * sin(theta);
        x = x0;
        y = y0;
        };

Particle::Particle (double brzina, double kut, double polozaj_x, double polozaj_y ,double vrijeme){
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

double Particle::range(){
        while (y >= 0){
            pomak();
            }
        double d = x - x0;
        restart();
        return d;
        };

double Particle::time(){
        double t = 0.0;
        while (y >= 0){
            pomak();
            t = t + dt;
            }
        restart();
        return t;
        };


