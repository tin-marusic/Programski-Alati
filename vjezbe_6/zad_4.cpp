#include <iostream>
using namespace std;

void dvije_jednadzbe(float a1, float b1, float c1, float a2, float b2, float c2){
    float y = (c2 * a1 - a2 * c1) / (-a2 * b1 + a1 * b2);
    float x = (c1 - b1*y) / a1;
    std::cout << "x: " << x << "\ny: " << y <<std::endl;
};

int main(){
    dvije_jednadzbe(1,9,12,4,-4,8);
    return 0;
};