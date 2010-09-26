import time
import Pyro4

print "Autoreconnect using PYRO uri."

# We create a proxy with a PYRO uri.
# Reconnect logic depends on the server now.
# (it needs to restart the object with the same id)
uri=raw_input("Enter the uri that the server printed:")
obj=Pyro4.core.Proxy(uri)

while True:
    print "call..."
    try:
        obj.method(42)
        print "Sleeping 1 second"
        time.sleep(1)
    except Pyro4.errors.ConnectionClosedError,x:     # or possibly even ProtocolError
        print "Connection lost. REBINDING..."
        print "(restart the server now)"
        obj._pyroReconnect()
