def read_population_data(filename):
    """Зчитує дані про популяцію з файлу."""
    with open(filename, 'r', encoding='utf-8') as file:
        data = [line.strip().split(", ") for line in file.readlines()]
    return [(country, float(area), int(population)) for country, area, population in data]

def sort_by_area(data):
    """Сортує дані за площею (від найбільшої до найменшої)."""
    return sorted(data, key=lambda x: x[1], reverse=True)

def sort_by_population(data):
    """Сортує дані за населенням (від найбільшого до найменшого)."""
    return sorted(data, key=lambda x: x[2], reverse=True)
