class Coins:
    """
    Calculate coins
    """

    def __init__(self, total_sum: int):
        self._coins = (1, 2, 5, 10, 25, 50)
        self.total_sum = total_sum

    def change(self):
        """
        Function for calculate coins
        :return: dict with result. Example:
            In: 185
            Out: {50: 3, 25: 1, 10: 1, 5: 0, 2: 0, 1: 0}
        """
        result = dict()
        item = len(self._coins) - 1
        while item >= 0:
            coin = self._coins[item]
            num_of_coin = self.total_sum // coin
            result[coin] = num_of_coin
            self.total_sum -= coin * num_of_coin
            item -= 1
        return result


a = Coins(185)
print(a.change())


class Coins:
    """
    Calculate minimal number of coins for a given amount.
    """

    def __init__(self, total_sum: int):
        self._coins = (1, 2, 5, 10, 25, 50)
        self.total_sum = total_sum

    def change(self) -> dict[int, int]:
        """
        Return dict with coin breakdown.
        Example:
            In: 185
            Out: {50: 3, 25: 1, 10: 1, 5: 0, 2: 0, 1: 0}
        """
        result = {}
        remaining = self.total_sum
        for coin in reversed(self._coins):
            result[coin], remaining = divmod(remaining, coin)
        return result


a = Coins(185)
print(a.change())
