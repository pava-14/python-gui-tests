__author__ = 'apavlenko'

import random


def test_delete_group(app):
    app.groups.check_for_groups()
    old_groups = app.groups.get_group_list()
    group_name = random.choice(old_groups)
    app.groups.delete_first_matched_group_by_name(group_name)
    new_groups = app.groups.get_group_list()
    old_groups.remove(group_name)
    assert sorted(old_groups) == sorted(new_groups)
