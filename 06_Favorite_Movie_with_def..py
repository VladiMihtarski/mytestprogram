def calculate_ascii_sum(movie_title):
    movie_sum = 0
    title_length = len(movie_title)

    for c in movie_title:
        if c.islower():
            movie_sum += ord(c) - (2 * title_length)
        elif c.isupper():
            movie_sum += ord(c) - title_length
        else:
            movie_sum += ord(c)

    return movie_sum


def find_best_movie():
    MAX_MOVIES = 7
    movieCount = 0
    bestMovieSum = 0
    bestMovieTitle = ""

    while movieCount < MAX_MOVIES:
        movieTitle = input()

        if movieTitle == "STOP":
            break

        movieSum = calculate_ascii_sum(movieTitle)

        if movieSum > bestMovieSum:
            bestMovieSum = movieSum
            bestMovieTitle = movieTitle

        movieCount += 1

    if movieCount == MAX_MOVIES:
        return "The limit is reached.\n" + f"The best movie for you is {bestMovieTitle} with {bestMovieSum} ASCII sum."

    return f"The best movie for you is {bestMovieTitle} with {bestMovieSum} ASCII sum."


print(find_best_movie())
