from includes.measurement import Measurement as M
from includes.equation import Equation as Eq

from includes.flm.flm import FLM

from includes.chemistry.element import Element as E
from includes.chemistry.compound import Compound as C
from includes.chemistry.chemicalequation import ChemicalEquation as Ceq

from includes.chemistry.chemical_equation_solver import chemical_equation_solver as ceqs
from includes.chemistry.stoichiometry import stoichiometry as stoich
from includes.chemistry.limiting_reagent import limiting_reagent as lr

Eq.setLatexPrint(True)
Ceq.setLatexPrint(True)
FLM.setLatexPrint(True)