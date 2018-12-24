import allure

class TestLogin:
    def test_a(self):
        print("\n111")
        assert 1

    @allure.step('我是测试步骤001')
    def test_b(self):
        allure.attach('描述1','请输入用户名')
        print("\n222")
        allure.attach('描述2','请输入密码')
        print("\naaa")
        assert 0