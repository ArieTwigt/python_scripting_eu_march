from argparse import ArgumentParser
from handy_functions.calc_functions import calc_pythagoras
from our_functions.calc_functions import calc_circle


# initiate the argument parser
parser = ArgumentParser()

# add arguments to the parser
parser.add_argument('--diameter', type=float, required=True)
parser.add_argument('--rounding', type=int, required=False, default=1)

# parse the args
args = parser.parse_args()

# evaluate the parsed arguments
diameter = args.diameter
rounding = args.rounding

if __name__ == '__main__':
    # use the function 
    surface_circle = calc_circle(diameter, round_value=rounding)
    
    # print out the inserted argument
    print(f"The result is: {surface_circle}")

