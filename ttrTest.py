import sys
import termios
import tty

#標準入力のファイルディスクプリタを取得
fd = sys.stdin.fileno()

#fdの端末属性をゲットする
old = termios.tcgetattr(fd)

try:
    #標準入力のモードを切り替える
    #cbreakとrawのどっちもエンターいらなくなるけど、rawはctrl-cとかもきかなくなる
    #tty.setcbreak(sys.stdin.fileno())
    tty.setraw(sys.stdin.fileno())
    ch = sys.stdin.read(1)
    
finally:
    # fdの属性を元に戻す
    termios.tcsetattr(fd, termios.TCSANOW, old)

print("aa")
print(ch)
