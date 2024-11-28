from datetime import time, date
class Dollar:
    def __init__(self, value) -> None:
        self.value = round(value, 2)
    def __str__(self) -> str:
        return f"$ {self.value}"

class Ticket:
    def __init__(self, hours:int, salary:Dollar, penalty:Dollar) -> None:
        self.hours = time(hour=hours).hour
        self.salary = salary
        self.penalty = penalty

    @staticmethod
    def compare(t1:'Ticket', t2:'Ticket', by="hour"):
        match by:
            case 'hour':
                result = Ticket._compareValues(t1.hours, t2.hours)
                if not result:
                    return Ticket.compare(t1, t2, by='salary')
            case 'salary':
                result = Ticket._compareValues(t1.salary.value, t2.salary.value)
                if not result:
                    return Ticket.compare(t1, t2, by="penalty")
            case 'penalty':
                result = Ticket._compareValues(t1.penalty.value, t2.penalty.value)
        
        return result
    
    @staticmethod
    def daytohour(day:date):
        return day.day*60
    @staticmethod
    def _compareValues(v1, v2):
        if v1 > v2:
            return 1
        elif v1 < v2:
            return -1
        elif v1 == v2:
            return 0
    
    def __str__(self) -> str:
        return f"deadline: {self.hours}, salary: {self.salary}, penalty: {self.penalty}"
class TicketList:
    def __init__(self, array:list = []) -> None:
        self.array = array
        self.total = {'hour':0, 'payment':0, 'penalty':0}
    
    def insert(self, t:Ticket):
        self.array.append(t)
        self.total['hour'] += t.hours
        self.total['payment'] += t.salary.value
        self.total['penalty'] += t.penalty.value

deadline = date(day=2)
tickets= [Ticket(1, Dollar(23), Dollar(10)),Ticket(4, Dollar(20), Dollar(10)), Ticket(4, Dollar(20), Dollar(15)), Ticket(15, Dollar(25), Dollar(30)), Ticket(20,Dollar(20), Dollar(15))]
t = TicketList()
# for ticket in tickets:
#     t.insert(ticket)
end = len(tickets)-1

while end >= 0:
    temp = tickets[end].hours() + t.total['hour']
    if temp < Ticket.daytohour(deadline):
        t.insert(temp)