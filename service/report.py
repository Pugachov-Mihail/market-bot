import datetime

from config.config import session
from models import goods


def report_goods() -> list[str]:
    res = session.query(goods.Goods).filter(goods.Goods.status == False).all()
    result = []

    for i in res:
        tup = datetime.datetime.now() - i.create_date
        result.append(f"<b>{i.id}</b>) <b>{i.name}</b>:\nЗакупка: <b>{i.sales_price}</b> "
                            f"\nПродажа: <b>{i.purchase_price}</b>\nКол-во: <b>{i.count}</b>\n"
                      f"Оборачиваемость:<b>{tup}</b>\n")

    return result


def report_sales() -> list[str]:
    pass