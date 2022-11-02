from Scripts.Object.Player.Animation.Player_Static_State import null, RD, LD, UD, DD, RU, LU, UU, DU
from Scripts.Object.Player.Animation.Player_Idle import Player_Idle
from Scripts.Object.Player.Animation.Player_Working import Player_Working
from Scripts.Object.Player.Animation.Player_Dash import Player_Dash

next_state = {
    Player_Idle: {null: Player_Idle,
                  RD: Player_Working, RU: Player_Idle,
                  LD: Player_Working, LU: Player_Idle,
                  UD: Player_Working, UU: Player_Idle,
                  DD: Player_Working, DU: Player_Idle},
    Player_Working: {null: Player_Idle,
                     RD: Player_Working, RU: Player_Working,
                     LD: Player_Working, LU: Player_Working,
                     UD: Player_Working, UU: Player_Working,
                     DD: Player_Working, DU: Player_Working},
    Player_Dash: {null: Player_Dash,
                  RD: Player_Dash, RU: Player_Dash,
                  LD: Player_Dash, LU: Player_Dash,
                  UD: Player_Dash, UU: Player_Dash,
                  DD: Player_Dash, DU: Player_Dash}
}
