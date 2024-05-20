import webview
import webview.menu
import pathlib
import os

class Window(object):
    def __init__(self, assets_path: pathlib.Path, debug: bool = False, **kwargs) -> None:
        self.win_debug = debug
        self.assets_path = assets_path
        self.config = {
            'ai_page': self.assets_path.joinpath('assets/main.html').as_uri(),
            'camera_page': self.assets_path.joinpath('assets/video.html').as_uri(),
            'window_size': {
                'default': {'width': 1600, 'height': 1800},
                'small': {'width':1200, 'height': 1350},
                'large': {'width':2400, 'height': 2000 },
            }
        }
        
        if 'uris' in kwargs and isinstance(kwargs['uris'], dict):
            """uri 设置"""
            self.config.update({'uris': kwargs['uris']})
            
    
    def success(self, uri_name):
        print('success python', uri_name)
        if uri_name == 'paint':
            self.config['window_size'].update({
                'default': {'width': 1600, 'height': 1800},
                'small': {'width':1200, 'height': 1350},
                'large': {'width':2400, 'height': 2000 },
            })
        else:
            self.config['window_size'].update({
                'default': {'width': 1600, 'height': 2000},
                'small': {'width':1200, 'height': 1550},
                'large': {'width':2400, 'height': 2200 },
            })
    
    def error(self, *args, **kwargs):
        print('error python', args, kwargs),
    
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
        win_size = self.config['window_size'][type]
        w = webview.active_window()
        w.resize(**win_size)
    
    def restore_win(self):
        w = webview.active_window()
        w.restore()
    
    def run(self):
        win_config = {
            'url': self.config['ai_page'],
            'background_color': '#171717',
            'frameless': True,
            'width': 800,
            'height': 900,
            'easy_drag': True,
        }

        def uri_by_name(uri_name: str) -> str:
            return self.config['uris'][uri_name]
        
        win = webview.create_window('AI 助手', **win_config)
        win.expose(
            self.success, self.error,
            self.close_win, self.min_win, self.max_win, self.restore_win, self.resize_win,
            uri_by_name,
        )
        storage_path = self.assets_path.joinpath('app.data').__str__()
        webview.start(args=win, private_mode=False, storage_path=storage_path, debug=self.win_debug)

def main(assets_path: pathlib.Path, debug: bool = False, **kwargs):
    win = Window(assets_path=assets_path, debug=debug, **kwargs)
    win.run()
