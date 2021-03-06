import datetime

class Hurricane:
	def __init__(self, name, atcf_number, year):
		self.name = name
		self.atcf_number = atcf_number
		self.year = year

		self.data = []
		self.track = []

		self.start_time = None
		self.end_time = None
		self.max_wind = None
		self.min_pressure = None
		self.made_landfall = False
		self.landfall_count = 0

	def add_data_line(self, data_line):
		self.data.append(data_line)
		self.track.append(data_line.pos)

		if self.start_time == None or self.start_time > data_line.time:
			self.start_time = data_line.time
		if self.end_time == None or self.end_time < data_line.time:
			self.end_time = data_line.time
		if self.max_wind == None or self.max_wind < data_line.max_wind:
			self.max_wind = data_line.max_wind
		if self.min_pressure == None or self.min_pressure > data_line.min_pressure:
			self.min_pressure = data_line.min_pressure
		if data_line.event == "L":
			self.made_landfall = True
			self.landfall_count = self.landfall_count + 1

	def __str__(self):
		return "%s %d %d" % (self.name, self.atcf_number, self.year)

class DataLine:
	def __init__(self, row):
		self.year = int(row[0][0:4])
		self.month = int(row[0][4:6])
		self.day = int(row[0][6:8])

		self.hour = int(row[1][1:3])
		self.minute = int(row[1][3:5])

		self.time = datetime.datetime(self.year, self.month, self.day, self.hour, self.minute)

		self.event = row[2][1]
		self.system_status = row[3][1:]

		self.lat = float(row[4][:-1])
		if row[4][-1] == "S":
			self.lat = self.lat * -1
		self.long = float(row[5][:-1])
		if row[5][-1] == "W":
			self.long = self.long * -1
		self.pos = [self.long, self.lat]

		self.max_wind = int(row[6])
		self.min_pressure = int(row[7])

		# The order goes NE, SE, SW, NW
		self.wind_radii_ts = [
			int(row[8]),
			int(row[9]),
			int(row[10]),
			int(row[11])
		]
		self.wind_radii_storm = [
			int(row[12]),
			int(row[13]),
			int(row[14]),
			int(row[15])
		]
		self.wind_radii_hurricane = [
			int(row[16]),
			int(row[17]),
			int(row[18]),
			int(row[19])
		]