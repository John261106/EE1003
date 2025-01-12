#include <math.h>
void trapezoidal(double *x, double *y, int n, double h) {
    y[0] = 0; 
    for (int i = 0; i < n - 1; i++) {
        y[i+1]=y[i]+h*cos(x[i])-(h*h*sin(x[i]))/2;
    }
}
void function(double *x,double *y,int n){
	for(int i=0;i<n;i++){
		y[i]=cos(x[i]);
	}
}

