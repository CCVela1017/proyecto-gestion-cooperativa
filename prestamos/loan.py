import random
from enum import Enum
from data_structures.list import List

class Loan:
    def __init__(self, code_loan: str,
                 code_associate: str,
                 amount_request: int,
                 nu_dues: int,
                 state: str,
                 income_associate: int,
                 warranty: str,
                 files: List,
                 plan: str):
        self.code_loan = code_loan
        self.code_associate = code_associate
        self.state_loan = state
        self.amount_request = amount_request
        self.amount_approved = self.amount_approved()
        self.nu_dues = nu_dues
        self.income_associate = income_associate
        self.warranty = warranty
        self.files = files
        self.plan = plan
        self.historial = List()

    def amount_approved(self) -> int:
        return int(0.43 * self.amount_request)
