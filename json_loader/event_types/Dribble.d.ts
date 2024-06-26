// Generated by https://quicktype.io
//
// To change quicktype's target language, run command:
//
//   "Set quicktype target language"

export interface Dribble {
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
    location: number[];
    duration: number;
    under_pressure: boolean;
    dribble: DribbleClass;
    off_camera: boolean;
    out: boolean;
}

export interface DribbleClass {
    outcome: Foreign;
    overrun: boolean;
    nutmeg: boolean;
    no_touch: boolean;
}

export interface Foreign {
    id: number;
    name: string;
}
