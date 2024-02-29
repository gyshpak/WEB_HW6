SELECT st.name_st student, g.number_gr 
FROM groups g
JOIN students st ON g.fr_st = st.id_st
WHERE g.number_gr  = (SELECT g2.number_gr FROM groups g2 ORDER BY RANDOM() LIMIT 1)