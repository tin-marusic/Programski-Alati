#include <bits/stdc++.h>
using namespace std;
  
bool inRange(unsigned low, unsigned high, unsigned x )
{
    
    return  ((x-low) <= (high-low));
    
}
void zamjena(int lista[], int a , int b){


  int stari = lista[a];
  lista[a] = lista[b];
  lista[b] = stari;

  for (auto i = 0; i < 5; i++)
        cout << lista[i] << " ";

}
  
int main(){
    
    list<int> x = {3,21,135,45,34};

    for (auto i = x.begin(); i != x.end(); i++)
        inRange(10, 100, *i )? cout << *i << ("\n"): cout <<"" ;


    x.reverse();
    for (auto i = x.begin(); i != x.end(); i++)
        cout << *i << " ";
    cout << endl;

    x.sort();
    for (auto i = x.begin(); i != x.end(); i++)
        cout << *i << " ";
    cout << endl;

    int arr[x.size()];
    int k = 0;
    for (int const &i: x) {
        arr[k++] = i;
    }
 
    zamjena(arr,2,3);
        
    return 0;
  
}