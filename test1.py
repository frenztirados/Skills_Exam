from dataclasses import dataclass
from unittest import TestCase

@dataclass
class Longitude:
    value: float

    def __post_init__(self):
        if self.value > 180:
            raise ValueError
        if self.value < -180:
            raise ValueError


@dataclass
class Latitude:
    value: float

    def __post_init__(self):
        if self.value > 90:
            raise ValueError
        if self.value < -90:
            raise ValueError


@dataclass
class GEOCoordinates:
    lat: Latitude
    lon: Longitude