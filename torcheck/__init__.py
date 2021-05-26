from .registry import Registry
from .message_utils import (
    verbose_on,
    verbose_off,
    is_verbose
)

registry = Registry()

register = registry.register
add_tensor = registry.add_tensor
add_module = registry.add_module
add_tensor_changing_check = registry.add_tensor_changing_check
add_tensor_not_changing_check = registry.add_tensor_not_changing_check
add_tensor_nan_check = registry.add_tensor_nan_check
add_tensor_inf_check = registry.add_tensor_inf_check
add_module_changing_check = registry.add_module_changing_check
add_module_not_changing_check = registry.add_module_not_changing_check
add_module_output_range_check = registry.add_module_output_range_check
add_module_nan_check = registry.add_module_nan_check
add_module_inf_check = registry.add_module_inf_check

disable_optimizers = registry.disable_optimizers
disable_modules = registry.disable_modules
disable = registry.disable
enable_optimizers = registry.enable_optimizers
enable_modules = registry.enable_modules
enable = registry.enable
