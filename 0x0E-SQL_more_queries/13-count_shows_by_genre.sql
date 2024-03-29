-- Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- First column must be called genre
-- Second column must be called number_of_shows
-- Don’t display a genre that doesn’t have any shows linked
-- Results must be sorted in descending order by the number of shows linked


SELECT tv_shows.title as genre, count(tv_show_genres.genre_id) as number_of_shows
    FROM tv_shows
    LEFT JOIN tv_show_genres
    ON tv_shows.id=tv_show_genres.show_id
    WHERE tv_shows.id IS NULL
    OR Tv_show_genres.show_id IS NULL
    ORDER BY tv_shows.title, tv_show_genres.genre_id;
