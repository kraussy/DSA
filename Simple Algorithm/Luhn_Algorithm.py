def verify_card_number(card_number):
    if "." in card_number:
        card_number = card_number.replace('.', '')

    elif "-" in card_number:
        card_number = card_number.replace('-', '')

    elif " " in card_number:
        card_number = card_number.replace(' ', '')

    integer_list = [int(i) for i in card_number ]

    integer_list.reverse()
    for i, integer in enumerate(integer_list):
        if (i+1) % 2 == 0:
            value = integer * 2
        
            if value > 9:
                tens, ones = divmod(value, 10)
                result = tens + ones
                integer_list[i] = result
            else:
                integer_list[i] = value
        
    
    print(integer_list)
    total_sum = sum(integer_list)
    print(total_sum)
    if total_sum % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"


       
        


print(verify_card_number('453914889'))
