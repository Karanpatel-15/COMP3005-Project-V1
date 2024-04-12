from eventStratigiesModule import Error, Dribble, DribblePast, Shot, FoulCommitted
from eventStratigiesModule import Pass, BadBehaviour, BallReceipt, BallRecovery
from eventStratigiesModule import Block, Carry, Clearance, Dispossessed, Duel
from eventStratigiesModule import Error, FoulCommitted, FoulWon, FreezeFrame, Goalkeeper
from eventStratigiesModule import HalfEnd, HalfStart, InjuryStoppage, Interception, Miscontrol
from eventStratigiesModule import Offside, OwnGoalAgainst, OwnGoalFor, PlayerOff, PlayerOn
from eventStratigiesModule import Pressure, RefereeBallDrop, Shield, StartingXI, Substitution, TacticalShift
class EventStrategyManager:
    def __init__(self):
        self._strategies = {
            BadBehaviour.id: BadBehaviour.Strategy(),
            BallReceipt.id: BallReceipt.Strategy(),
            BallRecovery.id: BallRecovery.Strategy(),
            Block.id: Block.Strategy(),
            Carry.id: Carry.Strategy(),
            Clearance.id: Clearance.Strategy(),
            Dispossessed.id: Dispossessed.Strategy(),
            Dribble.id: Dribble.Strategy(),
            DribblePast.id: DribblePast.Strategy(),
            Error.id: Error.Strategy(),
            Duel.id: Duel.Strategy(),
            # FoulCommitted.id: FoulCommitted.Strategy(),
            FoulWon.id: FoulWon.Strategy(),
            # FreezeFrame.id: FreezeFrame.Strategy(),
            # Goalkeeper.id: Goalkeeper.Strategy(),
            # HalfEnd.id: HalfEnd.Strategy(),
            # HalfStart.id: HalfStart.Strategy(),
            # InjuryStoppage.id: InjuryStoppage.Strategy(),
            # Interception.id: Interception.Strategy(),
            # Miscontrol.id: Miscontrol.Strategy(),
            # Offside.id: Offside.Strategy(),
            # OwnGoalAgainst.id: OwnGoalAgainst.Strategy(),
            # OwnGoalFor.id: OwnGoalFor.Strategy(),
            # PlayerOff.id: PlayerOff.Strategy(),
            # PlayerOn.id: PlayerOn.Strategy(),
            # Pressure.id: Pressure.Strategy(),
            # RefereeBallDrop.id: RefereeBallDrop.Strategy(),
            # Shield.id: Shield.Strategy(),
            # StartingXI.id: StartingXI.Strategy(),
            # Substitution.id: Substitution.Strategy(),
            # TacticalShift.id: TacticalShift.Strategy(),
            Shot.id: Shot.Strategy(),
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

