import click
import numpy as np
from numpy import pi
import pandas as pd

#creates command group 
@click.group()
def smallangle():
    pass

#creates sin command 
@smallangle.command()

#gives amount of steps as option
@click.option(
    "-n",
    "--number",
    default=10,
    help="Number of steps between 0 and 2pi",
    show_default=True,  # show default in help
)

#sin function
def sin(number):
    """Gives sinus of numbers between 0 and 2pi"""    
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

#creates tan command 
@smallangle.command()

#gives amount of steps as option
@click.option(
    "-n",
    "--number",
    default=10,
    help="Number of steps between 0 and pi",
    show_default=True,  # show default in help
)

#tan function
def tan(number):
    """Gives tangent of numbers between 0 and 2pi"""   
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)

if __name__ == "__main__":
    smallangle()