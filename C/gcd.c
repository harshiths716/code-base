/*

The greatest common divisor (GCD) of two or more integers (at least one of which is not zero), 
is the largest positive integer that divides the numbers without a remainder.
For example, the GCD of 8 and 12 is 4.

NOTE: The following program computes gcd of two numbers.

*/

#include<stdio.h>

  int gcd(int a,int b){  

    int c=b%a;
    
    if(c==0) return a;
    else return gcd(c,a);
  }


int main(){
  
    int x,y;
    
    printf("GCD of two numbers\nEnter x and y:: ");
    scanf("%d%d",&x,&y);
    
    if(x<y) printf("\n GCD:: %d",gcd(x,y));
    else
      printf("\n GCD:: %d",gcd(y,x));
  
    return 0;
}

/*
With regards,
Shivaji Varma
*/
