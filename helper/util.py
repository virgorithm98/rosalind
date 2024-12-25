def extract_string_from_txt(file_path: str) -> str:
    with open(file_path, "r") as text:
        return text.read().strip()


def separate_two_dna_strings(file_path: str) -> tuple[str, str]:
    with open(file_path, "r") as text:
        string_a, string_b = text.read().split("\n")

    return string_a.strip(), string_b.strip()


def extract_genotype_number_pair(file_path: str) -> dict[str, int]:
    with open(file_path, "r") as text:
        return {key : int(value) for key, value in [data.split(":") for data in text.read().split(" ")]}