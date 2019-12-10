import unittest

from parameterized import parameterized

import api
from api.api_employee import ApiEmployee
from tools.read_txt import read_txt
from tools.assert_common import assert_common


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api=ApiEmployee()

    @parameterized.expand(read_txt("employee_post.txt"))
    def test01_post(self,username,mobile,workNumber):
        r = self.api.api_post_employee(username,mobile,workNumber)

        print("新增员工后结果:",r.json())
        api.user_id=r.json().get("data").get("id")
        print("新增的员工id为",api.user_id)
        assert_common(self,r)

    def test02_put(self,username="mao888"):
        r = self.api.api_put_employee(username)
        print("更新员工姓名为:",r.json())
        assert_common(self,r)
    def test03_get(self):
        r =self.api.api_get_employee()
        print("查询姓名为",r.json())
        assert_common(self,r)


    def test04_delect(self):
        r =self.api.api_delete_employee(api.user_id)
        print(r.json())
        assert_common(self, r)



