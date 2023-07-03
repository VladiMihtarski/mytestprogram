#include <iostream>
#include <string>

float calculateTotalPoints(const std::string& actorName, float initialPoints, int numEvaluators) {
    float totalPoints = initialPoints;

    for (int i = 0; i < numEvaluators; i++) {
        std::string evaluatorName;
        float evaluatorPoints;

        std::getline(std::cin >> std::ws, evaluatorName);  // Прочитаме целия ред, включително интервалите
        std::cin >> evaluatorPoints;

        int evaluatorLength = evaluatorName.length();
        float points = evaluatorLength * evaluatorPoints / 2;

        totalPoints += points;

        if (totalPoints > 1250.5) {
            break;
        }
    }

    return totalPoints;
}

int main() {
    std::string actorName;
    float initialPoints;
    int numEvaluators;

    std::getline(std::cin >> std::ws, actorName);  // Прочитаме целия ред, включително интервалите
    std::cin >> initialPoints;
    std::cin >> numEvaluators;

    float totalPoints = calculateTotalPoints(actorName, initialPoints, numEvaluators);

    if (totalPoints > 1250.5) {
        std::cout << "Congratulations, " << actorName << " got a nominee for leading role with " << totalPoints << "!" << std::endl;
    } else {
        float neededPoints = 1250.5 - totalPoints;
        std::cout << "Sorry, " << actorName << ", you need " << neededPoints << " more!" << std::endl;
        std::getline(std::cin >> std::ws, actorName);  // Прочитаме целия ред, включително интервалите
    }

    return 0;
}
