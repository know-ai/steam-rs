from .eda import EDA
from .etl import ETL
from .mlo import MLO

# Init Resources
def init_app(app):

    from .eda.resources import init_app as init_eda
    from .etl.resources import init_app as init_etl
    from .mlo.resources import init_app as init_mlo

    init_eda()
    init_etl()
    init_mlo()
    
    return app
