# Write your MySQL query statement below

(SELECT u.name AS results FROM Users u, MovieRating r WHERE u.user_id = r.user_id Group By r.user_id ORDER BY COUNT(r.user_id) DESC, u.name LIMIT 1)
UNION ALL
(SELECT m.title AS results FROM Movies m, MovieRating r WHERE m.movie_id = r.movie_id AND r.created_at LIKE "2020-02-%" Group By r.movie_id ORDER BY AVG(r.rating) DESC, m.title LIMIT 1);