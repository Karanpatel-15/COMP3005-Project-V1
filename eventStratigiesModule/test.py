from EventStrategyManager import EventStrategyManager

if __name__ == '__main__':
    context = EventStrategyManager()
    x= context.get_strategy_by_id(10)
    x.handle("Testing")
    print("Testing")