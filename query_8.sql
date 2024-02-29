SELECT t.name_tc teacher, sub.name_sb subject, AVG(as1.assessment)
FROM assessment_subj as1 
JOIN subjects sub ON as1.fr_sb = sub.id_sb 
RIGHT JOIN teachers t ON sub.fr_tc = t.id_tc  
WHERE t.id_tc = (SELECT t2.id_tc FROM teachers t2 ORDER BY RANDOM() LIMIT 1)
GROUP BY sub.id_sb 