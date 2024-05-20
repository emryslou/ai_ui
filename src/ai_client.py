"""Ai Client"""
import app.window as win
import app.tools as tools
import os
import pathlib

if __name__ == '__main__':
    # Just for app.window assets path
    assets_path = pathlib.Path().cwd()
    env_path = assets_path.joinpath('.env')

    if os.getenv('PACKAGE_TYPE') == 'pyinstaller':
        """For pyinstaller make a exe file"""
        assets_path = assets_path.joinpath('_internal')
    else:
        """For dev"""
        assets_path = assets_path.joinpath('src')
    if not env_path.exists():
        demo_env = """# 用于开启调试
# AI_CLIENT_DEBUG = false

# 聊天服务
# UI_CHAT_SERVER = http://192.168.1.15:8080/

# 画图服务
# UI_PAINT_SERVER = http://192.168.1.15:7860/
"""
    
        env_path.touch()
        env_path.write_bytes(data=demo_env.encode('utf-8'))
    
    tools.parse_env_from_file(env_path)
    # Open debug from env
    debug = os.environ.get('AI_CLIENT_DEBUG', 'false').lower() == 'true'
    uri_pages = {
        'chat':  os.environ.get('UI_CHAT_SERVER', 'http://192.168.1.15:8080/'),
        'paint': os.environ.get('UI_PAINT_SERVER', 'http://192.168.1.15:7860/'),
    }
    # """Run app.window"""
    win.main(assets_path, debug, uris=uri_pages)