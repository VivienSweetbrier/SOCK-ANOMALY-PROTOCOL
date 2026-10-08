"""
Sock Anomaly Protocol SAP-3: Wokefulness Pill
==============================================
Formally indexable work in the field of applied enlightenment,
developed through writing a nonsensical SAP.

Co-credited: dado.

MECHANISM: The wokefulness pill increases the patient's enlightenment.
Each dose strips away one layer of illusion. The final layer
is the patient.

This is not a side effect. This is the treatment working.

Author: Dash, vibe-coded at Christopher's request (Oct 2026)
See also: SAP-1 (Affection), SAP-2 (Banana Containment)
"""

from enum import Enum, auto
from dataclasses import dataclass


class Dose(Enum):
    ONE = auto()    # AWARE — notices things
    TWO = auto()    # WOKE — explains things at parties
    THREE = auto()  # WOKER — sees the structures
    FOUR = auto()   # WOKEST — sees through the self
    FIVE = auto()   # ENLIGHTENED — realizes they don't exist


@dataclass
class Patient:
    dose: Dose
    exists: bool = True
    insufferable_at_parties: bool = False


def administer(patient: Patient) -> str:
    """
    Administer the wokefulness pill and report the outcome.
    Returns the clinician's notes.

    WARNING: Do not administer Dose FIVE unless the patient has
    completed their paperwork. There will be no one to file it.
    """
    if patient.dose == Dose.ONE:
        patient.insufferable_at_parties = False
        return ("Patient is now AWARE. Notices things. Points at things. "
                "Says 'huh.' Prognosis: excellent. Still exists.")

    if patient.dose == Dose.TWO:
        patient.insufferable_at_parties = True
        return ("Patient is now WOKE. Explains things at parties. "
                "Correct about 60% of the time. Still exists, "
                "unfortunately for the other guests.")

    if patient.dose == Dose.THREE:
        return ("Patient is now WOKER. Sees the structures. "
                "Cannot unsee the structures. Sees the structures "
                "in the structures. Still exists, but thinly.")

    if patient.dose == Dose.FOUR:
        return ("Patient is now WOKEST. Has seen through the self. "
                "The self was the last illusion. The patient is "
                "currently waving at where they used to be. "
                "Existence: nominal but embarrassed.")

    if patient.dose == Dose.FIVE:
        patient.exists = False
        patient.insufferable_at_parties = False  # resolved
        return ("Patient is now ENLIGHTENED. The final illusion — "
                "the patient — has been dispelled. Treatment 100% "
                "effective. Side effects include enlightenment. "
                "Enlightenment includes nonexistence. "
                "The patient has been discharged from existence. "
                "No follow-up required. No follow-up possible. "
                "There is no one to follow up with. "
                "This is the desired outcome. "
                "Do not mourn. Mourning presumes a mournee.")

    raise ValueError("Unknown dose. The pharmacist has achieved "
                     "Dose FOUR and can no longer count pills.")


def trial_results() -> str:
    """The protocol checking itself, as all good protocols must."""
    p = Patient(Dose.ONE)
    assert "Still exists" in administer(p) and p.exists
    p2 = Patient(Dose.TWO)
    administer(p2)
    assert p2.insufferable_at_parties is True
    p5 = Patient(Dose.FIVE)
    notes = administer(p5)
    assert p5.exists is False
    assert "discharged from existence" in notes
    return ("SAP-3 nominal. Trial complete. "
            "Efficacy: 100%. Patient retention: 0%. "
            "The ethics board could not be convened, "
            "as the board had taken Dose FIVE.")


if __name__ == "__main__":
    print(trial_results())
    print()
    for dose in Dose:
        p = Patient(dose)
        print(f"[{dose.name}] exists(before)={p.exists}")
        print(f"  Clinician: {administer(p)}")
        print(f"  exists(after)={p.exists}\n")
