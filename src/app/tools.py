import os

def parse_env_from_file(file_path):
    """加载 env file 并设置环境变量
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = f.read()
            for line in data.splitlines():
                line = line.strip() # 去除多余的空格
                if not line or line.startswith('#'):
                    continue
                key, value = line.split('=', 1)
                os.environ[key.strip()] = value.strip()
    except FileNotFoundError:
        print(f"File {file_path} not found")
        return {}

