import sys, os
import mimetypes
import magic
import hashlib
import json

class Chart:
    def __init__(self, chart_type, difficulty, level, author, double, players = 1):
        self.chart_type = chart_type
        self.diffName = difficulty
        self.author = author
        self.diffNumber = level
        self.double = double
        self.players = players

class Song:
    def __init__(self, pack, title, subtitle, artist, credit, bpm, charts, hash):
        self.pack = pack
        self.songName = title
        self.subtitle = subtitle
        self.songArtist = artist
        self.credit = credit
        self.bpm = bpm
        self.difficulties = charts
        self.hash = hash

songs = []

# change this path to your actual stepmania song directory if you wish to run this file somewhere else
songs_path = "."

for pack in os.listdir(songs_path):
    pack_dir = os.path.join(songs_path,pack)
    if os.path.isdir(pack_dir):
        for song in os.listdir(pack_dir):
            song_dir = os.path.join(songs_path,pack_dir,song)
            if os.path.isdir(song_dir):
                for sm in os.listdir(song_dir):

                    if (sm.endswith(".sm")) or (sm.endswith(".ssc")):
                        charts = []
                        path = os.path.join(song_dir,sm)
                        hash = hashlib.sha1(open(path, 'rb').read()).hexdigest()
                        type = magic.Magic(mime=True).from_file(path)
                        # Ran into improperly encoded SM files
                        if "unknown-8bit" not in type:
                            with open(path, "r") as simfile:
                                if "iso-8859-1" in type:
                                    simfile = open(path, encoding='iso-8859-1')
                                for line in simfile:
                                    if "#ARTIST:" in line:
                                        artist = line.rstrip().split(":")[1][:-1]
                                    if "#TITLE:" in line:
                                        title = line.rstrip().split(":")[1][:-1]
                                    if "#CREDIT:" in line:
                                        credit = line.rstrip().split(":")[1][:-1]
                                    if "#SUBTITLE:" in line:
                                        subtitle = line.rstrip().split(":")[1][:-1]
                                    if "#BPMS:" in line:
                                        bpm = float(line.rstrip().split(":")[1].split(",")[0].split("=")[1].split(";")[0])
                                    if "dance-single:" in line:
                                        author = simfile.readline().lstrip().split(':')[0]
                                        difficulty = simfile.readline().lstrip().split(':')[0]
                                        level = int(simfile.readline().lstrip().split(':')[0])
                                        double = False
                                        charts.append(Chart("dance-single", difficulty, level, author, double, 1))
                                    if "dance-double:" in line:
                                        author = simfile.readline().lstrip().split(':')[0]
                                        difficulty = simfile.readline().lstrip().split(':')[0]
                                        level = int(simfile.readline().lstrip().split(':')[0])
                                        double = True
                                        charts.append(Chart("dance-double", difficulty, level, author, double, 1))
                            songs.append(Song(pack, title, subtitle, artist, credit, bpm, charts, hash))
                            break
#Pretty print
#output = json.dumps(songs, default=lambda x: x.__dict__, indent=4)
output = json.dumps(songs, default=lambda x: x.__dict__)
outfile = open("output.json", "w")
outfile.write(output)
outfile.close()
