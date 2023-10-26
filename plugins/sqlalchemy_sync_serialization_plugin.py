from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from litestar import Litestar, post
from litestar.contrib.sqlalchemy.plugins import SQLAlchemySerializationPlugin

if TYPE_CHECKING:
    from typing import List


class Base(DeclarativeBase):
    ...


class TodoItem(Base):
    __tablename__ = "todo_item"
    title: Mapped[str] = mapped_column(primary_key=True)
    done: Mapped[bool]


@post("/", sync_to_thread=True)
def add_item(data: TodoItem) -> List[TodoItem]:
    return [data]


app = Litestar(route_handlers=[add_item], plugins=[SQLAlchemySerializationPlugin()])
