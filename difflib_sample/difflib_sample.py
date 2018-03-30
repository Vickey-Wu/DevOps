#!/usr/bin/python
# -*- coding: UTF-8 -*-


import difflib
import filecmp

text_1 = """how old are you?
i am five"""
text_2 = """how are you?
i am fine"""
text_1_lines = text_1.splitlines()
text_2_lines = text_2.splitlines()

# # compare str by lines with Differ()
# d = difflib.Differ()
# compare = d.compare(text_1_lines, text_2_lines)
# print("\n".join(list(compare)))

#　# compare str by lines with HtmlDiff()
d = difflib.HtmlDiff()
print(d.make_file(text_1_lines, text_1_lines))


import filecmp

#　return True if compare files is the same
print(filecmp.cmp("E:\pythonProcess\DevOps\DevOps\difflib_sample\compare_str.html", "E:\pythonProcess\DevOps\DevOps\difflib_sample\difflib_sample.py"))

