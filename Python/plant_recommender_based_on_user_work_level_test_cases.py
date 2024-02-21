# Plant recommender 
# A program containing a function that recommends a plant to the user based on their maintenance or work efforts level of the plant 


def plant_recommendation(care):
    if care == 'low':
        print('aloe')
    elif care == 'medium':
        print('pothos')
    elif care == 'high':
        print('orchid')

# Debugging and creating Test cases via recalling the function with different levels of care
        
plant_recommendation('low')
plant_recommendation('medium')
plant_recommendation('high')

