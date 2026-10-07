# pydantic 负责把外部传进来的，不可信的数据，校验成期望的结构
import json
from pydantic import BaseModel, Field, ValidationError


class User(BaseModel):
    name: str
    age: int
    email: str = "未填写"


u = User(name="whh", age=22)
print(u)
print(u.model_dump())

try:
    User(name="whh", age="不是数字")

except ValidationError as e:
    print("错误条数：", e.error_count())
    print(e.errors()[0]["loc"], e.errors()[0]["msg"])


# Fielde Field(min_length=1, gt=0, ge=0) 之类的细粒度要求。gt 是大于，ge 是大于等于。
class Product(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    price: float = Field(gt=0, description="价格必须大于0")
    stock: int = Field(default=0, ge=0)


try:
    Product(name="book", price=-1)
except ValidationError as e:
    for err in e.errors():
        print("字段", err["loc"], "->", err["msg"])


# 嵌套模型
class Address(BaseModel):
    city: str
    street: str


class Customer(BaseModel):
    name: str
    address: Address  # 字段类型是另一个模型
    tags: list[str] = []  # 默认值是空列表


# 传字典也行，pydantic会自动转换成模型
cus = Customer(
    name="whh", address={"city": "shanghai", "street": "hh road"}, tags=["new customer"]
)
print(cus.address.city)
print(cus.model_dump())

# 字典 → 模型 → 字典 往返
back = Customer.model_validate(json.loads(json.dumps(cus.model_dump())))
print("往返一致：", back == cus)
