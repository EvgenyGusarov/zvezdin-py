from typing import List, Optional

from kline import Kline
from order import Order


class SignalEmitter:
    def get_order_request(self, klines: List[Kline]) -> Optional[Order]:
        """
        :param klines: historical klines. Current kline open price equals to klines[-1].close
        :return:
        """
        raise NotImplementedError
