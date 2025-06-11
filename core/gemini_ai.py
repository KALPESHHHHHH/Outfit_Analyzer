# # outfit_recommender/core/gemini_ai.py

# import google.generativeai as genai
# import base64
# from django.conf import settings
# import json

# def configure_genai():
#     """Configure the Gemini API with the API key."""
#     genai.configure(api_key=settings.GEMINI_API_KEY)

# def encode_image_to_base64(image_path):
#     """Encode an image file to base64."""
#     with open(image_path, "rb") as image_file:
#         return base64.b64encode(image_file.read()).decode('utf-8')

# def analyze_outfit(image_path):
#     """
#     Analyze an outfit image using Gemini AI.
    
#     Args:
#         image_path: Path to the image file
        
#     Returns:
#         dict: Analysis results including whether it looks good and suggestions
#     """
#     configure_genai()
    
#     # Get the Gemini Pro Vision model
#     model = genai.GenerativeModel('gemini-pro-vision')
    
#     # Encode the image
#     image_data = encode_image_to_base64(image_path)
    
#     # Prepare the prompt
#     prompt = """
#     Analyze this outfit image and provide detailed feedback:
    
#     1. Does this outfit look good? (Yes/No)
#     2. What are the strengths of this outfit? (List at least 3 points)
#     3. What could be improved about this outfit? (List at least 3 suggestions)
#     4. Suggest 3 alternative outfit combinations that would work better.
    
#     Format your response as a JSON object with the following structure:
#     {
#         "looks_good": true/false,
#         "strengths": ["point1", "point2", "point3"],
#         "improvements": ["suggestion1", "suggestion2", "suggestion3"],
#         "alternative_outfits": [
#             {"name": "Outfit 1", "description": "Description of outfit 1"},
#             {"name": "Outfit 2", "description": "Description of outfit 2"},
#             {"name": "Outfit 3", "description": "Description of outfit 3"}
#         ]
#     }
#     """
    
#     try:
#         # Call the Gemini API with the image
#         response = model.generate_content([
#             prompt,
#             {
#                 "inlineData": {
#                     "mimeType": "image/jpeg",
#                     "data": image_data
#                 }
#             }
#         ])
        
#         # Extract the JSON response
#         response_text = response.text
        
#         # Find JSON content in the response
#         start_idx = response_text.find('{')
#         end_idx = response_text.rfind('}') + 1
        
#         if start_idx >= 0 and end_idx > start_idx:
#             json_str = response_text[start_idx:end_idx]
#             result = json.loads(json_str)
#             return result
#         else:
#             # Fallback if JSON parsing fails
#             return {
#                 "looks_good": False,
#                 "strengths": ["Could not analyze strengths"],
#                 "improvements": ["Could not analyze improvements"],
#                 "alternative_outfits": [
#                     {"name": "Casual Outfit", "description": "Could not generate recommendation"}
#                 ]
#             }
            
#     except Exception as e:
#         print(f"Error analyzing outfit: {e}")
#         return {
#             "looks_good": False,
#             "strengths": ["Error analyzing outfit"],
#             "improvements": ["Please try again with a clearer image"],
#             "alternative_outfits": [
#                 {"name": "Error", "description": "Could not generate recommendations"}
#             ]
#         }


# outfit_recommender/core/gemini_ai.py

# import google.generativeai as genai
# import base64
# from django.conf import settings
# import json
# from datetime import datetime

# def configure_genai():
#     """Configure the Gemini API with the API key."""
#     genai.configure(api_key=settings.GEMINI_API_KEY)

# def encode_image_to_base64(image_path):
#     """Encode an image file to base64."""
#     with open(image_path, "rb") as image_file:
#         return base64.b64encode(image_file.read()).decode('utf-8')

# def analyze_outfit(image_path):
#     """
#     Analyze an outfit image using Gemini AI.
    
#     Args:
#         image_path: Path to the image file
        
#     Returns:
#         dict: Analysis results including whether it looks good and suggestions
#     """
#     configure_genai()
    
#     try:
#         # Use the recommended gemini-1.5-flash model
#         model = genai.GenerativeModel('gemini-1.5-flash')
        
#         # Encode the image
#         image_data = encode_image_to_base64(image_path)
        
#         # Prepare the prompt with current date context
#         current_date = datetime.now().strftime("%B %d, %Y")
#         prompt = f"""
#         As a fashion expert analyzing this outfit on {current_date}, provide detailed feedback:
        
#         1. Does this outfit look good? (Yes/No)
#         2. What are the strengths of this outfit? (List at least 3 points)
#         3. What could be improved about this outfit? (List at least 3 suggestions)
#         4. Suggest 3 alternative outfit combinations that would work better.
        
#         Format your response as a JSON object with the following structure:
#         {{
#             "looks_good": true/false,
#             "strengths": ["point1", "point2", "point3"],
#             "improvements": ["suggestion1", "suggestion2", "suggestion3"],
#             "alternative_outfits": [
#                 {{"name": "Outfit 1", "description": "Description of outfit 1"}},
#                 {{"name": "Outfit 2", "description": "Description of outfit 2"}},
#                 {{"name": "Outfit 3", "description": "Description of outfit 3"}}
#             ]
#         }}
#         """
        
#         # Call the Gemini API with the correct format
#         response = model.generate_content(
#             [
#                 prompt,
#                 {
#                     "mime_type": "image/jpeg",
#                     "data": image_data
#                 }
#             ],
#             generation_config={
#                 "temperature": 0.5,
#                 "max_output_tokens": 2048,
#             }
#         )
        
#         # Extract and parse the JSON response
#         response_text = response.text
#         start_idx = response_text.find('{')
#         end_idx = response_text.rfind('}') + 1
        
#         if start_idx >= 0 and end_idx > start_idx:
#             return json.loads(response_text[start_idx:end_idx])
            
#     except Exception as e:
#         print(f"Error analyzing outfit: {e}")
    
#     # Fallback response if anything fails
#     return {
#         "looks_good": False,
#         "strengths": ["Could not analyze outfit"],
#         "improvements": ["Please try again with a clearer image"],
#         "alternative_outfits": [
#             {"name": "Classic Look", "description": "Try neutral colors with clean lines"},
#             {"name": "Smart Casual", "description": "Combine tailored pieces with relaxed items"},
#             {"name": "Error", "description": "Could not generate recommendations"}
#         ]
#     }

# gemini_ai.py

# import google.generativeai as genai
# import base64
# from django.conf import settings
# import json
# from datetime import datetime

# def configure_genai():
#     """Configure the Gemini API with the API key."""
#     genai.configure(api_key=settings.GEMINI_API_KEY)

# def encode_image_to_base64(image_path):
#     """Encode an image file to base64."""
#     with open(image_path, "rb") as image_file:
#         return base64.b64encode(image_file.read()).decode('utf-8')

# def analyze_outfit(image_path, user_prompt=None):
#     """
#     Analyze an outfit image using Gemini AI.

#     Args:
#         image_path: Path to the image file
#         user_prompt: Optional user question (e.g., "Is this outfit looking good on me?")
        
#     Returns:
#         dict: Analysis results including score, explanation, strengths, improvements, and outfit ideas
#     """
#     configure_genai()

#     try:
#         model = genai.GenerativeModel('gemini-1.5-flash')
#         image_data = encode_image_to_base64(image_path)
#         current_date = datetime.now().strftime("%B %d, %Y")

#         # Build the prompt based on whether user prompt exists
#         if user_prompt:
#             prompt = f"""
#             Today is {current_date}.
#             You are a top-tier AI fashion stylist.

#             The user uploaded an image and asked: "{user_prompt}"

#             Please provide:
#             1. A percentage score (0 to 100) on how good the outfit looks.
#             2. A short explanation of the score.
#             3. Three strengths of the outfit.
#             4. Three areas of improvement.
#             5. Three alternative outfit ideas for improvement (with name + description).

#             Respond only in the following JSON structure:
#             {{
#                 "score": 80,
#                 "score_explanation": "The outfit complements your body shape and color palette, but shoes could be improved.",
#                 "strengths": ["Nice color matching", "Good fit", "Trendy accessories"],
#                 "improvements": ["Try a different pair of shoes", "Add a layer", "Try a darker shade for contrast"],
#                 "alternative_outfits": [
#                     {{"name": "Urban Casual", "description": "Ripped jeans, white tee, and leather jacket"}},
#                     {{"name": "Smart Street", "description": "Fitted chinos, loafers, and casual blazer"}},
#                     {{"name": "Chic Workwear", "description": "Pencil skirt, blouse, and pumps"}}
#                 ]
#             }}
#             """
#         else:
#             prompt = f"""
#             Today is {current_date}.
#             You are a professional AI fashion consultant.

#             Please evaluate the uploaded outfit image and return the following:
#             1. A percentage score (0 to 100) for how good the outfit looks.
#             2. A short explanation of why it got that score.
#             3. Three strong points about the outfit.
#             4. Three things to improve.
#             5. Three better outfit ideas, each with a name and description.

#             Use this exact JSON format:
#             {{
#                 "score": 75,
#                 "score_explanation": "Well coordinated outfit with nice tones, but lacks structure.",
#                 "strengths": [...],
#                 "improvements": [...],
#                 "alternative_outfits": [...]
#             }}
#             """

#         response = model.generate_content(
#             [
#                 prompt,
#                 {
#                     "mime_type": "image/jpeg",
#                     "data": image_data
#                 }
#             ],
#             generation_config={
#                 "temperature": 0.7,
#                 "max_output_tokens": 2048,
#             }
#         )

#         # Parse the JSON from response
#         response_text = response.text
#         start_idx = response_text.find('{')
#         end_idx = response_text.rfind('}') + 1

#         if start_idx >= 0 and end_idx > start_idx:
#             return json.loads(response_text[start_idx:end_idx])

#     except Exception as e:
#         print(f"Error analyzing outfit: {e}")

#     # Fallback
#     return {
#         "score": 0,
#         "score_explanation": "Sorry, we couldn't analyze the outfit. Please upload a clearer image.",
#         "strengths": ["Image unclear or low quality"],
#         "improvements": ["Ensure full outfit is visible", "Use good lighting", "Avoid blur"],
#         "alternative_outfits": [
#             {"name": "Fallback Classic", "description": "White shirt with dark jeans and clean sneakers"},
#             {"name": "Neutral Smart", "description": "Beige chinos with navy blue button-up"},
#             {"name": "Trendy Casual", "description": "Oversized tee, cargos, and high-top shoes"}
#         ]
#     }


# import google.generativeai as genai
# import base64
# from django.conf import settings
# import json
# from datetime import datetime

# def configure_genai():
#     """Configure the Gemini API with the API key."""
#     genai.configure(api_key=settings.GEMINI_API_KEY)

# def encode_image_to_base64(image_path):
#     """Encode an image file to base64."""
#     with open(image_path, "rb") as image_file:
#         return base64.b64encode(image_file.read()).decode('utf-8')

# def analyze_outfit(image_path, user_prompt=None):
#     """
#     Analyze an outfit image using Gemini AI.

#     Args:
#         image_path: Path to the image file
#         user_prompt: Optional user question (e.g., "Is this outfit looking good on me?")

#     Returns:
#         dict: Analysis results including score, explanation, strengths, improvements, and outfit ideas
#     """
#     configure_genai()

#     try:
#         model = genai.GenerativeModel('gemini-1.5-flash')
#         image_data = encode_image_to_base64(image_path)
#         current_date = datetime.now().strftime("%B %d, %Y")

#         # Build the prompt based on whether user prompt exists
#         if user_prompt:
#             prompt = f"""
#             Today is {current_date}.
#             You are a top-tier AI fashion stylist.

#             The user uploaded an image and asked: "{user_prompt}"

#             Please provide:
#             1. A percentage score (0 to 100) on how good the visible parts of the outfit look.
#             2. A short explanation of the score, considering any missing context.
#             3. Three strengths of the visible outfit.
#             4. Three areas of improvement, including specific suggestions for completing the outfit if incomplete.
#             5. Three alternative outfit ideas for improvement (with name + description), considering the visible items.
#             6. Specific recommendations for items that complement the visible ones (e.g., jeans color for a shirt).

#             Respond only in the following JSON structure:
#             {{
#                 "score": 60,
#                 "score_explanation": "The black polo shirt is stylish, but the image lacks a complete outfit for full assessment.",
#                 "strengths": ["Good fit", "Classic style", "Versatile color"],
#                 "improvements": ["Pair with grey jeans", "Add a belt", "Consider layering with a jacket"],
#                 "alternative_outfits": [
#                     {{"name": "Casual Chic", "description": "Pair with grey jeans and sneakers"}},
#                     {{"name": "Smart Casual", "description": "Wear with beige chinos and loafers"}},
#                     {{"name": "Edgy Street", "description": "Combine with black jeans and boots"}}
#                 ]
#             }}
#             """
#         else:
#             prompt = f"""
#             Today is {current_date}.
#             You are a professional AI fashion consultant.

#             Please evaluate the uploaded outfit image and return the following:
#             1. A percentage score (0 to 100) for how good the visible parts of the outfit look.
#             2. A short explanation of why it got that score, considering any missing context.
#             3. Three strong points about the visible outfit.
#             4. Three things to improve, including specific suggestions for completing the outfit if incomplete.
#             5. Three better outfit ideas, each with a name and description, considering the visible items.
#             6. Specific recommendations for items that complement the visible ones (e.g., jeans color for a shirt).

#             Use this exact JSON format:
#             {{
#                 "score": 50,
#                 "score_explanation": "The black polo shirt is stylish, but the image lacks a complete outfit for full assessment.",
#                 "strengths": [...],
#                 "improvements": [...],
#                 "alternative_outfits": [...]
#             }}
#             """

#         response = model.generate_content(
#             [
#                 prompt,
#                 {
#                     "mime_type": "image/jpeg",
#                     "data": image_data
#                 }
#             ],
#             generation_config={
#                 "temperature": 0.7,
#                 "max_output_tokens": 2048,
#             }
#         )

#         # Parse the JSON from response
#         response_text = response.text
#         start_idx = response_text.find('{')
#         end_idx = response_text.rfind('}') + 1

#         if start_idx >= 0 and end_idx > start_idx:
#             return json.loads(response_text[start_idx:end_idx])

#     except Exception as e:
#         print(f"Error analyzing outfit: {e}")

#     # Fallback
#     return {
#         "score": 0,
#         "score_explanation": "Sorry, we couldn't analyze the outfit. Please upload a clearer image.",
#         "strengths": ["Image unclear or low quality"],
#         "improvements": ["Ensure full outfit is visible", "Use good lighting", "Avoid blur"],
#         "alternative_outfits": [
#             {"name": "Fallback Classic", "description": "White shirt with dark jeans and clean sneakers"},
#             {"name": "Neutral Smart", "description": "Beige chinos with navy blue button-up"},
#             {"name": "Trendy Casual", "description": "Oversized tee, cargos, and high-top shoes"}
#         ]
#     }












import google.generativeai as genai
import base64
from django.conf import settings
import json
from datetime import datetime
from django.http import JsonResponse
import os 
def configure_genai():
    """Configure the Gemini API with the API key."""
    genai.configure(api_key=settings.GEMINI_API_KEY)

def encode_image_to_base64(image_path):
    """Encode an image file to base64."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def analyze_outfit(image_path, user_prompt=None):
    """
    Analyze an outfit image using Gemini AI.

    Args:
        image_path: Path to the image file
        user_prompt: Optional user question (e.g., "Will I wear this on Ganesh Chaturthi?")

    Returns:
        dict: Analysis results including a direct response to the user's query
    """
    configure_genai()

    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        image_data = encode_image_to_base64(image_path)
        # print(image_data)
        current_date = datetime.now().strftime("%B %d, %Y")

        # Build the prompt to focus on the user's specific question
        prompt = f"""
        Today is {current_date}.
        You are a top-tier AI fashion stylist.

        The user uploaded an image and asked: "{user_prompt}"

        Please provide a direct response to the user's question first. Then, include the following if relevant:
        1. A percentage score (0 to 100) for how good the visible parts of the outfit look.
        2. A short explanation of the score, considering any missing context.
        3. Three strengths of the visible outfit.
        4. Three areas of improvement, including specific suggestions for completing the outfit if incomplete.
        5. Three alternative outfit ideas for improvement (with name + description), considering the visible items.
        6. Specific recommendations for items that complement the visible ones (e.g., jewelry, footwear).
        7. A detailed response in 5 to 6 sentences.
        8. Suggestions in 5 to 6 sentences.
        9. An analysis of whether the photo is suitable for an Instagram post, if the user asks about Instagram.
        10. Enhanced captions for the Instagram post if suitable and if the user asks about Instagram.

        Respond only in the following JSON structure:
        {{
            "direct_response": "<direct_answer_to_user_query>",
            "score": <score>,
            "score_explanation": "<explanation>",
            "strengths": ["<strength1>", "<strength2>", "<strength3>"],
            "improvements": ["<improvement1>", "<improvement2>", "<improvement3>"],
            "alternative_outfits": [
                {{"name": "<outfit1_name>", "description": "<outfit1_description>"}},
                {{"name": "<outfit2_name>", "description": "<outfit2_description>"}},
                {{"name": "<outfit3_name>", "description": "<outfit3_description>"}}
            ],
            "response": "<detailed_response>",
            "suggestions": "<suggestions>",
            "instagram_analysis": {{
                "feedback": "<instagram_feedback>",
                "captions": ["<caption1>", "<caption2>", "<caption3>"]
            }}
        }}
        """

        response = model.generate_content(
            [
                prompt,
                {
                    "mime_type": "image/jpeg",
                    "data": image_data
                }
            ],
            generation_config={
                "temperature": 0.7,
                "max_output_tokens": 2048,
            }
        )

        # Parse the JSON from response
        response_text = response.text
        print(response)
        print(response_text)
        start_idx = response_text.find('{')
        end_idx = response_text.rfind('}') + 1

        if start_idx >= 0 and end_idx > start_idx:
            return json.loads(response_text[start_idx:end_idx])

    except Exception as e:
        print(f"Error analyzing outfit: {e}")

    # Fallback
    return {
        "direct_response": "I'm sorry, I couldn't analyze the outfit. Please upload a clearer image.",
        "score": 0,
        "score_explanation": "Sorry, we couldn't analyze the outfit. Please upload a clearer image.",
        "strengths": ["Image unclear or low quality"],
        "improvements": ["Ensure full outfit is visible", "Use good lighting", "Avoid blur"],
        "alternative_outfits": [
            {"name": "Fallback Classic", "description": "White shirt with dark jeans and clean sneakers"},
            {"name": "Neutral Smart", "description": "Beige chinos with navy blue button-up"},
            {"name": "Trendy Casual", "description": "Oversized tee, cargos, and high-top shoes"}
        ],
        "response": "Your outfit looks great! The light blue dress is elegant and perfect for outdoor settings. Consider adding more jewelry to enhance the look. Experimenting with a different hairstyle could also complement the outfit well. A small clutch or bag could add a nice touch. Overall, the outfit is well-coordinated and stylish.",
        "suggestions": "Try adding more jewelry like bangles or a statement necklace. Experiment with a different hairstyle to see what complements the outfit best. Consider carrying a small clutch or bag to enhance the look. A flowy maxi dress in a similar pastel shade could be a great alternative. A light blue palazzo set with a contrasting embroidered top is another stylish option.",
        "instagram_analysis": {
            "feedback": "This photo is suitable for an Instagram post. The outfit is stylish and well-coordinated.",
            "captions": [
                "Feeling elegant in my light blue dress! 👗💙 #OOTD #Fashion",
                "Outdoor vibes in my favorite dress! 🌳👗 #StyleInspo #FashionBlogger",
                "Loving this light blue outfit! 💕👗 #FashionGram #OutfitIdeas"
            ]
        }
    }

# views.py

def fashion_feedback_view(request):
    """API view to handle fashion feedback dynamically via image + prompt."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            question = data.get('question', "Is outfit looking good on me?")
            image_url = data.get('image_path')

            # Assuming image_url is accessible and can be converted to a local path
            image_path = os.path.join(settings.MEDIA_ROOT, image_url.split('/media/')[-1])

            result = analyze_outfit(image_path, user_prompt=question)

            return JsonResponse({
                "direct_response": result.get("direct_response", ""),
                "looks_good": result.get('score', 0) >= 70 if 'score' in result else None,  # Assuming 70% is the threshold for "looks good"
                "percentage_score": result.get('score', 0),
                "explanation": result.get('score_explanation', ""),  # Corrected key
                "strengths": result.get('strengths', []),
                "improvements": result.get('improvements', []),
                "alternative_outfits": result.get('alternative_outfits', []),
                "response": result.get('response', ""),
                "suggestions": result.get('suggestions', ""),
                "instagram_analysis": result.get('instagram_analysis', {})
            })

        except Exception as e:
            return JsonResponse({
                "error": f"Failed to analyze: {str(e)}"
            }, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)
