"""
Michael Pacheco

Time Complexity: O(1) Since we only work with constants.
"""
def calculate_expected_offspring(no_of_offspring, probability_of_each_genotype, no_of_couple):
   exp_offspring_w_dominant_phenotype = 0
   for i in range(0,5):
       exp_offspring_w_dominant_phenotype += \
       no_of_offspring*probability_of_each_genotype[i]*no_of_couple[i]

   return exp_offspring_w_dominant_phenotype


no_of_offspring = 2
probability_of_each_genotype = [1,1,1,.75,.5,0]
no_of_couples = [17559, 16265, 18355, 19866, 18270, 17692]

print(calculate_expected_offspring(no_of_offspring,probability_of_each_genotype, no_of_couples))