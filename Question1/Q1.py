import pickle


class Admin:

    def __init__(self, name):
        self.__id = 1
        self.__name = name

    def set_name(self, name):
        self.__name = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def viewProducts(self):
        try:
            with open("product", "rb") as file_obj:
                while(True):
                    try:
                        prod_obj = pickle.load(file_obj)
                        print prod_obj.get_id(), "\t\t", 
                        print prod_obj.get_name(),"\t\t",
                        print prod_obj.get_group(), "\t\t", 
                        print prod_obj.get_subgroup()
                    except EOFError:
                        break
        except:
            print "No Products Available"
        

    def addProduct(self):
        name = raw_input("name of product : ")
        group = raw_input("group of product : ")
        subgroup = raw_input("subgroup of product : ")
        price = int(raw_input("price of product : "))
        new_prod = Product(name, group, subgroup, price)

        with open("product", "a+b") as file_obj:
            pickle.dump(new_prod, file_obj)

    def deleteProduct(self):
        del_id = int(raw_input("enter id of product to be deleted : "))
        l = []
        try:
            with open("product", "rb") as file_obj:
                while(True):
                    try:
                        prod_obj = pickle.load(file_obj)
                        if prod_obj.get_id() != del_id:
                            l.append(prod_obj)
                    except EOFError:
                        break
        except:
            return
        
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
        try:
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
        except:
            return
        
        with open("product", "wb") as file_obj:
            for i in l:
                pickle.dump(i, file_obj)

    def makeShipment(self):
        pass

    def confirmdelivery(self):
        pass


class Customer:
    def __init__(self, name, address, phone):
        max_id = -1
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
        except :
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
        try:
            with open("product", "rb") as file_obj:
                while(True):
                    try:
                        prod_obj = pickle.load(file_obj)
                        print prod_obj.get_id(), "\t\t", 
                        print prod_obj.get_name(),"\t\t",
                        print prod_obj.get_group(), "\t\t", 
                        print prod_obj.get_subgroup()
                    except EOFError:
                        break
        except:
            print "No Products Available"

    def buyProducts(self):
        try:
            with open("bought", "rb") as file_obj:
                bl = pickle.load(file_obj)
                if self.__id in bl.keys():
                    l = bl[self.__id]
                    for i in l:
                        print i.get_name() + "\t" + str(i.get_price())
                else:
                    print "Nothing here"
                    return
        except:
            return

    def makePayment(self):
        old_c = None
        cart = None
        l = []
        try:
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
        except:
            return

        if old_c is None:
            print "Empty cart"
            return
        else:
            all_prod = []
            try:
                with open("product", "rb") as file_obj:
                    while(True):
                        try:
                            prod_obj = pickle.load(file_obj)
                            all_prod += [prod_obj.get_id()]
                        except EOFError:
                            prod = None
                            break
            except:
                pass
            
            bought_prod = old_c.get_products()

            available = [x for x in bought_prod if x.get_id() in all_prod]
            notavailable = [x for x in bought_prod if x.get_id()
                            not in all_prod]

            if len(notavailable) != 0:
                print "Products Out of stock :"
                for i in notavailable:
                    print i.get_name()
                print "Removed abovementioned products from cart and making payment for remaining products.."

            if len(available) == 0:
                print "empty cart"
                return

            bought_prod = available

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
                        l += bought_prod
                        bl[self.__id] = l
                        pickle.dump(bl, file_obj)
                    else:
                        bl[self.__id] = bought_prod
                        pickle.dump(bl, file_obj)
                except:
                    bl[self.__id] = bought_prod
                    pickle.dump(bl, file_obj)

            with open("cart", "wb") as file_obj:
                for i in l:
                    pickle.dump(i, file_obj)

    def addToCart(self):
        prod_id = int(raw_input("Enter product id : "))
        prod = None
        try:
            with open("product", "rb") as file_obj:
                while(True):
                    try:
                        prod_obj = pickle.load(file_obj)
                        if prod_id == prod_obj.get_id():
                            prod = prod_obj
                            break
                    except EOFError:
                        prod = None
                        break
        except:
            return
        

        if prod is None:
            print "No item with id " + str(prod_id) + " exists :("
            return

        old_c = None
        cart = None
        l = []
        try:
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
        except:
            pass
            
        if old_c is None:
            old_c = Cart(self.__id, [prod])
        else:
            old_c.set_NumberOfProducts(old_c.get_NumberOfProducts() + 1)
            old_c.set_total(old_c.get_total() + prod.get_price())
            old_cart_prod_list = old_c.get_products()
            old_cart_prod_list.append(prod)
            old_c.set_products( old_cart_prod_list )
        l.append(old_c)
        with open("cart", "wb") as file_obj:
            for i in l:
                pickle.dump(i, file_obj)

    def deleteFromCart(self):
        prod_id = int(raw_input("Enter product id : "))
        old_c = None
        l = []
        try:
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
        except:
            return
            
        if old_c is None:
            print "Empty cart"
            return
        else:
            prod_list = old_c.get_products()
            for prod in prod_list:
                if prod.get_id() == prod_id:
                    remove_prod = prod
                    break

            print remove_prod.get_id()

            if remove_prod is None:
                return
            else:
                prod_list.remove(remove_prod)
                old_c.set_products(prod_list)
                old_c.set_total(old_c.get_total() - remove_prod.get_price())
                old_c.set_NumberOfProducts(old_c.get_NumberOfProducts() - 1)
        if len(prod_list) > 0:
            l.append(old_c)
        with open("cart", "wb") as file_obj:
            for i in l:
                pickle.dump(i, file_obj)

    def viewCart(self):
        old_c = None
        l = []
        try:
            with open("cart", "rb") as file_obj:
                while(True):
                    try:
                        cart_obj = pickle.load(file_obj)
                        if cart_obj.get_id() == self.get_id():
                            old_c = cart_obj
                    except EOFError:
                        break
        except:
            print "Empty cart"
            return

        if old_c is not None:
            print "###### CART ######"
            print old_c.get_NumberOfProducts()
            for i in old_c.get_products():
                print i.get_name(), i.get_price()
            print "Total cost : " + str(old_c.get_total())
        else:
            print "Empty cart"
        
        return


class Guest:
    __guest_number1 = 0

    def __init__(self):
        Guest.__guest_number1 = Guest.__guest_number1 + 1
        self.__guest_number = Guest.__guest_number1

    def get_guest_number(self):
        return self.__guest_number

    def viewProducts(self):
        try:
            with open("product", "rb") as file_obj:
                while(True):
                    try:
                        prod_obj = pickle.load(file_obj)
                        print prod_obj.get_id(), "\t\t", 
                        print prod_obj.get_name(),"\t\t",
                        print prod_obj.get_group(), "\t\t", 
                        print prod_obj.get_subgroup()
                    except EOFError:
                        break
        except:
            print "No Products Available"

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
        except:
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
        self._total = 0
        for i in products:
            self._total += i.get_price()

    def get_id(self):
        return self.__id

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
                print
                admin.viewProducts()
                print
            elif choice == 2:
                print
                admin.addProduct()
                print
            elif choice == 3:
                print
                admin.deleteProduct()
                print
            elif choice == 4:
                print
                admin.modifyProduct()
                print
            elif choice == 5:
                print
                admin.makeShipment()
                print
            elif choice == 6:
                print
                admin.confirmdelivery()
                print
            elif choice == 7:
                return
        except KeyboardInterrupt:
            return
        except:
            continue


def customer_mode():
    uname = raw_input("Enter name : ")
    phone = int( raw_input( "Enter Phone : " ) )
    # uname = "rushit"
    # phone = 8866324686
    auth = False
    customer = None
    try:
        with open("user","rb") as file_obj:
            while True:
                try:
                    obj = pickle.load(file_obj)
                    if obj.get_name() == uname and obj.get_phNo() == phone:
                        auth = True
                        customer = obj
                        break
                except EOFError:
                    break
    except:
        pass
    
    if auth == False:
        print "Please Register first."
        return

    while(True):
        try:
            print "1 for view product"
            print "2 for add to cart"
            print "3 for delete from cart"
            print "4 for view cart"
            print "5 for make payment"
            print "6 for Order history"
            print "7 for exit"
            choice = int(raw_input())
            if choice == 1:
                print
                customer.viewProducts()
                print
            elif choice == 2:
                print
                customer.addToCart()
                print
            elif choice == 3:
                print
                customer.deleteFromCart()
                print
            elif choice == 4:
                print
                customer.viewCart()
                print
            elif choice == 5:
                print
                customer.makePayment()
                print
            elif choice == 6:
                print
                customer.buyProducts()
                print
            elif choice == 7:
                print
                print "Thank You :)"
                print
                return
        except KeyboardInterrupt:
            return
        except:
            continue


def guest_mode():
    try:
        g = Guest()
        while(True):
            print "1 for view product"
            print "2 for register"
            print "3 for exit"
            choice = int(raw_input())
            if choice == 1:
                print 
                g.viewProducts()
                print
            elif choice == 2:
                print
                g.getRegistered()
                print
                return
            elif choice == 3:
                return
    except KeyboardInterrupt:
            return
    except:
        return


while(True):
    try:
        print "Press 1 for Admin"
        print "Press 2 for Customer"
        print "Press 3 for Guest"
        print "Press 4 for Exit"
        user = int(raw_input())
        if user == 1:
            print
            admin_mode()
            print
        elif user == 2:
            print 
            customer_mode()
            print 
        elif user == 3:
            print 
            guest_mode()
            print 
        elif user == 4:
            exit()
        else:
            print "Please enter valid input"
    except KeyboardInterrupt:
        print
        exit()
    except :
        print
        print "Please enter valid input"
        exit()
