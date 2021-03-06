import json
from typing import Union, List

import pytest
from indexpy.openapi.schema import replace_definitions
from pydantic import BaseModel


class Foo(BaseModel):
    foo: int


class Bar(BaseModel):
    bar: str


class A(BaseModel):
    in_a: Foo


class B(BaseModel):
    in_b: Union[Foo, Bar]


class C(BaseModel):
    to_b: B
    in_c: List[Foo]


class D(BaseModel):
    to_c: C


@pytest.mark.parametrize("model", [Foo, Bar, A, B, C, D])
def test_schema_models(model):
    assert "$ref" not in json.dumps(replace_definitions(model.schema()))
