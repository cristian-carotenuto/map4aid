from fastapi import FastAPI
from pydantic import BaseModel
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

app = FastAPI()

MODEL_ID = "Qwen/Qwen2.5-3B-Instruct"  # puoi cambiare
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    device_map="auto",
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    trust_remote_code=True
)

class Req(BaseModel):
    message: str
    history: list[dict] | None = None  # opzionale

@app.post("/chat")
def chat(req: Req):
    messages = [{"role":"system","content":"Sei Aidano (Map4Aid). Rispondi in italiano, breve e utile."}]
    if req.history:
        messages += req.history[-8:]  # ultimi N turni
    messages.append({"role":"user","content": req.message})

    prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=220, do_sample=True, temperature=0.7, top_p=0.9)

    text = tokenizer.decode(out[0], skip_special_tokens=True)
    reply = text.split(req.message)[-1].strip()
    return {"reply": reply}
