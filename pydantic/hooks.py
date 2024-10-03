"""Types for schema generation hooks"""

from typing import Any, Callable

from pydantic_core import CoreSchema

WrappedCoreSchemaGenerator = Callable[[Any], CoreSchema]

# (obj: Any, handler: WrappedCoreSchemaGenerator, /) -> CoreSchema
WrapCoreSchemaGeneratorFunction = Callable[[Any, WrappedCoreSchemaGenerator], CoreSchema]

CoreSchemaGeneratorFunction = WrapCoreSchemaGeneratorFunction
