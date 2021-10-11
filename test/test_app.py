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
        test_mission = create.mission.dictionary_from(template_path).get("mission")
        self.assertEqual(test_mission["id"] , "unique number assigned by agency" )  

    def test_verify_team_name_template_available(self):
        template_path = '../templates/team-name-template.json'
        names = create.mission.dictionary_from(template_path).get("names")
        name_help = names.get("unique_name_help")
        self.assertEqual(name_help["id"] , "unique team id number assigned by agency" )

    def test_verify_log_template_available(self):
        template_path = '../templates/log-template.json'
        log = create.mission.dictionary_from(template_path).get("log_template")
        self.assertEqual(log["unique_generated_sid_here"]["team_name"] , "team that the logger is on" )
        
# test runner        
if __name__ == '__main__':
    unittest.main()        
