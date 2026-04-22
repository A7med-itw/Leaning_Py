from pydantic import BaseModel


class Building(BaseModel):
    id: int
    building_no: str
    governorate: str
    wilayat: str
    type: str
    units: int
    lat: float
    lng: float


class Stats(BaseModel):
    total: int
    total_units: int
    by_governorate: dict[str, int]
    by_type: dict[str, int]
