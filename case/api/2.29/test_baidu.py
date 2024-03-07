import requests
import allure
import pytest
import os
from loguru import logger

class TestBaidu:
    
    def setup_method(self):
        print("\nsetup_method……")
    
    @allure.title("百度接口测试")
    @allure.description("测试百度关键字接口测试")
    def test_baidu_com(self):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"}
        res = requests.get(url="https://www.baidu.com/s?wd=周杰伦")
        content = res.content
        logger.info(content)
        assert res.status_code == 200
    
    def teardown_method(self):
        print("\nteardown_method……")
        
if __name__ == '__main__':
    # # 生成json文件
    # pytest.main(['-s','-v','--alluredir=./report','--clean-alluredir'])
    # # 生成html文件
    # os.system('allure generate %s -o %s --clean'%("./report","./report/allure_html_path"))
    # os.system("allure serve .\report")
    pass