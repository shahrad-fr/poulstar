import random
password = input("password chandharfi ? : ");password = int(password)
print (''.join([random.choice
                (
                    'abcdefghijklmnopqrstuvwxyz'
                    +
                    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                    +
                    '!@#$%^&*()_+,><;./?`'
                    +
                    '1234567890'
                )
                for i in range(password)]))