from datetime import datetime


def create_report(
    algorithm,
    original_text,
    generated_hash
):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    report = f"""
==============================

HashForge Report

==============================

Date

{timestamp}

------------------------------

Algorithm

{algorithm}

------------------------------

Original Text

{original_text}

------------------------------

Generated Hash

{generated_hash}

==============================
"""

    return report
