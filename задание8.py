s = 'ЯРОСЛАВ'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    s1 = a + b + c + d + e
                    if s1.count('Я') <= 1 and s1.count('Р') <= 1 and s1.count('О') <= 1 and \
                        s1.count('С') <= 1 and s1.count('Л') <= 1 and s1.count('А') <= 1 and \
                        s1.count('В') <= 1 and \
                        s1.count('Р') + s1.count('С') + s1.count('Л') + s1.count('В') > s1.count('Я') + s1.count('О') + s1.count('А') and \
                        s1.count('ЯО') == 0 and s1.count('ЯА') == 0 and s1.count('ОА') == 0 and s1.count('ОЯ') == 0 and s1.count('АЯ') == 0 and s1.count('АО') == 0:
                        count += 1
print(count)