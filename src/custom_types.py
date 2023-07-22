from typing import Optional, Tuple, TypedDict, Union
from enum import Enum
from datetime import date


class state(Enum):
    PENDING = 'pending'
    READING = 'reading'
    COMPLETE = 'complete'


class AuthorRow(TypedDict):
    author_first_name: Optional[str]
    author_last_name: str
    author_birthdate: Optional[date]


class StatusRow(TypedDict):
    member_id: int
    book_id: int
    status: Optional[state]
    pct_read: int
    start_date: Optional[date]
    end_date: Optional[date]


class BookRow(TypedDict):
    author_id: Optional[int]
    title: str
    description: Optional[str]
    genre: str
