#include <map>
#include <vector>
#include <iostream>
#include <iomanip>
#include <ctime>
#include <algorithm>
#include <fstream>

// Opisanie nabora blinov
struct nabor
{
    std::vector<float> sleva{};
    std::vector<float> sprava{};
    friend std::ostream & operator<<(std::ostream& os, const nabor& nabor);
};

std::ostream& operator<<(std::ostream& os, const nabor& nabor)
{
    os << std::setprecision(2) << '[';
    for (const auto& x : nabor.sleva) os << x << ", ";
    os << "\b\b] <===> [";
    for (const auto& x : nabor.sprava) os << x << ", ";
    os << "\b\b] ";
    return os;
}

struct resultat
{
    uint32_t amount;
    float first;
    float second;
};

// Uslovie
auto grif = 12;
const auto blinchiki_amount = 100;
std::vector<float> bliny = {4.5, 4.5, 8.5, 8.5, 8, 8}; // 13, 13, , 11, 11, 11, 11
std::vector<int> coefficienty(bliny.size());
std::map<float, nabor> varianty;
std::vector<resultat> result;

// Ves perekosa na odnu storonu shtangi
auto perekos()
{
    float suma_blinov = 0;
    for (auto i{0}; i < bliny.size(); i++)
        suma_blinov += coefficienty[i] * bliny[i];
    return suma_blinov;
}

// Ves shtangi s odetim naborom blinov
auto ves()
{
    float suma_blinov = 0;
    for (auto i{0}; i < bliny.size(); i++)
        suma_blinov += abs(coefficienty[i]) * bliny[i];
    return suma_blinov + grif;
}

// Nabor blinov dlya vesa vishe
auto nabor_blinov()
{
    nabor nabor_blinov{};
    for (auto i{0}; i < bliny.size(); i++)
        if (coefficienty[i] == 1)
            nabor_blinov.sleva.push_back(bliny[i]);
        else if (coefficienty[i] == -1)
            nabor_blinov.sprava.push_back(bliny[i]);
    return nabor_blinov;
}

// Recursivnoe vzveshivanie
auto vzvesit(int index = -1, int coefficient = 1) -> void
{
    if (index < (int)bliny.size())
    {
        if (++index) coefficienty[index - 1] = coefficient;
        vzvesit(index, 1);
        vzvesit(index, 0);
        vzvesit(index, -1);
    }
    else if (perekos() == 0)
        varianty[ves()] = nabor_blinov();
}

// Samo rezhenie!
int main() 
{
    vzvesit();
    auto start = time(0);
    for (int i{0}; i < blinchiki_amount; i++)
    {
        for (int j{i}; j < blinchiki_amount; j++)
        {
            bliny[bliny.size() - 2] = 0.5 * i;
            bliny[bliny.size() - 1] = 0.5 * j;
            vzvesit();
            result.push_back({(uint32_t)varianty.size(), 0.5f * i, 0.5f * j});
            varianty.clear();
        }
        std::cout << i + 1 << "% done" << std::endl;
    }

    std::sort(result.begin(), result.end(), [](const resultat lhs, const resultat rhs)
    {
        return lhs.amount > rhs.amount;
    });

    auto end = time(0);
    std::cout << "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n";
    std::cout << "Time spent: " << end - start << 's' << std::endl;
    std::cout << "The most profitable to buy are blinchiki: " << result[0].first 
        << " and " << result[0].second << std::endl;
    std::cout << "They give as many as " << result[0].amount 
        << " shtanga combinations.\n" << std::endl;
    std::cout << "\nMost profitable combinations(top 50):\n";
    for (auto i{0}; i < 50; i++)
        std::cout << i + 1 << ") Amount: " << result[i].amount << ". Blinchiki: " << result[i].first
            << " and " << result[i].second << ".\n";
