from pathlib import Path

def getInput(day, example=False):
    """Load input data for a specific day.
    
    Args:
        day: The day number (1-25)
        
    Returns:
        List of strings, one per line in the input file
    """
    # Navigate from src/aoc_utils/ up to project root, then to Inputs/
    project_root = Path(__file__).parent.parent.parent
    path = project_root / 'Inputs' / f'Day{day}{"_example" if example else ""}.txt'
    
    with open(path, 'r') as f:
        data = f.read().splitlines()
    return data
