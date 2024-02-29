SELECT number_gr, AVG(ass.assessment) as sred_assessment, sub.name_sb as subject
FROM assessment_subj ass
JOIN students std ON ass.fr_st = std.id_st
JOIN groups gr ON std.id_st = gr.fr_st  
JOIN subjects sub ON ass.fr_sb = sub.id_sb 
WHERE sub.name_sb = "астрономія"
GROUP BY gr.number_gr 