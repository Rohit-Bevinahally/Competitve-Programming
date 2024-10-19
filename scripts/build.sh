g++-10 -static -DLOCAL -lm -s -x c++ -Wall -Wextra -Wno-unused -O2 -fsanitize=undefined -fno-sanitize-recover -std=c++20 -o $1 $1.cpp 
