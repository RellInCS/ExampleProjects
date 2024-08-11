class DPDA:
    def __init__(self):
    
        self.transitions = {
            ('q0', 'a', 'Z'): ('q0', 'aZ'),  
            ('q0', 'b', 'Z'): ('q0', 'bZ'),  
            ('q0', 'a', 'a'): ('q0', 'aa'), 
            ('q0', 'b', 'a'): ('q1', ''),    
            ('q1', 'b', 'a'): ('q1', ''),    
            ('q1', '', 'Z'): ('q2', 'Z')
            }
        self.accepting_states = {'q2'}

    def recognize(self, input_string):
        
        current_state = 'q0'
        stack = ['Z']

        for symbol in input_string:
            if (current_state, symbol, stack[-1]) in self.transitions:
                new_state, stack_action = self.transitions[(current_state, symbol, stack[-1])]
                
                if stack_action:
                    stack.pop()
                    stack.extend(stack_action)

                current_state = new_state
            else:
                return False

        return current_state in self.accepting_states and stack == ['Z']

