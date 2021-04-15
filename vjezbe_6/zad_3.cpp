#include <iostream>
using namespace std;
  
bool inRange(unsigned low, unsigned high, unsigned x )
{
    
    return  ((x-low) <= (high-low));
    
}
  
int main()
{
    int x[5] = {5,12,52,5,7};
    for (int i=0 ; i<5 ;i++){
    inRange(10, 100, x[i] )? cout << x[i] << ("\n"): cout <<"" ;
    }
}