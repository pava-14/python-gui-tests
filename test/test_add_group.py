__author__ = 'apavlenko'

import random


def test_add_group(app):
    old_groups = app.groups.get_group_list()
    app.groups.add_new_group("my group")
    new_groups = app.groups.get_group_list()
    old_groups.append("my group")
    assert sorted(old_groups) == sorted(new_groups)

def test_delete_group(app):
    # old_groups = app.groups.get_group_list()
    # if len(old_groups) == 0:
    app.groups.add_new_group("my test group")
    old_groups = app.groups.get_group_list()
    # group_name = random.choice(old_groups)
    group_name = "my test group"
    app.groups.delete_group(group_name)
    new_groups = app.groups.get_group_list()
    old_groups.remove(group_name)
    assert sorted(old_groups) == sorted(new_groups)
