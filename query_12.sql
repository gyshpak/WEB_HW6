SELECT as1.assessment assessment, as1.date_in, s.name_st, sub.name_sb, g.number_gr 
FROM assessment_subj as1
JOIN students s ON as1.fr_st = s.id_st 
JOIN subjects sub ON sub.id_sb = as1.fr_sb
JOIN groups g ON g.fr_st = s.id_st 
WHERE as1.date_in = (SELECT as2.date_in FROM assessment_subj as2 ORDER BY as2.date_in DESC LIMIT 1)
AND sub.id_sb = (SELECT sub2.id_sb FROM subjects sub2 ORDER BY RANDOM() LIMIT 1)
AND g.id_gr = (SELECT gr2.id_gr FROM groups gr2 ORDER BY RANDOM() LIMIT 1)