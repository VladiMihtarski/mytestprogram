#include <iostream>
#include <cmath>  // Include the cmath library for pow function

double calculateSnowballValue(int weight, int time, int quality) {
    // Calculate the value of a snowball using the given weight, time, and quality
    return pow(static_cast<double>(weight) / time, quality);
}

int main() {
    int n;
    std::cin >> n;  // Read the number of snowballs

    double highestValue = -1;  // Initialize with a value lower than any possible snowball value
    int bestWeight, bestTime, bestQuality;

    // Iterate through each snowball
    for (int i = 0; i < n; ++i) {
        int weight, time, quality;
        std::cin >> weight >> time >> quality;

        // Calculate the value of the current snowball
        double snowballValue = calculateSnowballValue(weight, time, quality);

        // Update the highest value if necessary
        if (snowballValue > highestValue) {
            highestValue = snowballValue;
            bestWeight = weight;
            bestTime = time;
            bestQuality = quality;
        }
    }

    // Print the details of the snowball with the highest value
    std::cout << bestWeight << " : " << bestTime << " = " << static_cast<int>(highestValue + 0.5) << " (" << bestQuality << ")\n";

    return 0;
}
