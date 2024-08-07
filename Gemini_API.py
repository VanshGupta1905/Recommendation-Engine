import google.generativeai as genai
import PIL.Image




chat = None

def Start_a_Chat():
    genai.configure(api_key='AIzaSyD8LorjjnvCHcnG3sD9ZQipXrjh65M57OY')
    model = genai.GenerativeModel('gemini-1.5-flash')
    global  chat
    import Data_Recommendation
    model = genai.GenerativeModel('gemini-1.5-flash')
    chat = model.start_chat(history=[])
    json_data = Data_Recommendation.data[:100].to_json(orient='records')

    initial_prompt = f"Here's some data:\n  {json_data} \n Please remember the data as u are the centeral management of entire store ."
    chat.send_message(initial_prompt)

def new_chat():
    chat = model.start_chat(history=[])

def images(path):
    img = PIL.Image.open(path)
    prompt2 = "Identify the clothing in the image and provide me with product id that matches with the product "
    prompt3 = "The Output format should list of product id For ex [1,2,3,4,5,8], If there is no product then give empty list The output should be just a list nothing else"
    prompt = f"{prompt2} ,{prompt3}"
    response = chat.send_message([prompt,img])
    li = response.text.split(',')[1:-1]
    print(li)
    return li

def give_indices(user_prompt):
    prompt1 = user_prompt
    print(user_prompt)
    prompt2 = "Given these above requirements provide me with product id that matches the user need "
    prompt3="The Output format should list of product id For ex [1,2,3,4,5,8], If there is no product then give empty list The output should be just a list nothing else"
    prompt=(f"User For men :{prompt1} , "
            f"{prompt2} ,{prompt3}")
    response = chat.send_message(prompt)
    print("Model Response : "+response.text)
    li = response.text.split(',')[1:-1]
    return li