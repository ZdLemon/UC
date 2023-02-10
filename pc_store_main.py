import pytest
import os


def init_setting(path):
    "初始化setting.py文件"
    with open(path, "rt", encoding="utf-8") as f:
        
        setting = [i for i in f.read().split("\n")]
        # 末尾连续2个空
        if setting[-2:] == ["", ""]:
            setting.pop()
 
    
        with open("setting.py", "wt", encoding="utf-8") as f:
            for line in setting:
                if line:
                    f.write(line)
                    f.write("\n")
                else:
                    f.write("\n")


if __name__ == "__main__":
    """
    docker run --name uc -v ~/uc:/uc -v /etc/localtime:/etc/localtime 097b55b4e972 python -m main
    -v /etc/localtime:/etc/localtime 意义：让容器使用和服务器同样的时间设置。
    """
    # 设置配置为test环境
    init_setting("setting_test.py")
    
    pytest.main([
        "-v",
        "--alluredir",
        "reports",
        "pc_store_testcases",
        "--clean-alluredir",
        "--disable-warnings",
        "--color",
        "yes"
    ])