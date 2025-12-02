from pathlib import Path

def getInput(day):
    path = 'Inputs\\Day' + str(day) + '.txt'

    with open(Path(__file__).parent / Path(path), 'r') as f:
        data = f.read().splitlines()
    return data


