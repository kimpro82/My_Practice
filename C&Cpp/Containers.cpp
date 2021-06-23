#include <iostream>

using namespace std;

int main()
{
    // array (old school)
    int arr[3] = {1, 2, 3};
    for (int i = 0; i < sizeof(arr)/4; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;

    // array (C++11)

    // vector

    // list

    // tuple

    return 0;
}