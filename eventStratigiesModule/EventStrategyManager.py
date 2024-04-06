from eventStratigiesModule import Error
from eventStratigiesModule import FoulCommitted


class EventStrategyManager:
    def __init__(self):
        self._strategies = {
            # Rayyan Strategies
            # Karan Strategies
            Error.id: Error.Strategy(),
            FoulCommitted.id: FoulCommitted.Strategy(),
            # Arhaan Strategies
        }
        self._strategy = None

    def get_strategy_by_id(self, strategy_id):
        self._strategy = self._strategies.get(strategy_id)
        if self._strategy is None:
            # raise ValueError("Invalid strategy ID ", strategy_id)
            print("strategy ID ", strategy_id, " is not implemented yet")
        else:
            print("strategy ID ", strategy_id, " is implemented")
        return self._strategy

