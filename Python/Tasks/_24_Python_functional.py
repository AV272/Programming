'''
Filter of valid emails

'''
def fun(s):
    # return True if s is a valid email, else return False
    if s.find('@')==-1 or s.find('.')==-1 or s.count('@')>1 or s.count(".")>1:
        return(False)
    name, web = s.split('@')
    for i in name:
        if i.isalnum() or i=='-' or i=='_':
            continue
        else:
            return(False)
    webs, ext = web.split('.')
    for i2 in webs:
        if i2.isalnum():
            continue
        else:
            return(False)
    if len(ext)>3:
        return(False)
    for i3 in ext:
        if i3.isalpha():
            continue
        else:
            return(False)
    if name=='' or webs=='':
        return(False)
    return(True)

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
