__author__ = 'apavlenko'

import os
import random
import string

import win32com.client


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
fqn_filename = os.path.join(project_dir, "groups.xlsx")
# delete file if exist
if os.path.exists(fqn_filename):
    os.remove(fqn_filename)
# open excel and create xlsx file
xl = win32com.client.DispatchEx("Excel.Application")
xl.Visible = 1
wb = xl.Workbooks.Add()
ws = wb.Worksheets("Лист1")
# fill data
for i in range(5):
    ws.Range(f"A{i + 1}").Value = random_string("Group ", 6)
wb.SaveAs(os.path.join(project_dir, "groups.xlsx"))
# close excel
xl.Quit()
