"""
fuocore.daemon.handlers.helper
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

良好的用文字展示一个对象

展示的时候需要注意以下几点：
1. 让 awk、grep 等 shell 工具容易处理

TODO: 让代码长得更好看
"""


def show_song(song, brief=False):
    artists = song.artists or []
    artists_name = ','.join([artist.name for artist in artists])
    if brief:
        s = '{song}\t#{title}-{artists_name}'.format(
            song=song,
            title=song.title,
            artists_name=artists_name)
        return s
    artists_id = ','.join([str(artist.identifier) for artist in artists])

    if song.album is not None:
        album_id = str(song.album.identifier)
        album_name = song.album.name
    else:
        album_id = None
        album_name = 'Unknown'
    msgs = (
        'provider     {}'.format(song.source),
        'identifier   {}'.format(song.identifier),
        'title        {}'.format(song.title),
        'duration     {}'.format(song.duration),
        'url          {}'.format(song.url),
        'artists      {}\t#{}'.format(artists_id, artists_name),
        'album        {}\t#{}'.format(album_id, album_name),
    )
    return '\n'.join(msgs)


def show_songs(songs):
    return '\n'.join([show_song(song, brief=True) for song in songs])


def show_artist(artist):
    msgs = [
        'provider      {}'.format(artist.source),
        'identifier    {}'.format(artist.identifier),
        'name          {}'.format(artist.name),
    ]
    if artist.songs:
        songs_header = ['songs::\n']
        songs = ['\t' + each for each in show_songs(artist.songs).split('\n')]
        msgs += songs_header
        msgs += songs
    return msgs


def show_album(album, brief=False):
    msgs = [
        'provider      {}'.format(album.source),
        'identifier    {}'.format(album.identifier),
        'name          {}'.format(album.name),
    ]
    if album.artists is not None:
        artists = album.artists
        artists_id = ','.join([str(artist.identifier) for artist in artists])
        artists_name = ','.join([artist.name for artist in artists])
        msgs_artists = ['artists       {}\t#{}'.format(artists_id, artists_name)]
        msgs += msgs_artists
    if not brief:
        msgs_songs_header = ['songs::\n']
        msgs_songs = ['\t' + each for each in show_songs(album.songs).split('\n')]
        msgs += msgs_songs_header
        msgs += msgs_songs
    return '\n'.join(msgs)
