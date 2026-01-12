from dog import Dogs, HerdingGroup, WorkingDogs, BorderCollie, SiberianHusky, feed_dogs

def test_polymorphism():
    collie = BorderCollie(3, "Female", "Skye", 10)
    husky = SiberianHusky(5, "Male", "Ghost", True)

    assert isinstance(collie, Dogs)
    assert isinstance(collie, HerdingGroup)
    assert isinstance(husky, Dogs)
    assert isinstance(husky, WorkingDogs)


def test_inherited_methods():
    collie = BorderCollie(2, "Male", "Ace", 9)

    assert collie.walk() == "Ace is walking."
    assert collie.herd() == "Ace is herding."


def test_variadic_function_and_list():
    dog1 = BorderCollie(1, "Female", "Luna", 8)
    dog2 = SiberianHusky(4, "Male", "Thor", True)

    meals = feed_dogs(dog1, dog2)

    assert isinstance(meals, list)
    assert len(meals) == 2
