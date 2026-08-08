from Utils.history import load_history


def get_statistics():

    history = load_history()

    total_hashes = len(history)

    file_hashes = sum(
        1 for item in history
        if item["record_type"] == "File"
    )

    text_hashes = sum(
        1 for item in history
        if item["record_type"] == "Text"
    )

    algorithms = {}

    for item in history:

        algo = item["algorithm"]

        algorithms[algo] = algorithms.get(algo, 0) + 1

    most_used = "None"

    if algorithms:

        most_used = max(
            algorithms,
            key=algorithms.get
        )

    return {

        "total_hashes": total_hashes,

        "text_hashes": text_hashes,

        "file_hashes": file_hashes,

        "most_used_algorithm": most_used
    }