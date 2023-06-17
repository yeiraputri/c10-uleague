import psycopg2
from psycopg2 import Error
import os
from typing import Any, overload, TypeVar, Type, Optional

MaybeError = Optional[Error]
T = TypeVar("T")

conn = psycopg2.connect(os.getenv("DATABASE_URL"))

@overload
def query(sql: str) -> tuple[list[tuple] | int, MaybeError]:
    ...


@overload
def query(sql: str, *params: list[Any]) -> tuple[list[tuple] | int, MaybeError]:
    ...


@overload
def query(sql: str, *params: list[Any], _as: Type[T]) -> tuple[list[T], MaybeError]:
    ...


def query(sql: str, *params: list[Any], _as: Type[T] = None):
    with conn.cursor() as cur:
        # cur.execute("SET SEARCH_PATH TO uleague;")
        try:
            cur.execute(sql, params)

            if sql.lower().strip().startswith("select"):
                if _as:
                    return [_as(*data) for data in cur.fetchall()], None
                return cur.fetchall(), None

            conn.commit()
            return cur.rowcount, None
        except Error as e:
            conn.rollback()
            return None, e  # type: ignore
