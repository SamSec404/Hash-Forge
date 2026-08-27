from dataclasses import dataclass, asdict


@dataclass
class HashRecord:

    record_type: str      # text or file

    original_input: str   # text or filename

    algorithm: str

    generated_hash: str

    timestamp: str

    def to_dict(self):

        return asdict(self)
