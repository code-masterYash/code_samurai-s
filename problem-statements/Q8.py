def sanitize_email(raw_input: str) -> str:
    
    cleaned = raw_input.strip()
    cleaned = cleaned.lower()
    
   
    if cleaned.count("@") != 1:
        return "Invalid Email"
    
   
    if cleaned == "":
        return "Invalid Email"
    
    return cleaned
