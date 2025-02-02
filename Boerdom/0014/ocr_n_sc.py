import pytesseract
from PIL import Image
import mss
import Quartz

def get_chrome_bounds():
    """Finds Chrome window bounds on macOS."""
    windows = Quartz.CGWindowListCopyWindowInfo(Quartz.kCGWindowListOptionOnScreenOnly, Quartz.kCGNullWindowID)
    for window in windows:
        if "Google Chrome" in window.get("kCGWindowOwnerName", ""):
            return window.get("kCGWindowBounds")
    return None

def capture_chrome_text():
    """Captures Chrome screen and extracts merged text (sentences) with positions."""
    bounds = get_chrome_bounds()
    if not bounds:
        print("Chrome window not found!")
        return []

    x, y, width, height = bounds["X"], bounds["Y"], bounds["Width"], bounds["Height"]
    region = {"top": int(y), "left": int(x), "width": int(width), "height": int(height)}

    with mss.mss() as sct:
        screenshot = sct.grab(region)
        img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)

        # Extract text with bounding boxes
        data = pytesseract.image_to_data(img, config="--psm 6", output_type=pytesseract.Output.DICT)
        
        sentences = []
        current_sentence = {"text": "", "x": None, "y": None, "width": 0, "height": 0}

        for i in range(len(data["text"])):
            word = data["text"][i].strip()
            if not word:
                continue  # Skip empty words

            word_x = x + data["left"][i]
            word_y = y + data["top"][i]
            word_width = data["width"][i]
            word_height = data["height"][i]

            # If this is the first word in a sentence, start a new one
            if current_sentence["text"] == "":
                current_sentence = {
                    "text": word,
                    "x": word_x,
                    "y": word_y,
                    "width": word_width,
                    "height": word_height
                }
            else:
                # Check if word is on the same line and close to the previous word
                if abs(word_y - current_sentence["y"]) < word_height * 0.5 and word_x - (current_sentence["x"] + current_sentence["width"]) < 15:
                    # Append word to current sentence
                    current_sentence["text"] += " " + word
                    current_sentence["width"] = (word_x + word_width) - current_sentence["x"]
                else:
                    # Store the completed sentence and start a new one
                    sentences.append(current_sentence)
                    current_sentence = {
                        "text": word,
                        "x": word_x,
                        "y": word_y,
                        "width": word_width,
                        "height": word_height
                    }

        # Append last sentence
        if current_sentence["text"]:
            sentences.append(current_sentence)

        return sentences

# Run OCR and print results
text_positions = capture_chrome_text()
for item in text_positions:
    print(f'Sentence: "{item["text"]}" at ({item["x"]}, {item["y"]}) Size: {item["width"]}x{item["height"]}')