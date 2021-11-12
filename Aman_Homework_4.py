
# Тут я немного считерил
# import datetime
# def convert(n):
#     return str(datetime.timedelta(seconds=n))
# n = int(input("Введите данные:"))
# print(convert(n))


class TimeDesk:
    def __init__(self, seconds):
        self.seconds = seconds

    def time(self):
        days = int(self.seconds / (24 * 60 * 60))
        self.seconds -= days * 24 * 60 * 60
        hours = int(self.seconds / 60 / 60)
        self.seconds -= hours * 60 * 60
        minutes = int(self.seconds / 60)
        self.seconds -= minutes * 60
        return f"{days} дней, {hours} часов, {minutes} минут, {self.seconds} секунд"

    def show_given_time(self):
        seconds = int(input("Введите данные: "))
        a = TimeDesk(seconds)
        return a.time()

    def __str__(self):
        return f"Секунд: {self.seconds}\n"


td = TimeDesk(1000)

print(td.show_given_time())





#     class Tank:
#     def __init__(self, nickname, model, year):
#         self.nickname = nickname
#         self.model = model
#         self.year = year
#
#     def description(self):
#         desc = f"{self.nickname} {self.model} is a support tank "
#         return desc
#
#     @staticmethod
#     def add_some():
#         summary = 1+2
#         return summary
#
#     @property
#     def fullname(self):
#         name = self.nickname + ' ' + self.model
#         return name
#
#     @fullname.setter
#     def fullname(self, nickname):
#         self.nickname, self.model = nickname.split()
#
#     # @fullname.deleter
#     # def fullname(self):
#     #     self.nickname = None
#     #     self.model = None
#     #     print("Information is deleted!")
#
#     def __str__(self):
#         return f"Fullname:{self.nickname} {self.model}\n" \
#                f"Year:{self.year}"
#
#
# tonk = Tank (nickname="Churchill",
#              model="III",
#              year="1941")

# print(tonk)
# print(tonk.fullname)
# print(tonk.description())
# tonk.nickname = "Sati"
# print(tonk.fullname)
# # del tonk.fullname
# print(tonk.fullname)

