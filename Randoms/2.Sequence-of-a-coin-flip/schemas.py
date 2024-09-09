from pydantic import BaseModel, Field, constr


class FlipDataInput(BaseModel):
    sequence: constr(pattern=r"^[HT]+$", min_length=5, max_length=70) = Field(
        ..., description="Sequence consisting only of 'H' and 'T' with length between 5 and 70 inclusive."
    )
    length: int = Field(..., ge=2, le=8, description="Integer L between 2 and 8 inclusive.")
    streak: int = Field(..., ge=1, le=8, description="Integer N between 1 and 8 inclusive.")
