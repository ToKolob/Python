import customtkinter as ctk
from datetime import datetime

def display_history(text):
  try:
    with open("data.txt", "r") as file:
      rows = file.readlines()
  except FileNotFoundError:
    rows = []

  rows.reverse() #This reverses the order of the rows
  content = "".join(rows)

  text.delete("1.0", ctk.END)
  text.insert(ctk.END, content) 
  return text

def calculate_today_focus(data_file):
  #data.txt format: YYYY-MM-DD      HH:MM:SS      HH:MM:SS
  try:
    with open(data_file, "r") as file:
      rows = file.readlines()
  except FileNotFoundError:
    rows = []
  #today format: YYYY-MM-DD
  today = datetime.now().strftime("%Y-%m-%d")
  today_minutes = 0
  today_seconds = 0
  today_hours = 0

  for row in rows:
    row = row.strip()
    date, time, pomo = row.split("      ")
    if date == today:
      minutes, seconds = pomo.split(":")
      today_minutes += int(minutes)
      today_seconds += int(seconds)

    if today_seconds >= 60:
      today_seconds -= 60
      today_minutes += 1

    if today_minutes >= 60:
      today_minutes -= 60
      today_hours += 1    

  today_focus = f"{today_hours:02d}:{today_minutes:02d}:{today_seconds:02d}"
  return today_focus

def main():
  # Initialize the GUI
  root = ctk.CTk()
  root.minsize(700,500)
  root.title("Pomodoro Timer")

  #initialize the timer variables
  minutes = 25
  standard_minutes = 25
  seconds = 0
  is_running = False  

  def frame1():
    nonlocal is_running

    def play_pause():
      nonlocal is_running

      minus_button.configure(state=ctk.DISABLED)
      plus_button.configure(state=ctk.DISABLED)

      if not is_running:

        is_running = True
        update_timer()
        play_pause_button.configure(text="Pause")

      else:
        is_running = False
        play_pause_button.configure(text="Resume")

    def stop_timer():
      nonlocal is_running, minutes, seconds, standard_minutes
      is_running = False
      record_time()
      minutes = standard_minutes
      seconds = 0
      update_timer()
      play_pause_button.configure(text="Start")
      minus_button.configure(state=ctk.NORMAL)
      plus_button.configure(state=ctk.NORMAL)

      frame2()





    def update_timer():
      nonlocal is_running, minutes, seconds
      if is_running:
        if minutes == 0 and seconds == 0:
          is_running = False
          play_pause_button.configure(text="Start")
          stop_timer()

        else:
          if seconds == 0:
            minutes -= 1
            seconds = 59
          else:
            seconds -= 1
          time.configure(text=f"{minutes:02d}:{seconds:02d}")
          root.after(1000, update_timer)
      else:
        time.configure(text=f"{minutes:02d}:{seconds:02d}")

    def add_time():
      nonlocal minutes, standard_minutes
      minutes += 5
      standard_minutes += 5
      update_timer()
    
    def subtract_time():
      nonlocal minutes, standard_minutes
      if minutes <= 5:
        return
      minutes -= 5
      standard_minutes -= 5
      update_timer()

    def record_time():
      nonlocal minutes, seconds

      # Calculate the time to record
      minutes_to_record = standard_minutes - minutes
      seconds_to_record = 60 - seconds
      if seconds > 0:
        minutes_to_record -= 1
        seconds_to_record = 60 - seconds
      elif seconds == 0:
        seconds_to_record = 0

      time_to_record = f"{minutes_to_record:02d}:{seconds_to_record:02d}"
      clock_time_to_record = datetime.now().strftime("%Y-%m-%d      %H:%M:%S")

      # Record the time
      with open("data.txt", "a") as file:
        file.write(f"{clock_time_to_record}      {time_to_record}\n")    

    #initialize frame
    frame1 = ctk.CTkFrame(root)
    frame1.place(relx=0.02, rely=0.03, relwidth=0.47, relheight=0.94)
    title = ctk.CTkLabel(frame1, 
    text="Timer", font=("Helvetica", 24))
    title.pack( pady=10)

    #clock
    time = ctk.CTkLabel(frame1, text=f"{minutes:02d}:{seconds:02d}", font=("monospace", 62))
    time.pack( pady=10)

    #start button
    play_pause_button = ctk.CTkButton(frame1, text="Start", font=("Helvetica", 24), command=play_pause)
    play_pause_button.pack( pady=10)
    
    #edit timer container
    button_container = ctk.CTkFrame(frame1, width=500, height=100)
    button_container.pack( pady=10,)

    #subtract  button
    minus_button = ctk.CTkButton(button_container, text="- 5min", font=("Helvetica", 24), command=lambda: subtract_time())
    minus_button.pack( side=ctk.RIGHT, pady=10)

    #plus button
    plus_button = ctk.CTkButton(button_container, text="+ 5min", font=("Helvetica", 24), command=lambda: add_time())
    plus_button.pack(side=ctk.LEFT, pady=10)

    #stop button
    stop_button = ctk.CTkButton(frame1, text="Stop", font=("Helvetica", 24), fg_color="#ac1f2b", hover_color="#750711", command=lambda: stop_timer())
    stop_button.pack( pady=10)


  def frame2():
    #initialize frame
    frame2 = ctk.CTkFrame(root)
    frame2.place( relx=0.51, rely=0.03, relwidth=0.47, relheight=0.94)

    #today's focus
    title_today_focus = ctk.CTkLabel(frame2, text="Today's Focus", font=("Helvetica", 24))
    title_today_focus.pack( pady=10)

    today_focus = ctk.CTkLabel(frame2, text=calculate_today_focus("data.txt"), font=("Helvetica", 48))
    today_focus.pack( pady=10)

    #history
    title_history = ctk.CTkLabel(frame2, text="History", font=("Helvetica", 24))
    title_history.pack( pady=10)
    scrollbar = ctk.CTkScrollbar(frame2)
    text = ctk.CTkTextbox(frame2, yscrollcommand=scrollbar.set, font=("Helvetica", 18))
    text.pack(fill=ctk.BOTH, expand=True )

    display_history(text)

  frame1()
  frame2()
  root.mainloop()    

if __name__ == "__main__":
  main()


