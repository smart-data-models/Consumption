from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, RootModel, constr


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class MeasurementUnit(Enum):
    MTQ = 'MTQ'


class MeasurementUnit1(Enum):
    KWH = 'KWH'


class EnergyConsumed(BaseModel):
    measurementUnit: Optional[Union[MeasurementUnit, MeasurementUnit1]] = Field(
        None,
        description='Measurement unit used. Official list at https://unece.org/trade/documents/2021/06/uncefact-rec20',
    )
    value: Optional[float] = Field(
        None, description='Value of the amount of the energy consumed'
    )


class Currency(Enum):
    EUR = 'EUR'
    GPD = 'GPD'
    JPY = 'JPY'
    USD = 'USD'


class TotalCost(BaseModel):
    currency: Optional[Currency] = Field(
        None,
        description="Currency names in ISO-4217 format. Enum:'[EUR, USD, GPD, JPY]'. Official list https://www.six-group.com/dam/download/financial-information/data-center/iso-currrency/lists/list_one.xls",
    )
    value: Optional[float] = Field(
        None, description='Value of the amount of the cost for energy consumed'
    )


class EnergyConsumedAndCostItem(BaseModel):
    energyConsumed: Optional[EnergyConsumed] = Field(
        None, description='Amount of energy consumed'
    )
    energyType: Optional[str] = Field(None, description='Type of energy')
    id: Optional[
        List[
            Optional[
                Union[
                    AnyUrl,
                    Union[
                        constr(
                            pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                            min_length=1,
                            max_length=256,
                        ),
                        AnyUrl,
                    ],
                ]
            ]
        ]
    ] = Field(
        None,
        description='Identifier of consumption lecture entity. For example, CUPS in Spain',
    )
    supplyName: Optional[str] = Field(None, description='Name of the supply company')
    totalCost: Optional[TotalCost] = Field(
        None, description='Amount of cost by energy consumed'
    )


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class Type6(Enum):
    ConsumptionCost = 'ConsumptionCost'


class ConsumptionCost(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    consumptionPoint: Optional[
        Union[
            UUID,
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ],
        ]
    ] = Field(None, description='Consumption point identifier which to entity refers')
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    energyConsumedAndCost: Optional[List[EnergyConsumedAndCostItem]] = Field(
        None,
        description='Array with energy consumption and cost by type of energy',
        min_length=1,
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    month: Optional[constr(pattern=r'(0[1-9]|1[0-2])')] = Field(
        None, description="The month to which the entity refers. Format MM, ex:'07'"
    )
    name: Optional[str] = Field(None, description='The name of this item')
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI entity type. It has to be ConsumptionCost'
    )
    year: Optional[constr(pattern=r'(2[0-9]{3})')] = Field(
        None, description="The year to which the entity refers. Format YYYY, ex:'2022'"
    )
