from dataclasses import dataclass
from typing import Union

import torch


@dataclass
class OutputSpec:
    module_name: str = None
    range: Union[list, tuple] = None
    negate: bool = False
    check_nan: bool = False
    check_inf: bool = False

    @property
    def name(self):
        if module_name is None:
            return "Module's output"
        else:
            return f"{self.module_name}'s output"

    @property
    def condition(self):
        low, high = self.range
        if low is None:
            return f"< {high}"
        elif high is None:
            return f"> {low}"
        else:
            return f"> {low} and < {high}"

    def validate(self, output):
        error_items = []
        if self.range is not None:
            error_items.append(self.validate_range(output))
        if self.check_nan:
            error_items.append(self.validate_nan(output))
        if self.check_inf:
            error_items.append(self.validate_inf(output))

        raise RuntimeError(message_utils.make_message(error_items, output))

    def validate_range(self, output):
        low, high = self.range
        status = torch.ones_like(output, dtype=torch.bool)
        if low is not None:
            status = output >= low
        if high is not None:
            status = status & (output <= high)
        
        if not negate:
            if not torch.all(status).item():
                return f"{self.name} should all {self.condition}. Some are out of range"
        else:
            if torch.all(status).item():
                return f"{self.name} shouldn't all {self.condition}"

    def validate_nan(self, output):
        if torch.any(torch.isnan(output)).item():
            return f"{self.name} contains NaN." 

    def validate_inf(self, output):
        if torch.any(torch.isinf(output)).item():
            return f"{self.name} contains inf." 
