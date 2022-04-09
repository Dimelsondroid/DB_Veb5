create table if not exists Genres (
		id serial primary key,
		genre_name varchar(40) not null
		);

create table if not exists Artists (
		id serial primary key,
		performer_name varchar(40) not null,
		alias varchar(60) not null
		);

create table if not exists Albums (
		id serial primary key,
		album_name varchar(40) not null,
		album_release_year integer check(album_release_year > 1900)
		);

create table if not exists Collections (
		id serial primary key,
		collection_name varchar(40) not null,
		collection_release_year integer check(collection_release_year > 1900)
		);

create table if not exists Tracks (
		id serial primary key,
		track_name varchar(80) not null,
		duration integer check(duration > 0),
		album_id integer references Albums (id)
		);
		
create table if not exists 	GenreArtist (
		id serial primary key,
		genre_id integer not null references Genres (id),
		artist_id integer not null references Artists (id)
		);
		
create table if not exists 	ArtistAlbum (
		id serial primary key,
		album_id integer not null references Albums (id),
		artist_id integer not null references Artists (id)
		);

create table if not exists 	CollectionTrack (
		id serial primary key,
		collection_id integer not null references Collections (id),
		track_id integer not null references Tracks (id)
		);
		
insert into Genres (genre_name) values 
('Pop'), 
('Rock'), 
('Folk'), 
('Jazz'),
('Techno');
insert into Artists (performer_name, alias) values 
('Jenifer Lopez', 'J-Lo'), 
('Mike Oldfield', 'Mikey'), 
('Petr Mamonov', 'Petunya'), 
('Marshal Bruce Mathers', 'Eminem'),
('Sting', 'St'), 
('Jethro Tull', 'J-To'), 
('Stiven Tyler', 'Stivie'), 
('B.B.King', 'BiBi');
insert into Albums (album_name, album_release_year) values 
('Shadows', 2005), 
('Down Under', 2010), 
('Zero Gravity', 2017), 
('Mastermind', 1999),
('Twin Cinema', 2018), 
('Transformer', 1972), 
('Rumours', 1977), 
('Discipline', 1981);
insert into Collections (collection_name, collection_release_year) values 
('Best of', 2009), 
('Jazzy', 2012), 
('Breaking Rules', 2019), 
('Poppity', 2018),
('Good morning v4', 2017), 
('2010 hits', 2011), 
('Golden hits 80th', 2005), 
('Best remix', 2015);
insert into Tracks (track_name, duration, album_id) values 
('Aba Daba Honeymoon', 321, 3), 
('Adoring You', 245, 4), 
('Ain"t We Got Fun', 167, 5), 
('Any Old Time At All', 189, 6),
('Bambalina', 201, 7), 
('Beautiful Ohio', 267, 8), 
('Birth of Passion', 373, 1), 
('Camptown Races', 199, 2),
('Party Non Stop', 199 , 3),
('Very Green Light', 232, 4),
('Притяжение', 177, 5),
('Shine On', 252, 6),
('opacities', 250, 7),
('Goodbye Tristam', 271, 8),
('Piano', 190, 1),
('By My Side', 251, 2);
insert into GenreArtist  (genre_id, artist_id) values 
(1, 2), (1, 1), (1, 7),
(2, 3), (2, 8),
(3, 4), (3, 1),
(4, 5), (4, 7),
(5, 6), (5, 8);
insert into ArtistAlbum  (album_id, artist_id) values 
(1, 2), (1, 1),
(2, 3), 
(3, 4), (3, 3),
(4, 5),
(5, 6), (5, 5),
(6, 7), 
(7, 8), (7, 7),
(8, 1);
insert into CollectionTrack (collection_id , track_id) values 
(1, 2), (1, 3), (1, 4), (1, 5),(1, 6), 
(2, 7), (2, 8), (2, 9), (2, 10), 
(3, 11), (3, 12), (3, 13),(3, 14), 
(4, 15), (4, 16), (4, 1),(4, 2), 
(5, 3), (5, 4), (5, 5),(5, 6), 
(6, 7), (6, 8), (6, 9), (6, 10), 
(7, 11), (7, 12), (7, 13),(7, 14), 
(8, 15), (8, 16), (8, 1);