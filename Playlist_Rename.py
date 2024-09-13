import re
import os

def edit_playlists(playlist_names: list):
    """ 
    Takes a list of m3u playlist filenames, where the content uses absolute paths of music files.
    Copies and replaces the absolute paths with relative paths and writes them to directory (Playlist_RelativePath).

    Eg:
    Original -  file:///home/jamesyoung/Music/MusicLibrary/Green%20Day/American%20Idiot/03%20Holiday.mp3
    RelativePath - ../Green%20Day/American%20Idiot/03%20Holiday.mp3
    """
    try:
        for playlist in playlist_names:
            # Read the original playlist file
            with open(original_playlist + "/" + playlist) as f:
                data = f.read()

            # Find all matches and replace
            regex_relative = r"file(.*?)Music"
            replacement_relative = re.sub(regex_relative,"..", data)

            # write the files
            with open("Playlists_RelativePath/"+playlist, 'w') as f:
                f.write(replacement_relative)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    # directory paths
    original_playlist = "./Playlists"
    relative_playlist = "./Playlists_RelativePath"

    # get original playlist files
    playlists = os.listdir(original_playlist)
    edit_playlists(playlists)
