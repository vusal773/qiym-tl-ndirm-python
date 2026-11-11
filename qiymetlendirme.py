def level(v):
    if v < -105:
        return 'zəif'
    else:
        -105 <= v < -95
        return 'yaxşı'
    

parts = input().split()
values = []
missing = 0
for p in parts:
    if p == 'N/A':
        missing += 1
    else:
        values.append(float(p))
        v = float(p)
        print(v, '→', level(v))

counts = {"zəif": 0, "orta": 0, "yaxşı": 0}
for v in values:
    s = level(v)
    counts[s] += 1
print(counts)
        
print('Min deyer', min(values))
print('Max deyer', max(values))
sum_values = sum(values)
avarage = sum_values / len(values)
print('Ortalama', round(avarage, 1))

share = round(counts['zəif'] / len(values) * 100, 1)
print('Zəif payı:', share, '%')
#######################################
if share >= 30:
    print('gonder')
if share >= 10:
    print('saxla')
else:
    print('normal')

current = 0
best = 0
for v in values:
    if level(v) == 'zeif':
        current += 1

    if current > best:
        best = current

    else:
        current = 0
print('En uzun zeif seriya', best)
########################################################