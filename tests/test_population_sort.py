import pytest
from population_sort import read_population_data, sort_by_area, sort_by_population

@pytest.fixture
def sample_data():
    return [
        ("Country A", 500000, 10000000),
        ("Country B", 1000000, 5000000),
        ("Country C", 750000, 20000000)
    ]

@pytest.mark.parametrize("func,expected", [
    (sort_by_area, [("Country B", 1000000, 5000000), ("Country C", 750000, 20000000), ("Country A", 500000, 10000000)]),
    (sort_by_population, [("Country C", 750000, 20000000), ("Country A", 500000, 10000000), ("Country B", 1000000, 5000000)])
])
def test_sorting_functions(sample_data, func, expected):
    assert func(sample_data) == expected
