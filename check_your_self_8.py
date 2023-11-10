#================== 1 ==================
class Auto:
    def ride(self):
        print('Riding on a ground')


class Boat:
    def swim(self):
        print('Floating on water')

class Amphibian(Auto,Boat):
    pass

obj = Amphibian() 
obj.ride() 
obj.swim() 


#================== 2 =====================
class ContactList(list):
    def __init__(self,contact_list):
        self.contact_list = contact_list

    def search_by_name(self,name):
        res = []
        for i in self.contact_list:
            if name in i:
                res.append(i)
        return res

all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
print(all_contacts.search_by_name('Olya')) 