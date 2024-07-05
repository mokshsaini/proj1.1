from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Pydantic model for storing user health records
class Records(BaseModel):
    Name: str 
    Date: datetime
    BP: str
    Weight_in_kg: float
    Gender: str
    Height_in_meters: float
    Fever: bool = False

# Pydantic model for storing user health records
class Records_fetch(BaseModel):
    Name: str 
    Date: Optional[datetime] = None
    BP: Optional[str] = None
    Weight_in_kg: Optional[float] = None
    Gender: Optional[str] = None
    Height_in_meters: Optional[float] = None
    Fever: Optional[float] = None 

