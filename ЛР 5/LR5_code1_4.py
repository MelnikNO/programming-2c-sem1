def find_country(city, countrylist):

    """Находит страну по названию города, где параметры:
    city: Название города.
    countrylist: Словарь, где ключи - страны, а значения - списки городов.
    """

    for country, cities in countrylist.items():
        if city in cities:
            yield country


def list_city(countrylist):

    """Создает список всех городов из словаря стран и городов, где параметры:
    countrylist: Словарь, где ключи - страны, а значения - списки городов.
    Возвращает список всех городов.
    """

    cities = []
    for city_list in countrylist.values():
        cities.extend(city_list)
    return cities


def main():
    countries_city = {
        "Россия": ["Москва", "Санкт - Петербург", "Казань", "Новосибирск"],
        "США": ["Нью - Йорк", "Лос - Анджелес", "Чикаго", "Хьюстон"],
        "Франция": ["Париж", "Марсель", "Лион", "Ницца"],
        "Италия": ["Рим", "Милан", "Венеция", "Флоренция"],
        "Китай": ["Пекин", "Шанхай", "Гуанчжоу", "Шэньчжэнь"]
    }

    c = list_city(countries_city)
    print("Доступные города: ", "\n ".join(c))

    city = input("Введите название города из предложенного списка: ")
    country = list(find_country(city, countries_city))

    if country:
        print(f"{city} находится в: {', '.join(country)}")
    else:
        print(f"{city} не найден в списке стран")


if __name__ == "__main__":
    main()