import statistics
import helper_functions as hpf


def return_english_text() -> str:
    text = ('HALF FINISH STOOL INJURY CLERK BEARD BUNDLE SOIL STREAM FROWN CRUTCH FAULT ACHIEVEMENT FRAGRANT BRIDGE '
            'STRENGTH COMBINATION GOLF SPEED SMALL PLEDGE COOPERATION HILL MANAGEMENT CULTURE SLEEVE CONCERT CIRCLE '
            'RUMOR AUTOMATIC SMOOTH FAREWELL FUNCTION EXPERIMENT TROPICAL DESPISE MONARCH HEAVEN PUSH PARTICIPATE '
            'PATIENCE SKIP TIMETABLE GRAZE BRUSH HANDY SICK LINGER DIFFICULT FILM QUESTION')
    return text


def create_statistics() -> None:
    text = return_english_text()
    num_words = statistics.count_words(text)
    text_as_index, text_as_gematria, text_as_runes = hpf.convert_english_text(text)
    gp_values_text = hpf.gp_values(text_as_index)
    ioc = statistics.calculate_ioc(text_as_index)
    gp_sums = statistics.gp_sums(text_as_gematria)
    doublets, doublet_frequency = statistics.count_doublets(text_as_index)
    quadgrams = statistics.calculate_quadgram_score(text_as_index)
    num_letters = len(text_as_index)

    with open("english_text/statistics.txt", "w", encoding="utf-8") as f:
        f.write(f"English text: {text}\n")
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
