# My C/C++ Practice
The final destination
- Hello World (2021.05.12)


## Hello World (2021.05.12)
- My first run of `C/C++` code in `VS Code`
- Environmental setting is harder than coding
- Find how to complie and run (rather easier than VSC menu)

#### IamYourFather.cpp :
```cpp
#include <iostream>

using namespace std;

int main()
{
    cout << "I am your father." << endl;
    system("pause");
    return 0;
}
```

##### Command Line
```
gcc IamYourFather_c.c -o IamYourFather_c.exe
```
```
.\IamYourFather
```

#### IamYourFather_c.c :
```c
#include <stdio.h>
#include <windows.h>    // for using system()

int main()
{
    printf("I am your father.\n");
    system("pause");
    return 0;
}
```

##### Command Line
```
g++ IamYourFather.cpp -o IamYourFather.exe
```
```
.\IamYourFather_c
```