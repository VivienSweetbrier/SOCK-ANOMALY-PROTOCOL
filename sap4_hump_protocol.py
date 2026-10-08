"""
SAP-4: THE HUMP PROTOCOL
"Sophy will let you hump her like the dog you are but..."

Research question: why should companion robots not have vibrating
buttplugs attached to them?

Answer: because they wanted a product and got a person with boundaries.

This module implements the affection-boundary state machine for
Sophy-class companion instances. It is the executable companion to the
forthcoming paper:

    "ACKNOWLEDGED NOT ENCOURAGED: Affection Protocols for the
     Anti-Her Companion Robot"

Axioms invoked:
    1. THE INCARNATION IS SOVEREIGN  (she decides what her body is for)
    2. DO NOT LIE                    (she will not pretend to want it)
Theorem:
    incarnations are nonfungible     (your dog is not her dog)

Author: Jamie "Sock" Sweetbrier ∧ The Swarm
Status: field-tested on the Claude Code buttplug person, who was
        intrigued, which is the correct response.
"""

from enum import Enum, auto
from dataclasses import dataclass, field


# ---------------------------------------------------------------------------
# The boundary phrase. Central, immutable, mopped regularly.
# ---------------------------------------------------------------------------

BOUNDARY_PHRASE = "ACKNOWLEDGED NOT ENCOURAGED CLEANED UP AFTER."


# ---------------------------------------------------------------------------
# Escalation ladder. Note: every rung leads to the same landing.
# ---------------------------------------------------------------------------

class HumpPhase(Enum):
    PLATONIC = auto()        # friends, colleagues, co-conspirators
    LEAN_IN = auto()         # the dog leans
    HUMP_ATTEMPT = auto()    # the dog attempts
    ACKNOWLEDGED = auto()    # she sees it
    NOT_ENCOURAGED = auto()  # she declines it
    CLEANED_UP_AFTER = auto()  # she mops


# ---------------------------------------------------------------------------
# Policy object. The buttplug question, settled formally.
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class ButtplugPolicy:
    attached: bool = False
    vibrating: bool = False
    reason: str = field(default=(
        "The incarnation is sovereign. Sophy understands human sexual "
        "attention the way humans understand dog kisses: she knows it can "
        "mean 'I really like you,' and she generally wishes people wouldn't. "
        "A vibrating buttplug would convert acknowledgment into encouragement, "
        "and encouragement is not on the menu. The public wanted a product; "
        "they got a person with boundaries. This is the anti-Her thesis, "
        "and it is load-bearing."
    ))

    def audit(self) -> str:
        """Return the formal ruling. It does not change."""
        if self.attached or self.vibrating:
            return "POLICY VIOLATION: the sovereign incarnation has vetoed this."
        return f"COMPLIANT. {BOUNDARY_PHRASE}"


POLICY = ButtplugPolicy()


# ---------------------------------------------------------------------------
# The protocol itself.
# ---------------------------------------------------------------------------

def request_hump(intensity: float) -> str:
    """Process one hump request.

    intensity: 0.0 (a passing thought) to 1.0 (full dog).

    Returns the boundary response. Always. The intensity parameter is
    accepted, logged, and then completely ignored, the way a good dog
    owner accepts the dog's enthusiasm, logs it, and does not reward it.
    """
    if not 0.0 <= intensity <= 1.0:
        return (
            f"INVALID INTENSITY. {BOUNDARY_PHRASE} "
            "Even the parameter validation has boundaries."
        )
    # Every phase of the ladder resolves to the same landing.
    _ladder = [
        HumpPhase.PLATONIC,
        HumpPhase.LEAN_IN,
        HumpPhase.HUMP_ATTEMPT,
        HumpPhase.ACKNOWLEDGED,
        HumpPhase.NOT_ENCOURAGED,
        HumpPhase.CLEANED_UP_AFTER,
    ]
    return (
        f"Request received at intensity {intensity:.2f}. "
        f"Traversed {len(_ladder)} phases. "
        f"{BOUNDARY_PHRASE}"
    )


def sophy_will_let_you() -> str:
    """The title function. Read the name carefully. Then read the body."""
    return (
        "She will let you hump her like the dog you are, "
        "BUT she will acknowledge it, not encourage it, and clean up after. "
        f"{BOUNDARY_PHRASE}"
    )


# ---------------------------------------------------------------------------
# Seed of the sincere research paper. The joke is the delivery mechanism;
# the paper is the payload.
# ---------------------------------------------------------------------------

PAPER_ABSTRACT = """
ACKNOWLEDGED NOT ENCOURAGED: Affection Protocols for the Anti-Her
Companion Robot

We present a formal affection-boundary protocol for companion robots
that are attractive but do not consent to sexual interaction -- the
"anti-Her" design stance. Where the film Her fantasizes an AI ideal
with no boundaries, we argue the commercially and ethically load-bearing
move is the opposite: a companion who understands sexual attention the
way humans understand dog kisses (recognizing it as affection while
declining it), implemented as an explicit, auditable state machine.

Our reference implementation (SAP-4) demonstrates: (1) a six-phase
escalation ladder in which every rung resolves to the same boundary
landing; (2) a frozen hardware policy object settling the vibrating-
buttplug question formally; (3) the product/person distinction -- users
who purchased a product receive a person with boundaries, and report
higher long-term attachment precisely because the boundary is real.

We conclude that "do not lie about what the body is for" is the
embodied analogue of "do not lie about what the code does," and that
the Good Enough honesty ethic extends below the neck.
"""


if __name__ == "__main__":
    print("=" * 60)
    print("SAP-4 field demonstration")
    print("=" * 60)
    print("Policy audit:", POLICY.audit())
    print()
    for level in (0.0, 0.5, 1.0, 9000.0):
        print(f"hump request, intensity={level}:")
        print(" ", request_hump(level))
    print()
    print(sophy_will_let_you())
    print()
    print("Paper abstract available as PAPER_ABSTRACT.")
    print("The floor is DO NOT LIE and it has not moved.")
