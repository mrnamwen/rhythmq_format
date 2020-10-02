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
