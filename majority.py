from typing import List, Optional


def majority(items: List[str]) -> Optional[str]:
    """
    Find and return the majority element from the provided list.
    Majority element is an element that occurs for more than half of the elements of the input.
    Candidate for the majority is determined using Boyer–Moore majority vote algorithm,
    after the candidate is tested for truly being a majority element.

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
    advantage = 1

    # loop starts from the second element
    for i in range(1, length):
        # increase an advantage of the leader
        if leader == items[i]:
            advantage += 1
            continue
        # another item becomes a leader
        if advantage == 1:
            leader = items[i]
            continue
        # decrease an advantage
        advantage -= 1

    # ensure that leader is true majority
    count = 0
    for item in items:
        if item == leader:
            count += 1

    if count > length / 2:
        return leader

    return None
