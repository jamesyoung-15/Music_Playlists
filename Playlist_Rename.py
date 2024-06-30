import re
import os

def edit_playlists(playlist_names: list):
    """ 
    Takes a list of m3u playlist filenames, where the content uses absolute paths of music files.
    Replaces the absolute paths with 2 versions of relative paths and writes them to two different directories (RelativePath and Jellyfin).

    Eg:
    Original -  file:///home/jamesyoung/Music/MusicLibrary/Green%20Day/American%20Idiot/03%20Holiday.mp3
    RelativePath - ../Green%20Day/American%20Idiot/03%20Holiday.mp3
    Jellyfin - ../MusicLibrary/Green%20Day/American%20Idiot/03%20Holiday.mp3
    """
    try:
        for playlist in playlist_names:
            # Read the original playlist file
            with open(original_playlist + "/" + playlist) as f:
                data = f.read()

            # Find all matches and replace
            regex_relative = r"file(.*?)Music"
            regex_jellyfin = r"file(.*?)MusicLibrary"
            replacement_relative = re.sub(regex_relative,"..", data)
            replacement_jellyfin = re.sub(regex_jellyfin,"..", data)

            # write the files for Android
            with open("Playlists_RelativePath/"+playlist, 'w') as f:
                f.write(replacement_relative)

            # write the files for Jellyfin
            with open("Playlists_Jellyfin/"+playlist, 'w') as f:
                f.write(replacement_jellyfin)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    # directory paths
    original_playlist = "./Playlists"
    relative_playlist = "./Playlists_RelativePath"
    jellyfin_playlist = "./Playlists_Jellyfin"

    # get original playlist files
    playlists = os.listdir(original_playlist)
    edit_playlists(playlists)