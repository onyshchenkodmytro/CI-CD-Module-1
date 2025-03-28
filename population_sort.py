def read_population_data(filename):
    """Зчитує дані про популяцію з файлу."""
    with open(filename, 'r', encoding='utf-8') as file:
        data = [line.strip().split(", ") for line in file.readlines()]
    return [(country, float(area), int(population)) for country, area, population in data]
