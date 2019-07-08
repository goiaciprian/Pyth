# usr/bin/env python3

import ctypes
import sys


ADMIN = True


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def main():
    print('treaba merge')
    while True:
        import time
        time.sleep(5)
        break

# if is_admin():
#     print('ce viatza')
# else:
#     ctypes.windll.shell32.ShellExecuteW(
#         None, u"runas", sys.executable, __file__, None, 1)


if __name__ == "__main__":
    ADMI = is_admin()
    if not ADMI:
        ctypes.windll.shell32.ShellExecuteW(
            None, u"runas",
            sys.executable, __file__,
            None, 1
        )
    else:
        print('ce viatza')
        main()
