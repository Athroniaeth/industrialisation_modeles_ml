import pandas as pd
import time
import random


def generate_tonal_exams(exam_count: int, csv_filename: str, init_freq: int = 125) -> None:
    '''Generate a examen_count number of tonal exam and save it ti csv_filename
        INPUT:
            exam_count: number of exam desired
            csv_filemame: name of the csv where all the exam will be saved
            init_freq: starting frequency of tonal exam
        OUPUT:
            csv file named as csv_filename
    '''
    # Generate column headers
    headers = ["exam_" + str(init_freq * (2 ** i)) + '_Hz' for i in range(7)]
    headers_before = ["before_" + freq for freq in headers]
    headers_after = ["after_" + freq for freq in headers]
    columns = headers_before + headers_after

    # For each exam
    for i in range(exam_count):
        print(f'Exam {i + 1}')

        # Generate random threshold values before and after hearing aid fitting
        # Bigger loss on high frequency
        thresholds_before = [random.randint(0, 100) + j * 5 for j, _ in enumerate(headers)]
        # If bigger loss in high frequency,also better rehab
        thresholds_after = [random.randint(round(threshold / 3), threshold) - j for j, threshold in enumerate(thresholds_before)]

        exam_values = thresholds_before + thresholds_after
        new_row = pd.DataFrame(columns=columns, data=[exam_values])
        new_row.to_csv(csv_filename, mode='a', header=not i, index=False)

    print(f"Tonal exams have been saved to the file '{csv_filename}'.")


start = time.time()
# Number of exam desired
exam_count = 10000
# Name of output file
filename = "tonal_exams.csv"
generate_tonal_exams(exam_count, filename)
end = time.time()

print(f'Total time: {round(end - start, 3)}')
