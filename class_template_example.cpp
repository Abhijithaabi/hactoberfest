// Class Template
#include <iostream>
using namespace std;

template <typename T>
class Sum
{
    int num1, num2;

public:
    T getSum(T a, T b)
    {
        return (a + b);
    }
};
int main()
{
    Sum<int> obj1;
    cout << "Sum of two integers 50 and 63 is " << obj1.getSum(50, 63) << endl;

    Sum<float> obj2;
    cout << "Sum of two floats 5.3 and 6.3 is " << obj2.getSum(5.3f, 6.3f) << endl;

    Sum<double> obj3;
    cout << "Sum of two doubles 5.0356 and 6.3256 is " << obj3.getSum(5.0356, 6.3256) << endl;

    return 0;
}