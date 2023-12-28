from pyteal import *

from marketplace_contract import Product

if __name__ == "__main__":
    product_instance = Product()
    approval_program = product_instance.approval_program()
    clear_program = product_instance.clear_program()

    # Mode.Application specifies that this is a smart contract
    compiled_approval = compileTeal(approval_program, Mode.Application, version=6)
    print(compiled_approval)
    with open('marketplace_approval.teal', 'w') as teal:
        teal.write(compiled_approval)
        teal.close()

    compiled_clear = compileTeal(clear_program, Mode.Application, version=6)
    print(compiled_clear)
    with open('marketplace_clear.teal', 'w') as teal:
        teal.write(compiled_clear)
        teal.close()