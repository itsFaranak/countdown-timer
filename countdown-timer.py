
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTimeEdit, QPushButton
from PyQt5.QtCore import QTimer
from PyQt5 import uic
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl , Qt

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        
        # Load the UI file
        uic.loadUi("countdown-timer-fixed.ui", self)

        # Define our widgets
        self.Title_label = self.findChild(QLabel, "Titlelabel")
        self.time_display = self.findChild(QLabel, "timeDisplay")
        
        # QTimeEdit
        self.time_edit = self.findChild(QTimeEdit, "timeEdit")
        
        # QPushButton
        self.start_button = self.findChild(QPushButton, "startButton")
        self.stop_button = self.findChild(QPushButton, "stopButton")
        self.reset_button = self.findChild(QPushButton, "resetButton")

        self.time_display.setAlignment(Qt.AlignCenter)

        # click button signals
        self.start_button.clicked.connect(self.start_timer)
        self.stop_button.clicked.connect(self.stop_timer)
        self.reset_button.clicked.connect(self.reset_timer)

        # QTimer set up
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        # timer
        self.time_left = 0
        self.paused = False
        self.time_display.setText("00:00:00")

        # Dark Neon Theme colors 
        self.color_default = "#1E1E2E"   
        self.color_paused = "#FFB86C"    
        self.color_done = "#50FA7B"     
        self.setStyleSheet(f"background-color: {self.color_default};")

        # MediaPlayer for alarm
        self.player = QMediaPlayer()
        # Show the App
        self.show()

    def start_timer(self):
        time = self.time_edit.time()
        self.time_left = time.hour() * 3600 + time.minute() * 60 + time.second()
        self.timer.start(1000)  # Update every 1000 milliseconds (1 second)
        self.paused = False
        self.setStyleSheet(f"background-color: {self.color_default};")

    # Get the timer 
    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            hour = self.time_left // 3600  # Converting seconds hour
            minute = (self.time_left % 3600) // 60  # Converting minute 
            seconds = self.time_left % 60  
            self.time_display.setText(f"{hour:02d}:{minute:02d}:{seconds:02d}")
        # وقتی زمان به پایان رسید
        if self.time_left == 0:
            self.timer.stop() # stop timer
            self.time_display.setText("00:00:00")
            self.setStyleSheet(f"background-color: {self.color_done};")  
            self.play_sound()
            # Reset after 8 seconds
            QTimer.singleShot(8000, self.reset_after_alarm)

    def play_sound(self): # Alarm ringing
        url = QUrl.fromLocalFile("Alarm-Clock.mp3")  # Alarm
        self.player.setMedia(QMediaContent(url))
        self.player.play()

    def stop_timer(self):
        if self.paused is False:
            self.timer.stop()
            self.stop_button.setText("Resume")
            self.paused = True
            self.setStyleSheet(f"background-color: {self.color_paused};")  
        else:
            self.timer.start(1000)  #ادامه تایمر 
            self.stop_button.setText("Stop")
            self.paused = False
            self.setStyleSheet(f"background-color: {self.color_default};")
        
    def reset_timer(self):
        self.timer.stop()  # توقف تایمر
        initial_time = self.time_edit.time() 
        self.time_left = (initial_time.hour() * 3600 + initial_time.minute() * 60 + initial_time.second())
        self.stop_button.setText("Stop")
        # نمایش دوباره زمان اولیه
        self.time_display.setText(initial_time.toString("HH:mm:ss"))
        self.setStyleSheet(f"background-color: {self.color_default};")

    def reset_after_alarm(self):
        # Reset to initial QTimeEdit value
        self.timer.stop()
        self.time_display.setText("00:00:00")
        self.setStyleSheet(f"background-color: {self.color_default};")


#Initilize the App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()