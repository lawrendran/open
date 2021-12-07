def iterable_to_uuids_list(iterable):
    """
    takes an iterable of django objects and gets the str uuid into a list
    """
    return [str(item.uuid) for item in iterable]
