SELECT std.name_st as student, AVG(ass.assessment) as max_sred_assessment
FROM students std
JOIN assessment_subj ass ON std.id_st = ass.fr_st
GROUP BY ass.fr_st 
order by max_sred_assessment
DESC
LIMIT 5