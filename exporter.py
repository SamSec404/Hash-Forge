import csv
import json


def export_txt(history, filename):

    with open(filename, "w") as file:

        for item in history:

            file.write(
                f"""
Type : {item['record_type']}
Input : {item['original_input']}
Algorithm : {item['algorithm']}
Hash : {item['generated_hash']}
Time : {item['timestamp']}

----------------------------------------

"""
            )


def export_json(history, filename):

    with open(filename, "w") as file:

        json.dump(
            history,
            file,
            indent=4
        )


def export_csv(history, filename):

    with open(
        filename,
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Type",
            "Input",
            "Algorithm",
            "Hash",
            "Timestamp"
        ])

        for item in history:

            writer.writerow([
                item["record_type"],
                item["original_input"],
                item["algorithm"],
                item["generated_hash"],
                item["timestamp"]
            ])