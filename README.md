
# ScreenColor

Simple Python library to get average color of monitor(s)




## Usage/Examples

Get average screen color every 5 seconds

```python
from screencolor import ScreenColor
import threading
import time


sc = ScreenColor(monitor_id=-1)
# Start refresh color loop
threading.Thread(target=sc.start_loop).start()

# Print monitor color every 5 seconds
while True:
    print(sc.get(rgb=False))
    time.sleep(5)
```

