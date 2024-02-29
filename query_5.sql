SELECT s.name_sb subject
FROM subjects s 
JOIN teachers t ON t.id_tc = s.fr_tc 
WHERE t.name_tc = "Ярослава Девдюк"