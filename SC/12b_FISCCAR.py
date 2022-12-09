
#pip install -U scikit-fuzzy
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

distance = ctrl.Antecedent(np.arange(0, 11, 1), 'distance')
speed = ctrl.Antecedent(np.arange(0, 11, 1), 'speed')
action = ctrl.Consequent(np.arange(0, 26, 1), 'action')

# Auto-membership function population is possible with .automf(3, 5, or 7)
distance.automf(3)
speed.automf(3)

# Custom membership functions can be built interactively with a familiar, Pythonic API
action['slow'] = fuzz.trimf(action.universe, [0, 5, 10])
action['medium'] = fuzz.trimf(action.universe, [2.5, 7.5, 10])
action['fast'] = fuzz.trimf(action.universe, [5, 7.5, 10])
distance['average'].view()
speed.view()
action.view()

rule1 = ctrl.Rule(distance['far'] & speed['slow'], action['slow'])
rule2 = ctrl.Rule(distance['far'] & speed['fast'], action['medium'])
rule3 = ctrl.Rule(distance['near'] | speed['fast'], action['fast'])
rule1.view()

crossing_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
crossing = ctrl.ControlSystemSimulation(crossing_ctrl)
crossing.input['distance'] = 2
crossing.input['speed'] = 7

# Crunch the numbers
crossing.compute()
print(crossing.output['action'])
action.view(sim=crossing)
