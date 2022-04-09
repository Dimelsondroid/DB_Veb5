import sqlalchemy
from pprint import pprint

class DataBase:
    db = 'postgresql://'
    engine = sqlalchemy.create_engine(db)
    connection = engine.connect()

my_db = DataBase()

#Домашнее задание к лекции «Группировки, выборки из нескольких таблиц»
print("1 количество исполнителей в каждом жанре")
pprint(my_db.connection.execute(
    """
    SELECT genre_name, COUNT(performer_name) FROM Genres g
    JOIN GenreArtist ga ON g.id = ga.genre_id
    JOIN Artists a ON ga.artist_id = a.id
    GROUP BY g.id;
    """
).fetchall())

print("2 количество треков, вошедших в альбомы 2019-2020 годов")
pprint(my_db.connection.execute(
    """
    SELECT COUNT(track_name) FROM Albums a
    JOIN Tracks t ON a.id = t.album_id
    WHERE album_release_year IN (2019, 2020)
    """
).fetchall())

print("3 средняя продолжительность треков по каждому альбому")
pprint(my_db.connection.execute(
    """
    SELECT album_name, ROUND(AVG(duration), 2) FROM Albums a
    JOIN Tracks t ON a.id = t.album_id
    GROUP BY a.album_name
    ORDER BY AVG(duration) DESC;
    """
).fetchall())

print("4 все исполнители, которые не выпустили альбомы в 2020 году")
pprint(my_db.connection.execute(
    """
    SELECT DISTINCT performer_name pn FROM Artists ar
    JOIN ArtistAlbum aa ON ar.id = aa.artist_id
    JOIN Albums al ON aa.album_id = al.id
    WHERE album_release_year NOT IN (
    SELECT album_release_year FROM Albums
    WHERE album_release_year = 2020);
    """
).fetchall())

print("5 названия сборников, в которых присутствует конкретный исполнитель 'B.B.King'")
pprint(my_db.connection.execute(
    """
    SELECT collection_name cn FROM Collections c
    JOIN CollectionTrack ct ON c.id = ct.collection_id
    JOIN Tracks t ON ct.track_id = t.id
    JOIN Albums al ON t.album_id = al.id
    JOIN ArtistAlbum aa ON al.id = aa.album_id
    JOIN Artists ar ON aa.artist_id = ar.id
    WHERE performer_name LIKE 'B.B.King';
    """
).fetchall())

print("6 название альбомов, в которых присутствуют исполнители более 1 жанра")
pprint(my_db.connection.execute(
    """SELECT album_name, COUNT(g.id) FROM Artists ar
    JOIN GenreArtist ga ON ga.artist_id = ar.id
    JOIN Genres g ON g.id = ga.genre_id
    JOIN ArtistAlbum aa ON ar.id = aa.artist_id
    JOIN Albums al ON al.id = aa.album_id
    GROUP BY album_name
    HAVING COUNT(g.id) > 1
    ORDER BY COUNT(g.id)
    """
).fetchall())

print("7 наименование треков, которые не входят в сборники")
pprint(my_db.connection.execute(
    """
    SELECT track_name from Tracks t
    FULL JOIN CollectionTrack ct ON t.id = ct.track_id
    FULL JOIN Collections c ON ct.collection_id = c.id
    WHERE ct.id is NULL
    GROUP BY track_name;
    """
).fetchall())

print("8 исполнителя(-ей), написавшего самый короткий по продолжительности трек")
pprint(my_db.connection.execute(
    """
    SELECT performer_name, t.duration from Artists ar
    JOIN ArtistAlbum aa ON ar.id = aa.artist_id
    JOIN Albums al ON aa.album_id = al.id
    JOIN Tracks t ON al.id = t.album_id
    WHERE duration = (SELECT MIN(duration) from Tracks);
    """
).fetchall())

print("9 название альбомов, содержащих наименьшее количество треков")
pprint(my_db.connection.execute(
    """
    SELECT album_name, COUNT(track_name) FROM Albums al
    JOIN Tracks t ON al.id = t.album_id
    GROUP BY album_name
    HAVING COUNT(track_name) = (
    SELECT COUNT(track_name) FROM Albums al
    JOIN Tracks t ON al.id = t.album_id
    GROUP BY album_name
    ORDER BY COUNT(track_name)
    LIMIT 1)
    ;
    """
).fetchall())