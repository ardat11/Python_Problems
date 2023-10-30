if __name__ == '__main__':
    s = input()

is_num = any(c.isalnum() for c in s)

is_alpha = any(c.isalpha() for c in s)

is_digit = any(c.isdigit() for c in s)

is_lower = any(c.islower() for c in s)

is_upper = any(c.isupper() for c in s)

print(is_num)

print(is_alpha)

print(is_digit)

print(is_lower)

print(is_upper)