__author__ = 'apavlenko'


def test_add_group(app):
    old_groups = app.groups.get_group_list()
    app.groups.add_new_group("my group")
    new_groups = app.groups.get_group_list()
    old_groups.append("my group")
    assert sorted(old_groups) == sorted(new_groups)
