import random
from enum import Enum
from data_structures.list import List


class State(Enum):
    CREATED = 0
    APPROVED = 1
    CURSE = 2
    FINISH = 3


class Loan:
    def __init__(self, code_associate: str,
                 amount_request: int,
                 nu_dues: int,
                 income_associate: int,
                 warranty: str,
                 files: List,
                 plan: int):
        self.__code_loan = random.randint(1, 5000)
        self.__code_associate = code_associate
        self.__state_loan = State.CREATED
        self.__amount_request = amount_request
        self.__amount_approved = self.amount_approved()
        self.__nu_dues = nu_dues
        self.__income_associate = income_associate
        self.__warranty = warranty
        self.__files = files
        self.__plan = plan
        self.__historial = List()

    def amount_approved(self) -> int:
        return int(0.43 * self.__amount_request)
