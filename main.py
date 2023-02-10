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
    docker run --name uc -v /root/jenkins-data/workspace/uc:/home/uc b4d20e595b48 python main.py
    
    # jenkins部署
    docker run \
    -u root \
    -d \
    -p 8080:8080 \
    -p 50000:50000 \
    -v /root/jenkins-data:/var/jenkins_home \
    -v /root/.ssh:/var/jenkins_home/.ssh \
    -v /var/run/docker.sock:/var/run/docker.sock \
    jenkinsci/blueocean
    """
    # 设置配置为test环境
    init_setting("setting_test.py")
    
    pytest.main([
        "-v",
        "--alluredir",
        "reports",
        "testcases",
        "--clean-alluredir",
        "--disable-warnings",
        "--color",
        "yes"
    ])