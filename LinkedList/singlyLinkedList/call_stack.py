from stack_using_SLL import Stack


class CallFrame:
    def __init__(self,function_name,params):
        self.function_name=function_name
        self.params=params
    def __str__(self):
        return f"{self.function_name}({self.params})"


class CallStack(Stack):
    
    def push_frame(self, function_name, params):
        frame = CallFrame(function_name, params)
        self.push(frame)
        
    
    def pop_frame(self):
        self.pop()
    
    def show_call_stack(self):
        self.display()
        


call_stack = CallStack(max_size=10)
call_stack.push_frame("main", [])
call_stack.push_frame("calculate", [5])
call_stack.push_frame("factorial", [5])
call_stack.push_frame("factorial", [4])
call_stack.push_frame("factorial", [3])


call_stack.show_call_stack()
