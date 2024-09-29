from datetime import datetime

def is_it_valid(pic: str) -> bool:
    control_chars = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    
    if len(pic) != 11:
        return False

    try:
        day = int(pic[0:2])
        month = int(pic[2:4])
        year = int(pic[4:6])
        century_marker = pic[6]
        personal_id = pic[7:10]
        control_char = pic[-1]
        
        if century_marker == "+":
            full_year = 1800 + year
        elif century_marker == "-":
            full_year = 1900 + year
        elif century_marker == "A":
            full_year = 2000 + year
        else:
            return False
        
        datetime(full_year, month, day)

        nine_digit_number = int(f"{pic[0:6]}{personal_id}")
        remainder = nine_digit_number % 31
        
        return control_char == control_chars[remainder]
    
    except:
        return False