
# encoding=utf-8
from __future__ import unicode_literals
import BMESBIO2Data

import sys

# 切换到上级目录
sys.path.append("../")
# 引入本地库

M2D = BMESBIO2Data.BMESBIO2Data("BMES")


Demo = M2D.toData("/home/terry/dev/ChineseAnnotator/test.txt")
print("qqqw")
