import whisper 
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
model=whisper.load_model("large-v2")
audios=os.listdir("audios")


for audio in audios:
    if("Python"in audio):
        number=audio.split(".")[0]
        title=audio.split(".")[1][:-8]
    
        print(number,title)
        
        result=model.transcribe(audio=f"audios/{audio}",
    task="translate",language="hi",word_timestamps=False)
        chunks=[]

        for segment in result["segments"]:
            chunks.append({"number":number,"title":title,"start":segment["start"],"end":segment["end"],"text":segment["text"]})
    
            print(chunks)
            
            chunks_with_metadata= {"chunks":chunks,"text":result["text"]}
        with open(f"text.json","w")as f:
                 json.dump(chunks_with_metadata,f)



    
    