from .models import Building

BUILDINGS: list[Building] = [
    Building(id=1,  building_no="B-0001", governorate="Muscat",    wilayat="Muttrah",   type="Residential", units=12, lat=23.6145, lng=58.5923),
    Building(id=2,  building_no="B-0002", governorate="Muscat",    wilayat="Bawshar",   type="Commercial",  units=4,  lat=23.5859, lng=58.4059),
    Building(id=3,  building_no="B-0003", governorate="Muscat",    wilayat="Seeb",      type="Residential", units=24, lat=23.6703, lng=58.1891),
    Building(id=4,  building_no="B-0004", governorate="Dhofar",    wilayat="Salalah",   type="Mixed",       units=18, lat=17.0194, lng=54.0897),
    Building(id=5,  building_no="B-0005", governorate="Dhofar",    wilayat="Taqah",     type="Residential", units=6,  lat=17.0389, lng=54.4017),
    Building(id=6,  building_no="B-0006", governorate="Al Batinah", wilayat="Sohar",    type="Industrial",  units=1,  lat=24.3477, lng=56.7298),
    Building(id=7,  building_no="B-0007", governorate="Al Batinah", wilayat="Barka",    type="Residential", units=10, lat=23.6782, lng=57.8890),
    Building(id=8,  building_no="B-0008", governorate="Al Dakhiliyah", wilayat="Nizwa", type="Commercial",  units=3,  lat=22.9333, lng=57.5333),
    Building(id=9,  building_no="B-0009", governorate="Al Dakhiliyah", wilayat="Bahla", type="Residential", units=8,  lat=22.9833, lng=57.3000),
    Building(id=10, building_no="B-0010", governorate="Musandam",  wilayat="Khasab",    type="Residential", units=5,  lat=26.1794, lng=56.2486),
    Building(id=11, building_no="B-0011", governorate="Al Buraimi", wilayat="Al Buraimi", type="Mixed",     units=14, lat=24.2500, lng=55.7931),
    Building(id=12, building_no="B-0012", governorate="Al Sharqiyah", wilayat="Sur",    type="Residential", units=9,  lat=22.5667, lng=59.5289),
]
