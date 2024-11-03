def mj_prompt(profile_Data):
    mid_prompt =  f"""
    Create a studio photography-style single portrait of a person who matches the following profile: {profile_Data}. 
    The portrait should have a clean, professional studio background with soft, even lighting. 
    The person should be posed naturally and confidently, making eye contact with the camera. The attire, expression, 
    and styling should align with the details of the character’s background, career, and personality traits, reflecting their unique look and persona. 
    Ensure the image captures high detail, realistic textures, and a polished, professional finish.
    """

    return mid_prompt


mj_instructions = """
    Take the following passage and convert this into a midjourney prompt
    """
