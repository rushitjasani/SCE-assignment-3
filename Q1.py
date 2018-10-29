import pickle
class Admin:
    __id1 = 0
    def __init__(self,name):
        Admin.__id1 = Admin.__id1 + 1 
        self.__id = Admin.__id1
        self.__name = name

    def set_name(self,name):
        self.__name = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name 

    def viewProducts(self):
        with open("product","rb") as file_obj:
            while(True):
                try:
                    prod_obj = pickle.load(file_obj)
                    print prod_obj.get_id(), prod_obj.get_name(), prod_obj.get_group(), prod_obj.get_subgroup()
                except EOFError:
                    break

    def addProduct(self):
        name = raw_input("name of product : ")
        group = raw_input("group of product : ")
        subgroup = raw_input("subgroup of product : ")
        price = int(raw_input("price of product : "))
        new_prod = Product(name,group,subgroup,price)
        print new_prod
        file_obj = open("product","a+b")
        pickle.dump(new_prod,file_obj)
        file_obj.close()

    def deleteProduct(self):
        del_id = int(raw_input("enter id of product to be deleted : "))
        l = []
        with open("product","rb") as file_obj:
            while(True):
                try:
                    prod_obj = pickle.load(file_obj)
                    if prod_obj.get_id() != del_id:
                        l.append(prod_obj)
                except EOFError:
                    break
        file_obj = open("product","wb")
        for i in l:
            pickle.dump(i,file_obj)
        file_obj.close()
    
    def modifyProduct(self):
        change_id = int(raw_input("enter id of product to be modified : "))
        name = raw_input("new name of product : ")
        group = raw_input("new group of product : ")
        subgroup = raw_input("new subgroup of product : ")
        price = int(raw_input("new price of product : "))
        l = []
        with open("product","rb") as file_obj:
            while(True):
                try:
                    prod_obj = pickle.load(file_obj)
                    if prod_obj.get_id() == change_id:
                        prod_obj.set_name(name)
                        prod_obj.set_group(group)
                        prod_obj.set_subgroup(subgroup)
                        prod_obj.set_price(price)
                    l.append(prod_obj)
                except EOFError:
                    break
        file_obj = open("product","wb")
        for i in l:
            pickle.dump(i,file_obj)
        file_obj.close()
    def makeShipment(self):
        pass
    def confirmdelivery(self):
        pass

class Customer:
    __id1 = 0
    def __init__(self,name,address,phone):
        Customer.__id1 = Customer.__id1 + 1
        self.__id = Customer.__id1
        self._name = name
        self._address = address
        self._phNo = phone
    
    def set_name(self,name):
        self._name = name

    def set_address(self,address):
        self._address = address

    def set_phNo(self,phone):
        self._phNo = phone

    def get_id(self):
        return self.__id

    def get_name(self):
        return self._name 

    def get_address(self):
        return self._address 

    def get_phNo(self):
        return self._phNo 

    def viewProducts(self):
        with open("product","rb") as file_obj:
            while(True):
                try:
                    prod_obj = pickle.load(file_obj)
                    print prod_obj.get_id(), prod_obj.get_name(), prod_obj.get_group(), prod_obj.get_subgroup()
                except EOFError:
                    break
    def buyProducts(self):
        pass
    def makePayment(self):
        pass
    def addToCart(self):
        pass
    def deleteFromCart(self):
        pass

class Guest:
    __guest_number1 = 0

    def __init__(self):
        Guest.__guest_number1 = Guest.__guest_number1 + 1 
        self.__guest_number = Guest.__guest_number1

    def get_guest_number(self):
        return self.__guest_number

    def viewProducts(self):
        with open("product","rb") as file_obj:
            while(True):
                try:
                    prod_obj = pickle.load(file_obj)
                    print prod_obj.get_id(), prod_obj.get_name(), prod_obj.get_group(), prod_obj.get_subgroup()
                except EOFError:
                    break

    def getRegistered(self):
        name = raw_input("name : ")
        address = raw_input("address : ")
        phone = int(raw_input("phone : "))
        new_cust = Customer(name,address,phone)
        file_obj = open("user","a+b")
        pickle.dump(new_cust,file_obj)
        file_obj.close()

class Product:
    __id1 = 0
    def __init__(self,name,group,subgroup,price):
        Product.__id1 = Product.__id1+1
        self.__id = Product.__id1
        self._name = name
        self._group = group
        self._subgroup = subgroup
        self._price = price
    
    def set_name(self,name):
        self._name = name
    def set_group(self,group):
        self._group = group
    def set_subgroup(self,subgroup):
        self._subgroup = subgroup
    def set_price(self,price):
        self._price = price
    def get_id(self):
        return self.__id
    def get_name(self):
        return self._name 
    def get_group(self):
        return self._group 
    def get_subgroup(self):
        return self._subgroup
    def get_price(self):
        return self._price 

class Payment:
    def __init__(self,name,cardtype,cardnum):
        #customer id handling.
        self._name = name
        self.__cardtype = cardtype
        self.__cardnum = cardnum
    
    def set_cardtype(self,cardtype):
        self.__cardtype = cardtype
    def set_cardnum(self, cardnum):
        self.__cardnum
    def get_name(self):
        return self.get_name
    def get_cardtype(self):
        return self.__cardtype
    def get_cardnum(self):
        return self.__cardnum

class Cart:
    __id1 = 0
    def __init__(self,products=[]):
        Cart.__id1 = Cart.__id1+1
        self.__id = Cart.__id1
        self._NumberOfProducts = len(products)
        self._products = products
        for i in products:
            self._total += i.get_price()
    
    def set_NumberOfProducts(self, NumberOfProducts):
        self._NumberOfProducts = NumberOfProducts
    def get_NumberOfProducts(self):
        return self._NumberOfProducts

    def get_total(self):
        return self._total
        
admin = Admin("rushit")
def admin_mode():
    while(True):
        try:
            print "1 for view product"
            print "2 for add product"
            print "3 for delete product"
            print "4 for modify product"
            print "5 for make shipments"
            print "6 for confirm delivery"
            print "7 for exit"
            choice = int(raw_input())
            if choice == 1:
                admin.viewProducts()
            elif choice == 2:
                admin.addProduct()
            elif choice == 3:
                admin.deleteProduct()
            elif choice == 4:
                admin.modifyProduct()
            elif choice == 5:
                admin.makeShipment()
            elif choice == 6:
                admin.confirmdelivery()
            elif choice == 7:
                return   
        except :
            continue
            
def customer_mode():
    pass

def guest_mode():
    try:
        g = Guest()
        while(True):
            print "1 for view product"
            print "2 for register"
            print "3 for exit"
            choice = int(raw_input())
            if choice == 1:
                g.viewProducts()
            elif choice == 2:
                g.getRegistered()
                return
            elif choice == 3:
                return   
    except :
        return

while(True):
    print "Press 1 for Admin"
    print "Press 2 for Customer"
    print "Press 3 for Guest"
    user = int(raw_input())
    if user == 1:
        admin_mode()
    elif user == 2:
        customer_mode()
    elif user == 3:
        guest_mode()
    else:
        print "Please enter valid input"