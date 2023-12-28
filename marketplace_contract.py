from pyteal import *

class Product:
    class Variable:
        name = Bytes('NAME')
        image = Bytes('IMAGE')
        description = Bytes('DESCRIPTION')
        price = Bytes('PRICE')
        sold = Bytes('SOLD')

    class AppMethods:
        buy = Bytes('buy')

    def application_creation(self):
        return Seq([
            Assert(Txn.application_args.length() == Int(4)),
            Assert(Txn.note() == Bytes('tutorial-marketplace:uv1')),
            Assert(Btoi(Txn.application_args[3]) > Int(0)),
            App.globalPut(self.Variable.name, Txn.application_args[0]),
            App.globalPut(self.Variable.image, Txn.application_args[1]),
            App.globalPut(self.Variable.description, Txn.application_args[2]),
            App.globalPut(self.Variable.price, Btoi(Txn.application_args[3])),
            App.globalPut(self.Variables.sold, Int(0)),
            Approve()
        ])
    
    # Handler for the buy interaction

    def buy(self):
        count = Txn.application_args[1]
        valid_number_of_transactions = Global.group_size() == Int(2)

        valid_payment_to_seller = And(
            Gtxn[1].type_enum() == TxnType.Payment,
            Gtxn[1].receiver() == Global.creator_address(),
            Gtxn[1].amount() == App.globalGet(self.Variable.price) * Btoi(count),
            Gtxn[1].sender() == Gtxn[0].sender(),
        
        )
