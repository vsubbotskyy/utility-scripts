import glob, os, re, time, shutil

def get_image_file_names():
	files = glob.glob('**/*.jpg')
	return files


#just in case we'll need them in future)
available_drives = (re.findall(r"[A-Z]+:.*$",os.popen("mountvol /").read(),re.MULTILINE))


def sort_photos():
	images = get_image_file_names()
	for image in images:
		created = time.localtime(os.path.getctime(image))
		
		#we need a folder with current year name
		year_directory = './organized/' + str(created.tm_year)
		if not os.path.exists(year_directory):
			os.makedirs(year_directory)

		event_directory = str(created.tm_mon) + '.' + str(created.tm_mday)
		month_directory = year_directory + '/' + event_directory
		if not os.path.exists(month_directory):
			os.makedirs(month_directory)

		os.rename(image, month_directory + '/' + os.path.basename(image))

		print(image + ' moved to: ' + month_directory)


sort_photos()