#include <iostream>
#include "mysum.h"

double
test_passing_array(double* data, int len) {
    double total_1{}, total_2{}, total_3{}, total_4{};

    for(int i = 0, k = 0; i <= (len/4); i++, k += 4) {
        total_1 += data[k];
        total_2 += data[k+1];
        total_3 += data[k+2];
        total_4 += data[k+3];
    }

    return (total_1 + total_2) + (total_3 + total_4);
}


void
tmp_function(
    void
) {
    int arr[] = {1,2,3,4,5};

    auto &&range = arr;
    auto begin = std::begin(range);

    for(const auto &x: arr) {
        std::cout << x << std::endl;
        std::cout << begin << std::endl;
    }

}