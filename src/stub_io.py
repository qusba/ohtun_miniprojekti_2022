class StubIO:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs  = []
    

    def input_value(self,value):
        self.inputs.append(value)

    def write(self, value):
        self.outputs.append(value)
    
    def read(self, prompt):
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        else:
            return ""

    def get_inputs(self):
        return self.inputs
    
    def get_outputs(self):
        return self.outputs
    
    def get_output_with_index(self, index):
        return self.outputs[index]