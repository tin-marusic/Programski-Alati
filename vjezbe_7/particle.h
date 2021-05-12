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

        void pomak();
        void restart();

    public:
        Particle (double brzina, double kut, double polozaj_x, double polozaj_y ,double vrijeme);
        ~Particle();

        double range();
        double time();
};
