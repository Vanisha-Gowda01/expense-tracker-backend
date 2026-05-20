from pydantic import BaseModel


class IncomeCreate(BaseModel):

    source: str

    amount: float