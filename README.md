# ytSubs
Download youtube subtitles passing an url, receive a document with ONLY the subtitles and nothing else.

## Requirements
`pip install youtube_dl`

## Usage
`$ python vtt2text.py $url`

## TODO:
- ### Python
  - [x] Download subs with youtube-dl
  - [x] Remove tags <> for timestamps, empty lines, repetead lines
  - [ ] Automate choice between classic and auto-generated subtitles 
- ### Shell
  - [ ] Pass the result to a word processor:
  `pandoc -o output.docx input.txt`
