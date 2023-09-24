def frequency(s,l) :
    if l not in s :
        print(l," is not present in the sentence")
    else :
        length = len(s)
        count = 0
        for i in range(length) :
            if s[i] == l :
                count += 1
        print(l," is present ",count," times in the sentence")
s = input("Enter a sentence : ")
l = input("Enter the letter to be found : ")
frequency(s,l)
