from pydantic import BaseModel, constr, PositiveFloat, Field


class MassDistanceBase(BaseModel):
    mass_1: PositiveFloat = Field(
        ..., description="Mass of object 1. Must be a positive float."
    )
    mass_2: PositiveFloat = Field(
        ..., description="Mass of object 2. Must be a positive float."
    )
    distance: PositiveFloat = Field(
        ..., description="Distance between the two objects. Must be a positive float."
    )


class MassDistanceUnitsBase(BaseModel):
    unit_m1: constr(pattern=r"^(kg|g|µg|mg|lb)$") = Field(
        ..., description="Unit for mass of object 1."
    )
    unit_m2: constr(pattern=r"^(kg|g|µg|mg|lb)$") = Field(
        ..., description="Unit for mass of object 2."
    )
    unit_d: constr(pattern=r"^(m|cm|mm|ft|µm)$") = Field(
        ..., description="Unit for the distance between the objects."
    )
