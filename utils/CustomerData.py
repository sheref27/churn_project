from pydantic import BaseModel, Field
from typing import Literal

class CustomerData(BaseModel):
    creditscore: int = Field(description="Credit score of the customer")
    geography: Literal["France", "Germany", "Spain"] = Field(description="Customer's country")
    gender: Literal["Male", "Female"] = Field(description="Customer's gender")
    age: int = Field(description="Customer's age", ge=18, le=100)
    tenure: int = Field(description="Years as a customer (0-10)", ge=0, le=10)
    balance: float = Field(description="Account balance", ge=0)
    numofproducts: int = Field(description="Number of bank products (1-4)", ge=1, le=4)
    hascrcard: Literal[0, 1] = Field(description="Has credit card (0=No, 1=Yes)")
    isactivemember: Literal[0, 1] = Field(description="Active member status (0=No, 1=Yes)")
    estimatedsalary: float = Field(description="Estimated annual salary", ge=0)
