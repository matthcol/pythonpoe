import re
from typing import List

def sanitize_cities_fr(cities: List[str]):
    return list(filter(
        lambda city: re.match(r"[a-z ]+", city, flags=re.I),
        (city.strip() for city in cities)
    ))

cities = [
    " Pau",
    "Toulouse\n",
    " \tMontpellier",
    '東京',
]

cities2 = sanitize_cities_fr(cities)
print(cities2)

city_tuples =  (
    " Pau",
    "Toulouse\n",
    " \tMontpellier",
    '東京',
)
cities3 = sanitize_cities_fr(city_tuples)
print(cities3)

bad_data = [ 1, 2, 3, 4 ]
sanitize_cities_fr(bad_data)
