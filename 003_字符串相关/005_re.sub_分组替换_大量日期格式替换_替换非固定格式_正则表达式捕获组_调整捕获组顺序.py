# -*- coding:utf-8 -*-

import re

s = '2016-05-23 10:52:12 i am ok, you are ok'

# 替换s中的日期为05/23/2016(美国日期格式)
# 简单替换可以直接使用replace
t1 = s.replace('2016-05-23', '05/23/2019')
print(t1)
print("*" * 50)

# 大量替换，替换字符复杂可使用re.sub并且可以进行编组
# \d代表任意数字，后面的{4}代表4个数字
t2 = re.sub(r'\d{4}-\d{2}-\d{2}','05/28/2019', s)
print(t2)
print("*" * 50)

# 上面是日期进行的替换，但是我们不修改日期，只修改格式
# 编组方式1：按位置编组（推荐使用）
# 表达式捕获组需要是小括号，表达式自左到右，依次编号1、2、3...
# 替换组使用\编号
t3 = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', s)
print(t3)
print("*" * 50)

# 编组方式2：关键字编组(复杂尽量不用，有时候匹配会错)
# 捕获组进行关键字编号，格式如下：(?P<名称>) \g<名称>
t4 = re.sub(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})',
            r'\g<month>/\g<day>/\g<year>', s)
print(t4)
print("*" * 50)
