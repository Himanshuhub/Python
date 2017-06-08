# Call Center
class Call(object):
    def __init__(self, unique_id, caller_name, caller_phone_number, time_of_call, reason_for_call):
        self.unique_id = unique_id
        self.caller_name = caller_name
        self.caller_phone_number = caller_phone_number
        self.time_of_call = time_of_call
        self.reason_for_call = reason_for_call

    def display(self):
        print "unique_id: ", self.unique_id
        print "caller_name: ", self.caller_name
        print "caller_phone_number: ", self.caller_phone_number
        print "time_of_call: ", self.time_of_call
        print "reason_for_call: ", self.reason_for_call

class CallCenter(object):
    def __init__(self, arg):
        self.arg = arg
    def init(self):
        self.calls = []
        self.queue = [len(self.calls)]
        print calls
        print self.queue
        return self
    def add(self):
        self.calls.append(1)
        return self
    def remove(self):
        for i in range(len(self.calls-1),0, -1):
            self.calls[i-1] = self.calls[i]
    def info(self):
        print "prints the name and phone number for each call in the queue as well as the length of the queue."

call1 = Call("1", "Hi", "858", "12", "reason_for_call")
call1.display()
