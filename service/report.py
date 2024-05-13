import datetime

from config.config import session
from models import goods


def report_sales() -> list[str]:
    res = (session.query(goods.Goods).
           filter(goods.Goods.status == False).all())
    result = []
    for i in res:
        result.append(f"<b>{i.id}</b>) <b>{i.name}</b>: закупка <b>{i.sales_price}</b> "
                      f"продажа <b>{i.purchase_price}</b> кол-во <b>{i. count}</b> \n")

    return result