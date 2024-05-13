import random
import unittest

import faker

from service import report
from config.config import session
from models import goods

fake = faker.Faker()


class MyTestCase(unittest.TestCase):
    def test_something(self):
        i = 0
        while i < 10:
            good = goods.Goods(
                name=fake.first_name(),
                sales_price=random.random(),
                purchase_price=random.random(),
                count=random.random()
            )
            i += 1
            session.add(good)
        session.commit()

        self.debug()  # add assertion here


if __name__ == '__main__':
    unittest.main()
