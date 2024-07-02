#!/bin/bash

dir1="$1"
dir2="$2"

[[ -d "$dir2/Media/Images" ]] || mkdir -p "$dir2/Media/Images"
[[ -d "$dir2/Documents" ]] || mkdir -p "$dir2/Documents"
[[ -d "$dir2/Others" ]] || mkdir -p "$dir2/Others"
[[ -d "$dir2/Media/Videos" ]] || mkdir -p "$dir2/Media/Videos"
[[ -d "$dir2/Media/Gifs" ]] || mkdir -p "$dir2/Media/Gifs"
[[ -d "$dir2/Applications" ]] || mkdir -p "$dir2/Applications"
[[ -d "$dir2/Torrents" ]] || mkdir -p "$dir2/Torrents"
[[ -d "$dir2/Media/Music" ]] || mkdir -p "$dir2/Media/Music"
[[ -d "$dir2/Documents/Text" ]] || mkdir -p "$dir2/Documents/Text"

find "$dir1" -type f -exec bash -c '
    dir2="$1"
    case "$0" in
        *.jpg|*.png|*.webp|*.jpeg|*.bmp|*.tiff|*.svg|*.raw|*.jpeg) mv "$0" "$dir2/Media/Images/" ;;
        *.gif) mv "$0" "$dir2/Media/Gifs/" ;;
        *.AppImage|*.exe|*.sh|*.dmg|*.deb|*.rpm|*.msi|*.pkg|*.zip|*.tar|*.tar.gz|*.tar.bz2) mv "$0" "$dir2/Applications/" ;;
        *.torrent) mv "$0" "$dir2/Torrents/" ;;
        *.text|*.md|*.html) mv "$0" "$dir2/Documents/Text/" ;;
        *.pdf|*.doc|*.docx|*.odt|*.epub|*.rtf) mv "$0" "$dir2/Documents/" ;;
        *.mp4|*.mov|*.mkv|*.avi|*.mpeg) mv "$0" "$dir2/Media/Videos/" ;;
        *.mp3|*.ogg|*.aac|*.wav|*.flac|*.ape|*.aiff|*.pcm|*.opus) mv "$0" "$dir2/Media/Music/" ;;
        *) mv "$0" "$dir2/Others/" ;;
    esac
' {} "$dir2" \;

echo "Complete!"
