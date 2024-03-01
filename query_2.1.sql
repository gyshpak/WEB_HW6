SELECT std.name_st as student, AVG(ass.assessment) as max_sred_assessment, sub.name_sb as subject
FROM students std
JOIN assessment_subj ass ON std.id_st = ass.fr_st
JOIN subjects sub ON ass.fr_sb = sub.id_sb 
WHERE sub.id_sb = (SELECT sub2.id_sb FROM subjects sub2 ORDER BY RANDOM() LIMIT 1)
GROUP BY ass.fr_st , ass.fr_sb
ORDER BY max_sred_assessment
DESC 
LIMIT 1