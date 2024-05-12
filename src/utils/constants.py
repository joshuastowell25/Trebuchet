import os


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__)).split('Trebuchet')[0] + 'Trebuchet' # execution location agnostic project root
CALIBRATIONS_PATH = os.path.join(PROJECT_ROOT, 'test', 'input')
OUTPUTS_PATH = os.path.join(PROJECT_ROOT, 'test', 'output')