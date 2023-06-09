#include <iostream>
#include <vector>
#include <cmath>
#include <SFML/Graphics.hpp>

void draw_pascal_pyramid(int height) {
    std::vector<std::vector<int>> pascal_triangle(height, std::vector<int>(height, 0));

    // Изчисляване на числата от Триъгълника на Паскал
    for (int i = 0; i < height; i++) {
        pascal_triangle[i][0] = 1;
        pascal_triangle[i][i] = 1;

        for (int j = 1; j < i; j++) {
            pascal_triangle[i][j] = pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j];
        }
    }

    // Изобразяване на пирамидата
    int rows = height;
    int cols = 2 * height - 1;
    int squareSize = 50;
    int padding = 20;
    int windowWidth = cols * squareSize + padding * 2;
    int windowHeight = rows * squareSize + padding * 2;

    sf::RenderWindow window(sf::VideoMode(windowWidth, windowHeight), "Pascal Pyramid");

    sf::Font font;
    if (!font.loadFromFile("arial.ttf")) {
        std::cout << "Error loading font! " << std::endl;
        return;
    }

    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        window.clear(sf::Color::White);

        for (int i = 0; i < rows; i++) {
            int offset = (cols - (2 * i + 1)) / 2;
            for (int j = 0; j <= i; j++) {
                sf::RectangleShape square(sf::Vector2f(squareSize, squareSize));
                square.setPosition((j * 2 + offset) * squareSize + padding, i * squareSize + padding);
                square.setOutlineThickness(2);
                square.setOutlineColor(sf::Color::Black);
                window.draw(square);

                int number = pascal_triangle[i][j];
                sf::Text text;
                text.setString(std::to_string(number));
                text.setCharacterSize(20);
                text.setFillColor(sf::Color::Black);
                text.setStyle(sf::Text::Bold);
                text.setFont(font);
                sf::FloatRect textRect = text.getLocalBounds();
                text.setOrigin(textRect.left + textRect.width / 2.0f, textRect.top + textRect.height / 2.0f);
                text.setPosition((j * 2 + offset) * squareSize + padding + squareSize / 2, i * squareSize + padding + squareSize / 2);
                window.draw(text);
            }
        }

        window.display();
    }
}

int main() {
    int height;
    std::cout << "Enter the height of the pyramid: ";
    std::cin >> height;

    draw_pascal_pyramid(height);

    return 0;
}
