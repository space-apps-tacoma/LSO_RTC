import importlib.util
import json
import unittest
# # #
# https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path
spec = importlib.util.spec_from_file_location("module.name", "../server/create.py")
create = importlib.util.module_from_spec(spec)                                              
spec.loader.exec_module(create)
# # #

# tests

class InceptionTests(unittest.TestCase):

    def test_verify_mission_template_available(self):
        template_path = '../templates/mission-template.json'
        test_mission = create.mission.default(template_path).get("mission")
        self.assertEqual(test_mission["id"] , "unique number assigned by agency" )  

        
# test runner        
if __name__ == '__main__':
    unittest.main()        
