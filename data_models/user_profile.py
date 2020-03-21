# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from typing import List


class UserProfile:
    def __init__(
        self, name: str = None, age: int = 0, symptoms: List[str] = None, plz: int = 0, risk_countries: List[str] = None
    ):
        self.name: str = name
        self.age: int = age
        self.symptoms: List[str] = symptoms
        self.plz: int = plz
        self.risk_countries: List[str] = risk_countries
