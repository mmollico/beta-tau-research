# Beta/Tau Analysis 
#
# This program is designed to gather and analyze data from various types of data files produced by software owned and operated by the Western University Meteor Physics Group. This data is then used for analysis of simultaeneous radar and video meteors with emphasis on determining the ratio beta/tau.
#
# Authour: Michael Molliconi
# Date Created: June, 2017

import numpy as np
import matplotlib.pyplot as plt

###
######################### Main Program Start ##################################
###

file_name = 'state.met'

# Parse state file for frame # with radar tags

with open(file_name, 'r') as f:
	for line in f:
		# Get theta and phi from the [29] tag
		if 'type interf text' in line:
			current = line.split()
			theta_29 = current[27]
			phi_29 = current[29]
			print(theta_29, phi_29)

	# Set an initial large min dist between 29 flag and meteor
	min_dist = 10000000;

	for line in f:
		# Loop through the state file and get theta and phi from the current line and compare with [29] tag
		if 'site 4 fr' in line:
			current = line.split()
			theta = current[27]
			phi = current[29]

			# transform theta into declination
			delta_1 = np.pi()/2 - theta
			delta_2 = np.pi()/2 - theta_29

			# Calculate angular distance between the two points
			ang_dist = np.sec(sin(delta_1)*sin(delta_2) + np.cos(delta_1)*np.cos(delta_2)*cos(phi - phi_29))

			# Store the new minimum distance
			if (min_dist < ang_dist):
				fr_29 = line.split() # store data from that line
				min_dist = ang_dist

	# Store the magnitude at the specular point (29)
	mag_tavis_29 = fr_29[27]
	mag_err_tavis_29 = fr_29[29]

	for line in f:
		# Get theta and phi from the [time] tag
		if 'type echotime text' in line:
			current = line.split()
			theta_time = current[27]
			phi_time = current[29]
			print(theta_time, phi_time)

	# Set an initial large min dist between time flag and meteor
	min_dist = 10000000;			

	for line in f:
		# Loop through the state file and get theta and phi from the current line and compare with [time] tag
		if 'site 4 fr' in line:
			current = line.split()
			theta = current[27]
			phi = current[29]

			# transform theta into declination
			delta_1 = np.pi()/2 - theta
			delta_2 = np.pi()/2 - theta_time

			# Calculate angular distance between the two points
			ang_dist = np.sec(sin(delta_1)*sin(delta_2) + np.cos(delta_1)*np.cos(delta_2)*cos(phi - phi_29))

			# Store the new minimum distance
			if (min_dist < ang_dist):
				fr_time = line.split() # store data from that line
				min_dist = ang_dist

	# Store the magnitude at the specular point (time)
	mag_tavis_time = fr_time[27]
	mag_err_tavis_time = fr_time[29]






			


