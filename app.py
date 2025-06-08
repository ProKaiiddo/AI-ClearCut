# ✅ Import libraries
import gradio as gr
from rembg import remove
from PIL import Image
import io

# ✅ Background remover function
def remove_background(image: Image.Image) -> Image.Image:
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_bytes = buffered.getvalue()
    output_bytes = remove(img_bytes)
    output_image = Image.open(io.BytesIO(output_bytes)).convert("RGBA")
    return output_image

# ✅ Example Images (updated with working URLs)
examples = [
    ["https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Cat_August_2010-4.jpg/480px-Cat_August_2010-4.jpg"],
    ["https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Cat_November_2010-1a.jpg/480px-Cat_November_2010-1a.jpg"]
]

# ✅ Social Media & Credits Markdown
socials = """
### 🤝 Special Thanks  
- Built with 💖 using [rembg](https://github.com/danielgatis/rembg) — the amazing open-source AI background remover.
### 👨‍💻 Developer  
- @Kaiiddo
### 🔗 Follow Me
- 📺 [YouTube](https://youtube.com/@kaiiddo)
- 🐦 [Twitter / X](https://twitter.com/kaiiddo)
- 👋🏻 [Telegram](https://telegram.me/kaiiddo)
- 👑 [GitHub](https://github.com/prokaiiddo)
- 🌐 [BlueSky](https://bsky.app/profile/kaiiddo.bsky.social)
- 💼 [LinkedIn](https://www.linkedin.com/in/kaiiddo)
"""

# ✅ Gradio Interface
interface = gr.Interface(
    fn=remove_background,
    inputs=gr.Image(type="pil", label="🖼️ Upload Image"),
    outputs=gr.Image(type="pil", label="🎯 Output (Transparent Background)"),
    title="🖼️ AI ClearCut - Background Remover",
    description="""
Welcome to AI ClearCut!  
Remove image backgrounds instantly using AI. Upload any image and get a transparent version in seconds.
✅ Fast  
✅ Free  
✅ No Login Needed
""",
    examples=examples,
    article=socials
)

# ✅ Launch it on Colab (shareable public link)
interface.launch(share=True)
