from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import re

app = FastAPI()

class InputData(BaseModel):
    data: List[str]

class ResponseData(BaseModel):
    is_success: bool
    user_id: str
    email: str
    roll_number: str
    odd_numbers: List[str]
    even_numbers: List[str]
    alphabets: List[str]
    special_characters: List[str]
    sum: str
    concat_string: str

@app.post("/bfhl", response_model=ResponseData)
async def process_data(input_data: InputData):
    try:
        data = input_data.data
        
        # Initialize arrays
        odd_numbers = []
        even_numbers = []
        alphabets = []
        special_characters = []
        all_alphabets = []  # For concatenation logic
        numbers_sum = 0
        
        # Process each item in the data array
        for item in data:
            # Check if item is a number
            if item.isdigit():
                num = int(item)
                if num % 2 == 0:
                    even_numbers.append(item)
                else:
                    odd_numbers.append(item)
                numbers_sum += num
            
            # Process characters in the item
            for char in item:
                if char.isalpha():
                    alphabets.append(char.upper())
                    all_alphabets.append(char)
                elif char.isdigit():
                    # Already handled above for whole numbers
                    continue
                else:
                    # Special character
                    if char not in special_characters:
   
