
#include <iostream>

int main()
{

#ifdef DEBUG
    std::cout << "Debug on!" << std::endl;
#else
    std::cout << "Debug off!" << std::endl;
#endif

    return 0;
}
