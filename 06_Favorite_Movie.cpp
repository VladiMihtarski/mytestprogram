#include <iostream>
#include <string>

int main() {
    const int MAX_MOVIES = 7;
    std::string movieTitle;
    std::string bestMovieTitle;
    int bestMovieSum = 0;
    int movieCount = 0;

    while (movieCount < MAX_MOVIES) {
        std::getline(std::cin, movieTitle);

        if (movieTitle == "STOP") {
            break;
        }

        int movieSum = 0;
        int titleLength = movieTitle.length();

        for (char c : movieTitle) {
            if (islower(c)) {
                movieSum += static_cast<int>(c) - (2 * titleLength);
            } else if (isupper(c)) {
                movieSum += static_cast<int>(c) - titleLength;
            } else {
                movieSum += static_cast<int>(c);
            }
        }

        if (movieSum > bestMovieSum) {
            bestMovieSum = movieSum;
            bestMovieTitle = movieTitle;
        }

        movieCount++;
    }

    if (movieCount == MAX_MOVIES) {
        std::cout << "The limit is reached." << std::endl;
    }

    std::cout << "The best movie for you is " << bestMovieTitle << " with " << bestMovieSum << " ASCII sum." << std::endl;

    return 0;
}
#include <iostream>
#include <string>

int main() {
    const int MAX_MOVIES = 7;
    std::string movieTitle;
    std::string bestMovieTitle;
    int bestMovieSum = 0;
    int movieCount = 0;

    while (movieCount < MAX_MOVIES) {
        std::getline(std::cin, movieTitle);

        if (movieTitle == "STOP") {
            break;
        }

        int movieSum = 0;
        int titleLength = movieTitle.length();

        for (char c : movieTitle) {
            if (islower(c)) {
                movieSum += static_cast<int>(c) - (2 * titleLength);
            } else if (isupper(c)) {
                movieSum += static_cast<int>(c) - titleLength;
            } else {
                movieSum += static_cast<int>(c);
            }
        }

        if (movieSum > bestMovieSum) {
            bestMovieSum = movieSum;
            bestMovieTitle = movieTitle;
        }

        movieCount++;
    }

    if (movieCount == MAX_MOVIES) {
        std::cout << "The limit is reached." << std::endl;
    }

    std::cout << "The best movie for you is " << bestMovieTitle << " with " << bestMovieSum << " ASCII sum." << std::endl;

    return 0;
}
