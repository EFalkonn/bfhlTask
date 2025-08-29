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
                        special_characters.append(char)
        
        # Remove duplicates from alphabets while preserving order
        unique_alphabets = []
        for alpha in alphabets:
            if alpha not in unique_alphabets:
                unique_alphabets.append(alpha)
        alphabets = unique_alphabets
        
        # Create concatenated string with alternating caps
        reversed_alphabets = all_alphabets[::-1]
        concat_string = ""
        for i, char in enumerate(reversed_alphabets):
            if i % 2 == 0:  # Even index - uppercase
                concat_string += char.upper()
            else:  # Odd index - lowercase
                concat_string += char.lower()
        
        # 🔥 UPDATE THESE WITH YOUR DETAILS:
        response = ResponseData(
            is_success=True,
            user_id="afzal_ahamed_shaheena_20112003",  # Replace with your name and DOB
            email="afzal.ahamed2022@vitstudent.ac.in",         # Replace with your email
            roll_number="22BAI1266",        # Replace with your roll number
            odd_numbers=odd_numbers,
            even_numbers=even_numbers,
            alphabets=alphabets,
            special_characters=special_characters,
            sum=str(numbers_sum),
            concat_string=concat_string
        )
        
        return response
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/")
async def root():
    return {"message": "BFHL API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
