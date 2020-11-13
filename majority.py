from typing import List, Optional


def majority(items: List[str]) -> Optional[str]:
    """
    Find and return the majority element from the provided list.
    Majority element is an element that occurs at least half of the elements of the input.
    Candidates for the majority is determined using improved Boyer–Moore majority vote algorithm,
    after the candidates are tested for truly being a majority element.

    NOTE: If two majority elements (50% and 50%) are in the list - first one will be returned as a majority element.

    :param items: list if items
    :type items: List

    :return: Majority element if exists, else None
    :rtype str or None
    """

    length = len(items)
    if not length:
        return None

    # first element is a leader
    leader = items[0]
    advantage_current = 1
    # first element also is a peak leader
    peak_leader = leader
    peak_advantage = advantage_current

    # skip first element
    for i in range(1, length):
        # increase an advantage of the leader
        if leader == items[i]:
            advantage_current += 1

            # increase peak advantage
            if peak_leader == leader:
                peak_advantage += 1
            # change peak leader and peak advantage points
            elif peak_advantage < advantage_current:
                peak_leader = leader
            continue

        # another item becomes a leader
        if advantage_current == 1:
            leader = items[i]
            continue

        # decrease an advantage of current leader
        advantage_current -= 1

    # ensure that candidates are true majority (50% or more)
    half_length = length / 2
    leader_count = peak_leader_count = 0

    for item in items:
        if item == peak_leader:
            peak_leader_count += 1
        elif item == leader:
            leader_count += 1

    # peak leader trying his luck first
    if peak_leader_count >= half_length:
        return peak_leader
    elif leader_count >= half_length:
        return leader

    return None
