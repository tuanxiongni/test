class UpperOrLower:
    def judge(self, word: str) -> bool:

        if not word:
            return False
        if len(word) == 1:
            return True
        count = 0
        for i in range(1, len(word)):
            if word[i] >= 'A' and word[i] <= 'Z':
                count += 1
            if count == 0 or count == i:
                continue
            else:
                return False
        if count == 0:
            return True
        if count == len(word) - 1:
            if word[0] >= 'A' and word[0] <= 'Z':
                return True
            else:
                return False


if __name__ == '__main__':
    word1 = UpperOrLower()
    while True:
        """主程序"""
        inp=input('输入：')
        judge = word1.judge(inp)
        print(judge)
