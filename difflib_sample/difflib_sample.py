#!/usr/bin/python
# -*- coding: UTF-8 -*-


import difflib
import filecmp

text_1 = """how are you? what the fuck are yourrr talking about?i am fine
<tr><td>(f)irst change</td> </tr>
fuck
                      <tr><td>(n)ext change</td> </tr>
                      <tr><td>(t)op</td> </tr>"""
text_2 = """how are you? what the fuck are yrou talking about?i am fine

fuck"""
text_1_lines = text_1.splitlines()
text_2_lines = text_2.splitlines()

# compare str by lines with Differ()
d = difflib.Differ()
compare = d.compare(text_1_lines, text_2_lines)
# "-" mean content at first text but not second, "+" reverse to "-", "?" mean this line exist difference and "^" point to the difference, "-" after "?" line mean some words was delete , "+" reverse to "-"
print("\n".join(list(compare)))

# compare str by lines with HtmlDiff()
d = difflib.HtmlDiff()
print(d.make_file(text_1_lines, text_2_lines))


import filecmp
#　return True if compare files is the same
text_1 = "E:\pythonProcess\DevOps\DevOps\difflib_sample\difflib_sample.py"
text_2 = "E:\pythonProcess\DevOps\DevOps\difflib_sample\compare_str.html"
dir1 = "E:\pythonProcess\DevOps\DevOps\dnspython"
dir2 = "E:\pythonProcess\DevOps\DevOps\difflib_sample"
# compare two files
print(filecmp.cmp(text_1, text_2))
# compare more than two files
print(filecmp.cmpfiles(dir2, dir2, ["difflib_sample.py","difflib_sample.py"]))
# compare dirs
dir_com = filecmp.dircmp(dir1, dir2)
print(dir_com.report())
