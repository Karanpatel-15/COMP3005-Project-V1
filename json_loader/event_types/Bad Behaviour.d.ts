// Generated by https://quicktype.io
//
// To change quicktype's target language, run command:
//
//   "Set quicktype target language"

export interface BadBehaviour {
    id: string;
    index: number;
    period: number;
    timestamp: string;
    minute: number;
    second: number;
    type: Foreign;
    possession: number;
    possession_team: Foreign;
    play_pattern: Foreign;
    team: Foreign;
    player: Foreign;
    position: Foreign;
    duration: number;
    bad_behaviour: BadBehaviourClass;
    off_camera: boolean;
}

export interface BadBehaviourClass {
    card: Foreign;
}

export interface Foreign {
    id: number;
    name: string;
}