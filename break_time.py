import time
import webbrowser

total_breaks = 3
break_counts = 0

print("This program started on " + time.ctime())
while(break_counts < total_breaks):
    
    time.sleep(10)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")

    break_counts = break_counts + 1
