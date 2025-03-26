import subprocess
import time
import sys
print(sys.argv)

# Start QEMU as a subprocess
proc = subprocess.Popen(sys.argv[1:],
                        stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

while True:
    line = proc.stdout.readline()
    if not line:
        break  # QEMU exited

    sys.stdout.write(repr(line))

    if "Test this media" in line:
        print("Detected boot prompt! Sending keys...")
        time.sleep(0.1)
        proc.stdin.write("sendkey up\n")
        time.sleep(0.1)
        proc.stdin.write("sendkey ret\n")
        proc.stdin.flush()
