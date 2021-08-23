__author__ = 'apavlenko'

import os

import pytest
import win32com.client

from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("C:\\WORK\\FreeAddressBook\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture


def pytest_generate_tests(metafunc):
    if "excel_group" in metafunc.fixturenames:
        testdata = load_from_excel()
        metafunc.parametrize("excel_group", testdata, ids=[str(x) for x in testdata])


def load_from_excel():
    groups = []
    project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    fqn_filename = os.path.join(project_dir, "groups.xlsx")
    excel = win32com.client.DispatchEx("Excel.Application")
    wb = excel.Workbooks.Open(fqn_filename)
    ws = wb.Worksheets("Лист1")
    for i in range(5):
        groups.append(ws.Range(f"A{i + 1}").Value)
    excel.Quit()
    return groups
