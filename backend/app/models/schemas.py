from pydantic import BaseModel
from typing import List, Optional


class ParsedInfo(BaseModel):
    name: Optional[str] = ""
    phone: Optional[str] = ""
    email: Optional[str] = ""
    address: Optional[str] = ""
    job_intention: Optional[str] = ""
    expected_salary: Optional[str] = ""
    work_years: Optional[str] = ""
    education: Optional[str] = ""
    projects: List[str] = []


class MatchResult(BaseModel):
    score: int
    keyword_match_rate: float
    matched_keywords: List[str]
    missing_keywords: List[str]
    analysis: str