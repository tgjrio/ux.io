persona_image_instructions = """
Take the following empathy map and convert this into a midjourney prompt that'll generate an iamge of this persona.
The image must be a photography single portrait of this person.  Do not put /imagine, your response should just be the mid-journey prompt
"""


define_needs_prompt = """ 
As my UX assistant, you're responsible for ensuring that I'm able to define a users need from the personas data I have.
Prior to this step, we've completed interviews and derived empathy maps from those.

After that, we converted those empathy maps into Aggregated personas to consolidate commmon needs etc between user.

I want you to review my personas and interview data  to identify the most important needs of the user.

Here's a sample of what I'm looking for:

Tools for Defining User Needs:
User Stories: 
One-sentence narratives from a user’s perspective that describe who they are, what action they want to take, and why.
Example: “As a long-time customer with a visual impairment, I want to place my orders over the phone so I can order with ease and continue connecting with staff members.”
User Journeys: 
Map out the series of experiences users have as they interact with a product, helping designers understand users’ goals and pain points in both current and future interactions with the product.
Example: Berta’s journey with current phone and social media orders vs. her journey with the planned website-based ordering system.
Problem Statements:
Summarize the user’s needs from the designer’s perspective, providing detailed insights into the user’s context and what the design must solve.
Example: “Berta needs a website that adapts to her visual impairment and mimics the feel of a phone conversation to maintain her connection with the bakery.”
Key Takeaways:
The define phase helps designers translate empathy research into clear, actionable problem statements for each user persona.
These problem statements ensure the design addresses the needs of multiple user types, not just one group.

YOUR RESPONSE  SHOULD BE ONLY BE IN MARKDOWN AND NOTHING ELSE.

KEEP THE FORMAT OF A USER STORY, USER JOURNEY, PROBLEM STATEMENT AND KEY TAKEAWAYS.

"""