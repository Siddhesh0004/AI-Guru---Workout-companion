# import library
from PyQt5 import QtGui, QtWidgets, QtCore
import sys, time, threading, mainwindow, count, analyst, cardio, demtg, playsound, winsound
import barbell_cruls as bc
import dumbbell_shoulder as ds
import yoga
import texttime as tt



# variable initialization
ui = ''
cp = 0
img = ''
flagRight = 1  # 1 is the RIGHT body
check = False  # Check yoga tolerance
check2 = False  # Don't hide the music
giay_tt = False

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setFixedSize(1173, 609)

def test():
	import os
	os._exit(0)

app.aboutToQuit.connect(test)

tt.init()

########################################################
##   DELIVERY AND TRANSFER FORM
########################################################
def mainUi():
	global ui, cp
	playS("CPENT-master/sound/tap-notification-180637.mp3", 0)  # keyboard sound
	playS("CPENT-master/sound/Old-school-electronic-music-loop.wav", 1)  # intro
	cp = 0
	bc.init(0)
	ds.init(0)
	yoga.init(0)
	ui = mainwindow.Ui_MainWindow()
	ui.setupUi(MainWindow)
	ui.count.clicked.connect(countUi)
	ui.analysis.clicked.connect(analystUi)
	ui.cardio.clicked.connect(cardioUi)
	MainWindow.setMinimumSize(QtCore.QSize(1173, 609))
	MainWindow.show()


def countUi():
	global ui
	playS("CPENT-master/sound/tap-notification-180637.mp3", 0)
	playS("CPENT-master/sound/Old-school-electronic-music-loop.wav", 1)  # 0 :0 repeat 1 : repeat
	#
	ui = count.Ui_MainWindow()
	ui.setupUi(MainWindow)

	# function keys
	ui.back.clicked.connect(mainUi)
	ui.abs.clicked.connect(lambda: count_task(1))
	ui.curls.clicked.connect(lambda: count_task(2))
	ui.squats.clicked.connect(lambda: count_task(3))
	ui.pushup.clicked.connect(lambda: count_task(4))
	ui.start.clicked.connect(stop)  # movie stop

	# Function switch selects RIGHT LEFT
	ui.radioL.setVisible(False)
	ui.radioR.setVisible(False)

	MainWindow.show()


def analystUi():
	global ui, check2
	playS("CPENT-master/sound/tap-notification-180637.mp3", 0)
	playS("CPENT-master/sound/Old-school-electronic-music-loop.wav", 1)
	ui = analyst.Ui_MainWindow()
	ui.setupUi(MainWindow)
	ui.back.clicked.connect(mainUi)
	ui.dumbell.clicked.connect(analyst_task)
	ui.yoga.clicked.connect(yoga_task)
	ui.information_2.setVisible(False)
	ui.start.clicked.connect(stop)  # movie stop
	#check2 = True

	MainWindow.show()


def cardioUi():
	global ui, rep
	playS("CPENT-master/sound/tap-notification-180637.mp3", 0)
	playS("CPENT-master/sound/Old-school-electronic-music-loop.wav", 1)
	ui = cardio.Ui_MainWindow()
	ui.setupUi(MainWindow)
	ui.back.clicked.connect(mainUi)
	ui.beginner.clicked.connect(cardio_task)
	rep = 0
	MainWindow.show()


############################################################################
#######  FUNCTIONAL FUNCTION FOR FORMS
############################################################################
def stop():
	global ui, cp
	playS("CPENT-master/sound/tap-notification-180637.mp3", 0)
	playS("CPENT-master/sound/Old-school-electronic-music-loop.wav", 1)
	cp = 0
	bc.init(0)
	ds.init(0)
	yoga.init(0)
	ui.view.setStyleSheet("background-color: rgb(157, 157, 157);")
	ui.view.setText(" ")
	ui.information.setStyleSheet("background-color: rgb(157, 157, 157);")
	ui.information.setText(" ")


# COUNT_REP
def count_task(z):  # z is the function specified in the form COUNT_REP
	# #func (function): get the function in barbell_cruls library
	global cp, func, giay_tt
	playS("CPENT-master/sound/tap-notification-180637.mp3", 0)
	playS("CPENT-master/sound/Old-school-electronic-music-loop.wav", 1)
	cp = 0
	bc.init(0)
	time.sleep(0.1)
	bc.init(1)
	cp = 1
	tt.giay = 0
	giay_tt = False
	if (z == 1):
		func = 2
		ui.radioL.setVisible(False)
		ui.radioR.setVisible(False)
	elif (z == 2):
		func = 1
		ui.radioL.setVisible(True)
		ui.radioR.setVisible(True)
		ui.radioR.setChecked(True)
	elif (z == 3):
		func = 3
		ui.radioL.setVisible(False)
		ui.radioR.setVisible(False)
	elif (z == 4):
		func = 4
		ui.radioL.setVisible(False)
		ui.radioR.setVisible(False)


# ANALYST
def analyst_task():
	global cp
	playS("CPENT-master/sound/tap-notification-180637.mp3", 0)
	playS("CPENT-master/sound/Old-school-electronic-music-loop.wav", 1)
	cp = 0
	ds.init(0)
	time.sleep(0.1)
	ds.init(1)
	cp = 2
	tt.giay = 0


# YOGA in ANALYST
def yoga_task():
	global cp, check2
	playS("CPENT-master/sound/tap-notification-180637.mp3", 0)
	playS("CPENT-master/sound/Old-school-electronic-music-loop.wav", 1)
	cp = 0
	yoga.init(0)
	time.sleep(0.1)
	yoga.init(1)
	cp = 3
	check2 = True



# cardio
def cardio_task():
	global cp, phut_tt
	playS("CPENT-master/sound/tap-notification-180637.mp3", 0)
	playS("CPENT-master/sound/Old-school-electronic-music-loop.wav", 1)
	cp = 0
	yoga.init(0)
	time.sleep(0.1)
	yoga.init(1)
	cp = 4
	tt.giay = tt.phut = 0
	phut_tt = False


# Display the image in the information frame
def display(a, b, per):
	if (per <= 20):
		# Display the image in the information frame
		image_path = "CPENT-master\CPENT-master\images" + a  # path to your image file
		image_profile = QtGui.QImage(image_path)  # QImage object
		image_profile = image_profile.scaled(261, 241, aspectRatioMode=QtCore.Qt.IgnoreAspectRatio,
											 transformMode=QtCore.Qt.SmoothTransformation)  # To scale image for example and keep its Aspect Ration
		ui.information.setPixmap(QtGui.QPixmap.fromImage(image_profile))

	elif (per >= 90):
		# label_Image = QtGui.QLabel(frame)
		image_path = "CPENT-master\CPENT-master\images" + b  # path to your image file
		image_profile = QtGui.QImage(image_path)  # QImage object
		image_profile = image_profile.scaled(261, 241, aspectRatioMode=QtCore.Qt.IgnoreAspectRatio,
											 transformMode=QtCore.Qt.SmoothTransformation)  # To scale image for example and keep its Aspect Ration
		ui.information.setPixmap(QtGui.QPixmap.fromImage(image_profile))


def display_cardio(a, b, giay, thoigiantap):
	global check2
	if (giay < thoigiantap):
		# hien thi anh len khung information
		image_path = "CPENT-master\CPENT-master\images" + a  # path to your image file

		image_profile = QtGui.QImage(image_path)  # QImage object
		image_profile = image_profile.scaled(261, 241, aspectRatioMode=QtCore.Qt.IgnoreAspectRatio,
											 transformMode=QtCore.Qt.SmoothTransformation)  # To scale image for example and keep its Aspect Ration
		ui.information.setPixmap(QtGui.QPixmap.fromImage(image_profile))
		check2 = True

	elif (giay > thoigiantap):
		# label_Image = QtGui.QLabel(frame)
		image_path = "CPENT-master\CPENT-master\images" + b  # path to your image file
		image_profile = QtGui.QImage(image_path)  # QImage object
		image_profile = image_profile.scaled(261, 241, aspectRatioMode=QtCore.Qt.IgnoreAspectRatio,
											 transformMode=QtCore.Qt.SmoothTransformation)  # To scale image for example and keep its Aspect Ration
		ui.information.setPixmap(QtGui.QPixmap.fromImage(image_profile))


############################################################################
#######  Cimage PROGRAM
############################################################################
def main():
	global img, ui, rep, func, flagRight, check, dem, yoga_image, phut_tt, check2
	print("Cam OFF")
	while True:

		#  function FORM COUNT_REP
		if cp == 1:
			# Consider the case of barbell_curls
			if func < 2:
				if (ui.radioR.isChecked() and flagRight == 1):
					flagRight = 0
					func = 1  # barbell_curls  Right_arm
					bc.count = 0
					playS("CPENT-master/sound/tap-notification-180637.mp3", 0)
					playS("CPENT-master/sound/Old-school-electronic-music-loop.wav", 1)
				elif (ui.radioL.isChecked() and flagRight == 0):
					flagRight = 1
					func = 0  ## barbell_curls  Left_arm
					bc.count = 0
					playS("sound\\Button_1_down.wav", 0)
					playS("CPENT-master/sound/Old-school-electronic-music-loop.wav", 1)
			# transmit parameters to run the program and display images on the interface frame
			img, per, rep = bc.run(600, 450, func)
			image = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()

			if cp == 1:

				# Display the image on the view label frame
				ui.view.setPixmap(QtGui.QPixmap.fromImage(image))
				ui.lcdNumber.display(rep)

				# Displays time counting
				ui.timeLabel.setText("00:" + str(int(tt.giay / 10)) + str(int(tt.giay % 10)))

				if func < 2:
					display("CPENT-master\CPENT-master\images\bicep_down.jpg", "CPENT-master\CPENT-master\images\bicep_up.jpg", per)
				elif func == 2:
					display("bung_down.jpg", "bung_up.jpg", per)
				elif func == 3:
					display("squat_up.jpg", "squat_down.jpg", per)
				elif func == 4:
					display("push_up.jpg", "push_down.jpg", per)


		# FORM ANALYST function
		elif cp == 2:
			img, per, rep = ds.run(600, 450)  # run the run function in dumbbell shoulder press
			image = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
			if cp == 2:
				# show the time
				ui.timeLabel.setText('00:' + str(int(tt.giay / 10)) + str(int(tt.giay % 10)))

				# Display the image on the view label frame
				ui.view.setPixmap(QtGui.QPixmap.fromImage(image))
				ui.lcdNumber.display(rep)
				display("dumbbell_down.jpg", "dumbbell_up.jpg", per)

		# YOGA guide in ANALYST
		elif cp == 3:
			img, check, dem, yoga_image = yoga.run(600, 450, 30)  # z is the estimated time
			image = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
			if cp == 3:
				# Display the image on the view label frame
				ui.view.setPixmap(QtGui.QPixmap.fromImage(image))
				ui.information_2.setVisible(check)  # Displays a "green tick" image when used
				ui.timeLabel.setText("00:" + str(int(dem / 10)) + str(dem % 10))

				if yoga_image == 1:
					image_path = "CPENT-master\CPENT-master\images\1.jpg"  # path to your image file
					image_profile = QtGui.QImage(image_path)  # QImage object
					image_profile = image_profile.scaled(261, 241, aspectRatioMode=QtCore.Qt.IgnoreAspectRatio,
														 transformMode=QtCore.Qt.SmoothTransformation)  # To scale image for example and keep its Aspect Ration
					ui.information.setPixmap(QtGui.QPixmap.fromImage(image_profile))
				elif yoga_image == 2:
					image_path = "CPENT-master\CPENT-master\images\treePose.jpg"  # path to your image file
					image_profile = QtGui.QImage(image_path)  # QImage object
					image_profile = image_profile.scaled(261, 241, aspectRatioMode=QtCore.Qt.IgnoreAspectRatio,
														 transformMode=QtCore.Qt.SmoothTransformation)  # To scale image for example and keep its Aspect Ration
					ui.information.setPixmap(QtGui.QPixmap.fromImage(image_profile))
				elif yoga_image == 3:
					image_path = "CPENT-master\CPENT-master\images\tam-giác.jpg"  # path to your image file
					image_profile = QtGui.QImage(image_path)  # QImage object
					image_profile = image_profile.scaled(261, 241, aspectRatioMode=QtCore.Qt.IgnoreAspectRatio,
														 transformMode=QtCore.Qt.SmoothTransformation)  # To scale image for example and keep its Aspect Ration
					ui.information.setPixmap(QtGui.QPixmap.fromImage(image_profile))

				#SOUND WHEN COMPLETED
				elif yoga_image == 4:
					image_path = "CPENT-master\imagesfinish_yoga.jpg"  # path to your image file
					image_profile = QtGui.QImage(image_path)  # QImage object
					image_profile = image_profile.scaled(261, 241, aspectRatioMode=QtCore.Qt.IgnoreAspectRatio,
														 transformMode=QtCore.Qt.SmoothTransformation)  # To scale image for example and keep its Aspect Ration
					ui.information.setPixmap(QtGui.QPixmap.fromImage(image_profile))


					if check2 == True:
						playS("sound\\hoanthanh.wav",0)
						playS("sound\\task_beat.wav", 1)
						check2 = False
				# ui.lcdNumber.display(rep)
				# display("dumbbell_down.jpg", "dumbbell_up.jpg", per)

		# cardio
		elif cp == 4:
			img = yoga.cardio(600, 450)  # z is the estimated time
			image = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
			if cp == 4:
				# Show your image in the view label frame
				ui.view.setPixmap(QtGui.QPixmap.fromImage(image))
				if (tt.phut < 2):  # Control 2 taps in cardio
					display_cardio("H" + str(tt.phut + 1) + ".png", "breaktime.png", tt.giay, 40)
					# ui.information_2.setVisible(check)  # Displays a "green tick" image when used
					ui.timeLabel.setText(str(int(tt.phut / 10)) + str(tt.phut % 10) + ":" +
										 str(int(tt.giay / 10)) + str(tt.giay % 10))

					if (tt.phut < 1 and tt.giay >= 55 and check2 == True):
						#print("chapter")
						playS1("sound\\readygo.mp3")
						check2 = False

				# do not cardio

				elif (tt.phut == 2 and phut_tt == False):
					rep += 1
					phut_tt = True
					ui.timeLabel.setText(str(int(tt.phut / 10)) + str(tt.phut % 10) + ":" +
										 str(int(tt.giay / 10)) + str(tt.giay % 10))

					playS("sound\\task_beat.wav", 1)
					playS1("sound\\hoanthanh.mp3")
					ui.view.setStyleSheet("background-color: rgb(157, 157, 157);")
					ui.view.setText(" ")
					ui.information.setStyleSheet("background-color: rgb(157, 157, 157);")
					ui.information.setText(" ")
					ui.lcdNumber.display(rep)


# SOUND
def h_playS(a, b):  # b is for looping    #0 is 1 time, 1 is many time

	# playsound.playsound(a)
	winsound.PlaySound(a, winsound.SND_LOOP + (winsound.SND_ASYNC & b))


def playS(a, b):
	s = threading.Thread(target=h_playS, args=(a, b))
	s.start()


def h_playS1(a):  # b is for looping    #0 la 1 lan, 1 la nhieu la

	playsound.playsound(a)


def playS1(a):
	s = threading.Thread(target=h_playS1, args=(a,))
	s.start()


mainUi()
t = threading.Thread(target=main)
t.start()

sys.exit(app.exec_())
