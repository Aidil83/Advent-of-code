from typing import List

input = [ '67562556-67743658','62064792-62301480','4394592-4512674','3308-4582','69552998-69828126','9123-12332','1095-1358','23-48','294-400','3511416-3689352','1007333-1150296','2929221721-2929361280','309711-443410','2131524-2335082','81867-97148','9574291560-9574498524','648635477-648670391','1-18','5735-8423','58-72','538-812','698652479-698760276','727833-843820','15609927-15646018','1491-1766','53435-76187','196475-300384','852101-903928','73-97','1894-2622','58406664-58466933','6767640219-6767697605','523453-569572','7979723815-7979848548','149-216' 
         ]

def countInvalids(data: List[str]) -> int:
    total = 0

    for s in data:
        a, b = [], []

        # start of range
        for i in range(len(s)):
            if s[i] == '-':
                break
            a.append(s[i])

        # end of range
        for i in range(len(s)-1, -1, -1):
            if s[i] == '-':
                break
            b.append(s[i])

        start = int(''.join(a))
        end = int(''.join(reversed(b)))

        # iterate actual IDs, not distances
        for num in range(start, end + 1):
            sNum = str(num)

            # must have even length
            if len(sNum) % 2 != 0:
                continue

            mid = len(sNum) // 2
            left = sNum[:mid]
            right = sNum[mid:]

            # repeated twice?
            if left == right:
                total += num

    return total

inputEx = [ '11-22','95-115','998-1012','1188511880-1188511890','222220-222224', '1698522-1698528','446455-446449','38593856-38593862','565653-565659', '824824821-824824827','2121212118-2121212124' ]

# print(countInvalids(input))
print(countInvalids(inputEx))