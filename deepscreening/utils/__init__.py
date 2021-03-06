#coding: utf-8
import os
import warnings

UTILS_DIR_PATH  = os.path.dirname(os.path.abspath(__file__))
BASE_DIR_PATH   = os.path.dirname(UTILS_DIR_PATH)
PARAMS_DIR_PATH = os.path.join(BASE_DIR_PATH, "params")

try:
    from rdkit import Chem
    import pubchempy as pcp
    MOL_IMPORTABLE = True
except ImportError:
    MOL_IMPORTABLE = False
    warnings.warn("You can't import `rdkit`, or `pubchempy`. " + \
                  "Therefore, you couldn't import some source files.")

from . import generic_utils
from . import keras_utils
from . import params_utils
from . import training_utils

from .generic_utils import pad_string

from .keras_utils import arange_losses
from .keras_utils import arange_metrics
from .keras_utils import arange_optimizers

from .params_utils import load_params
from .params_utils import update_params

from .training_utils import smiles2onehot
from .training_utils import load_data
from .training_utils import arange_datasets
from .training_utils import arange_all_datasets

if MOL_IMPORTABLE:
    from . import mol_utils
    from .mol_utils import name2SMILES
    from .mol_utils import zincid2SMILES
    from .mol_utils import SMILES2QED
    from .mol_utils import SMILES2mol
    from .mol_utils import mol2SMILES
    from .mol_utils import canonicalizeSMILES
