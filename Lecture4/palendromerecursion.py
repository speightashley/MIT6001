def isPalindrome(s):

    def toChars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters

    def isPal(s):
        print(f"isPal called with {s}")
        if len(s) <= 1:
            print("About to return true from base case")
            return True
        else:
            answer = s[0] == s[-1] and isPal(s[1:-1])
            print(f"About to return {answer} for {s}")
            return answer

    return isPal(toChars(s))


print(isPalindrome("racecar"))
