# Chapter06_3
# 파이썬 패키지
# 파이썬 작성 및 사용법
# 파이썬은 패키지로 분할 된 개별적인 모듈로 구성
# __init__.py : Python 3.3 부터는 없어도 패키지로 인식 -> 단, 하위 호환을 위해 작성 추천
# 상대경로 : ..(부모 디렉토리), .(현재 디렉토리) -> 모듈 내부에서만 사용

# 예제1
import sub.sub1.module1
import sub.sub2.module2

# 사용
sub.sub1.module1.mod1_test1()                       # Path :  c:\python_study\Basic\chapter06\sub\sub1\module1.py
sub.sub1.module1.mod1_test2()                       # Path :  c:\python_study\Basic\chapter06\sub\sub1\module1.py

sub.sub2.module2.mod2_test1()                       # Path :  c:\python_study\Basic\chapter06\sub\sub2\module2.py
sub.sub2.module2.mod2_test2()                       # Path :  c:\python_study\Basic\chapter06\sub\sub2\module2.py

# 예제2
from sub.sub1 import module1
from sub.sub2 import module2 as m2

module1.mod1_test1()                                # Path :  c:\python_study\Basic\chapter06\sub\sub1\module1.py
module1.mod1_test2()                                # Path :  c:\python_study\Basic\chapter06\sub\sub1\module1.py

m2.mod2_test1()                                     # Path :  c:\python_study\Basic\chapter06\sub\sub2\module2.py
m2.mod2_test2()                                     # Path :  c:\python_study\Basic\chapter06\sub\sub2\module2.py

# 예제3
from sub.sub1 import *
from sub.sub2 import *

module1.mod1_test1()
module1.mod1_test2()

module2.mod2_test1()
module2.mod2_test2()