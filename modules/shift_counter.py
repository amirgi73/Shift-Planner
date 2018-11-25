from collections import OrderedDict
import random


class ShiftCounter(object):
    def __init__(self, holi_c, pre_c, interns, days, n, ipd=False, spi=False):
        if ipd == spi:
            raise ValueError
        self.interns = interns
        random.shuffle(interns)
        self.days = days
        self.holi_c = holi_c
        self.pre_c = pre_c
        self.nl_c = self.days - (holi_c + pre_c)
        self.shifts = OrderedDict()
        self.holi_shifts = OrderedDict()
        self.pre_shifts = OrderedDict()
        self.nl_shifts = OrderedDict()
        random.shuffle(interns)
        for intern in interns:
            self.shifts[intern] = 0
        random.shuffle(interns)
        for intern in self.interns:
            self.holi_shifts[intern] = 0
        r_interns = list(reversed(self.interns))
        for intern in r_interns:
            self.pre_shifts[intern] = 0
        random.shuffle(self.interns)
        for intern in self.interns:
            self.nl_shifts[intern] = 0
        if ipd:
            self.interns_perday = n
            self.__ipd_init()
        elif spi:
            self.shifts_perintern = n

    def __ipd_init(self):
        t_shifts = self.days * self.interns_perday
        t_holi_shifts = self.holi_c * self.interns_perday
        t_pre_shifts = self.pre_c * self.interns_perday
        t_nl_shifts = t_shifts - (t_pre_shifts + t_holi_shifts)

        while sum(self.shifts.values()) < t_shifts:
            for i, j in self.shifts.items():
                self.shifts[i] += 1
                if sum(self.shifts.values()) >= t_shifts:
                    break

        while sum(self.holi_shifts.values()) < t_holi_shifts:
            for i, j in self.holi_shifts.items():
                self.holi_shifts[i] += 1
                if sum(self.holi_shifts.values()) >= t_holi_shifts:
                    break

        while sum(self.pre_shifts.values()) < t_pre_shifts:
            for i, j in self.pre_shifts.items():
                self.pre_shifts[i] += 1
                if sum(self.pre_shifts.values()) >= t_pre_shifts:
                    break

        while sum(self.nl_shifts.values()) < t_nl_shifts:
            for i, j in self.nl_shifts.items():
                if sum([self.holi_shifts[i], self.pre_shifts[i], self.nl_shifts[i]]) < self.shifts[i]:
                    self.nl_shifts[i] += 1
                    if sum(self.nl_shifts.values()) >= t_nl_shifts:
                        break
                else:
                    continue
        print('Total:\t', self.shifts)
        print('Holi:\t', self.holi_shifts)
        print('Pre:\t', self.pre_shifts)
        print('Nl:\t', self.nl_shifts)

    def __spi_init(self):
        t_shifts = self.shifts_perintern * len(self.interns)
        intern_perday = t_shifts // self.days
        remain = t_shifts % self.days
        intern_perday = [(intern_perday, self.days-remain), (intern_perday+1, remain)]
