import os
import openai
import base64
import argparse
openai.api_key = os.getenv("OPEN_AI_API_KEY")

#initiate parsing (Used for taking parameter for image generation from command line)
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--prompt", help = "Insert Text to genrate image.", default= "baby panda with gun in high detail")
parser.add_argument("-n", "--number", help = "Enter number of images required", default = 2)
parser.add_argument("-s", "--size", help = "Size of image", default = 256)

#Reading arguments from command line 
args = parser.parse_args()

#Creating a response
res = openai.Image.create(
    prompt = args.prompt, #promt for genrated images  -- "spider hulk in ironman suit, high detail"
    n = int(args.number),
    size=f"{args.size}x{args.size}",
    response_format = "b64_json" # b64_json is a string representation of image
)

#Iterating over the response and genrating image and saving iamge locally
for i in range(len(res['data'])):
    b64_blob = res['data'][i]['b64_json']
    print("Genrating Image...")
    with open(f"image_gen{i+1}.jpg","wb") as file:
        file.write(base64.urlsafe_b64decode(b64_blob))
