from collections import Counter
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .data import BUILDINGS
from .models import Building, Stats

STATIC_DIR = Path(__file__).parent / "static"

app = FastAPI(title="Buildings Dashboard")


@app.get("/api/buildings", response_model=list[Building])
def list_buildings(governorate: str | None = None, type: str | None = None) -> list[Building]:
    items = BUILDINGS
    if governorate:
        items = [b for b in items if b.governorate == governorate]
    if type:
        items = [b for b in items if b.type == type]
    return items


@app.get("/api/buildings/{building_id}", response_model=Building)
def get_building(building_id: int) -> Building:
    for b in BUILDINGS:
        if b.id == building_id:
            return b
    raise HTTPException(status_code=404, detail="Building not found")


@app.get("/api/stats", response_model=Stats)
def stats() -> Stats:
    by_gov = Counter(b.governorate for b in BUILDINGS)
    by_type = Counter(b.type for b in BUILDINGS)
    return Stats(
        total=len(BUILDINGS),
        total_units=sum(b.units for b in BUILDINGS),
        by_governorate=dict(by_gov),
        by_type=dict(by_type),
    )


app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/")
def index() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")
