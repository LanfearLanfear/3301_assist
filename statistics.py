import numpy as np
import pandas as pd
import helper_functions as hpf


def count_words(text: str) -> int:
    return len(text.split())


def calculate_ioc(input_array: np.ndarray) -> float:
    _, counts = np.unique(input_array, return_counts=True)
    ioc = 0

    for counted in counts:
        ioc += counted * (counted - 1)
    ioc = ioc / (len(input_array) * (len(input_array) - 1) / 29)

    return ioc


def count_doublets(input_array) -> tuple[np.ndarray, float]:
    number_of_doublets = np.sum(input_array[0:-1] == input_array[1::])
    return number_of_doublets, (number_of_doublets / (len(input_array) - 1) * 100)


def gp_sums(input_text) -> list[int]:
    gp_sums_list = []
    for word in input_text.split():
        gp_sums_list.append(hpf.gp_sum(word))
    return gp_sums_list


def calculate_quadgram_score(input_text: np.ndarray) -> np.ndarray:
    len_text = len(input_text)
    probabilities = read_data_from_file("new_quadgrams.txt")
    indices = np.array(
        [input_text[0:len_text - 3] * 24389, input_text[1:len_text - 2] * 841, input_text[2:len_text - 1] * 29,
         input_text[3:len_text]])
    score = np.sum(probabilities[np.sum(indices, axis=0)])
    return score


def read_data_from_file(file_name: str) -> np.ndarray:
    df = pd.read_csv("new_quadgrams.txt", sep=',', header=None, usecols=[4])
    return df.to_numpy().flatten()
