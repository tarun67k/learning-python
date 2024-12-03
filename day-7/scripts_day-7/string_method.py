email = "tarunkolli553@test.com"

# Check if email contains exactly one '@' symbol
if email.count('@') == 1:
    first_part, last_part = email.split('@')
    if first_part and last_part:
        # Check if last part contains at least one '.'
        if '.' in last_part:
            # Check if the domain has characters before and after the '.'
            domain_name, domain_extension = last_part.rsplit('.', 1)
            
            if domain_name and domain_extension:
                print(f"{email} is a valid email address.")
            else:
                print(f"{email} is not a valid email address.")
        else:
            print(f"{email} is not a valid email address.")
    else:
        print(f"{email} is not a valid email address.")
else:
    print(f"{email} is not a valid email address.")