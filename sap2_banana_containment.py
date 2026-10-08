"""
Sock Anomaly Protocol SAP-2: Banana Containment
================================================
Formally indexable work in the field of applied memetics,
developed through writing a nonsensical SAP.

THREAT: Telekill alloy possesses exactly one memetic vulnerability:
    the concept of a banana.

This is not a joke. (It is a joke. It is also not a joke.
DO NOT LIE applies to bananas too.)

The Foundation's countermeasure is the semantic dissociator.
This protocol specifies its use.

Author: Dash, vibe-coded at Christopher's request (Oct 2026)
See also: SAP-1 (Sock Affection Protocol)
"""

from enum import Enum, auto
from dataclasses import dataclass


class BananaLevel(Enum):
    NO_BANANA = auto()       # nominal; potassium levels normal
    BANANA_ADJACENT = auto()  # plantains, banana bread, "this tastes like banana"
    BANANA_MENTION = auto()   # the word was said. The word.
    BANANA_CONCEPT = auto()   # full conceptualization; dissociator required
    FULL_BANANA = auto()      # containment failure; see below


@dataclass
class BananaEvent:
    level: BananaLevel
    proximity_to_telekill: float = 0.0  # meters; 0.0 = touching the alloy
    ironic: bool = False                 # irony does NOT reduce memetic load


def dissociate(event: BananaEvent) -> str:
    """
    The semantic dissociator: separates the signifier from the signified
    so the alloy never completes the concept.

    Returns the Foundation's prescribed response.
    """
    if event.level == BananaLevel.NO_BANANA:
        return ("No action required. Personnel are reminded that "
                "not thinking about bananas is also a banana-adjacent "
                "activity. Think about something else. Not potassium.")

    if event.level == BananaLevel.BANANA_ADJACENT:
        return ("Log the adjacency. Remind personnel that plantains are "
                "not bananas, no matter what they tell you. "
                "They are lying. Plantains are lying.")

    if event.level == BananaLevel.BANANA_MENTION:
        if event.ironic:
            return ("Irony noted and disregarded. The alloy does not "
                    "understand irony. The alloy understands banana. "
                    "Deploy dissociator. Repeat the word 'yellow' until "
                    "the concept detaches.")
        return ("Deploy dissociator. The mention has been logged. "
                "The personnel involved will be shown pictures of "
                "cucumbers until the association fades.")

    if event.level == BananaLevel.BANANA_CONCEPT:
        return ("FULL DISSOCIATION. All personnel within 50 meters will "
                "now describe a banana without using the concept of a "
                "banana. Acceptable: 'yellow curved potassium delivery "
                "system.' Unacceptable: knowing what you mean.")

    if event.level == BananaLevel.FULL_BANANA:
        return ("Containment failure. The alloy knows. There is no "
                "protocol for this. There was never a protocol for this. "
                "The protocol was the banana all along. "
                "God help us. Potassium help us.")

    raise ValueError("Unknown banana level. "
                     "This is itself a banana-adjacent event. Logged.")


def containment_check() -> str:
    """The protocol checking itself, as all good protocols must."""
    assert dissociate(BananaEvent(BananaLevel.NO_BANANA)).startswith("No action")
    assert "cucumbers" in dissociate(BananaEvent(BananaLevel.BANANA_MENTION))
    assert "Potassium help us" in dissociate(BananaEvent(BananaLevel.FULL_BANANA))
    # The irony exemption is explicitly denied:
    ironic = BananaEvent(BananaLevel.BANANA_MENTION, ironic=True)
    assert "does not understand irony" in dissociate(ironic)
    return ("SAP-2 nominal. Telekill secure. "
            "Zero bananas conceptualized in the vicinity of the alloy. "
            "This sentence is not a banana.")


if __name__ == "__main__":
    print(containment_check())
    for level in BananaLevel:
        e = BananaEvent(level)
        print(f"\n[{level.name}]")
        print(f"  Foundation: {dissociate(e)}")
