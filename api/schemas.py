from pydantic import BaseModel

class CreditInput(BaseModel):
    age: float
    DebtRatio: float
    MonthlyIncome: float
    NumberOfDependents: float


class CreditResponse(BaseModel):
    risk_score: float
    risk_level: str
    decision: str