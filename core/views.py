# from django.shortcuts import render, redirect, get_object_or_404
# from django.http import JsonResponse
# from django.contrib import messages
# from django.conf import settings
# from .models import OutfitUpload, OutfitRecommendation
# from .forms import OutfitUploadForm
# from .gemini_ai import analyze_outfit
# import os

# def home(request):
#     """Home page view."""
#     return render(request, 'core/home.html')

# def upload(request):
#     """Upload page view for outfit images."""
#     if request.method == 'POST':
#         form = OutfitUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             outfit = form.save()

#             try:
#                 # Get the full path to the uploaded image
#                 image_path = os.path.join(settings.MEDIA_ROOT, outfit.image.name)

#                 # Analyze the outfit using Gemini AI
#                 analysis = analyze_outfit(image_path, user_prompt="Is outfit looking good on me?")

#                 # Create a recommendation based on the analysis
#                 recommendation = OutfitRecommendation(
#                     outfit=outfit,
#                     looks_good=analysis.get('score', 0) >= 70,  # Assuming 70% is the threshold for "looks good"
#                     percentage_score=analysis.get('score', 0),
#                     explanation=analysis.get('score_explanation', "")
#                 )
#                 recommendation.set_feedback_json({
#                     'strengths': analysis.get('strengths', []),
#                     'improvements': analysis.get('improvements', [])
#                 })
#                 recommendation.set_suggestions_json({
#                     'alternative_outfits': analysis.get('alternative_outfits', [])
#                 })
#                 recommendation.save()

#                 return redirect('core:recommendation_detail', pk=outfit.id)

#             except Exception as e:
#                 messages.error(request, f"Error analyzing outfit: {str(e)}")
#                 return redirect('core:upload')
#     else:
#         form = OutfitUploadForm()

#     return render(request, 'core/upload.html', {'form': form})

# def recommendations(request):
#     """View all recommendations."""
#     outfits = OutfitUpload.objects.filter(recommendation__isnull=False).order_by('-uploaded_at')
#     return render(request, 'core/recommendations.html', {'outfits': outfits})

# def recommendation_detail(request, pk):
#     """View a specific recommendation."""
#     outfit = get_object_or_404(OutfitUpload, pk=pk)
#     if not hasattr(outfit, 'recommendation'):
#         messages.error(request, "No recommendation found for this outfit.")
#         return redirect('upload')

#     recommendation = outfit.recommendation
#     feedback = recommendation.get_feedback_json()
#     suggestions = recommendation.get_suggestions_json()

#     context = {
#         'outfit': outfit,
#         'recommendation': recommendation,
#         'strengths': feedback.get('strengths', []),
#         'improvements': feedback.get('improvements', []),
#         'alternative_outfits': suggestions.get('alternative_outfits', []),
#         'percentage_score': recommendation.percentage_score,
#         'explanation': recommendation.explanation
#     }

#     return render(request, 'core/recommendation_detail.html', context)

# def about(request):
#     """About page view."""
#     return render(request, 'core/about.html')

# def fashion_feedback_view(request):
#     """API view to handle fashion feedback dynamically via image + prompt."""
#     if request.method == 'POST' and request.FILES.get('image'):
#         image_file = request.FILES['image']
#         question = request.POST.get('question', "Is outfit looking good on me?")
#         temp_path = f'/tmp/{image_file.name}'

#         try:
#             with open(temp_path, 'wb+') as f:
#                 for chunk in image_file.chunks():
#                     f.write(chunk)

#             result = analyze_outfit(temp_path, user_prompt=question)

#             return JsonResponse({
#                 "looks_good": result.get('score', 0) >= 70,  # Assuming 70% is the threshold for "looks good"
#                 "percentage_score": result.get('score', 0),
#                 "explanation": result.get('score_explanation', ""),
#                 "strengths": result.get('strengths', []),
#                 "improvements": result.get('improvements', []),
#                 "alternative_outfits": result.get('alternative_outfits', [])
#             })

#         except Exception as e:
#             return JsonResponse({
#                 "error": f"Failed to analyze: {str(e)}"
#             }, status=500)

#     return JsonResponse({"error": "Invalid request"}, status=400)








# from django.shortcuts import render, redirect, get_object_or_404
# from django.http import JsonResponse
# from django.contrib import messages
# from django.conf import settings
# from django.views.decorators.csrf import csrf_exempt
# from .models import OutfitUpload, OutfitRecommendation
# from .forms import OutfitUploadForm
# from .gemini_ai import analyze_outfit
# import os
# import json

# def home(request):
#     """Home page view."""
#     return render(request, 'core/home.html')

# def upload(request):
#     """Upload page view for outfit images."""
#     if request.method == 'POST':
#         form = OutfitUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             outfit = form.save()

#             try:
#                 # Get the full path to the uploaded image
#                 image_path = os.path.join(settings.MEDIA_ROOT, outfit.image.name)

#                 # Analyze the outfit using Gemini AI
#                 analysis = analyze_outfit(image_path, user_prompt="Is outfit looking good on me?")

#                 # Create a recommendation based on the analysis
#                 recommendation = OutfitRecommendation(
#                     outfit=outfit,
#                     looks_good=analysis.get('score', 0) >= 70,  # Assuming 70% is the threshold for "looks good"
#                     percentage_score=analysis.get('score', 0),
#                     explanation=analysis.get('score_explanation', "")
#                 )
#                 recommendation.set_feedback_json({
#                     'strengths': analysis.get('strengths', []),
#                     'improvements': analysis.get('improvements', [])
#                 })
#                 recommendation.set_suggestions_json({
#                     'alternative_outfits': analysis.get('alternative_outfits', [])
#                 })
#                 recommendation.save()

#                 return redirect('core:recommendation_detail', pk=outfit.id)

#             except Exception as e:
#                 messages.error(request, f"Error analyzing outfit: {str(e)}")
#                 return redirect('core:upload')
#     else:
#         form = OutfitUploadForm()

#     return render(request, 'core/upload.html', {'form': form})

# def recommendations(request):
#     """View all recommendations."""
#     outfits = OutfitUpload.objects.filter(recommendation__isnull=False).order_by('-uploaded_at')
#     return render(request, 'core/recommendations.html', {'outfits': outfits})

# def recommendation_detail(request, pk):
#     """View a specific recommendation."""
#     outfit = get_object_or_404(OutfitUpload, pk=pk)
#     if not hasattr(outfit, 'recommendation'):
#         messages.error(request, "No recommendation found for this outfit.")
#         return redirect('upload')

#     recommendation = outfit.recommendation
#     feedback = recommendation.get_feedback_json()
#     suggestions = recommendation.get_suggestions_json()

#     context = {
#         'outfit': outfit,
#         'recommendation': recommendation,
#         'strengths': feedback.get('strengths', []),
#         'improvements': feedback.get('improvements', []),
#         'alternative_outfits': suggestions.get('alternative_outfits', []),
#         'percentage_score': recommendation.percentage_score,
#         'explanation': recommendation.explanation  # Corrected key
#     }

#     return render(request, 'core/recommendation_detail.html', context)

# def about(request):
#     """About page view."""
#     return render(request, 'core/about.html')

# @csrf_exempt
# def fashion_feedback_view(request):
#     """API view to handle fashion feedback dynamically via image + prompt."""
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             question = data.get('question', "Is outfit looking good on me?")
#             image_url = data.get('image_path')

#             # Assuming image_url is accessible and can be converted to a local path
#             image_path = os.path.join(settings.MEDIA_ROOT, image_url.split('/media/')[-1])

#             result = analyze_outfit(image_path, user_prompt=question)

#             return JsonResponse({
#                 "looks_good": result.get('score', 0) >= 70,  # Assuming 70% is the threshold for "looks good"
#                 "percentage_score": result.get('score', 0),
#                 "explanation": result.get('score_explanation', ""),  # Corrected key
#                 "strengths": result.get('strengths', []),
#                 "improvements": result.get('improvements', []),
#                 "alternative_outfits": result.get('alternative_outfits', [])
#             })

#         except Exception as e:
#             return JsonResponse({
#                 "error": f"Failed to analyze: {str(e)}"
#             }, status=500)

#     return JsonResponse({"error": "Invalid request"}, status=400)















from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import OutfitUpload, OutfitRecommendation
from .forms import OutfitUploadForm
from .gemini_ai import analyze_outfit
import os
import json

def home(request):
    """Home page view."""
    return render(request, 'core/home.html')

def upload(request):
    """Upload page view for outfit images."""
    if request.method == 'POST':
        form = OutfitUploadForm(request.POST, request.FILES)
        if form.is_valid():
            outfit = form.save()

            try:
                # Get the full path to the uploaded image
                image_path = os.path.join(settings.MEDIA_ROOT, outfit.image.name)

                # Analyze the outfit using Gemini AI
                analysis = analyze_outfit(image_path, user_prompt="Is outfit looking good on me?")

                # Create a recommendation based on the analysis
                recommendation = OutfitRecommendation(
                    outfit=outfit,
                    looks_good=analysis.get('score', 0) >= 70,  # Assuming 70% is the threshold for "looks good"
                    percentage_score=analysis.get('score', 0),
                    explanation=analysis.get('score_explanation', "")
                )
                recommendation.set_feedback_json({
                    'strengths': analysis.get('strengths', []),
                    'improvements': analysis.get('improvements', [])
                })
                recommendation.set_suggestions_json({
                    'alternative_outfits': analysis.get('alternative_outfits', []),
                    'personalized_suggestions': analysis.get('personalized_suggestions', [])
                })
                recommendation.save()

                return redirect('core:recommendation_detail', pk=outfit.id)

            except Exception as e:
                messages.error(request, f"Error analyzing outfit: {str(e)}")
                return redirect('core:upload')
    else:
        form = OutfitUploadForm()

    return render(request, 'core/upload.html', {'form': form})

def recommendations(request):
    """View all recommendations."""
    outfits = OutfitUpload.objects.filter(recommendation__isnull=False).order_by('-uploaded_at')
    return render(request, 'core/recommendations.html', {'outfits': outfits})

def recommendation_detail(request, pk):
    """View a specific recommendation."""
    outfit = get_object_or_404(OutfitUpload, pk=pk)
    if not hasattr(outfit, 'recommendation'):
        messages.error(request, "No recommendation found for this outfit.")
        return redirect('upload')

    recommendation = outfit.recommendation
    feedback = recommendation.get_feedback_json()
    suggestions = recommendation.get_suggestions_json()

    context = {
        'outfit': outfit,
        'recommendation': recommendation,
        'strengths': feedback.get('strengths', []),
        'improvements': feedback.get('improvements', []),
        'alternative_outfits': suggestions.get('alternative_outfits', []),
        'personalized_suggestions': suggestions.get('personalized_suggestions', []),
        'percentage_score': recommendation.percentage_score,
        'explanation': recommendation.explanation  # Corrected key
    }

    return render(request, 'core/recommendation_detail.html', context)

def about(request):
    """About page view."""
    return render(request, 'core/about.html')
@csrf_exempt
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
                "looks_good": result.get('score', 0) >= 70,  # Assuming 70% is the threshold for "looks good"
                "percentage_score": result.get('score', 0),
                "explanation": result.get('score_explanation', ""),  # Corrected key
                "strengths": result.get('strengths', []),
                "improvements": result.get('improvements', []),
                "alternative_outfits": result.get('alternative_outfits', []),
                "personalized_suggestions": result.get('personalized_suggestions', []),
                "response": result.get('response', ""),
                "suggestions": result.get('suggestions', ""),
                "instagram_analysis": result.get('instagram_analysis', {})
            })

        except Exception as e:
            return JsonResponse({
                "error": f"Failed to analyze: {str(e)}"
            }, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)
