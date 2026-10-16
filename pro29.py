import time
def pomodoro_Timer(work_min=1,break_min=5,cycles=4):
    print("Welcome to Pomodoro Timer")
    for cycle in range(1, cycles + 1):
        print(f"Cycle {cycle}:work for {work_min} minutes")
        time.sleep(work_min * 60)
        print("Work session complete!")
        
        if cycle>cycles:
            print(f"Take a break for {break_min} minutes")
            time.sleep(break_min * 60)
            print("break timeout, back to work")
    print("All pomodoro Cycle Comleted! Great Job")        
pomodoro_Timer()