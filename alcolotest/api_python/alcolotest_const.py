#!/usr/bin/env python3
from pydantic import BaseModel, Field


class People(BaseModel):
    id: int = Field(default = 1, title = "ID")
    last_name: str = Field(default = "Dupont", title = 'Last name')
    first_name: str = Field(default = "Jacques", title = 'First name')
    birthday: str = Field(default = "02/10/91", title = "Birthday")
    sex: str = Field(default = "M", title = "Sex")
    mass: float = Field(default = '60', titre = "Mass (kg)")


# Examples
PEOPLE_EXAMPLE = {
    "id": "112233",
    "last_name": "Lupin",
    "first_name": "Arsene",
    "mass": "81"
    }
