import os
from re import sub
from utils import constants, file_manipulation
from utils.logging import log_error


def process_calibration_line(line):
    numbers_only = sub("[^0-9]", "", line)
    if numbers_only:
        return int(numbers_only[0] + numbers_only[-1])
    else:
        return None

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
            calibration = input(f"Enter calibration file to process. Test calibrations are: \n{calibration_names}\nQ to quit.\n")
            if calibration in calibration_names:
                result = process_calibration(calibration)
                print(f"Result: {result}\n")
            elif calibration == 'q' or calibration == 'Q':
                break
            else:
                print("Invalid calibration name.")

    except Exception as e:
        log_error()