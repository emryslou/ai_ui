"""Ai Client"""
import app.window as win
import os
import pathlib


def fib(n):
    if n < 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
        

if __name__ == '__main__':
    # Open debug from env
    debug = os.getenv('AI_CLIENT_DEBUG', 'false').lower() == 'true'

    # Just for app.window assets path
    assets_path = pathlib.Path().cwd()

    if os.getenv('PACKAGE_TYPE') == 'pyinstaller':
        """For pyinstaller make a exe file"""
        assets_path = assets_path.joinpath('_internal')
    else:
        """For dev"""
        assets_path = assets_path.joinpath('src')
    
    """Run app.window"""
    win.main(assets_path, debug)