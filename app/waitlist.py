"""Northside Food Pantry: waitlist for full Saturdays (course sample code)."""


def waitlist_position(waitlist, family):
    """Return the family's place in line (1 is first), or 0 when not on the waitlist."""
    if family not in waitlist:
        return 0
    return waitlist.index(family)
