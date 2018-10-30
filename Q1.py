import pickle


class Admin:
    __id1 = 0

    def __init__(self, name):
        Admin.__id1 = Admin.__id1 + 1
        self.__id = Admin.__id1
        self.__name = name

    def set_name(self, name):
        self.__name = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def viewProducts(self):
        with open("product", "rb") as file_obj:
            while(True):
                try:
                    prod_obj = pickle.load(file_obj)
                    print prod_obj.get_id(), prod_obj.get_name(
                    ), prod_obj.get_group(), prod_obj.get_subgroup()
                except EOFError:
                    break

    def addProduct(self):
        name = raw_input("name of product : ")
        group = raw_input("group of product : ")
        subgroup = raw_input("subgroup of product : ")
        price = int(raw_input("price of product : "))
        new_prod = Product(name, group, subgroup, price)

        with open("product", "wb") as file_obj:
            pickle.dump(new_prod, file_obj)

    def deleteProduct(self):
        del_id = int(raw_input("enter id of product to be deleted : "))
        l = []
        with open("product", "rb") as file_obj:
            while(True):
                try:
                    prod_obj = pickle.load(file_obj)
                    if prod_obj.get_id() != del_id:
                        l.append(prod_obj)
                except EOFError:
                    break
        with open("product", "wb") as file_obj:
            for i in l:
                pickle.dump(i, file_obj)

    def modifyProduct(self):
        change_id = int(raw_input("enter id of product to be modified : "))
        name = raw_input("new name of product : ")
        group = raw_input("new group of product : ")
        subgroup = raw_input("new subgroup of product : ")
        price = int(raw_input("new price of product : "))
        l = []
        with open("product", "rb") as file_obj:
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
        with open("product", "wb") as file_obj:
            for i in l:
                pickle.dump(i, file_obj)

    def makeShipment(self):
        pass

    def confirmdelivery(self):
        pass


class Customer:
    def __init__(self, name, address, phone):
        max_id = 0
        try:
            with open("user", "rb") as file_obj:
                while True:
                    try:
                    x = pickle.load(file_obj)
                    if x.get_id() > max_id:
                        max_id = x.get_id()
                    except EOFError:
                        break
            self.__id = max_id+1
        except FileNotFound:
            self.__id = 1

        self._name = name
        self._address = address
        self._phNo = phone

    def set_name(self, name):
        self._name = name

    def set_address(self, address):
        self._address = address

    def set_phNo(self, phone):
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
        with open("product", "rb") as file_obj:
            while(True):
                try:
                    prod_obj = pickle.load(file_obj)
                    print prod_obj.get_id(), prod_obj.get_name(
                    ), prod_obj.get_group(), prod_obj.get_subgroup()
                except EOFError:
                    break

    def buyProducts(self):
        try:
            with open("bought", "rb") as file_obj:
                bl = pickle.load(file_obj)
                if self.__id in bl.keys():
                    l = bl[self.__id]
                    for i in l:
                        print i.get_name() + "\t\t" + i.get_price()
                else:
                    print "Nothing here"
                    return
        except:
            return

    def makePayment(self):
        old_c = None
        cart = None
        l = []
        with open("cart", "rb") as file_obj:
            while(True):
                try:
                    cart_obj = pickle.load(file_obj)
                    if cart_obj.get_id() != self.get_id():
                        l.append(cart_obj)
                    else:
                        old_c = cart_obj
                except EOFError:
                    break

        if old_c == None:
            print "Empty cart"
            return
        else:
            all_prod = []
            with open("product", "rb") as file_obj:
                while(True):
                    try:
                        prod_obj = pickle.load(file_obj)
                        all_prod += prod_obj.get_id()
                    except EOFError:
                        prod = None
                        break

            bough_prod = old_c.get_products()

            available = [x for x in bough_prod if x.get_id() in all_prod]
            notavailable = [x for x in bough_prod if x.get_id()
                            not in all_prod]

            print "Products Out of stock :"
            for i in notavailable:
                print i.get_name()
            print "Removed abovementioned products from cart and making payment for remaining products.."

            if len(available) == 0:
                print "empty cart"
                return

            bough_prod = available

            cardtype = raw_input("card type : ")
            cardnum = raw_input("card number : ")
            payment_obj = Payment(self.__id, self._name, cardtype, cardnum)
            with open("payment", "a+b") as file_obj:
                pickle.dump(payment_obj, file_obj)

            bl = {}
            try:
                with open("bought", "rb") as file_obj:
                    bl = pickle.load(file_obj)
            except:
                pass

            with open("bought", "wb") as file_obj:
                try:
                    if self.__id in bl.keys():
                        l = bl[self.__id]
                        l += bough_prod
                        bl[self.__id] = l
                        pickle.dump(bl, file_obj)
                    else
                    bl[self.__id] = bough_prod
                    pickle.dump(bl, file_obj)
                except:
                    bl[self.__id] = bough_prod
                    pickle.dump(bl, file_obj)

            with open("cart", "wb") as file_obj:
            for i in l:
                pickle.dump(i, file_obj)

    def addToCart(self):
        prod_id = int(raw_input("Enter product id : "))
        prod = None
        with open("product", "rb") as file_obj:
            while(True):
                try:
                    prod_obj = pickle.load(file_obj)
                    if prod_id == prod_obj.get_id():
                        break
                except EOFError:
                    prod = None
                    break

        if prod == None:
            print "No item with id " + prod_id + " exists :("
            return

        old_c = None
        cart = None
        l = []
        with open("cart", "rb") as file_obj:
            while(True):
                try:
                    cart_obj = pickle.load(file_obj)
                    if cart_obj.get_id() != self.get_id():
                        l.append(cart_obj)
                    else:
                        old_c = cart_obj
                except EOFError:
                    break

        if old_c == None:
            old_c = Cart(self.__id, [prod])
        else:
            old_c.set_NumberOfProducts(old_c.get_NumberOfProducts() + 1)
            old_c.set_total(old_c.get_total() + prod.get_price())
            old_c.set_products(old_c.get_products().append(prod))
        l.append()
        with open("cart", "wb") as file_obj:
            for i in l:
                pickle.dump(i, file_obj)

    def deleteFromCart(self):
        prod_id = int(raw_input("Enter product id : "))
        old_c = None
        cart = None
        l = []
        with open("cart", "rb") as file_obj:
            while(True):
                try:
                    cart_obj = pickle.load(file_obj)
                    if cart_obj.get_id() != self.get_id():
                        l.append(cart_obj)
                    else:
                        old_c = cart_obj
                except EOFError:
                    break
        remove_prod = None

        if old_c == None:
            print "Empty cart"
            return
        else:
            prod_list = old_c.get_products()
            for prod in prod_list:
                if prod.get_id() == prod_id:
                    remove_prod = prod
                    break

            if remove_prod == None:
                return
            else:
                new_list = prod_list.remove(remove_prod)
                old_c.set_products(new_list)
                old_c.set_total(old_c.get_total() - remove_prod.get_price())
                old_c.set_NumberOfProducts(old_c.get_NumberOfProducts() - 1)

        with open("cart", "wb") as file_obj:
            for i in l:
                pickle.dump(i, file_obj)

    def viewCart(self):
        old_c = None
        l = []
        with open("cart", "rb") as file_obj:
            while(True):
                try:
                    cart_obj = pickle.load(file_obj)
                    if cart_obj.get_id() == self.get_id():
                        old_c = cart_obj
                except EOFError:
                    break

        if old_c != None:
            print "###### CART ######"
            print old_c.get_NumberOfProducts
            for i in old_c.get_products:
                print i.get_name(), i.get_price()
            print " Total cost : " + old_c.get_total()

        return


class Guest:
    __guest_number1 = 0

    def __init__(self):
        Guest.__guest_number1 = Guest.__guest_number1 + 1
        self.__guest_number = Guest.__guest_number1

    def get_guest_number(self):
        return self.__guest_number

    def viewProducts(self):
        with open("product", "rb") as file_obj:
            while(True):
                try:
                    prod_obj = pickle.load(file_obj)
                    print prod_obj.get_id(), prod_obj.get_name(
                    ), prod_obj.get_group(), prod_obj.get_subgroup()
                except EOFError:
                    break

    def getRegistered(self):
        name = raw_input("name : ")
        address = raw_input("address : ")
        phone = int(raw_input("phone : "))
        new_cust = Customer(name, address, phone)
        with open("user", "a+b") as file_obj:
            pickle.dump(new_cust, file_obj)


class Product:
    def __init__(self, name, group, subgroup, price):
        max_id = 0
        try:
            with open("product", "rb") as file_obj:
                while True:
                    try:
                    x = pickle.load(file_obj)
                    if x.get_id() > max_id:
                        max_id = x.get_id()
                    except EOFError:
                        break
            self.__id = max_id+1
        except FileNotFound:
            self.__id = 1
        self._name = name
        self._group = group
        self._subgroup = subgroup
        self._price = price

    def set_name(self, name):
        self._name = name

    def set_group(self, group):
        self._group = group

    def set_subgroup(self, subgroup):
        self._subgroup = subgroup

    def set_price(self, price):
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
    def __init__(self, id, name, cardtype, cardnum):
        self._id = id
        self._name = name
        self.__cardtype = cardtype
        self.__cardnum = cardnum

    def set_cardtype(self, cardtype):
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

    def __init__(self, id, products=[]):
        self.__id = id
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

    def set_total(self, total):
        self._total += total

    def set_products(self, args=[]):
        self._products = args

    def get_products(self):
        return self._products


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
        except:
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
    except:
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
