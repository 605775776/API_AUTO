import unittest
import os
from datetime import datetime

from common.HwTestReport import HTMLTestReport
from test_cases import test_abc
#
# 收集测试用例 TestLoader 加载器 加载测试用例
# 放到测试集合和测试套件 TestSuite

# 1 初始化testloader
from test_cases.test_login import TestLogin

testloader = unittest.TestLoader()

# 2 加载测试用例
dir_path = os.path.dirname(os.path.abspath(__file__))
case_path = os.path.join(dir_path, 'test_cases')
# print(os.path.abspath(__file__))
# print(dir_path)
# print(case_path)

# 加载多个模块测试用例 保存到测试套件中
suite = testloader.loadTestsFromModule(test_abc)
# suite2 = testloader.loadTestsFromModule(test_login)

# 添加指定的测试类 快捷键alt+enter
# suite3 = testloader.loadTestsFromTestCase(TestLogin)

# 测试套件组合
# suite_total = unittest.TestSuite()
# suite_total.addTests(suite)
# suite_total.addTests(suite2)


# suite = testloader.discover(start_dir=case_path, pattern='test*.py', top_level_dir=None)
# 放到report
report_path = os.path.join(dir_path, 'report')
print(report_path)
if not os.path.exists(report_path):
    os.mkdir(report_path)
# file_path = os.path.join(report_path, 'test_result.txt')
# with open(file_path, 'w', encoding='utf8') as f:
#
#     # 初始化运行器 文本生成报告
#     runner = unittest.TextTestRunner(f, verbosity=2)
#
#     # 运行测试用例
#     runner.run(suite_total)
# time_str = datetime.now().strftime('%Y%m%d%H%M%S')
time_str = datetime.now().strftime('%Y%m%d%H%M')
file_name = 'test_report_' + time_str + '.html'
file_path = os.path.join(report_path, file_name, )
# with open(file_path, 'wb') as f:
#     # 使用HTMLTestRunner
#     runner = HTMLTestReport(f)
#     runner.run(suite_total)


# 要用二进制打开
with open(file_path, 'wb+') as f:
    runner = HTMLTestReport(stream=f,
                            verbosity=2,
                            )
# f = open(file_path, 'wb')
# runner = HTMLTestReport(stream=f,
#                         verbosity=2,
#                             )

    runner.run(suite)