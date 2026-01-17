def feed_dogs(*dogs):
    return [dog.eat() for dog in dogs]