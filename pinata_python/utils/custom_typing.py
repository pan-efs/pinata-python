from typing import Any, Dict, Union


Headers = Dict[str, str]

Options = Dict[str, Any]

JsonResponse = Dict[str, str]

ErrorResponse = Dict[str, int]

ByHashResponse = Dict[str, Any]

PinataResponse = Union[JsonResponse, ErrorResponse, ByHashResponse]