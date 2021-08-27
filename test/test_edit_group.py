__author__ = 'apavlenko'

import random


def test_edit_group(app):
    old_groups = app.groups.check_for_groups()
    group_name = random.choice(old_groups)
    new_group_name = "Edited Group"
    app.groups.edit_first_matched_group_by_name(old_name=group_name, new_name=new_group_name)
    new_groups = app.groups.get_group_list()
    old_groups[old_groups.index(group_name)] = new_group_name
    assert sorted(old_groups) == sorted(new_groups)
