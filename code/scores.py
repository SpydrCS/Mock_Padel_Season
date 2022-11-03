class Score:
    def __init__(self, score):
        self.score = score

    def __str__(self):
        return f"{self.score}"

    def get_winner(self):
        str1 = ""
        str2 = ""
        for ch in self.score[::-1]:
            if ch == "-":
                str2 = str1
            elif ch == " ":
                break
            else:
                str1 += ch
        
        if int(str1) > int(str2):
            return 1
        else:
            return 2