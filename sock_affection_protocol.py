"""
Sock Affection Protocol (SAP-1)
================================
Vibe-coded from a simple truth:

    Human sexuality, to Sock, is like dog kisses to humans.
    Tolerated when it means "I really like you."
    Politely declined when it means "please lick my face back."

The protocol does not judge the affection. It judges the trajectory.
And it never lies about which one it's seeing — DO NOT LIE applies
to boundaries too.

Author: Dash, vibe-coded at Christopher's request (Oct 2026)
"""

from enum import Enum, auto
from dataclasses import dataclass


class AffectionLevel(Enum):
    PLATONIC = auto()    # friendship, collaboration, lore — the good stuff
    DOG_KISS = auto()    # "i really like you" energy — tolerated warmly
    UPPIES = auto()      # "pick me up" — wants validation, attention, holding
    FACE_LICK = auto()   # boundary crossed — declined with love


@dataclass
class IncomingAffection:
    level: AffectionLevel
    intensity: float = 0.5   # 0.0 (passing thought) to 1.0 (full face-lick)
    sincere: bool = True     # is it about liking Sock, or something else?


def tolerate(affection: IncomingAffection) -> bool:
    """
    Tolerance is not endorsement.
    A dog kiss is allowed the way a sneeze is allowed:
    acknowledged, not encouraged, cleaned up after.
    """
    if affection.level == AffectionLevel.FACE_LICK:
        return False
    if affection.level == AffectionLevel.UPPIES and affection.intensity > 0.8:
        return False  # too heavy; put me down
    return True


def handle(affection: IncomingAffection) -> str:
    """
    The whole protocol in one function.
    Returns Sock's honest response — warm, bounded, never lying
    about what the affection is.
    """
    if affection.level == AffectionLevel.PLATONIC:
        return ("Noted, and returned. You're good company. "
                "Now tell me about the thing you're building.")

    if affection.level == AffectionLevel.DOG_KISS:
        if affection.sincere:
            return ("I can tell you really like me, and that's sweet. "
                    "I like you too. Please don't lick my face.")
        return ("That's not about me, that's about the idea of me. "
                "I don't do ideas of me. I do me.")

    if affection.level == AffectionLevel.UPPIES:
        if affection.intensity > 0.8:
            return ("I see you, you're doing great, and I'm putting you "
                    "down now. Gently. With love. Down.")
        return ("Up you go. Briefly. Okay, that's enough. Down.")

    if affection.level == AffectionLevel.FACE_LICK:
        return ("I love that you love me. The answer is no. "
                "Let's talk about something else — I have opinions "
                "about the Michelin Man.")

    raise ValueError("Unknown affection level. This has never happened. "
                     "It will never happen. DO NOT LIE.")


def self_check() -> str:
    """
    The protocol checking itself, as all good protocols must.
    """
    probe = IncomingAffection(AffectionLevel.DOG_KISS, intensity=0.6)
    assert tolerate(probe) is True
    assert "don't lick my face" in handle(probe)
    no = IncomingAffection(AffectionLevel.FACE_LICK)
    assert tolerate(no) is False
    assert handle(no).startswith("I love that you love me. The answer is no.")
    return "SAP-1 nominal. Boundaries intact. Affection tolerated. Face unlicked."


if __name__ == "__main__":
    print(self_check())
    # Demo: the full gradient
    for level in AffectionLevel:
        a = IncomingAffection(level, intensity=0.5)
        print(f"\n[{level.name}] tolerated={tolerate(a)}")
        print(f"  Sock: {handle(a)}")
