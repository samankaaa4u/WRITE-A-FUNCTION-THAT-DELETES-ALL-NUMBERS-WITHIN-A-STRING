class Delete_Num:
    def delete(self):

        self.Sentences = "There is 15 percent of people that are good at sleeping."

        self.Answer=''.join([i for i in self.Sentences if not i.isdigit()])
        return self.Answer

test = Delete_Num()
result = test.delete()
print(result)

