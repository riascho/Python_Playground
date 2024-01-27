#TODO: turn franchises and menus into dictionaries instead of lists

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

class Franchise:

  def __init__(self, address, menus=[]):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return f"Adress: {self.address}"

  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    if available_menus == []:
      return f"No menu available at {time}:00!"
    return available_menus
  
class Menu:

  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self):
    return f"{self.name.title()} menu: served between {self.start_time}:00 - {self.end_time}:00."

  def calculate_bill(self, purchased_items):
    total_price = 0
    # purchased_items = ['pancakes', 'coffee']
    for item in purchased_items:
        total_price += self.items.get(item, 0)
    return total_price



brunch_items =  {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
brunch = Menu('brunch',brunch_items,11,16)

earlybird_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}
earlybird = Menu('early-bird',earlybird_items,15,18)

dinner_items = {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}
dinner = Menu('dinner',dinner_items,17,23)

kids_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
kids = Menu('kids',kids_items, 11, 21)

print(brunch)
print(earlybird)
print(brunch.calculate_bill(['pancakes','home fries','coffee']))
print(brunch.calculate_bill(['pancakes','homefries','coffee']))
print(earlybird.calculate_bill(['salumeria plate','mushroom ravioli (vegan)']))
print(earlybird.calculate_bill(['salumeria plate','vegan mushroom ravioli']))


flagship_store = Franchise('1232 West End Road',[brunch,earlybird, dinner, kids])
print(flagship_store)
new_installment = Franchise('12 East Mulberry Street', [brunch, dinner, kids])
print(new_installment)

print(flagship_store.available_menus(12))
print(new_installment.available_menus(17))
print(new_installment.available_menus(10))



basta = Business("Basta Fazoolin' with my Heart",[flagship_store, new_installment])
print(basta)

arepas_menu = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
arepas = Menu("Take a' Arepa",arepas_menu,10,20)

arepas_place = Franchise("189 Fitzgerald Avenue",[arepas])
arepa = Business("Take a' Arepa",arepas_place)

print(arepa.franchises.menus)
print(basta.franchises[0].available_menus(13))
