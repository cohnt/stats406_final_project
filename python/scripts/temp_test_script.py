import sys

import read_data
from visualization.track import *
from visualization.storm_lifetime import *

# hurricane_list = read_data.read_file("../data/hurdat2-1851-2018-051019.csv")
hurricane_list = read_data.read_file("../data/by_year/2000-2018.csv")
# hurricane_list = read_data.read_file("../data/by_year/1992.csv")
# hurricane_list = read_data.read_file("../data/by_year/2018.csv")

# track_list = [h.track for h in hurricane_list]
# plot_track_map(track_list[0])
# plot_tracks_map(track_list)

# plot_track_status(hurricane_list[0])
# plot_tracks_status(hurricane_list)

# plot_tracks_wind_speed(hurricane_list)
plot_tracks_wind_speed(hurricane_list, create_florida_map())

# plot_tracks_status(hurricane_list, create_florida_map())

# plot_lifetime_max_wind(hurricane_list[13])