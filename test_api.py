import requests
import json

# Test data from the examples
test_cases = [
    {
        "name": "Example A",
        "data": ["a","1","334","4","R", "$"]
    },
    {
        "name": "Example B", 
        "data": ["2","a", "y", "4", "&", "-", "*", "5","92","b"]
    },
    {
        "name": "Example C",
        "data": ["A","ABcD","DOE"]
    }
]

def test_api_locally():
    """Test the API logic locally without making HTTP requests"""
    from main import process_data
    from main import InputData
    
    print("Testing API logic locally...")
    print("=" * 50)
    
    for test_case in test_cases:
        print(f"\n{test_case['name']}:")
        print(f"Input: {test_case['data']}")
        
        try:
            # Create input data
            input_data = InputData(data=test_case['data'])
            
            # Process using our API function
            import asyncio
            result = asyncio.run(process_data(input_data))
            
            print(f"Output:")
            print(f"  odd_numbers: {result.odd_numbers}")
            print(f"  even_numbers: {result.even_numbers}")
            print(f"  alphabets: {result.alphabets}")
            print(f"  special_characters: {result.special_characters}")
            print(f"  sum: {result.sum}")
            print(f"  concat_string: {result.concat_string}")
            
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    test_api_locally()
