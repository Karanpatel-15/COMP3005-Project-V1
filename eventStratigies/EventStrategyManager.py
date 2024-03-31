from Shot import Shot


class EventStrategyManager:
    def __init__(self):
        self._strategies = {
            Shot.id: Shot()
        }
        self._strategy = None

    def get_strategy_by_id(self, strategy_id):
        self._strategy = self._strategies.get(strategy_id)
        if self._strategy is None:
            raise ValueError("Invalid strategy ID ", strategy_id)
        return self._strategy
    