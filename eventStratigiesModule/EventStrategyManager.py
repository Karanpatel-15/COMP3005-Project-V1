from eventStratigiesModule import Error, Dribble, DribblePast, Shot, FoulCommitted, Pass
class EventStrategyManager:
    def __init__(self):
        self._strategies = {
            # Rayyan Strategies
            Dribble.id: Dribble.Strategy(),
            DribblePast.id: DribblePast.Strategy(),
            # Karan Strategies
            Error.id: Error.Strategy(),
            Shot.id: Shot.Strategy(),
            # FoulCommitted.id: FoulCommitted.Strategy(),
            # Arhaan Strategies
            Pass.id: Pass.Strategy(),
        }
        self._strategy = None

    def get_strategy_by_id(self, strategy_id):
        self._strategy = self._strategies.get(strategy_id)
        if self._strategy is None:
            # raise ValueError("Invalid strategy ID ", strategy_id)
            # print("strategy ID ", strategy_id, " is not implemented yet")
            return None
        else:
            # print("strategy ID ", strategy_id, " is implemented")
            return self._strategy

