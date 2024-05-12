import os
import regex as re
from utils import constants, file_manipulation
from utils.logging import log_error

match_mappings = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}
word_patterns = "(one|two|three|four|five|six|seven|eight|nine|[1-9])"

def process_calibration_line(line):
    matches = re.findall(word_patterns, line, overlapped=True)
    return int(match_mappings[matches[0]] + match_mappings[matches[-1]])

def process_calibration(calibration):
    file_input = file_manipulation.get_file(os.path.join(constants.CALIBRATIONS_PATH, calibration))
    result = map(process_calibration_line, file_input)
    result = filter(lambda x: x is not None, result)
    result = sum(result)
    file_input.close()
    return result

if __name__ == "__main__":
    try:
        calibration_names = os.listdir(constants.CALIBRATIONS_PATH)
        calibration = None
        while True:
            calibration = input(f"Enter calibration file to process. Test calibrations are: \n{calibration_names}\nQ then Return key to quit.\n")
            if calibration in calibration_names:
                result = process_calibration(calibration)
                print(f"Result: {result}\n")
            elif calibration == 'q' or calibration == 'Q':
                break
            else:
                print("Invalid calibration name.")
    except Exception as e:
        log_error()