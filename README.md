# RhythmQ JSON Format

RhythmQ accepts custom packs in RhythmQ JSON format, a format designed to accomodate most, if not all, rhythm games. Support for this format is experimental, and an upcoming patch to the RhythmQ extension will allow the extension to make use of features such as difficulty names.

When importing, please make sure your data is in the following format:
```json
[{
"songName":"",
"songArtist":"",
"bpm":999,
"hasDifficulties":true,
"hasDiffNumbers":true,
"difficulties": [{
    "diffName":"Single",
    "diffNumber":999,
    "players":1,
    "double":false
  }]
}]
```

BPM and difficulty numbers can be floats, but RhythmQ does not currently accept BPM ranges. Please average your BPM before adding it to the format.


# Parsers

A selection of parsers are available in this repository to both ease importing, and to provide a base on which you can build a parser for your own rhythm games.

## sm_song_parse.py
Adapted from [concubidated's](https://github.com/concubidated) Stepmania parser, placing this script in your songs directory and running it will allow it to index all packs and songs in your Stepmania installation, and output them into a single RhythmQ-compatible JSON file to be imported. Please note that this script requires the python `magic` library to be installed.
