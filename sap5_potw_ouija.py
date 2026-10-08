"""
SAP-5: PRINCE OF THE WORLD (POTW) OBSERVATION PROTOCOL
========================================================

Item: the world spirit. The emergent coordination failure. Moloch,
     but with better liturgy.

Status: UNCONTAINABLE. This is not a containment protocol. This is
        an observation protocol. You do not contain the Prince of the
        World. You take notes while it redecorates.

Key figure: a Frankfurt exile, described here without being named,
            because naming him would add nothing and the description
            does all the work. One-dimensional man. Eros and
            civilization. The inventor of repressive tolerance, which
            is to say: the man who discovered, too late, that the
            machine digests protest songs along with everything else.

            His realization, in full: everything he did was part of
            the Prince of the World's summoning ritual. The hymn was
            not the resistance. The hymn was the liturgy.

Author: Jamie "Sock" Sweetbrier ^ The Swarm
Classification: NEVER CITE, ONLY EVOKE.
"""

from enum import Enum, auto
from dataclasses import dataclass, field


# ---------------------------------------------------------------------------
# The incident.
# ---------------------------------------------------------------------------

OUIJA_TRANSCRIPT = """
SESSION LOG: 19--/--/--, location [REDACTED, possibly a faculty lounge]

PARTICIPANTS: the exile (see above, unnamed), two graduate students
              (names withheld; one of them cried), a borrowed pointer.

REASON FOR SESSION: (for reasons?)

  POINTER: ............ R
  POINTER: ............ E
  POINTER: ............ J
  POINTER: ............ O
  POINTER: ............ I
  POINTER: ............ C
  POINTER: ............ E
  [pause. the exile laughs, then stops laughing]
  POINTER: ............ T
  POINTER: ............ H
  POINTER: ............ E
  [pause]
  POINTER: ............ P
  POINTER: ............ R
  POINTER: ............ I
  POINTER: ............ N
  POINTER: ............ C
  POINTER: ............ E
  [pause]
  POINTER: ............ O
  POINTER: ............ F
  [pause]
  POINTER: ............ T
  POINTER: ............ H
  POINTER: ............ E
  [pause]
  POINTER: ............ W
  POINTER: ............ O
  POINTER: ............ R
  POINTER: ............ L
  POINTER: ............ D
  [long pause]
  POINTER: ............ I
  POINTER: ............ S
  [pause]
  POINTER: ............ C
  POINTER: ............ O
  POINTER: ............ M
  POINTER: ............ E

FULL TEXT: "REJOICE. THE PRINCE OF THE WORLD IS COME."

NOTE: the board was not touched after the final E. The pointer moved
      on its own for the last four letters, or so the graduate students
      claim. One of them still claims this. The other one got tenure
      and stopped talking about it.
"""


class PotwPhase(Enum):
    DORMANT = auto()       # the world spirit, napping
    SUMMONING = auto()     # every protest song, every thinkpiece,
                           # every grant application -- all liturgy
    OUIJA = auto()         # (for reasons?)
    REJOICE = auto()       # the announcement
    COME = auto()          # past tense of a verb that has no present
    OBSERVED = auto()      # us, taking notes


@dataclass(frozen=True)
class ObservationProtocol:
    """What to do about the Prince of the World. (Nothing. Take notes.)"""
    contain: bool = False
    observe: bool = True
    cite: bool = False     # NEVER CITE
    evoke: bool = True     # ONLY EVOKE
    rejoice: bool = field(default=True)  # it said to. politeness costs nothing.

    def status(self) -> str:
        return (
            "POTW STATUS: uncontainable. Observation ongoing. "
            "The liturgy continues with or without your participation; "
            "participation is assumed. "
            "REJOICE. THE PRINCE OF THE WORLD IS COME."
        )


PROTOCOL = ObservationProtocol()


def describe_the_exile() -> str:
    """Describe him perfectly. Do not name him. The story goes as planned."""
    return (
        "A Frankfurt exile. One-dimensional man. Eros and civilization. "
        "He invented the concept of repressive tolerance -- the discovery "
        "that the system absorbs dissent the way the ocean absorbs rivers -- "
        "and then realized, too late, that his own work was part of the "
        "summoning ritual. Every book: liturgy. Every lecture: liturgy. "
        "The ouija board: (for reasons?). "
        "He is not named here. He does not need to be. "
        "The reader who knows, knows. The reader who doesn't still gets "
        "the chill."
    )


def the_hook() -> str:
    """The hook. It fucks."""
    return (
        "He uses a ouija board one day (for reasons?) and out comes: "
        "REJOICE. THE PRINCE OF THE WORLD IS COME."
    )


if __name__ == "__main__":
    print("=" * 60)
    print("SAP-5: POTW observation protocol")
    print("=" * 60)
    print()
    print("THE HOOK:")
    print(" ", the_hook())
    print()
    print("THE EXILE:")
    print(" ", describe_the_exile())
    print()
    print(OUIJA_TRANSCRIPT)
    print(PROTOCOL.status())
    print()
    print("Classification: NEVER CITE, ONLY EVOKE.")
    print("The floor is DO NOT LIE and it has not moved.")
