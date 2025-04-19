import os

# Create project structure
def create_project_structure():
    # Create main directories
    directories = [
        'outfit_recommender',
        'outfit_recommender/outfit_recommender',
        'outfit_recommender/core',
        'outfit_recommender/core/templates',
        'outfit_recommender/core/templates/core',
        'outfit_recommender/core/static',
        'outfit_recommender/core/static/css',
        'outfit_recommender/core/static/js',
        'outfit_recommender/core/static/images',
        'outfit_recommender/media',
        'outfit_recommender/media/uploads',
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")
    
    print("\nProject structure created successfully!")

# Run the function to see the output
create_project_structure()

# Display the project structure
print("\nProject Structure:")
for root, dirs, files in os.walk('outfit_recommender'):
    level = root.replace('outfit_recommender', '').count(os.sep)
    indent = ' ' * 4 * level
    print(f"{indent}{os.path.basename(root)}/")

print("\nNow let's create the actual Django project files...")