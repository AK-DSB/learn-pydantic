from pydantic import BaseModel, Field
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base


class MyModel(BaseModel):
    metadata: dict[str, str] = Field(alias='metadata_')

    class Config:
        orm_mode = True


Base = declarative_base()


class SQLModel(Base):
    __tablename__ = 'my_table'
    id = sa.Column('id', sa.Integer, primary_key=True)
    # metadata is reserved by SQLAlchemy, hence hte _
    metadata_ = sa.Column('metadata', sa.JSON)


sql_model = SQLModel(metadata_={'key': 'val'}, id=1)

pydantic_model = MyModel.from_orm(sql_model)
print(pydantic_model.dict())
print(pydantic_model.dict(by_alias=True))

