#include <math.h>
#include <stdio.h>

double slow_computation(int n) {
    double result = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 1000; j++) {
            result += sin(i * j) * cos(i * j);
        }
    }
    return result;
}

int main() {
    double r = 0;
    for (int i = 0; i < 100; i++) {
        r += slow_computation(1000);
    }
    printf("Result: %f\n", r);
    return 0;
}
