print("Hello, GitHub Actions!")

import traceback
import parser
import scanner

def fuzz_stuff(function, arguments):
    try:
        function(*arguments)
    except Exception:
        print("Fuzzing {} with parameters {} threw an error".format(function.__name__, str(arguments)))
        print(traceback.format_exc())
        #print()
    
if __name__ == '__main__':
    keyMiner_inputs = [None, dict(), {"val":"stuff", "else":False, "what":None, True:"no"}, set(), [], ["heehoo", "not empty", False, None, r":)"], "string", 123, False, r"RAWSTRING", 0.231]
    for first in keyMiner_inputs:
        for second in keyMiner_inputs:
            fuzz_stuff(parser.keyMiner, [first, second]) # didn't actually throw any errors despite throwing a bunch at it
    
    getKeyRecursively_dict_inputs = [None, [], set(), 0.231, dict(), {"val":"stuff", "else":False, "what":None, True:"no"}]
    getKeyRecursively_list_inputs = [[], set(), (), False, None]
    getKeyRecursively_depth_inputs = [-1,0.239,0,2,10000,"false",True,None]
    for dict_input in getKeyRecursively_dict_inputs:
        for list_input in getKeyRecursively_list_inputs:
            for depth_input in getKeyRecursively_depth_inputs:
                fuzz_stuff(parser.getKeyRecursively, (dict_input, list_input, depth_input))
    
    update_json_path_inputs = [None, 0, 23912, 0.123, "String", [None], {"Example", "More"}, {"Something":"Else", "Also":"This"}, r"words", ["numbers", 0.231, 934284, -12]]
    for input in update_json_path_inputs:
        fuzz_stuff(parser.update_json_paths, [input])
    
    getSingleDict_inputs = [None, {"fool","as"}, ["you","are"], "StringText", {"something":"wicked", "this":"way", "rides":None, False:True, None:r"WEEE"}, 
                            [{"test":"something", "test.YAML.DOC.1":"else"}, {"test":"something else"}]]
    for input in getSingleDict_inputs:
        fuzz_stuff(parser.getSingleDict4MultiDocs, [input])
    
    getYAMLFiles_inputs = [None, "this_better_not_be_a_directory_i_swear", "././././././././././././././././././bandit_scanning", False, "scanner.py"]
    for input in getYAMLFiles_inputs:
        fuzz_stuff(scanner.getYAMLFiles, [input])
    
    getItemFromSecret_sec_dict = [None, ["stuff","things"], {"key":None}, "string", {"key":["some","keys","to","peruse"], "other_key":"stuff", "other_key":[213]}]
    getItemFromSecret_pos = [False, 0, -1, 12, slice(0, 2), "1"]
    for dict_input in getItemFromSecret_sec_dict:
        for pos_input in getItemFromSecret_pos:
            fuzz_stuff(scanner.getItemFromSecret, (dict_input, pos_input))