# molecular_weight_carbohydrate.py
#   A program that calculates the molecular weight of a carbohydrate based on the number of hyrdrogen, carbon, and oxygen atoms in the molecule.

def main():
    print("This program calculates the molecular weight of a carbohydrate (in g/mol) based on the number of hydrogen, carbon, and oxygen atoms in the molecule.")
    print()
    
    H = int(input("Enter the number of Hydrogen atoms: "))
    C = int(input("Enter the number of Carbon atoms: "))
    O = int(input("Enter the number of Oxygen atoms: "))

    mol_weight = H * 1.00794 + C * 12.0107 + O * 15.9994

    print(f"The molecular weight of the molecule is {mol_weight:.2f} grams per mole")

main()
