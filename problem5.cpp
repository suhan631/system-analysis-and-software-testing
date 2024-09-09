#include <bits/stdc++.h>
using namespace std;
int main()
{
int number;
cout<<"Enter a number to find factorial: ";    cin>>number;
long long int fact=1;
int j=1;
for(int i = number; i>0; i--)
{
cout<<"Factorial in iteration "<<j<<" is : "<<fact<<" * "<<i<<" = "<<fact<<endl;
fact = fact * i;
j +=1;
}
cout<<endl<<number<<"! = "<<fact<<endl;
return 0;
}
