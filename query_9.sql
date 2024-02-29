SELECT st.name_st student, sub.name_sb subject
FROM students st
JOIN assessment_subj as1 ON as1.fr_st = st.id_st 
JOIN subjects sub ON as1.fr_sb = sub.id_sb 
WHERE st.id_st = (SELECT st2.id_st FROM students st2 ORDER BY RANDOM() LIMIT 1)
GROUP BY sub.id_sb 