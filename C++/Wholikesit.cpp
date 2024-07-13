#include <string>
#include <vector>
#include <iostream>

std::string likes(const std::vector<std::string> &names)
{
    switch(names.size())
    {
        case 0:
            return "no one likes this"; // Ако няма имена в списъка
        case 1:
            return names[0] + " likes this"; // Ако има само едно име
        case 2:
            return names[0] + " and " + names[1] + " like this"; // Ако има две имена
        case 3:
            return names[0] + ", " + names[1] + " and " + names[2] + " like this"; // Ако има три имена
        default:
            return names[0] + ", " + names[1] + " and " + std::to_string(names.size() - 2) + " others like this"; // Ако има повече от три имена
    }
}

int main()
{
    // Примери за тестване
    std::vector<std::string> test1 = {};
    std::vector<std::string> test2 = {"Peter"};
    std::vector<std::string> test3 = {"Jacob", "Alex"};
    std::vector<std::string> test4 = {"Max", "John", "Mark"};
    std::vector<std::string> test5 = {"Alex", "Jacob", "Mark", "Max"};
    
    std::cout << likes(test1) << std::endl; // no one likes this
    std::cout << likes(test2) << std::endl; // Peter likes this
    std::cout << likes(test3) << std::endl; // Jacob and Alex like this
    std::cout << likes(test4) << std::endl; // Max, John and Mark like this
    std::cout << likes(test5) << std::endl; // Alex, Jacob and 2 others like this
    
    return 0;
}
