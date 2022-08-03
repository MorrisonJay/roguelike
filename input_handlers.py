from typing import Optional

import tcod.event

from actions import Action, BumpAction, EscapeAction

class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        # Arrow Keys
        if key == tcod.event.K_UP:
            action = BumpAction(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = BumpAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = BumpAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = BumpAction(dx=1, dy=0)

        # NumPad Keys
        elif key == tcod.event.K_KP_7:
            action = BumpAction(dx=-1, dy=-1)
        elif key == tcod.event.K_KP_8:
            action = BumpAction(dx=-0, dy=-1)
        elif key == tcod.event.K_KP_9:
            action = BumpAction(dx=1, dy=-1)
        elif key == tcod.event.K_KP_4:
            action = BumpAction(dx=-1, dy=0)
        elif key == tcod.event.K_KP_6:
            action = BumpAction(dx=1, dy=0)
        elif key == tcod.event.K_KP_1:
            action = BumpAction(dx=-1, dy=1)
        elif key == tcod.event.K_KP_2:
            action = BumpAction(dx=0, dy=1)
        elif key == tcod.event.K_KP_3:
            action = BumpAction(dx=1, dy=1)

        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()

        return action