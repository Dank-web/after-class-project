class ReverseString:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        words = self.text.split()   # শব্দে ভাগ করা 
        words.reverse()             # শব্দগুলো উল্টানো
        return " ".join(words)      # আবার স্ট্রিং বানানো


# Example
s = ReverseString("I love Python")
print(s.reverse())