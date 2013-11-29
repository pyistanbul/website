import multiprocessing

 
bind = "127.0.0.1:9009"
proc_name = "pyistanbul"
workers = multiprocessing.cpu_count() * 2 + 1
backlog = 2048
debug = False
daemon = True
pidfile = "/tmp/" + proc_name + ".pid"
logfile = "/tmp/" + proc_name + ".log"
