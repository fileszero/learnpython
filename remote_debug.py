import ptvsd

# Allow other computers to attach to ptvsd at this IP address and port.
ptvsd.enable_attach(address=('0.0.0.0', 3210), redirect_output=True)

# Pause the program until a remote debugger is attached
ptvsd.wait_for_attach()

file = open('/etc/os-release')
content = file.read()
print(content)
file.close()

## you can debug without source edit...
# python3 -m ptvsd --host 0.0.0.0 --port 3210 --wait intro.py
# OR
# python3d intro.py
