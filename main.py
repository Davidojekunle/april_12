from fastapi import FastAPI
from pydantic import BaseModel
import re
import random as r
import string as s

class Password(BaseModel):
    password : str


app = FastAPI()


@app.post("/user/")
async def get_user_info(user_input: Password):
    passint = user_input.password

    def check_password(user_password):
        password_pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
        match = re.match(password_pattern, string=user_password) 
        return bool(match)

    def generate_password():
        upper_letters = s.ascii_uppercase
        lower_letters = s.ascii_lowercase
        punctuation = s.punctuation
        numbers = s.digits
        first_letter = ''.join(r.sample(upper_letters, 4))
        second_letter = ''.join(r.sample(lower_letters, 3))
        comma = ''.join(r.sample(punctuation, 4))
        third_value = ''.join(r.sample(numbers ,3))

        all_values = first_letter + second_letter + comma +third_value

        password = list(all_values)
        r.shuffle(password)
        
        shuffled_password = ''.join(password)
        return  shuffled_password


    

    

    if not check_password(passint):
        return {"message" : f"Password is not strong,suggested password: {generate_password()}"}
    else:
        return {"message": "Password is strong"}

    
    


