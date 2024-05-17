import webview
import webview.menu
import pathlib
import os

class Window(object):
    def __init__(self, assets_path: pathlib.Path, debug: bool = False, **kwargs) -> None:
        self.win_debug = debug
        self.assets_path = assets_path
        self.config = {
            'chat_url': os.getenv('AI_CLIENT_URL', 'http://192.168.1.15:8080'),
            'ai_helper_page': self.assets_path.joinpath('assets/main.html').as_uri(),
            'camera_page': self.assets_path.joinpath('assets/video.html').as_uri(),
        }
        
    
    def success(self):
        print('success python')
    
    def error(self):
        print('error python')
    
    def close_win(self):
        w = webview.active_window()
        w.destroy()
    
    def max_win(self):
        w = webview.active_window()
        w.maximize()
    
    def min_win(self):
        w = webview.active_window()
        w.minimize()
    
    def resize_win(self, type: str):
        win_size_by_type = {
            'default': {'width': 1600, 'height': 1800},
            'small': {'width':1200, 'height': 1350},
            'large': {'width':2400, 'height': 2000 },
        }
        
        win_size = win_size_by_type[type]
        w = webview.active_window()
        w.resize(**win_size)
    
    def restore_win(self):
        w = webview.active_window()
        w.restore()
    
    def run(self):
        win_config = {
            'url': self.config['ai_helper_page'],
            'background_color': '#171717',
            'frameless': True,
            'width': 800,
            'height': 900,
        }
        
        def chat_uri() -> str:
            return self.config['chat_url']
        
        win = webview.create_window('AI 助手', **win_config)
        win.expose(
            self.success, self.error,
            self.close_win, self.min_win, self.max_win, self.restore_win, self.resize_win,
            chat_uri
        )
        print(win_config)
        storage_path = self.assets_path.joinpath('app.data').__str__()
        webview.start(args=win, private_mode=False, storage_path=storage_path, debug=self.win_debug)

def main(assets_path: pathlib.Path, debug: bool = False, **kwargs):
    win = Window(assets_path=assets_path, debug=debug, **kwargs)
    win.run()
