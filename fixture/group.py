__author__ = 'apavlenko'


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def get_group_list(self):
        group_list = []
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        group_list = [node.text() for node in root.children()]
        self.close_group_editor()
        return group_list

    def add_new_group(self, name):
        self.open_group_editor()
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        self.set_text_to_edit(name)
        self.close_group_editor()

    def delete_first_matched_group_by_name(self, name):
        self.open_group_editor()
        if self.select_first_matched_group_by_name(name):
            self.group_editor.window(auto_id="uxDeleteAddressButton").click()
            window_delete_group = self.app.application.window(title="Delete group")
            # window_delete_group.window(auto_id="uxDeleteAllRadioButton").click_input()
            window_delete_group.Button.click()
            # window_delete_group.window(auto_id="uxOKAddressButton").click()
            window_delete_group.Button3.click()
        self.close_group_editor()

    def select_first_matched_group_by_name(self, group_name):
        is_selected = False
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        for node in root.children():
            if node.text() == group_name:
                node.select()
                is_selected = True
                break
        return is_selected

    def set_text_to_edit(self, text):
        input = self.group_editor.window(class_name="Edit")
        input.set_text(text)
        input.type_keys("\n")

    def edit_first_matched_group_by_name(self, old_name, new_name):
        self.open_group_editor()
        if self.select_first_matched_group_by_name(old_name):
            self.group_editor.window(auto_id="uxEditAddressButton").click()
            self.set_text_to_edit(new_name)
        self.close_group_editor()

    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait("visible")

    def close_group_editor(self):
        self.group_editor.close()

    def check_for_groups(self):
        old_groups = self.app.groups.get_group_list()
        if len(old_groups) == 0:
            self.app.groups.add_new_group("my test group")
            old_groups = self.app.groups.get_group_list()
        return old_groups
