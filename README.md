# gaze_control

The overall goal of this repository is to experiment with user interaction by gaze detection. For example looking up/down/right/left to replace arrow key input.

# Current step
    - Experiment with local model
        - streamline exporting in linux and import in windows
            - num_workers=0 when exporting
            - PosixPath=WindowsPath when importing
    - make prediction better
    

Resources:
- https://towardsdatascience.com/video-streaming-in-the-jupyter-notebook-635bc5809e85
- https://github.com/maartenbreddels/ipywebrtc

# Next steps:
- get PIL Image into correcto format for feeding it to the model

# Done so far:
- Classify myself looking in directions (simple)
- Load trained fastai model
- Try out binder
- Make webcam widget work with voila
- Take single images from the stream
- Get a webcam stream going in a jupyter notebook.
- push from paperspace to github
- cloned on paperspace
- setup repo on github