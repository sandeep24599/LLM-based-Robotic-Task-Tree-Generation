# Dish Preparation Task Tree Generator with Google Gemini

## Project Overview
This project leverages **Google Gemini's Generative AI** to generate task trees for preparing various dishes. The system takes in a list of available ingredients, kitchen appliances, and a menu of dishes, and uses generative models to create task trees detailing the step-by-step process to prepare each dish.

## How It Works
1. **Input**: The project uses files like `kitchen.txt` (containing ingredients, utensils, and appliances), `input.json` (containing menu items and their ingredients), and `prompt.txt` (the guiding prompt).
2. **Processing**: 
   - The script reads the available kitchen tools and ingredients.
   - Using **Google Gemini**, the model generates task trees to prepare the dishes based on the input files.
   - The task tree includes each step, such as handling utensils, ingredients, and applying cooking techniques.
3. **Output**: Task trees for each dish are written as JSON files.

## Key Components
- **`gemini.py`**: The main script that handles input processing, generates prompts, and retrieves task trees from Google Gemini.
- **`kitchen.txt`**: Lists available ingredients and kitchen tools.
- **`input.json`**: Contains various dish recipes, categorized by cuisine type.
- **`prompt.txt`**: Provides the instructions for creating task trees using available resources.
- **Google Gemini**: The AI model used to generate task trees based on the input and prompt.

## Installation & Setup
1. Clone the repository.
2. Install dependencies, including **Google Gemini SDK**.
3. Set the **Google API Key** in your environment variable: `GOOGLE_API_KEY`.
4. Run the main script `gemini.py` to generate task trees.

## Example Dishes
- Grilled Seasoned Chicken Breast
- Classic Grilled Cheese
- Chicken Shawarma
- Margherita Pizza
