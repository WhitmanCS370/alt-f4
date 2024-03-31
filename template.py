import argparse
import sys

def ValidateArguments(args):
    """
    Validate command line arguments.
    
    :param args: Parsed arguments from argparse.
    :raises ValueError: If validation fails.
    """
    if '--play' in sys.argv and len([arg for arg in sys.argv if '--play' in arg]) > 1:
        raise ValueError("--play option can only be used once.")

    if args.input_merge and args.play == 'parallel':
        raise ValueError("--input-merge is incompatible with --play=parallel.")

def ProcessArguments(args):
    """
    Process and act on the validated arguments.
    
    :param args: Parsed arguments from argparse.
    """
    # Program logic based on arguments
    print(f"Play mode: {args.play}")
    if args.input_merge:
        print("Input merge is enabled")
    # Add your actual program logic here

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='Sound tool for playing sounds in different modes.')

    # Define command line arguments
    parser.add_argument('--play', type=str, choices=['mute', 'sequential', 'parallel'],
                        help='Set the play mode: mute, sequential, or parallel')
    parser.add_argument('--input-merge', action='store_true',
                        help='Enable input merging. This is incompatible with --play=parallel.')

    # Parse the arguments
    args = parser.parse_args()

    # Validate arguments
    try:
        ValidateArguments(args)
    except ValueError as e:
        parser.error(str(e))

    # Process validated arguments
    ProcessArguments(args)

if __name__ == "__main__":
    main()
