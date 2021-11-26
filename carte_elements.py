from dataclasses import dataclass
from typing import Sequence

@dataclass
class Pizza:
    name: str
    price: float
    description: str
    ingredients: Sequence[str]
    base: str

@dataclass
class Drink:
    name: str
    price: float
    alcoohol: bool

@dataclass
class Dessert:
    name: str
    price: float
    ingredients: Sequence[str]
    home_made: bool

