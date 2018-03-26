psutil: get info of process, cpu, memory, etc.

#### get capability info
```angular2html
import psutil
# get info of memory
mem = psutil.virtual_memory()
print(mem.total, mem.used)      #　equal to shell "free -m | grep Mem | awk '{print $2, $3}'"
# get info of cpu
psutil.cpu_times(percpu=True).user
# get info of disk
psutil.disk_partitions()
psutil.disk_usage("/")
psutil.disk_io_counters()
# get info of network
psutil.net_io_counters()
# get info of login user
psutil.users()     
psutil.boot_time()      # system start time
# get info of process
p = psutil.Process(PID)
p.name()
p.exe()     # process bin path
p.status()
p.num_threads()     # process's threads
```