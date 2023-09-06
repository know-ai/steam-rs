from .preprocessing import Preprocessing
from .scaler import Scaler
from .fit import Fit
from .evaluation import Eval

class MLO:
    """Documentation here
    """


    def __init__(self):
        
        self.scaler = Scaler()
        self.preprocessing = Preprocessing()
        self.fit = Fit()
        self.eval = Eval()

    def run(self):
        """Documentation here
        """
        pass