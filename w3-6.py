from sqlalchemy import create_engine, String, Integer, Boolean, ForeignKey, select, func
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship

engine = create_engine(
    "mysql+pymysql://root:123456@localhost:3306/demo", echo=True  # 打印sql
)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    todos: Mapped[list["Todo"]] = relationship("Todo", back_populates="user")


class Todo(Base):
    __tablename__ = "todos"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    done: Mapped[bool] = mapped_column(Boolean, default=False)
    user: Mapped["User"] = relationship(back_populates="todos")
    tags: Mapped[list["Tags"]] = relationship("Tags", back_populates="todo")


class Tags(Base):
    __tablename__ = "tags"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    todo_id: Mapped[int] = mapped_column(ForeignKey("todos.id"))
    todo: Mapped["Todo"] = relationship(back_populates="tags")


Base.metadata.create_all(engine)

with Session(engine) as s:
    