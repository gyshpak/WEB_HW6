SELECT t.name_tc teacher, st.name_st student, AVG(as1.assessment) "middle assessment" 
FROM teachers t
JOIN subjects sub ON sub.fr_tc = t.id_tc 
JOIN assessment_subj as1 ON as1.fr_sb  = sub.id_sb
JOIN students st ON as1.fr_st = st.id_st 
WHERE st.id_st = (SELECT st2.id_st FROM students st2 ORDER BY RANDOM() LIMIT 1)
AND t.id_tc  = (SELECT t2.id_tc FROM teachers t2 ORDER BY RANDOM() LIMIT 1)