SELECT s.name_sb subject, t.name_tc teacher
FROM subjects s 
RIGHT JOIN teachers t ON t.id_tc = s.fr_tc 
WHERE t.name_tc = (SELECT t2.name_tc FROM teachers t2 ORDER BY RANDOM() LIMIT 1)