"""Includes utilities that might help while solving AoC2022"""
from pathlib import Path


def read_input_file(day: str) -> str:
    """Opens the file, reads the contents and returns the raw_inputs

    Parameters
    ----------
    day : str
        String, that represents the day for which the input should be read.

    Returns
    -------
    str
        String, that represents the raw content of the input text file.
    """
    try:
        with open(Path(rf'../inputs/{day}_input.txt'), encoding='utf-8') as fh:
            raw_input = fh.read()
        return raw_input
    except:
        raise FileNotFoundError(f'{day}_input.txt is not yet available.')
