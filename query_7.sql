SELECT gr.number_gr "group", sub.name_sb subject, st.name_st student, as1.assessment
FROM assessment_subj as1 
JOIN subjects sub ON as1.fr_sb = sub.id_sb 
JOIN students st ON as1.fr_st = st.id_st
JOIN groups gr ON gr.fr_st = st.id_st 
WHERE gr.number_gr  = (SELECT g2.number_gr FROM groups g2 ORDER BY RANDOM() LIMIT 1)
AND sub.name_sb = (SELECT s2.name_sb FROM subjects s2 ORDER BY RANDOM() LIMIT 1)