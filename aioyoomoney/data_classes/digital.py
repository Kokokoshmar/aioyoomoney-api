from dataclasses import dataclass


@dataclass
class DigitalProduct:
    merchant_article_id: str
    serial: str
    secret: str


@dataclass
class DigitalBonus:
    serial: str
    secret: str


@dataclass
class DigitalGood:
    products: list[DigitalProduct]
    bonuses: list[DigitalBonus]
