import subprocess
child.wait()
child = subprocess.Popen('adb connect 127.0.0.1:62001')
child.wait()
child = subprocess.Popen('adb connect 127.0.0.1:62025')
child.wait()
child = subprocess.Popen('adb connect 127.0.0.1:62026')
child.wait()
child = subprocess.Popen('adb connect 127.0.0.1:62027')
child.wait()
child = subprocess.Popen('adb connect 127.0.0.1:62028')
child.wait()
child = subprocess.Popen('adb devices')