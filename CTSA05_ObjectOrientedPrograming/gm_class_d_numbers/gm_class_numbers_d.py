# gm_class_numbers_d.py: coded by Kinya MIURA 230418
# ---------------------------------------------------------
print('*** class GMNumbersD: operating numbers ***')
print('   *** with string function ***')

# =========================================================
print('## --- section_class: (GMNumbersD) describing class --- ##')
class GMNumbersD():
    ## --- section_ca: initializing class instance --- ##
    def __init__(self, aa, bb) -> None:
        self.__aa, self.__bb = None, None  # private instance variables
        self.set_aabb(aa, bb)
    ## --- section_cb: setting and getting functions --- ##
    ## setting functions
    def set_aabb(self, aa: float = None, bb: float = None) -> None:
        if aa is not None: self.__aa = aa
        if bb is not None: self.__bb = bb
    ## getting functions
    def aa(self) -> float: return self.__aa
    def bb(self) -> float: return self.__bb
    ## --- section_cc: string function for print() --- ##
    def __str__(self) -> str:
        return f'(GMNumbersD): aa = {self.__aa:g}, bb = {self.__bb:g}'
    ## --- section_cd: functions for arithmetics --- ##
    def calc(self) -> tuple:
        return self.__aa + self.__bb, self.__aa - self.__bb

# =========================================================
print('## --- section_main: (GMMumbersD) main process --- ##')
## --- section_ma: calculating arithmetics --- ##
numbs = GMNumbersD(3, 2)  # creating instance
print(numbs)
add, sub = numbs.calc()  # using instance functions
print(f'{add = }, {sub = }')
## --- section_mb: calculating arithmetics --- ##
numbs.set_aabb(aa=7, bb=3)  # setting instance variables
print(numbs)
add, sub = numbs.calc()  # using instance functions
print(f'{add = }, {sub = }\n')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** class GMNumbersD: operating numbers ***
   *** with string function ***
## --- section_class: (GMNumbersD) declaring class --- ##
## --- section_main: (GMMumbersD) main process --- ##
(GMNumbersD): aa = 3, bb = 2
add = 5, sub = 1
(GMNumbersD): aa = 7, bb = 3
add = 10, sub = 4
'''
