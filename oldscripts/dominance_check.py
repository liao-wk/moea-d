#!/opt/python/bin/python

import numpy as np

def remove_newly_dominated_solutions(EP, offspring, objective_sense='min'):
	"""
	Remove from EP any solutions that are dominated by the offspring.
	:param EP: External popluation, a list of efficient solutions.
	:param offspring: A new solution generated by the genetic operators.
	:param objective_sense: Whether we 'min' or 'max' the objective.
	"""
	filtered_EP = []
	for es in EP:
		es_dominated_by_offspring = False
		if objective_sense == 'min':
			if np.greater_equal(es.objective_val, offspring.objective_val).all() and not np.equal(es.objective_val, offspring.objective_val).all():
				es_dominated_by_offspring = True
		elif objective_sense == 'max':
			if np.less_equal(es.objective_val, offspring.objective_val) and not np.equal(es.objective_val, offspring.objective_val):
				es_dominated_by_offspring = True
		else:
			raise ValueError('Objective sense should be either "min" or "max".')
		if not es_dominated_by_offspring:
			filtered_EP.append(es)
	return filtered_EP

def add_if_not_dominated(offspring, EP, objective_sense='min'):
	"""
	Add offspring to EP if it is not dominated by any solution in EP.
	:param offspring: A new solution generated by the genetic operators.
	:param EP: External popluation, a list of efficient solutions.
	:param objective_sense: Whether we 'min' or 'max' the objective.
	"""
	offspring_dominated_by_EP = False
	for es in EP:
		if objective_sense == 'min':
			if np.less_equal(es.objective_val, offspring.objective_val).all() and not np.equal(es.objective_val, offspring.objective_val).all():
				offspring_dominated_by_EP = True
		elif objective_sense == 'max':
			if np.greater_equal(es.objective_val, offspring.objective_val).all() and not np.equal(es.objective_val, offspring.objective_val).all():
				offspring_dominated_by_EP = True
		else:
			raise ValueError('Objective sense should be either "min" or "max".')
	if not offspring_dominated_by_EP:
		EP.append(offspring)
	return EP

