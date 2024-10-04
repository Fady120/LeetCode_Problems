# Write your MySQL query statement below

SELECT requester_id AS id,
       (SELECT COUNT(*) FROM RequestAccepted WHERE id = accepter_id OR id = requester_id) AS num
FROM RequestAccepted
GROUP BY requester_id
UNION
SELECT accepter_id AS id,
       (SELECT COUNT(*) FROM RequestAccepted WHERE id = accepter_id OR id = requester_id) AS num
FROM RequestAccepted
GROUP BY accepter_id
ORDER BY num DESC
LIMIT 1;