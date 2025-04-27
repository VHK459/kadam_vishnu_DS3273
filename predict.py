import torch
from PIL import Image
from torchvision import transforms
from config import resize_x, resize_y

inference_transform = transforms.Compose([
    transforms.Resize((resize_x, resize_y)),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

def cryptic_inf_f(model, image_paths):
    model.eval()
    images = []

    for path in image_paths:
        image = Image.open(path).convert("RGB")
        image = inference_transform(image).unsqueeze(0)
        images.append(image)

    images = torch.cat(images).to(next(model.parameters()).device)

    with torch.no_grad():
        outputs = model(images)
        predictions = outputs.argmax(1).cpu().tolist()

    return predictions
