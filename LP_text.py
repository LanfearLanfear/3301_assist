import statistics
import pandas as pd
import helper_functions as hpf


def read_csv_file() -> pd.DataFrame:
    df = pd.read_csv("readeasiertranscript2.csv", usecols=["word", "sections"])
    df.sections = df.sections - 1
    return df


def section_names() -> list[str]:
    return ["00-02-cross", "03-07-spirals", "08-14-branches", "15-22-mobius", "23-26-mayfly", "27-32-wing-tree",
            "33-39-cunfeiform", "40-55-spiral-branches", "54-55-jpg", "56-an-end", "57-parable"]


def create_statistics() -> None:
    df = read_csv_file()
    section_name = section_names()
    for index, section in enumerate(section_name):
        dx = df.loc[df.sections == index].reset_index(drop=True)
        write_statistics_to_file(dx=dx, section_name=section)


def write_statistics_to_file(section_name: str, dx: pd.DataFrame) -> None:
    num_words, text = get_words(dx)
    text_as_index, text_as_gematria, text_as_runes = hpf.convert_english_text(text)
    gp_values_text = hpf.gp_values(text_as_index)
    ioc = statistics.calculate_ioc(text_as_index)
    gp_sums = statistics.gp_sums(text_as_gematria)
    doublets, doublet_frequency = statistics.count_doublets(text_as_index)
    quadgrams = statistics.calculate_quadgram_score(text_as_index)
    num_letters = len(dx)

    with open(f"LP/{section_name}.txt", "w", encoding="utf-8") as f:
        f.write(f"Word count: {num_words}\n")
        f.write(f"Number of letters: {num_letters}\n")
        f.write(f"Text in indices: {text_as_index.tolist()}\n")
        f.write(f"Text in gematria english: {text_as_gematria}\n")
        f.write(f"Text in runes: {text_as_runes}\n")
        f.write(f"Text gp values: {gp_values_text.tolist()}\n")
        f.write(f"Text gp sums: {gp_sums}\n")
        f.write(f"Text total gp sums: {sum(gp_sums)}\n")
        f.write(f"Doublets: {doublets}\n")
        f.write(f"Doublet frequency: {doublet_frequency}%\n")
        f.write(f"IoC: {ioc}\n")
        f.write(f"Quadgram score: {quadgrams}")


def get_words(dx: pd.DataFrame) -> tuple[int, str]:
    dx["changed"] = dx["word"].shift(1, fill_value=dx["word"].head(1)) != dx["word"]
    words = list(dx.loc[dx["changed"], "word"])
    dx.drop(columns=["changed"], inplace=True)
    words.insert(0, dx.word[0])
    new_list = [x.replace(",", "").upper() for x in words]
    return len(new_list), ' '.join(new_list)
