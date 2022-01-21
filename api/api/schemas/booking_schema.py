from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List

from .interpreter_schema import InterpreterBookingResponseSchema
from models.booking_enums import BookingPeriodEnum, BookingStatusEnum, BookingRequestedByEnum, BookingMethodOfAppearanceEnum, BookingInterpretForEnum


class BookingDateSchema(BaseModel):
    id: Optional[int]
    date: Optional[datetime]
    period: BookingPeriodEnum
    arrivalTime: Optional[str]
    
    class Config():
        orm_mode = True
        allow_population_by_field_name = True


class BookingBase(BaseModel):
       
    case_name: Optional[str] = Field(alias="caseName")
    comment: Optional[str]
    method_of_appearance: Optional[BookingMethodOfAppearanceEnum] = Field(alias="methodOfAppearance")
    prosecutor: Optional[str]
    reason: Optional[str]
    registry: Optional[str]
    requested_by: Optional[BookingRequestedByEnum] = Field(alias="requestedBy")
    room: Optional[str]
    file: Optional[str]
    interpret_for: Optional[BookingInterpretForEnum] = Field(alias="interpretFor")
    status: Optional[BookingStatusEnum]    
    federal: bool = False  
    language_name: Optional[str] = Field(alias="language")
    location_id: Optional[int] = Field(alias="locationId")    
    dates: List[BookingDateSchema]

    class Config():
        orm_mode = True
        allow_population_by_field_name = True


class BookingRequestSchema(BookingBase):
    interpreter_id: Optional[int] = Field(alias="interpreterId")


class BookingResponseSchema(BookingBase):
    id: Optional[int]           
    interpreter: InterpreterBookingResponseSchema


class PageSchema(BaseModel):
    page: int = 1
    limit: int = 1000


class BookingResponsePageSchema(BaseModel):
    data: List[BookingResponseSchema]
    pagination: PageSchema
    
    class Config():
        orm_mode = True


class DateRangeSchema(BaseModel):
    endDate: Optional[str]
    startDate: Optional[str]


class BookingSearchRequestSchema(BaseModel):    

    dates: Optional[List[DateRangeSchema]]
    file: Optional[str]
    interpreter: Optional[str]
    isStartFromToday: Optional[bool]
    locationId: Optional[int]
    
    
    