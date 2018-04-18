import unittest
import pandas as pd
from homework3 import create_dataframe

# Define a class in which the tests will run
class TestCreateDataframe(unittest.TestCase):
    #Testcase to check if the correct exception is raised for invalid file path
    def test_invalid_path(self):
        try:
            self.assertRaises(ValueError,create_dataframe,'test/class.db')
        except Exception as e:
            self.fail("Unexpected Exception Raised")
    
    #Testcase to check if the function returns a dataframe with the right columns
    def test_columns(self):
        dframe = create_dataframe('class.db')
        self.assertEqual(set(dframe.columns),{'category_id', 'language', 'video_id'})
        
    #Testcase to check if the video_id, language and category_id together is a key in the dataframe
    def test_key(self):
        dframe = create_dataframe('class.db')
        self.assertEqual(len(dframe),(dframe['video_id'].apply(str) + dframe['language'] + dframe['category_id'].apply(str)).nunique())
    
    #Testcase to check if the dataframe has 35950 rows
    def test_rowcount(self):
        dframe = create_dataframe('class.db')
        self.assertEqual(len(dframe),35950)

suite = unittest.TestLoader().loadTestsFromTestCase(TestCreateDataframe)
_ = unittest.TextTestRunner().run(suite)
