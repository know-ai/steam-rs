from unittest import TestLoader, TestSuite, TextTestRunner
from app.tests.test_helpers import TestHelpers
from app.tests.test_eda import TestEDA
from app.tests.test_etl import TestETL
from app.tests.test_mlo import TestMLO

def suite():
    r"""
    Documentation here
    """
    tests = list()
    suite = TestSuite()
    tests.append(TestLoader().loadTestsFromTestCase(TestHelpers))
    tests.append(TestLoader().loadTestsFromTestCase(TestEDA))
    tests.append(TestLoader().loadTestsFromTestCase(TestETL))
    tests.append(TestLoader().loadTestsFromTestCase(TestMLO))
    suite = TestSuite(tests)
    return suite

if __name__=='__main__':
    
    runner = TextTestRunner()
    runner.run(suite())