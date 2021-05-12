# My C/C++ Practice
The final destination
- Hello World (2021.05.12)


## Hello World (2021.05.12)
- My first run of **`C`/`C++`** code in **Visual Studio Code**
- Environmental setting is harder than coding
- Find how to **complie** and **run** (rather easier than VSC menu)
- `gcc` (for `C`) and `g++` (for `C++`) seem not so different

#### IamYourFather_c.c :
```c
#include <stdio.h>
#include <windows.h>    // for using system()

int main()
{
    printf("I am your father.\n");
    // system("pause");
    return 0;
}
```

##### Command Line
```
gcc --help
gcc -S IamYourFather_c.c
gcc IamYourFather_c.c -o IamYourFather_c.exe
```
```
.\IamYourFather_c
```
> I am your father.

#### IamYourFather_cpp.cpp :
```cpp
#include <iostream>

using namespace std;

int main()
{
    cout << "I am your father." << endl;
    // system("pause");
    return 0;
}
```

##### Command Line
```
g++ --help
g++ -S IamYourFather_cpp.cpp
g++ IamYourFather_cpp.cpp -o IamYourFather_cpp.exe
```
```
.\IamYourFather_cpp
```
> I am your father.