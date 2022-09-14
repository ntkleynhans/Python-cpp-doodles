
### Compile c++ lib (MAC)
```
clang -shared mysum.o -o mysum.dylib
clang -std=c++11 -Wall -Wextra -pedantic -O2 -mavx512f -c -fPIC mysum.cc -o mysum.o
```
